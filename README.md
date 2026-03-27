# 📝 백준 문제풀이 정리

Python 코딩테스트 실전 통과를 목표로 한 학습 기록입니다.
BaaaaaaaarkingDog 강의 커리큘럼과 개인 로드맵(Phase 0 → 5)을 병행하며,
"한 권으로 끝내는 코딩테스트 with Python" 교재 및 [joonlab](https://www.joonlab.com) 문제풀이 사이트를 활용한 학습도 함께 진행합니다.

📅 Last Update: 2026-03-27

---

## 프로젝트 구조

```
📦 Baekjoon/
├── 백준/               # BaekjoonHub 자동 업로드 — 티어별 풀이 코드 및 풀이 노트
├── tiers/              # 티어별 문제 목록 (bronze / silver / gold / platinum)
├── tags/               # 알고리즘 태그별 문제 목록
├── logs/               # 풀이 로그 CSV (문제번호, 제목, 티어, 태그, 제출날짜, 폴더경로)
├── LECTURE/
│   ├── BaaaaaaaarkingDog/  # BaaaaaaaarkingDog 강의 실습 코드
│   ├── joonlab/            # "한 권으로 끝내는 코딩테스트 with Python" 교재 + joonlab 사이트 풀이
│   └── coding_test_roadmap/  # 학습 로드맵 및 단계별 계획
├── boj_logger.py       # 자동화 스크립트 — 풀이 로깅 및 마크다운 생성
├── template.py         # 풀이 작성 템플릿
└── 합격자_풀이_전략.md  # 코딩테스트 합격자의 사고 루틴 및 풀이 전략 가이드
```

---

## 풀이 현황

| [Bronze](tiers/bronze.md) | [Silver](tiers/silver.md) | [Gold](tiers/gold.md) | [Platinum](tiers/platinum.md) | 합계 |
|:---:|:---:|:---:|:---:|:---:|
| 24 | 26 | 4 | 1 | 55 |

---

## 주요 태그 (5문제 이상)

| 태그 | 문제 수 |
|------|--------|
| [implementation](tags/implementation.md) | 30 |
| [data_structures](tags/data_structures.md) | 20 |
| [stack](tags/stack.md) | 10 |
| [math](tags/math.md) | 8 |
| [string](tags/string.md) | 6 |
| [arithmetic](tags/arithmetic.md) | 5 |
| [sorting](tags/sorting.md) | 5 |
| [deque](tags/deque.md) | 5 |

---

## 전체 풀이 목록 (최근 순)

| 번호 | 제목 | 티어 | 태그 | 제출날짜 |
|------|------|------|------|----------|
| 9012 | [괄호](백준/Silver/9012. 괄호) | Silver IV | data_structures, string, stack | 2025-12-27 19:05:19 |
| 2493 | [탑](백준/Gold/2493. 탑) | Gold V | data_structures, stack | 2025-12-23 22:39:49 |
| 1197 | [최소 스패닝 트리](백준/Gold/1197. 최소 스패닝 트리) | Gold IV | mst, graphs | 2025-09-01 23:04:05 |
| 11726 | [2×n 타일링](백준/Silver/11726. 2×n 타일링) | Silver III | dp | 2025-09-01 15:52:42 |
| 11047 | [동전 0](백준/Silver/11047. 동전 0) | Silver IV | greedy | 2025-09-01 15:18:52 |
| 1920 | [수 찾기](백준/Silver/1920. 수 찾기) | Silver IV | data_structures, sorting, binary_search, set, hash_set | 2025-08-31 18:49:09 |
| 2559 | [수열](백준/Silver/2559. 수열) | Silver III | prefix_sum, two_pointer, sliding_window | 2025-08-28 21:25:50 |
| 14503 | [로봇 청소기](백준/Gold/14503. 로봇 청소기) | Gold V | implementation, simulation | 2025-08-27 18:40:51 |
| 15649 | [N과 M (1)](백준/Silver/15649. N과 M （1）) | Silver III | backtracking | 2025-08-27 15:25:58 |
| 2667 | [단지번호붙이기](백준/Silver/2667. 단지번호붙이기) | Silver I | graphs, graph_traversal, bfs, dfs, grid_graph, flood_fill | 2025-08-26 19:22:40 |
| 1926 | [그림](백준/Silver/1926. 그림) | Silver I | graphs, graph_traversal, bfs, dfs, grid_graph, flood_fill | 2025-08-26 15:14:22 |
| 9655 | [돌 게임](백준/Silver/9655. 돌 게임) | Silver V | math, dp, game_theory, parity | 2025-07-24 14:27:47 |
| 10799 | [쇠막대기](백준/Silver/10799. 쇠막대기) | Silver II | data_structures, stack | 2025-07-17 15:50:05 |
| 3986 | [좋은 단어](백준/Silver/3986. 좋은 단어) | Silver IV | data_structures, stack | 2025-07-17 00:02:40 |
| 4949 | [균형잡힌 세상](백준/Silver/4949. 균형잡힌 세상) | Silver IV | data_structures, string, stack | 2025-07-16 21:59:23 |
| 11003 | [최솟값 찾기](백준/Platinum/11003. 최솟값 찾기) | Platinum V | data_structures, priority_queue, deque, deque_trick | 2025-07-12 17:58:04 |
| 5430 | [AC](백준/Gold/5430. AC) | Gold V | deque, parsing, implementation, string, data_structures | 2025-07-11 10:45:58 |
| 1021 | [회전하는 큐](백준/Silver/1021. 회전하는 큐) | Silver III | data_structures, deque | 2025-07-10 19:27:00 |
| 10866 | [덱](백준/Silver/10866. 덱) | Silver IV | implementation, data_structures, deque | 2025-07-10 15:35:50 |
| 1158 | [요세푸스 문제](백준/Silver/1158. 요세푸스 문제) | Silver IV | implementation, data_structures, queue | 2025-07-09 17:25:50 |
| 2164 | [카드2](백준/Silver/2164. 카드2) | Silver IV | data_structures, queue | 2025-07-08 23:15:06 |
| 18258 | [큐 2](백준/Silver/18258. 큐 2) | Silver IV | data_structures, queue | 2025-07-08 17:40:11 |
| 10845 | [큐](백준/Silver/10845. 큐) | Silver IV | data_structures, queue | 2025-07-03 19:07:21 |
| 1874 | [스택 수열](백준/Silver/1874. 스택 수열) | Silver II | data_structures, stack | 2025-07-03 15:04:35 |
| 10773 | [제로](백준/Silver/10773. 제로) | Silver IV | implementation, data_structures, stack | 2025-07-03 12:47:09 |
| 10828 | [스택](백준/Silver/10828. 스택) | Silver IV | implementation, data_structures, stack | 2025-07-03 12:21:20 |
| 2346 | [풍선 터뜨리기](백준/Silver/2346. 풍선 터뜨리기) | Silver III | data_structures, deque | 2025-07-02 16:20:05 |
| 5397 | [키로거](백준/Silver/5397. 키로거) | Silver II | data_structures, stack, linked_list | 2025-07-01 22:26:52 |
| 1406 | [에디터](백준/Silver/1406. 에디터) | Silver II | data_structures, stack, linked_list | 2025-07-01 15:41:04 |
| 1919 | [애너그램 만들기](백준/Bronze/1919. 애너그램 만들기) | Bronze II | implementation, string, set | 2025-06-27 19:07:33 |
| 11328 | [Strfry](백준/Bronze/11328. Strfry) | Bronze II | implementation, string | 2025-06-27 00:33:41 |
| 13300 | [방 배정](백준/Bronze/13300. 방 배정) | Bronze II | math, implementation | 2025-06-26 16:10:50 |
| 10807 | [개수 세기](백준/Bronze/10807. 개수 세기) | Bronze V | implementation | 2025-06-26 14:49:15 |
| 3273 | [두 수의 합](백준/Silver/3273. 두 수의 합) | Silver III | sorting, two_pointer | 2025-05-21 12:08:53 |
| 1475 | [방 번호](백준/Silver/1475. 방 번호) | Silver V | implementation | 2025-05-21 11:22:58 |
| 1000 | [A＋B](백준/Bronze/1000. A＋B) | Bronze V | implementation | 2025-05-21 11:22:58 |
| 2577 | [숫자의 개수](백준/Bronze/2577. 숫자의 개수) | Bronze II | math, implementation, arithmetic | 2025-05-20 22:48:19 |
| 2441 | [별 찍기 - 4](백준/Bronze/2441. 별 찍기 － 4) | Bronze III | implementation | 2025-05-16 00:05:35 |
| 10808 | [알파벳 개수](백준/Bronze/10808. 알파벳 개수) | Bronze IV | implementation, string | 2025-05-14 21:47:03 |
| 10093 | [숫자](백준/Bronze/10093. 숫자) | Bronze II | implementation | 2025-05-14 11:10:56 |
| 2443 | [별 찍기 - 6](백준/Bronze/2443. 별 찍기 － 6) | Bronze III | implementation | 2025-05-12 09:51:47 |
| 2440 | [별 찍기 - 3](백준/Bronze/2440. 별 찍기 － 3) | Bronze IV | implementation | 2025-05-12 09:17:21 |
| 2438 | [별 찍기 - 1](백준/Bronze/2438. 별 찍기 － 1) | Bronze V | implementation | 2025-05-12 09:04:31 |
| 2309 | [일곱 난쟁이](백준/Bronze/2309. 일곱 난쟁이) | Bronze I | bruteforcing, sorting | 2025-05-06 21:02:18 |
| 2587 | [대표값2](백준/Bronze/2587. 대표값2) | Bronze II | math, implementation, sorting, arithmetic | 2025-05-06 18:43:54 |
| 2576 | [홀수](백준/Bronze/2576. 홀수) | Bronze III | math, implementation | 2025-05-06 18:26:48 |
| 2490 | [윷놀이](백준/Bronze/2490. 윷놀이) | Bronze III | implementation | 2025-05-06 17:52:50 |
| 2480 | [주사위 세개](백준/Bronze/2480. 주사위 세개) | Bronze IV | math, implementation, arithmetic, case_work | 2025-05-06 17:15:27 |
| 2753 | [윤년](백준/Bronze/2753. 윤년) | Bronze V | implementation, arithmetic, math | 2025-05-05 22:41:50 |
| 2752 | [세수정렬](백준/Bronze/2752. 세수정렬) | Bronze IV | implementation, sorting | 2025-05-05 22:08:24 |
| 9498 | [시험 성적](백준/Bronze/9498. 시험 성적) | Bronze V | implementation | 2025-05-05 20:37:11 |
| 10869 | [사칙연산](백준/Bronze/10869. 사칙연산) | Bronze V | implementation, arithmetic, math | 2025-05-05 18:03:30 |
| 10171 | [고양이](백준/Bronze/10171. 고양이) | Bronze V | implementation | 2025-05-05 17:49:00 |
| 2557 | [Hello World](백준/Bronze/2557. Hello World) | Bronze V | implementation | 2025-05-05 17:26:29 |
| 10871 | [X보다 작은 수](백준/Bronze/10871. X보다 작은 수) | Bronze V | implementation | 2025-05-05 13:10:35 |
