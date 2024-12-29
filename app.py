from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

<<<<<<< HEAD
@app.route('/sum')
def sum_example():
    return str(-1 + -1)


#if __name__ == '__main__':
 #   app.run(debug=True)
=======
>>>>>>> df98f1657b95af4f79859e195a98508ef416a888
