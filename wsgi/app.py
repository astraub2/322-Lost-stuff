from flask import Flask, render_template, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login')
def loginagain():
    return render_template('login.html')

@app.route('/intransrep')
def intransrep():
    return render_template('intransrep.html')
    
@app.route('/inventoryrep')
def inventoryrep():
    return render_template('inventoryrep.html')

@app.route('/reportfs')
def reportfs():
    return render_template('reportfs.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')



if __name__ == "__main__":
    app.run()
