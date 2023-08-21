from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hi(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def multiword(num, word):
    result = ""
    for i in range(num):
        result += f"{i}, {word} "
    return result

if __name__ == '__main__':
    app.run(debug=True)