import argparse
import json
from pathlib import Path

DATA_FILE = Path.home() / '.habit_tracker.json'

def load_habits():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_habits(habits):
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f, indent=2)


def add_habit(name: str) -> None:
    habits = load_habits()
    if name not in habits:
        habits.append(name)
        save_habits(habits)
        print(f'Habit "{name}" added.')
    else:
        print(f'Habit "{name}" already exists.')


def list_habits() -> None:
    habits = load_habits()
    if not habits:
        print('No habits yet.')
    else:
        for habit in habits:
            print(habit)


def main() -> None:
    parser = argparse.ArgumentParser(description='Habit Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new habit')
    add_parser.add_argument('name', help='Name of the habit')

    subparsers.add_parser('list', help='List all habits')

    args = parser.parse_args()

    if args.command == 'add':
        add_habit(args.name)
    elif args.command == 'list':
        list_habits()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
