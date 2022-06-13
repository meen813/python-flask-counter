from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "this is  a counter"



@app.route('/')
def counter():

    if 'counter' not in session:
        session['counter'] = 0

    return render_template('index.html')

@app.route('/counter/<int:counter>')
def manipulation_counter(counter):

    session[f'counter'] += 1

    return redirect('/')

@app.route('/destory_session')
def reset_counters():

    session.clear()

    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)


