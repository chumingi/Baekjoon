import os
import re
import sys
import csv
import shutil
import requests
import pandas as pd
from datetime import datetime
from collections import Counter

# ─────────────────────────────────────────────────────────
# 경로 설정 (스크립트 위치 기준)
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR    = os.path.join(BASE_DIR, '백준')
LOG_FILE    = os.path.join(BASE_DIR, 'logs', 'problem_log.csv')
TIER_DIR    = os.path.join(BASE_DIR, 'tiers')
TAGS_DIR    = os.path.join(BASE_DIR, 'tags')
MAIN_README = os.path.join(BASE_DIR, 'README.md')
SOLVED_API  = 'https://solved.ac/api/v3/problem/show?problemId='

# tier 매핑
TIER_MAP = {
    1:'Bronze V',2:'Bronze IV',3:'Bronze III',4:'Bronze II',5:'Bronze I',
    6:'Silver V',7:'Silver IV',8:'Silver III',9:'Silver II',10:'Silver I',
    11:'Gold V',12:'Gold IV',13:'Gold III',14:'Gold II',15:'Gold I',
    16:'Platinum V',17:'Platinum IV',18:'Platinum III',19:'Platinum II',20:'Platinum I',
    21:'Diamond V',22:'Diamond IV',23:'Diamond III',24:'Diamond II',25:'Diamond I',
    26:'Ruby V',27:'Ruby IV',28:'Ruby III',29:'Ruby II',30:'Ruby I'
}


def tier_group_key(tier_full):
    """'Bronze V' → 'bronze', 'Gold III' → 'gold' 등 소문자 티어 그룹명을 반환한다."""
    grp = str(tier_full).split()[0]
    order = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby']
    return grp.lower() if grp in order else 'unknown'


def extract_pid_title(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # $ 앵커로 마지막 '- {숫자}' 를 pid로 추출
            # '별 찍기 - 1 - 2438' 같은 형식에서 2438을 정확히 추출
            m = re.match(r"# \[([^\]]+)\]\s*(.+?)\s*-\s*(\d+)\s*$", line)
            if m:
                return m.group(3), m.group(2).strip(), m.group(1).strip()
    return None, None, None


def extract_submission_date(readme_path):
    """제출 일자 헤더 이후 최대 4줄 내에서 날짜 패턴을 탐색한다.

    BaekjoonHub README 형식:
        ### 제출 일자
        <빈 줄>
        2025년 5월 5일 17:07:00
    """
    lines = open(readme_path, encoding='utf-8').read().splitlines()
    date_re = re.compile(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일\s*(\d{2}:\d{2}:\d{2})")
    for i, line in enumerate(lines):
        if '제출 일자' in line:
            for j in range(i, min(i + 4, len(lines))):
                m = date_re.search(lines[j])
                if m:
                    y, mo, da, tm = m.groups()
                    return f"{int(y):04d}-{int(mo):02d}-{int(da):02d} {tm}"
    return None


def extract_tags_from_readme(readme_path):
    """README의 분류 섹션에서 태그를 추출한다. solved.ac API 실패 시 fallback."""
    lines = open(readme_path, encoding='utf-8').read().splitlines()
    for i, line in enumerate(lines):
        if line.startswith('#') and '분류' in line:
            for j in range(i + 1, min(i + 4, len(lines))):
                raw = lines[j].strip()
                if raw:
                    return [t.strip() for t in raw.split(',') if t.strip()]
    return []


def get_tags(pid, readme_path=None):
    """solved.ac API로 영문 태그를 조회하고, 실패 시 README 분류 섹션을 사용한다."""
    try:
        r = requests.get(SOLVED_API + pid, timeout=5)
        if r.status_code == 200:
            tags = [t['key'] for t in r.json().get('tags', [])]
            if tags:
                return tags
    except Exception:
        pass
    if readme_path:
        return extract_tags_from_readme(readme_path)
    return []


def load_logged():
    """이미 로깅된 문제 번호 집합을 반환한다."""
    seen = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if row:
                    seen.add(row[0])  # pid만 dedup 키로 사용
    return seen


def _find_folder_path(pid, tier_group):
    """filesystem을 탐색해 문제 번호에 해당하는 실제 폴더 경로를 반환한다."""
    tier_path = os.path.join(ROOT_DIR, tier_group)
    if not os.path.isdir(tier_path):
        return None
    for folder in os.listdir(tier_path):
        # 폴더명이 '{pid}.' 또는 '{pid} ' 또는 '{pid}<공백류>' 로 시작하는지 확인
        if re.match(rf"^{re.escape(pid)}[\.\s\u2005]", folder):
            return f"백준/{tier_group}/{folder}"
    return None


def repair_log():
    """폴더경로와 문제번호가 불일치하는 잘못된 행을 제거한다.
    제거된 행은 main() 재실행 시 올바른 pid와 태그로 재등록된다.
    """
    if not os.path.exists(LOG_FILE):
        return
    df = pd.read_csv(LOG_FILE, dtype=str)
    if '폴더경로' not in df.columns:
        return

    def is_valid(row):
        fp = str(row.get('폴더경로', '')).strip()
        if not fp or fp == 'nan':
            return True
        folder_name = fp.split('/')[-1]
        m = re.match(r'^(\d+)', folder_name)
        return not (m and m.group(1) != str(row['문제번호']).strip())

    before = len(df)
    df = df[df.apply(is_valid, axis=1)]
    removed = before - len(df)
    if removed:
        df.to_csv(LOG_FILE, index=False, encoding='utf-8')
        print(f'[i] {removed}개의 잘못된 행을 제거했습니다. 재실행 시 올바르게 재등록됩니다.')


def migrate_log():
    """5컬럼 구버전 CSV를 6컬럼(폴더경로 추가)으로 업그레이드한다."""
    if not os.path.exists(LOG_FILE):
        return
    with open(LOG_FILE, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    if not rows or '폴더경로' in rows[0]:
        return
    rows[0] = rows[0] + ['폴더경로']
    for i in range(1, len(rows)):
        if len(rows[i]) < 3:
            rows[i] = rows[i] + ['']
            continue
        pid = rows[i][0]
        tier_group = rows[i][2].split()[0] if rows[i][2] else ''
        folder_path = _find_folder_path(pid, tier_group) or ''
        rows[i] = rows[i] + [folder_path]
    with open(LOG_FILE, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(rows)
    print('[i] 로그 파일을 6컬럼 형식으로 업그레이드했습니다.')


def append_log(pid, title, tier, tags, date, folder_path):
    logs_dir = os.path.dirname(LOG_FILE)
    if os.path.exists(logs_dir) and not os.path.isdir(logs_dir):
        os.remove(logs_dir)
    os.makedirs(logs_dir, exist_ok=True)

    try:
        write_header = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(['문제번호', '제목', '티어', '태그', '제출날짜', '폴더경로'])
            w.writerow([pid, title, tier, '|'.join(tags), date, folder_path])
    except PermissionError:
        print(f"[!] 권한 오류: '{LOG_FILE}' 파일을 닫거나 권한을 확인해 주세요.")
        sys.exit(1)


def _make_link(row, prefix=''):
    """문제 제목 링크를 생성한다.

    prefix: 파일 위치에 따른 경로 접두사
      - README.md (루트)        → prefix=''
      - tiers/*.md, tags/*.md  → prefix='../'
    """
    fp = str(row.get('폴더경로', '')).strip()
    if not fp or fp == 'nan':
        tier_group = str(row['티어']).split()[0]
        fp = _find_folder_path(str(row['문제번호']), tier_group) or \
             f"백준/{tier_group}/{row['문제번호']}. {row['제목']}"
    return f"[{row['제목']}]({prefix}{fp})"


def generate_markdowns():
    if not os.path.exists(LOG_FILE):
        print('[!] 로그 파일이 없습니다.')
        return

    df = pd.read_csv(LOG_FILE, dtype=str)
    df['tags_list'] = df['태그'].fillna('').str.split('|')
    df['tier_key'] = df['티어'].map(tier_group_key)

    # 날짜 내림차순 정렬 (tiers, tags, README 공통 사용)
    df['_sort_dt'] = pd.to_datetime(df['제출날짜'], errors='coerce')
    df_sorted = df.sort_values('_sort_dt', ascending=False).drop(columns=['_sort_dt'])

    os.makedirs(TIER_DIR, exist_ok=True)
    os.makedirs(TAGS_DIR, exist_ok=True)

    # 구버전 class/ 폴더가 남아있으면 삭제
    old_class_dir = os.path.join(BASE_DIR, 'class')
    if os.path.isdir(old_class_dir):
        shutil.rmtree(old_class_dir)
        print('[i] 구버전 class/ 폴더를 삭제했습니다.')

    # 티어별 md — 헤더 포함, 날짜 내림차순
    written_tiers = set()
    tier_display_order = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'ruby']
    for tier_key, grp in df_sorted.groupby('tier_key', sort=False):
        fname = f'{tier_key}.md'
        written_tiers.add(fname)
        with open(os.path.join(TIER_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(f'# {tier_key.capitalize()} 문제 목록\n\n')
            f.write('| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n')
            f.write('|------|------|------|------|----------|\n')
            for _, r in grp.iterrows():
                tags_str = ', '.join(t for t in r['tags_list'] if t)
                f.write(f"| {r['문제번호']} | {_make_link(r, '../')} | {r['티어']} | {tags_str} | {r['제출날짜']} |\n")
    # 더 이상 쓰이지 않는 tier 파일 삭제
    for fname in os.listdir(TIER_DIR):
        if fname.endswith('.md') and fname not in written_tiers:
            os.remove(os.path.join(TIER_DIR, fname))
            print(f'[i] 삭제됨: tiers/{fname}')

    # 태그별 md — 헤더 포함, 날짜 내림차순
    written_tags = set()
    for tag, grp in df_sorted.explode('tags_list').groupby('tags_list', sort=False):
        if not tag:
            continue
        fname = f'{tag}.md'
        written_tags.add(fname)
        with open(os.path.join(TAGS_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(f'# {tag} 태그 문제 목록\n\n')
            f.write('| 번호 | 제목 | 티어 | 제출날짜 |\n')
            f.write('|------|------|------|----------|\n')
            for _, r in grp.iterrows():
                f.write(f"| {r['문제번호']} | {_make_link(r, '../')} | {r['티어']} | {r['제출날짜']} |\n")
    # 더 이상 쓰이지 않는 태그 파일 삭제 (좀비 파일 제거)
    for fname in os.listdir(TAGS_DIR):
        if fname.endswith('.md') and fname not in written_tags:
            os.remove(os.path.join(TAGS_DIR, fname))
            print(f'[i] 삭제됨: tags/{fname}')

    # 루트 README.md — 링크는 모두 상대 경로
    tier_order = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby']
    tier_group_counts = df['티어'].apply(lambda x: str(x).split()[0]).value_counts()
    present_tiers = [t for t in tier_order if t in tier_group_counts]

    tag_counts = Counter(t for tags in df['tags_list'] for t in tags if t)
    major_tags = sorted(
        ((tag, cnt) for tag, cnt in tag_counts.items() if cnt >= 5),
        key=lambda x: -x[1]
    )

    with open(MAIN_README, 'w', encoding='utf-8') as f:
        f.write('# 📝 백준 문제풀이 정리\n\n')
        f.write('Python 코딩테스트 실전 통과를 목표로 한 학습 기록입니다.  \n')
        f.write('BaaaaaaaarkingDog 강의 커리큘럼과 개인 로드맵(Phase 0 → 5)을 병행합니다.\n\n')
        f.write(f'📅 Last Update: {datetime.now().strftime("%Y-%m-%d")}\n\n')
        f.write('---\n\n')

        # 티어별 분포 — 티어명 클릭 시 해당 tiers/*.md로 이동
        f.write('## 풀이 현황\n\n')
        total = sum(tier_group_counts.get(t, 0) for t in present_tiers)
        f.write('| ' + ' | '.join(f'[{t}](tiers/{t.lower()}.md)' for t in present_tiers) + ' | 합계 |\n')
        f.write('|' + '|'.join([':---:'] * (len(present_tiers) + 1)) + '|\n')
        f.write('| ' + ' | '.join(str(tier_group_counts.get(t, 0)) for t in present_tiers) + f' | {total} |\n\n')
        f.write('---\n\n')

        # 주요 태그 (5문제 이상)
        if major_tags:
            f.write('## 주요 태그 (5문제 이상)\n\n')
            f.write('| 태그 | 문제 수 |\n')
            f.write('|------|--------|\n')
            for tag, cnt in major_tags:
                f.write(f'| [{tag}](tags/{tag}.md) | {cnt} |\n')
            f.write('\n---\n\n')

        # 전체 풀이 목록 (최근 순)
        f.write('## 전체 풀이 목록 (최근 순)\n\n')
        f.write('| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n')
        f.write('|------|------|------|------|----------|\n')
        for _, r in df_sorted.iterrows():
            tags_str = ', '.join(t for t in r['tags_list'] if t)
            f.write(f"| {r['문제번호']} | {_make_link(r)} | {r['티어']} | {tags_str} | {r['제출날짜']} |\n")


def main():
    if not os.path.isdir(ROOT_DIR):
        print(f"[!] '{ROOT_DIR}' 폴더가 없습니다.")
        return

    migrate_log()
    repair_log()
    existing = load_logged()
    new_count = 0

    for tier in os.listdir(ROOT_DIR):
        tier_path = os.path.join(ROOT_DIR, tier)
        if not os.path.isdir(tier_path):
            continue
        for folder in os.listdir(tier_path):
            prob_dir = os.path.join(tier_path, folder)
            readme = os.path.join(prob_dir, 'README.md')
            if not os.path.exists(readme):
                continue

            pid, title, tier_name = extract_pid_title(readme)
            date = extract_submission_date(readme)
            if not pid or not date:
                print(f'[!] 파싱 실패: {tier}/{folder}')
                continue
            if pid in existing:
                continue

            tags = get_tags(pid, readme)
            folder_path = f"백준/{tier}/{folder}"
            append_log(pid, title, tier_name, tags, date, folder_path)
            existing.add(pid)
            new_count += 1
            print(f'[✔] 기록됨: {pid} - {title}')

    print(f'▶ 총 {new_count}개 기록 완료.')
    generate_markdowns()


if __name__ == '__main__':
    main()
