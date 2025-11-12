# Quiz Game App

Dette er en enkel Flask-app for diverse quiz-spørsmål. I første omgang hovedsteder, men vi håper å lage flere kategorier etter hvert.

## Installasjon

1. Klon repositoriet:

```bash
git clone https://github.com/madeleine/quiz-game.git
cd quiz-game
```

2. Opprett og aktiver virtuelt miljø:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installer avhengigheter:

```bash
pip3 install flask
```

## Kjøring

Start serveren:

```bash
python3 app.py
```

Åpne nettleseren og gå til:

```
http://127.0.0.1:5000
```

## Hvordan det fungerer

- Appen viser ett tilfeldig spørsmål om europeiske hovedsteder
- Brukeren skriver inn sitt svar
- Appen sjekker om svaret er riktig
