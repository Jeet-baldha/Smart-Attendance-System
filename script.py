from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/reg')
def reg():
    return render_template('registration-form.html')

if __name__ == '__main__':
    app.run()





