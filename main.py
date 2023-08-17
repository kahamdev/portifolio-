from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    name='home page'
    return render_template('base.html', name=name)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
