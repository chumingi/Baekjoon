import os
import re
import csv
import requests
from datetime import datetime
from collections import defaultdict

# ─── 설정 ─────────────────────────────────────────
ROOT_UPLOAD_DIR = "백준"                 # 백준허브가 업로드한 최상위 폴더
LOG_FILE        = "logs/problem_log.csv" # 기록용 CSV
SOLVED_API      = "https://solved.ac/api/v3/problem/show?problemId="

CLASS_DIR       = "class"  # 이후 generate_readme.py 에서 사용할 폴더
TAGS_DIR        = "tags"

# solved.ac level → 티어 문자열 매핑
TIER_MAP = {
    1:"Bronze V",2:"Bronze IV",3:"Bronze III",4:"Bronze II",5:"Bronze I",
    6:"Silver V",7:"Silver IV",8:"Silver III",9:"Silver II",10:"Silver I",
    11:"Gold V",12:"Gold IV",13:"Gold III",14:"Gold II",15:"Gold I",
    16:"Platinum V",17:"Platinum IV",18:"Platinum III",19:"Platinum II",20:"Platinum I",
    21:"Diamond V",22:"Diamond IV",23:"Diamond III",24:"Diamond II",25:"Diamond I",
    26:"Ruby V",27:"Ruby IV",28:"Ruby III",29:"Ruby II",30:"Ruby I"
}

# ─── 유틸리티 함수 ──────────────────────────────────

def get_problem_id_and_title(folder_name):
    m = re.match(r"(\d+)\.(.+)", folder_name)
    return (m.group(1), m.group(2).strip()) if m else (None,None)

def get_submission_date(problem_dir):
    """문제 폴더 내 README.md 에서 '제출 일자'를 찾아 'YYYY-MM-DD HH:MM:SS' 반환"""
    for f in os.listdir(problem_dir):
        if f.lower().endswith(".md"):
            with open(os.path.join(problem_dir,f), encoding="utf-8") as r:
                for line in r:
                    if "제출 일자" in line:
                        # 예: '2025년 5월 3일 20:33:49' → ISO 포맷으로 변경
                        parts = re.search(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일\s*(\d{2}:\d{2}:\d{2})", line)
                        if parts:
                            y,mo,d,HM = parts.groups()
                            return f"{int(y):04d}-{int(mo):02d}-{int(d):02d} {HM}"
    return None

def get_problem_info(pid):
    """solved.ac API로 제목, level, tags 조회"""
    r = requests.get(SOLVED_API+pid)
    if r.status_code!=200: return None
    j = r.json()
    tier = TIER_MAP.get(j["level"],"Unknown")
    return {
        "title": j["titleKo"],
        "level": j["level"],
        "tier": tier,
        "tags": [t["key"] for t in j["tags"]]
    }

def load_existing_logs():
    """(pid, date) 쌍으로 이미 기록된 목록 반환"""
    seen = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader,None)
            for row in reader:
                if len(row)>=5:
                    seen.add((row[0],row[4]))
    return seen

def append_log(info, date):
    """CSV에 한 줄 추가 (헤더 자동)"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    write_hdr = not os.path.exists(LOG_FILE)
    with open(LOG_FILE,"a",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        if write_hdr:
            w.writerow(["문제번호","제목","티어","태그","제출날짜"])
        w.writerow([info["id"],info["title"],info["tier"],
                    "|".join(info["tags"]),date])

# ─── 메인 처리 ─────────────────────────────────────

def main():
    if not os.path.isdir(ROOT_UPLOAD_DIR):
        print(f"[!] '{ROOT_UPLOAD_DIR}' 폴더가 없습니다.")
        return

    logged = load_existing_logs()
    new_count = 0

    # 예: 백준/Bronze/10871.X보다 작은 수/
    for tier in os.listdir(ROOT_UPLOAD_DIR):
        tier_p = os.path.join(ROOT_UPLOAD_DIR,tier)
        if not os.path.isdir(tier_p): continue

        for prob in os.listdir(tier_p):
            prob_p = os.path.join(tier_p,prob)
            if not os.path.isdir(prob_p): continue
            pid, _ = get_problem_id_and_title(prob)
            if not pid: continue

            info = get_problem_info(pid)
            if not info: continue

            date = get_submission_date(prob_p)
            if not date or (pid,date) in logged: continue

            # 기록
            info["id"] = pid
            append_log(info,date)
            logged.add((pid,date))
            new_count += 1
            print(f"[✔] {pid} 기록됨 ({date})")

    if new_count==0:
        print("▶ 신규 기록 없음.")
    else:
        print(f"▶ {new_count}개 문제 기록 완료.")

if __name__=="__main__":
    main()
