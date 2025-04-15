from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hit')
def hit():
    return "You got hit by a random Character!"

if __name__ == '__main__':
    app.run(debug=True)