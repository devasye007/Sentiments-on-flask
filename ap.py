# app.py
from flask import Flask, render_template, request
from sentiments import analyze_sentiment

ap = Flask(__name__)

@ap.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['text']
        result = analyze_sentiment(user_input)
    return render_template('form.html', result=result)

if __name__ == '__main__':
    ap.run(debug=True)
