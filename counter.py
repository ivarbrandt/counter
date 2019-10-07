from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ello'

@app.route('/')
def user():
    if 'views' in session:
        session['views'] += 1
    else: 
        session['views'] = 1
    return render_template('counter.html')

@app.route('/show', methods = ['POST'])
def destroy():
    session.pop('views')
    return redirect('/')
    


if __name__=="__main__":
    app.run(debug=True)