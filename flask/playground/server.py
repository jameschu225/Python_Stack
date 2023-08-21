from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:num>')
def playboxes(num):
    return render_template('boxes.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def playboxcolor(num,color):
    return render_template('playcolor.html', num=num, color=color)

if __name__=="__main__":   
    app.run(debug=True)   
