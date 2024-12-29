from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/sum')
def sum_example():
    return str(-1 + -1)


#if __name__ == '__main__':
 #   app.run(debug=True)
