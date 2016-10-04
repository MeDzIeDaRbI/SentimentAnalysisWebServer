from flask import Flask
from flask import render_template
from flask import request, redirect

import vaderSentiment as sentence
text = ''
output = None
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/output')
def output():
    global output
    output = sentence.sentiment(text)
    print output
    neg = output['neg']
    neu = output['neu']
    pos = output['pos']
    compound = output['compound']
    return render_template('output.html',
                           text=text,
                           neg=neg,
                           pos=pos,
                           neu=neu,
                           compound=compound)


@app.route('/sentimentAnalysis', methods = ['POST'])
def sentimentAnalysis():
    global text
    text = request.form['textarea']

    print("The input text is:\n" + text)
    return redirect('/output')

if __name__ == '__main__':
	app.run(debug=True)
