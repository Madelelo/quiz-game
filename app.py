from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Quiz-data: spørsmål og korrekte svar
QUIZ_DATA = {
    1: {"question": "Hva er hovedstaden i Norge?", "answer": "Oslo"},
    2: {"question": "Hva er hovedstaden i Sverige?", "answer": "Stockholm"},
    3: {"question": "Hva er hovedstaden i Danmark?", "answer": "København"},
    4: {"question": "Hva er hovedstaden i Tyskland?", "answer": "Berlin"},
    5: {"question": "Hva er hovedstaden i Frankrike?", "answer": "Paris"},
    6: {"question": "Hva er hovedstaden i Italia?", "answer": "Roma"},
    7: {"question": "Hva er hovedstaden i Spania?", "answer": "Madrid"},
    8: {"question": "Hva er hovedstaden i Nederland?", "answer": "Amsterdam"},
    9: {"question": "Hva er hovedstaden i Østerrike?", "answer": "Wien"},
    10: {"question": "Hva er hovedstaden i Polen?", "answer": "Warszawa"}
}

# Velger ett spørsmål når appen starter 
RANDOM_QUESTION_ID = random.randint(1, 10)

@app.route('/')
def quiz():
    # Viser spørsmålet på nettsiden
    return render_template('quiz.html', question=QUIZ_DATA[RANDOM_QUESTION_ID]['question'])

@app.route('/check_answer', methods=['POST', 'GET'])
def check_answer():
    # Leser svaret fra skjemaet og sammenligner (lower() gjør om til små bokstaver så det ikke har noe å si)
    user_answer = request.form['answer'].lower()
    correct_answer = QUIZ_DATA[RANDOM_QUESTION_ID]['answer']

    if user_answer == correct_answer.lower():
        return render_template('result.html', status='Riktig!')
    else:
        return render_template('result.html', status='Nope, prøv igjen!')

if __name__ == '__main__':
    # Starter serveren
    app.run(debug=True)

