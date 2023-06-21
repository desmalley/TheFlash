
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dad')
def dad():
    return render_template('Dogs.html')
@app.route('/Anne')
def Anne():
    return render_template('cottoncandy.html')
@app.route('/stolen')
def stolen():
    return render_template('stolencoolcode.html')
if __name__ == '__main__':
    app.run(debug=True)

