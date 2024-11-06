from flask import Flask, render_template, redirect, request, session
import json
from datetime import datetime

app = Flask(__name__)

start_date = datetime(2024, 11, 5)
current_day = (datetime.now() - start_date).days + 1

max_guesses = 5  # Number of guesses allowed per day

app.secret_key = 'super secret key that no one will ever guess haha'

def get_day_data(day):
    try:
        with open(f'private/days/{day}/data.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None  # Return None instead of redirecting
    except Exception as e:
        print(e)
        return None

@app.route('/')
def home():
    return redirect(f'/{current_day}')

@app.route('/<int:day>')
def day(day):
    if day > current_day:
        return redirect(f'/{current_day}')

    day_data = get_day_data(day)
    if day_data is None:
        return redirect('/')  # Redirect if data is missing or corrupted

    if 'attempts' not in session:
        session['attempts'] = {}

    # Ensure that day attempts are initialized as a list
    if not isinstance(session['attempts'].get(str(day)), list):
        session['attempts'][str(day)] = [0, False]

    attempts = session['attempts'][str(day)][0]
    correct = session['attempts'][str(day)][1]
    session.modified = True

    hints = [
        ('1 - Type', f"1 - {day_data['hint1']}"),
        ('2 - Known for', f"2 - {day_data['hint2']}"),
        ('3 - Popularity', f"3 - {day_data['hint3']}"),
        ('4 - Origin/Source', f"4 - {day_data['hint4']}"),
        ('5 - Reveal Image', f"5 - {day_data['hint5']}"),
    ]

    return render_template(
        'index.html',
        day=day,
        soundalike=day_data['soundalike'],
        hints=hints,
        guess=attempts,
        correct=correct,
        max_guesses=max_guesses,
        current_day=current_day
    )

@app.route('/<int:day>/guess', methods=['POST'])
def guess(day):
    day_data = get_day_data(day)
    if day_data is None:
        return redirect(f'/{day}')

    correct_answers = day_data['answers']
    user_guess = request.form.get('guess', '').lower()

    if 'attempts' not in session:
        session['attempts'] = {}

    if not isinstance(session['attempts'].get(str(day)), list):
        session['attempts'][str(day)] = [0, False]

    if session['attempts'][str(day)][0] >= max_guesses or session['attempts'][str(day)][1]:
        return redirect(f'/{day}')

    session['attempts'][str(day)][0] += 1
    session.modified = True

    if user_guess in correct_answers:
        session['attempts'][str(day)] = [session['attempts'][str(day)][0], True]
        session.modified = True
        return redirect(f'/{day}')
    else:
        return redirect(f'/{day}')
    
@app.route('/<int:day>/skip', methods=['POST'])
def skip(day):
    if 'attempts' not in session:
        session['attempts'] = {}

    if not isinstance(session['attempts'].get(str(day)), list):
        session['attempts'][str(day)] = [0, False]

    session['attempts'][str(day)][0] += 1
    session.modified = True

    return redirect(f'/{day}')

@app.route('/<int:day>/next', methods=['POST'])
def next_day(day):
    return redirect(f'/{day + 1}')

@app.route('/<int:day>/prev', methods=['POST'])
def prev_day(day):
    return redirect(f'/{day - 1}')

if __name__ == '__main__':
    app.run()
