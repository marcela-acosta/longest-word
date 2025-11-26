# wsgi.py

# pylint: disable=missing-docstring

from flask import Flask, render_template, request
from longest_word.game import Game # You need to import your Game class

# --- CRITICAL FIX: App Definition ---
app = Flask(__name__)

@app.route('/')
def home():
    # You should probably initialize the game here and pass the grid to the template
    game = Game()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    # Create a game instance
    game = Game()

    # Flask form data is always a string, so we list() it to simulate the grid setup
    game.grid = list(request.form['grid'])

    word = request.form['word']

    # Check if the word is valid
    is_valid = game.is_valid(word)

    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
