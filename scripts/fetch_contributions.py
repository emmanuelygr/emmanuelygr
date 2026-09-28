from pathlib import Path
import json
import requests
from bs4 import BeautifulSoup

USERNAME = "emmanuelygr"
URL = f"https://github.com/users/{USERNAME}/contributions"

OUTPUT = Path("data/contributions.json")


def fetch_contributions():
    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    days = []

    for cell in soup.select("td.ContributionCalendar-day"):
        date = cell.get("data-date")
        level = cell.get("data-level")

        if date and level is not None:
            days.append({
                "date": date,
                "level": int(level),
            })

    if not days:
        raise RuntimeError(
            "No contribution data was found on GitHub."
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT.write_text(
        json.dumps(
            {
                "username": USERNAME,
                "days": days,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Fetched {len(days)} contribution days.")
    print(f"Saved to {OUTPUT}")


if __name__ == "__main__":
    fetch_contributions()
