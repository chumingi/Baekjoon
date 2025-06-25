import os
import re
import sys
import csv
import requests
import pandas as pd
from datetime import datetime
from collections import Counter

# ─────────────────────────────────────────────────────────
# 경로 설정 (스크립트 위치 기준)
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR    = os.path.join(BASE_DIR, '백준')
LOG_FILE    = os.path.join(BASE_DIR, 'logs', 'problem_log.csv')
CLASS_DIR   = os.path.join(BASE_DIR, 'class')
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

def class_key_from_tier(tier_full):
    grp = tier_full.split()[0]
    order = ['Bronze','Silver','Gold','Platinum','Diamond','Ruby']
    return f'class{order.index(grp)+1}' if grp in order else 'class0'

def extract_pid_title(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = re.match(r"# \[([^\]]+)\]\s*(.+?)\s*-\s*(\d+)", line)
            if m:
                return m.group(3), m.group(2).strip(), m.group(1).strip()
    return None, None, None

def extract_submission_date(readme_path):
    lines = open(readme_path, encoding='utf-8').read().splitlines()
    for i, line in enumerate(lines):
        if '제출 일자' in line:
            # 같은 줄에 날짜
            m = re.search(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일\s*(\d{2}:\d{2}:\d{2})", line)
            if m:
                y,mo,da,tm = m.groups()
                return f"{int(y):04d}-{int(mo):02d}-{int(da):02d} {tm}"
            # 다음 줄에 날짜
            if i+1 < len(lines):
                m2 = re.search(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일\s*(\d{2}:\d{2}:\d{2})", lines[i+1])
                if m2:
                    y,mo,da,tm = m2.groups()
                    return f"{int(y):04d}-{int(mo):02d}-{int(da):02d} {tm}"
    return None

def get_tags(pid):
    try:
        r = requests.get(SOLVED_API + pid, timeout=5)
        if r.status_code == 200:
            return [t['key'] for t in r.json().get('tags', [])]
    except Exception:
        pass
    return []

def load_logged():
    seen = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 5:
                    seen.add((row[0], row[4]))
    return seen

def append_log(pid, title, tier, tags, date):
    # logs 폴더가 파일로 잘못 존재한다면 삭제 후 디렉터리 생성
    logs_dir = os.path.dirname(LOG_FILE)
    if os.path.exists(logs_dir) and not os.path.isdir(logs_dir):
        os.remove(logs_dir)
    os.makedirs(logs_dir, exist_ok=True)

    try:
        write_header = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(['문제번호','제목','티어','태그','제출날짜'])
            w.writerow([pid, title, tier, '|'.join(tags), date])
    except PermissionError:
        print(f"[!] 권한 오류: '{LOG_FILE}' 파일을 닫거나 권한을 확인해 주세요.")
        sys.exit(1)

def generate_markdowns():
    if not os.path.exists(LOG_FILE):
        print('[!] 로그 파일이 없습니다.')
        return

    df = pd.read_csv(LOG_FILE, dtype=str)
    df['tags_list'] = df['태그'].fillna('').str.split('|')
    df['class_key'] = df['티어'].map(class_key_from_tier)

    os.makedirs(CLASS_DIR, exist_ok=True)
    os.makedirs(TAGS_DIR, exist_ok=True)

    # 클래스별 md
    for cls, grp in df.groupby('class_key'):
        with open(os.path.join(CLASS_DIR, f'{cls}.md'), 'w', encoding='utf-8') as f:
            f.write('| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n')
            f.write('|------|------|------|------|----------|\n')
            for _, r in grp.iterrows():
                link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
                f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {', '.join(r['tags_list'])} | {r['제출날짜']} |\n")

    # 태그별 md
    for tag, grp in df.explode('tags_list').groupby('tags_list'):
        with open(os.path.join(TAGS_DIR, f'{tag}.md'), 'w', encoding='utf-8') as f:
            f.write('| 번호 | 제목 | 티어 | 제출날짜 |\n')
            f.write('|------|------|------|----------|\n')
            for _, r in grp.iterrows():
                link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
                f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {r['제출날짜']} |\n")

    # 루트 README.md
    with open(MAIN_README, 'w', encoding='utf-8') as f:
        f.write('# 📝 백준 문제풀이 정리\n\n')
        f.write(f'📅 Last Update: {datetime.now().strftime("%Y-%m-%d")}\n\n')
        f.write('## 📂 Class별 문제 수\n')
        for cls, cnt in df['class_key'].value_counts().sort_index().items():
            f.write(f'- [{cls}]({CLASS_DIR}/{cls}.md) - {cnt}문제\n')
        f.write('\n## 🏷️ 태그별 문제 수\n')
        tag_counts = Counter(sum(df['tags_list'], []))
        for tag, cnt in sorted(tag_counts.items()):
            f.write(f'- [{tag}]({TAGS_DIR}/{tag}.md) - {cnt}문제\n')
        f.write('\n---\n')
        f.write('## 📘 전체 풀이 목록\n')
        f.write('| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n')
        f.write('|------|------|------|------|----------|\n')
        for _, r in df.iterrows():
            link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
            f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {', '.join(r['tags_list'])} | {r['제출날짜']} |\n")

def main():
    if not os.path.isdir(ROOT_DIR):
        print(f"[!] '{ROOT_DIR}' 폴더가 없습니다.")
        return

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
            if not pid or not date or (pid, date) in existing:
                continue

            tags = get_tags(pid)
            append_log(pid, title, tier_name, tags, date)
            existing.add((pid, date))
            new_count += 1
            print(f'[✔] 기록됨: {pid} - {title}')

    print(f'▶ 총 {new_count}개 기록 완료.')
    generate_markdowns()

if __name__ == '__main__':
    main()
