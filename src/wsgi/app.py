from flask import Flask, render_template, request, session, redirect, url_for
import psycopg2
from config import dbname, dbhost, dbport, secret_key

app = Flask(__name__)

app.config["SECRET_KEY"] = secret_key

@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():
	if request.method == 'POST':
		conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
		cur = conn.cursor()
		username = request.form['username']
		password = request.form['password']
		role=request.form['role']
		cur.execute('SELECT username FROM users WHERE username=%s', (username,))
		try:
			result = cur.fetchone()
		except ProgrammingError:
			result = None

		if result == None:
			#also add role if not in roles
			cur.execute('SELECT role_pk FROM roles WHERE role_name=%s', (role,))
			try:
				results = cur.fetchone()
			except ProgrammingError:
				results = None
			if results == None:
				#role is not in table
				cur.execute('INSERT INTO roles (role_name) VALUES (%s)', (role,))
				cur.execute('SELECT role_pk FROM roles WHERE role_name=%s', (role,))
				try:
					role_pk = cur.fetchone()
				except ProgrammingError:
					role_pk = None
				if role_pk != None:
					cur.execute('INSERT INTO users (username, password, role_fk) VALUES (%s, %s, %s)', (username, password, role_pk))
					conn.commit()
					cur.close()
					conn.close()
					return render_template('user_added.html')
			else:	
				#role is in table, results=role_pk
				cur.execute('INSERT INTO users (username, password, role_fk) VALUES (%s, %s, %s)', (username, password, results))
				conn.commit()
				cur.close()
				conn.close()
				return render_template('user_added.html')
			
		else:
			cur.close()
			conn.close()
			return render_template('user_exists.html')

	return render_template('create_user.html')

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
		cur = conn.cursor()
		username = request.form['username']
		password = request.form['password']
		cur.execute('SELECT username, password FROM users WHERE username=%s AND password=%s', (username, password))
		try:
			result = cur.fetchone()
		except ProgrammingError:
			result = None

		if result == None:
			return render_template('incorrect_credentials.html')
		else:
			session['username'] = username
			session['logged_in'] = True
			return redirect(url_for('dashboard'))

	return render_template('login.html')

@app.route('/dashboard', methods = ['GET',])
def dashboard():
	return render_template('dashboard.html')
@app.route('/add_facility', methods = ['POST', 'GET'])
def add_facility():
    if request.method == 'GET':
    	conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
		cur = conn.cursor()
        command='SELECT common_name FROM facilities'
        cur.execute(command)
        res = cur.fetchall()
        processed_data = [] 
        for r in res:
                processed_data.append( dict(zip(('column_name1'), r)) )  # just making a dict out of the tuples from res
        session['session.processed_facilities'] = processed_data
        resp = make_response(render_template('add_facility.html'))
        return resp

    if request.method == 'POST':
        conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
        cur = conn.cursor()
	

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=8080)
