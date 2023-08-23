from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def display():

    if 'count' and 'visit' not in session:
        count = 0
        visit = 0
    else:
        count = session['count']
        visit = session['visit']

    count += 1
    visit += 1
    session['count'] = count
    session['visit'] = visit
    return render_template('display.html')

@app.route('/destroy_session')
def clear():    
    session.clear()
    return redirect('/')

@app.route('/count', methods=['POST'])
def plustwo():
    count = session['count']
    if 'value' not in session:
        value =0
    else:
        value = session['value']
    count += 2
    value += 2
    session['count'] = count
    session['value'] = value
    return render_template('display.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/increase', methods=['POST'])
def increase():
    if 'value' not in session:
        value =0
    else:
        value = session['value']

    count = session['count']
    number = int(request.form['number'])
    count += number
    value += number
    session['count'] = count
    session['value'] = value
    return render_template('display.html')

if __name__=="__main__":   
    app.run(debug=True)   
