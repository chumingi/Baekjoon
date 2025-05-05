import os
import pandas as pd
from datetime import datetime
from collections import Counter

# ─── 설정 ─────────────────────────────────────────
LOG_FILE     = "logs/problem_log.csv"
MAIN_README = "README.md"
CLASS_DIR   = "class"
TAGS_DIR    = "tags"

# solved.ac level → 클래스 번호 매핑 (예: Bronze V~I → class1)
def class_key_from_tier(tier_full):
    # Bronze → class1, Silver → class2, Gold → class3, …
    grp = tier_full.split()[0]
    order = ["Bronze","Silver","Gold","Platinum","Diamond","Ruby"]
    return f"class{order.index(grp)+1}" if grp in order else "class0"

# ─── 메인 처리 ─────────────────────────────────────

def main():
    if not os.path.exists(LOG_FILE):
        print("[!] 로그 파일이 없습니다.")
        return

    df = pd.read_csv(LOG_FILE, dtype=str)
    df["tags_list"] = df["태그"].str.split("|")
    df["class_key"] = df["티어"].map(class_key_from_tier)

    # class 별, tag 별 문제 수
    class_cnt = df["class_key"].value_counts().to_dict()
    tag_cnt   = Counter(sum(df["tags_list"], []))

    os.makedirs(CLASS_DIR, exist_ok=True)
    os.makedirs(TAGS_DIR, exist_ok=True)

    # ① class/*.md 생성
    for cls, grp in df.groupby("class_key"):
        path = os.path.join(CLASS_DIR, f"{cls}.md")
        with open(path,"w",encoding="utf-8") as f:
            f.write("| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n")
            f.write("|------|------|------|------|----------|\n")
            for _,r in grp.iterrows():
                tags = ", ".join(r["tags_list"])
                link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
                f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {tags} | {r['제출날짜']} |\n")

    # ② tags/*.md 생성
    for tag, grp in df.explode("tags_list").groupby("tags_list"):
        path = os.path.join(TAGS_DIR, f"{tag}.md")
        with open(path,"w",encoding="utf-8") as f:
            f.write("| 번호 | 제목 | 티어 | 제출날짜 |\n")
            f.write("|------|------|------|----------|\n")
            for _,r in grp.iterrows():
                link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
                f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {r['제출날짜']} |\n")

    # ③ 루트 README.md 생성
    with open(MAIN_README,"w",encoding="utf-8") as f:
        f.write("# 📝 백준 문제풀이 정리\n\n")
        f.write(f"📅 Last Update: {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write("## 📂 Class별 문제 수\n")
        for cls, cnt in sorted(class_cnt.items()):
            f.write(f"- [{cls}]({CLASS_DIR}/{cls}.md) - {cnt}문제\n")
        f.write("\n## 🏷️ 태그별 문제 수\n")
        for tag, cnt in sorted(tag_cnt.items()):
            f.write(f"- [{tag}]({TAGS_DIR}/{tag}.md) - {cnt}문제\n")
        f.write("\n---\n")
        f.write("## 📘 전체 풀이 목록\n")
        f.write("| 번호 | 제목 | 티어 | 태그 | 제출날짜 |\n")
        f.write("|------|------|------|------|----------|\n")
        for _,r in df.iterrows():
            tags = ", ".join(r["tags_list"])
            link = f"[{r['제목']}](백준/{r['티어'].split()[0]}/{r['문제번호']}.{r['제목']})"
            f.write(f"| {r['문제번호']} | {link} | {r['티어']} | {tags} | {r['제출날짜']} |\n")

    print("✅ README.md 및 md 파일 생성 완료.")

if __name__=="__main__":
    main()
