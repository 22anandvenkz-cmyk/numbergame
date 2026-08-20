from flask import Flask, render_template_string, request
import random

app = Flask(__name__)
secret_number = random.randint(1, 100)
attempts = 0

HTML = """
<!DOCTYPE html>
<html>
<head><title>Number Game</title></head>
<body style="text-align:center; font-family:Arial; margin-top:50px;">
  <h2>🎯 Number Guessing Game</h2>
  <p>I'm thinking of a number between 1 and 100</p>
  <form method="post">
    <input name="guess" type="number" min="1" max="100" required>
    <button>Guess</button>
  </form>
  <p><b>{{ message }}</b></p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    global secret_number, attempts
    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        attempts += 1
        if guess < secret_number:
            message = "Too low! Try again."
        elif guess > secret_number:
            message = "Too high! Try again."
        else:
            message = f"🎉 Correct! You found it in {attempts} attempts!"
            secret_number = random.randint(1, 100)
            attempts = 0
    return render_template_string(HTML, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
