from flask import Flask, render_template, request
from sentiments import sentiment_score

ap = Flask(__name__)


@ap.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        result = sentiment_score(text)

        return render_template(
            'results.html',
            text = text,
            polarity = result['polarity'],
            subjectivity = result['subjectivity'],
            label = result['label']
        )

    return render_template('form.html')

if __name__ == '__main__':
    ap.run(debug=True)