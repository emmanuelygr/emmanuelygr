import json
from datetime import datetime, timedelta
from pathlib import Path

INPUT = Path("data/contributions.json")
OUTPUT = Path("contrib-heatmap.svg")

CELL = 12
GAP = 4
LEFT = 40
TOP = 35

COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

# Load contribution data
with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

# Our JSON structure contains:
# {
#   "username": "emmanuelygr",
#   "days": [
#       {"date": "2026-01-01", "level": 2}
#   ]
# }

contributions = {
    item["date"]: int(item["level"])
    for item in data["days"]
}

if not contributions:
    raise SystemExit("No contribution data found.")

dates = sorted(contributions.keys())

end_date = datetime.strptime(dates[-1], "%Y-%m-%d")
start_date = end_date - timedelta(days=364)

# Align the first day to Sunday
start_date -= timedelta(days=(start_date.weekday() + 1) % 7)

weeks = []
current = start_date

while current <= end_date:
    week = []

    for day in range(7):
        date = current + timedelta(days=day)
        date_str = date.strftime("%Y-%m-%d")

        level = contributions.get(date_str, 0)

        week.append((date_str, level))

    weeks.append(week)
    current += timedelta(days=7)

width = LEFT + len(weeks) * (CELL + GAP)
height = TOP + 7 * (CELL + GAP) + 20

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<style>
    .cell {{
        animation: appear 0.4s ease-out both;
        transform-box: fill-box;
        transform-origin: center;
    }}

    .cell:hover {{
        stroke: #58a6ff;
        stroke-width: 1;
    }}

    @keyframes appear {{
        from {{
            opacity: 0;
            transform: scale(0.5);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}

    .title {{
        fill: #8b949e;
        font-family: monospace;
        font-size: 12px;
    }}
</style>

<text x="0" y="15" class="title">
    $ git contributions --year
</text>
'''

for week_index, week in enumerate(weeks):

    x = LEFT + week_index * (CELL + GAP)

    for day_index, (date_str, level) in enumerate(week):

        y = TOP + day_index * (CELL + GAP)

        color = COLORS[min(level, len(COLORS) - 1)]

        delay = week_index * 0.015

        svg += f'''
<rect
    class="cell"
    x="{x}"
    y="{y}"
    width="{CELL}"
    height="{CELL}"
    rx="2"
    fill="{color}"
    style="animation-delay:{delay:.3f}s"
>
    <title>{date_str} — level {level}</title>
</rect>
'''

svg += '''
</svg>
'''

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Created {OUTPUT}")
