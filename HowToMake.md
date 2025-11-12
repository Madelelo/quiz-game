# How to Make - Quiz Game App 🎮

En steg-for-steg guide til hvordan denne Quiz-appen er laget og kodet.

---

## 📋 Oversikt

Quiz-appen er en enkel **web-app** som bruker:

- **Python** og **Flask** for backend (serveren)
- **HTML** for frontend (det brukeren ser)

Appen viser tilfeldige spørsmål om europeiske hovedsteder, og sjekker om brukerens svar er riktig.

---

## 🎯 Steg 1: Installasjon og Oppsett

### 1.1 Installer Python

Sjekk at du har Python 3 installert:

```bash
python3 --version
```

### 1.2 Installer Flask

Flask er et lightweight web framework for Python. Installer det med pip:

```bash
pip3 install flask
```

### 1.3 Opprett prosjektmappen

```bash
mkdir quiz-game
cd quiz-game
```

### 1.4 Opprett mappene du trenger

```bash
mkdir templates
```

`templates/` mappen er der Flask lagrer HTML-filene.

---

## 🔧 Steg 2: Backend - app.py

### 2.1 Importer biblioteker

```python
from flask import Flask, render_template, request
import random
```

**Hva gjør disse?**

- `Flask` - Hovedbiblioteket for å lage web-appen
- `render_template` - For å vise HTML-filer med variabler
- `request` - For å lese data som bruker sender fra nettsiden
- `random` - For å velge tilfeldige spørsmål

### 2.2 Sett opp Flask-appen

```python
app = Flask(__name__)
```

**Hva gjør dette?**

- `Flask(__name__)` - Oppretter en Flask-applikasjon
- `__name__` - En Python-variabel som forteller Flask hvor det kjører fra. Disse må du _ikke_ endre på, da vil ikke appen kjøre.

### 2.3 Opprett quiz-data

```python
QUIZ_DATA = {
    1: {"question": "Hva er hovedstaden i Norge?", "answer": "Oslo"},
    2: {"question": "Hva er hovedstaden i Sverige?", "answer": "Stockholm"},
    # ... osv ...
    10: {"question": "Hva er hovedstaden i Polen?", "answer": "Warszawa"}
}
```

**Hva skjer her?**

- Enbruker **dictionary** for å lagre spørsmål og svar med en egen id per spørsmål.
- Hvert spørsmål inneholder `question` (spørsmålet) og `answer` (korrekt svar)

### 2.4 Velg ett tilfeldig spørsmål

```python
RANDOM_QUESTION_ID = random.randint(1, 10)
```

**Hva skjer her?**

- `random.randint(1, 10)` - Velger et tilfeldig tall mellom 1 og 10
- Hver gang appen startes, velges ett nytt spørsmål.

### 2.5 Første route: Vis spørsmålet

```python
@app.route('/')
def quiz():
    return render_template('quiz.html', question=QUIZ_DATA[RANDOM_QUESTION_ID]['question'])
```

**Hva skjer her?**

- `@app.route('/')` - Dette er "ruten" når du går til `http://127.0.0.1:5000/`
- `quiz()` - Funksjonen som kjøres når noen besøker denne ruten
- `render_template('quiz.html', question=...)` - Åpner `quiz.html` og sender spørsmålet til den
  - Spørsmålet vises som `{{question}}` i HTML-filen

NB! Her må du huske å lage html-filen `quiz.html` inne i `templates`-mappen. Se Steg 3 lengre ned for mer info.

**Eksempel:**

```
I URL-en: http://127.0.0.1:5000/
Brukeren ser: "Hva er hovedstaden i Norge?"
```

### 2.6 Andre route: Sjekk svaret

```python
@app.route('/check_answer', methods=['POST', 'GET'])
def check_answer():
    user_answer = request.form['answer'].lower()
    correct_answer = QUIZ_DATA[RANDOM_QUESTION_ID]['answer']

    if user_answer == correct_answer.lower():
        return render_template('result.html', status='Riktig!')
    else:
        return render_template('result.html', status='Nope, prøv igjen!')
```

**Hva skjer her?**

1. `@app.route('/check_answer', methods=['POST', 'GET'])` - En ny rute for å sjekke svaret

   - `methods=['POST', 'GET']` - Aksepterer både POST og GET-forespørsler

2. `user_answer = request.form['answer'].lower()` - Leser brukerens svar fra skjemaet

   - `.lower()` - Konverterer til små bokstaver (så "Oslo" og "oslo" blir det samme)

3. `correct_answer = QUIZ_DATA[RANDOM_QUESTION_ID]['answer']` - Henter det korrekte svaret

4. `if user_answer == correct_answer.lower():` - Sammenligner svarene
   - Hvis riktig: Vis "Riktig!"
   - Hvis feil: Vis "Nope, prøv igjen!"

### 2.7 Start serveren

```python
if __name__ == '__main__':
    app.run(debug=True)
```

**Hva gjør denne?**

- `if __name__ == '__main__':` - Sjekker om filen kjøres direkte (ikke importert)
- `app.run(debug=True)` - Starter serveren
  - `debug=True` - Restartet serveren automatisk når du endrer koden

---

## 🎨 Steg 3: Frontend

### Quiz-siden - quiz.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Europeiske hovedsteder</title>
  </head>
  <body>
    <div>
      <h1>Gjett hovedstaden!</h1>
      <p>{{question}}</p>
      <form action="check_answer" method="post">
        <label for="answer">Skriv inn ditt svar:</label>
        <input type="text" id="{{question_id}}" name="answer" />
        <input type="submit" value="Sjekk svaret ditt her!" />
      </form>
    </div>
  </body>
</html>
```

**Hva gjør denne?**

| Del                            | Forklaring                                                |
| ------------------------------ | --------------------------------------------------------- | --- |
| `<p>{{question}}</p>`          | **Flask-variabel** - Spørsmålet fra `app.py` vises her    |
| `<form action="check_answer">` | Sender data til `/check_answer` ruten når skjemaet sendes |     |
| `<input type="submit">`        | Knapp som sender skjemaet                                 |

---

### Resultat-siden - result.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Your result</title>
  </head>
  <body>
    <h1>{{status}}</h1>
    <a class="btn" href="/..">Tilbake</a>
  </body>
</html>
```

**Hva gjør denne?**

| Del                         | Forklaring                                            |
| --------------------------- | ----------------------------------------------------- |
| `<h1>{{status}}</h1>`       | Viser resultatet: "Riktig!" eller "Nope, prøv igjen!" |
| `<a href="/..">Tilbake</a>` | Link som tar deg tilbake til starten                  |

---

## 🚀 Steg 5: Kjør Appen

### 5.1 Start serveren

```bash
cd quiz-game
python3 app.py
```

Du vil se noe som:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 5.2 Åpne nettleseren

Gå til: `http://127.0.0.1:5000`

Du vil se spørsmålet, et tekstfelt, og en knapp ✨

---

## 📊 Hvordan Flyten Fungerer

```
1. Du åpner http://127.0.0.1:5000/
   ↓
2. Flask kjører quiz()-funksjonen
   ↓
3. Den velger et tilfeldig spørsmål fra QUIZ_DATA
   ↓
4. Den viser quiz.html med spørsmålet
   ↓
5. Du skriver inn et svar og klikker "Sjekk svaret ditt her!"
   ↓
6. Skjemaet sender POST-forespørsel til /check_answer
   ↓
7. Flask kjører check_answer()-funksjonen
   ↓
8. Den sammenligner ditt svar med det korrekte svaret
   ↓
9. Den viser result.html med "Riktig!" eller "Nope, prøv igjen!"
   ↓
10. Du klikker "Tilbake" og starter på nytt
```

---

## 🔑 Viktige Konsepter

### Ruter (Routes)

En rute er en vei i appen. For eksempel:

- `/` - Viser quizspørsmål
- `/check_answer` - Sjekker svaret

### Template-variabler

`{{variable_name}}` - Dette er en variabel som Flask fyller inn:

```html
<p>{{question}}</p>
<!-- Blir erstattet med det faktiske spørsmålet -->
```

### Dictionary/Ordbok

En måte å lagre data på:

```python
QUIZ_DATA = {
    1: {"question": "Spørsmål", "answer": "Svar"},
    2: {"question": "Spørsmål", "answer": "Svar"}
}
```

### Request/Response

- **Request** - Forespørsel fra bruker til server
- **Response** - Svar fra server til bruker (en HTML-side)

---

## 💡 Neste Steg: Forbedringer

Her er noen idéer til å utvikle appen videre:

✨ **Mulige tillegg:**

- Legg til CSS for å gjøre siden penere
- Teller hvor mange du fikk riktig
- Flere spørsmålskategorier (ikke bare hovedsteder)
- Vanskelighetsgrader
- Database i stedet for hardkodet data
- Brukerautentisering (login)

---

## 🤔 FAQ

**Q: Hva er Flask?**  
A: Et lett Python-rammeverk for å lage web-apper. Det gjør det enkelt å lage ruter og vise HTML-sider.

**Q: Hva er `{{question}}`?**  
A: En Jinja2-template variabel. Flask bytter den ut med det faktiske spørsmålet før siden vises.

**Q: Hvorfor bruker vi `.lower()`?**  
A: For å gjøre sammenligningen case-insensitive. "Oslo" og "oslo" blir behandlet som det samme.

**Q: Hva er `request.form`?**  
A: Data som brukeren sendte gjennom skjemaet.

---

**Laget med ❤️ for å lære deg Flask og webutvikling!**
