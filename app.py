from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/roll_dice')
def roll_dice():
    result = random.randint(1, 6)
    return render_template('roll_dice.html', result=result)
if __name__ == '__main__':
    app.run()
