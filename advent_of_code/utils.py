import os
import requests


SESSION_ID = os.getenv("aoc_session_id")

def get_data(day=1):
    headers = {"cookie":f"session={SESSION_ID}"}

    days_data = requests.get(f"https://adventofcode.com/2022/day/{day}/input", headers=headers)

    if not os.path.exists(f"advent_of_code\day_{day}"):
        os.makedirs(f"advent_of_code\day_{day}")
    with open(f"advent_of_code\day_{day}\data.txt", mode="w") as data_file:
        data_file.write(days_data.text)


if __name__ == "__main__":
    for i in range(1, 4):
        get_data(i)