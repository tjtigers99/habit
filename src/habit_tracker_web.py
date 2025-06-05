import os
from flask import Flask, render_template_string, request, redirect, url_for
from supabase import create_client, Client

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError('SUPABASE_URL and SUPABASE_KEY environment variables must be set')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        habit_name = request.form.get('name')
        if habit_name:
            supabase.table('habits').insert({'name': habit_name}).execute()
        return redirect(url_for('index'))

    response = supabase.table('habits').select('name').execute()
    habits = [item['name'] for item in response.data] if response.data else []

    html = '''
    <h1>Habit Tracker</h1>
    <form method="post">
        <input type="text" name="name" placeholder="New Habit" required>
        <button type="submit">Add Habit</button>
    </form>
    <ul>
    {% for habit in habits %}
        <li>{{ habit }}</li>
    {% endfor %}
    </ul>
    '''
    return render_template_string(html, habits=habits)


if __name__ == '__main__':
    app.run(debug=True)
