from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('index.html')

@app.route('/<int:num>')
def playboxes(num):
    return render_template('boxes.html', num=num)

@app.route('/<int:x>/<int:y>')
def playboxcolor(x,y):
    return render_template('playcolor.html', x=x, y=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def playboxcolorwnum(x,y,color1,color2):
    return render_template('playcolorwnum.html', x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":   
    app.run(debug=True)   
