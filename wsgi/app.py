from flask import Flask, render_template, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/')
def intransrep():
    return render_template('intransrep.html')
    
@app.route('/')
def inventoryrep():
    return render_template('inventoryrep.html')

@app.route('/')
def reportfs():
    return render_template('reportfs.html')

@app.route('/')
def logout():
    return render_template('logout.html')



if __name__ == "__main__":
    app.run()
