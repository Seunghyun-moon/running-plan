#!/usr/bin/env python3
import subprocess
from datetime import datetime

PLAN = [
    (0, '1주차', '5/12-5/18', '월', '조깅',    '40분 / 6:30-7:30/km / 심박수 140 이하'),
    (0, '1주차', '5/12-5/18', '화', '인터벌',  '400m x 8세트 / 2:00-2:05/400m / 총 5km'),
    (0, '1주차', '5/12-5/18', '수', '조깅',    '40분 / Easy / 심박수 140 이하'),
    (0, '1주차', '5/12-5/18', '목', '템포런',  '20분 / 5:19-5:38/km / 심박수 165-172'),
    (0, '1주차', '5/12-5/18', '금', '조깅',    '30분 / 회복 조깅'),
    (0, '1주차', '5/12-5/18', '토', '조깅',    '40분 / Easy / 내일 LSD 대비'),
    (0, '1주차', '5/12-5/18', '일', 'LSD',     '14km / 6:50-7:10/km / 심박수 140-150'),
    (1, '2주차', '5/19-5/25', '월', '조깅',    '40분 / Easy'),
    (1, '2주차', '5/19-5/25', '화', '인터벌',  '400m x 10세트 / 1:55-2:05/400m / 총 6km'),
    (1, '2주차', '5/19-5/25', '수', '조깅',    '40분 / Easy'),
    (1, '2주차', '5/19-5/25', '목', '템포런',  '25분 / 5:19-5:30/km / 심박수 165-172'),
    (1, '2주차', '5/19-5/25', '금', '조깅',    '30분 / 회복'),
    (1, '2주차', '5/19-5/25', '토', '조깅',    '20분 / 대회 전날 다리 풀기'),
    (1, '2주차', '5/19-5/25', '일', 'LSD',     '15km / 6:40-7:00/km / 심박수 140-150'),
    (2, '5/30 대회', '5/30',  '일', '하프마라톤', '존3-4 유지 / 초반 6:40/km 억제 / 목표 2:13-2:20'),
    (3, '3주차', '6/2-6/8',  '월', '휴식',     '스트레칭만'),
    (3, '3주차', '6/2-6/8',  '화', '가벼운 조깅', '30분 / 심박수 130 이하'),
    (3, '3주차', '6/2-6/8',  '수', '조깅',    '40분 / Easy'),
    (3, '3주차', '6/2-6/8',  '목', '가벼운 템포', '15분 / 5:30-5:40/km'),
    (3, '3주차', '6/2-6/8',  '금', '조깅',    '30분'),
    (3, '3주차', '6/2-6/8',  '토', '조깅',    '40분 / Easy'),
    (3, '3주차', '6/2-6/8',  '일', '완전 휴식', '대회 후 회복'),
]

DAYS = ['월', '화', '수', '목', '금', '토', '일']

def parse_range(date_str, year):
    s = date_str.strip()
    if '-' in s:
        a, b = s.split('-')
        sm, sd = map(int, a.split('/'))
        em, ed = map(int, b.split('/'))
        return datetime(year, sm, sd).date(), datetime(year, em, ed).date()
    elif '/' in s:
        m, d = map(int, s.split('/'))
        dt = datetime(year, m, d).date()
        return dt, dt
    return None, None

def notify(title, message):
    script = f'display notification "{message}" with title "{title}" sound name "Glass"'
    subprocess.run(['osascript', '-e', script])

today = datetime.now()
today_date = today.date()
today_day = DAYS[today.weekday()]

for row in PLAN:
    _, week, date_range, day, wtype, detail = row
    start, end = parse_range(date_range, today.year)
    if not start:
        continue

    if start == end and today_date == start:
        notify(f"🏃 오늘의 운동 — {wtype}", f"{week}  {detail}")
        break
    elif start <= today_date <= end and day == today_day:
        notify(f"🏃 오늘의 운동 — {wtype}", f"{week}  {detail}")
        break
