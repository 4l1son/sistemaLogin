from flask import Flask, render_template
from login import validate
from model import login_model
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_cadastrado():
    return validate(login_model)



if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)