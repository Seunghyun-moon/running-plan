#!/usr/bin/env python3
import subprocess
from datetime import datetime

PLAN = [
    (0, '1주차', '5/12-5/18', '월', 'Easy-이지런',     '40분 / Zone 2'),
    (0, '1주차', '5/12-5/18', '화', 'Interval-인터벌', '400m × 8세트 / Zone 5'),
    (0, '1주차', '5/12-5/18', '수', 'Easy-이지런',     '40분 / Zone 2'),
    (0, '1주차', '5/12-5/18', '목', 'Tempo-템포',      '20분 / Zone 4'),
    (0, '1주차', '5/12-5/18', '금', 'Easy-이지런',     '30분 / Zone 1 / 회복'),
    (0, '1주차', '5/12-5/18', '토', 'Easy-이지런',     '40분 / Zone 2'),
    (0, '1주차', '5/12-5/18', '일', 'Long-롱런',       '14km / Zone 2'),
    (1, '2주차', '5/19-5/25', '월', 'Easy-이지런',     '40분 / Zone 2'),
    (1, '2주차', '5/19-5/25', '화', 'Interval-인터벌', '400m × 10세트 / Zone 5'),
    (1, '2주차', '5/19-5/25', '수', 'Easy-이지런',     '40분 / Zone 2'),
    (1, '2주차', '5/19-5/25', '목', 'Tempo-템포',      '25분 / Zone 4'),
    (1, '2주차', '5/19-5/25', '금', 'Easy-이지런',     '30분 / Zone 1 / 회복'),
    (1, '2주차', '5/19-5/25', '토', 'Easy-이지런',     '20분 / 대회 전날 다리 풀기'),
    (1, '2주차', '5/19-5/25', '일', 'Long-롱런',       '15km / Zone 2'),
    (2, '5/30 대회', '5/30',  '일', 'Race-레이스',     '존3-4 유지 / 초반 6:40/km 억제 / 목표 2:13-2:20'),
    (3, '3주차', '6/2-6/8',  '월', 'Rest-휴식',       '스트레칭만'),
    (3, '3주차', '6/2-6/8',  '화', 'Easy-이지런',     '30분 / Zone 1'),
    (3, '3주차', '6/2-6/8',  '수', 'Easy-이지런',     '40분 / Zone 2'),
    (3, '3주차', '6/2-6/8',  '목', 'Tempo-템포',      '15분 / Zone 3'),
    (3, '3주차', '6/2-6/8',  '금', 'Easy-이지런',     '30분 / Zone 1'),
    (3, '3주차', '6/2-6/8',  '토', 'Easy-이지런',     '40분 / Zone 2'),
    (3, '3주차', '6/2-6/8',  '일', 'Rest-휴식',       '대회 후 완전 회복'),
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
