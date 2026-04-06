import json
import os

from datetime import date

def load_habit() -> list:
    if not os.path.exists('tracker.json'):
        return []
    with open('tracker.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_habit(habit: str):
    habits = load_habit()
    for h in habits:
        if h['habit'] == habit:
            return False
    habits.append({'habit': habit, 'date': None})
    with open('tracker.json', 'w', encoding = 'utf-8') as f:
        json.dump(habits, f, ensure_ascii = False)
        return True

def delete_habit(habit: str):
    habits = load_habit()
    for h in habits:
        if h['habit'] == habit:
            habits.remove(h)
            with open('tracker.json', 'w', encoding = 'utf-8') as f:
                json.dump(habits, f, ensure_ascii=False)
            return True
    return False

def mark_done(habit: str):
    habits = load_habit()
    for h in habits:
        if h['habit'] == habit:
            if h['date'] != date.today().isoformat():
                h['date'] = date.today().isoformat()
                with open('tracker.json', 'w', encoding = 'utf-8') as f:
                    json.dump(habits, f, ensure_ascii=False)
                return True
    return False

