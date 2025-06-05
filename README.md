# Habit Tracker

A simple command-line tool to help you track your habits.

## Usage

```bash
python src/habit_tracker.py add "Exercise"
python src/habit_tracker.py list
```

Habits are stored in `~/.habit_tracker.json`.

## Web UI

A minimal web interface is available that stores habits in a Supabase table named `habits`.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your Supabase credentials:

```bash
export SUPABASE_URL=<your supabase url>
export SUPABASE_KEY=<your service role or anon key>
```

3. Run the application:

```bash
python src/habit_tracker_web.py
```

The app will start a local Flask server. Visit `http://localhost:5000` to add and view habits.
