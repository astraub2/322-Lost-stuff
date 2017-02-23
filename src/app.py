from flask import Flask, make_response, render_template, request, session, redirect, url_for
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
    if request.method == 'POST':
        conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
        cur = conn.cursor()
        common_name = request.form['common_name']
        fcode = request.form['fcode']
        location=request.form['location']
        cur.execute('SELECT common_name FROM facilities WHERE common_name=%s', (common_name,))
        try:
                result = cur.fetchone()
        except ProgrammingError:
                result = None

        if result == None:
                cur.execute('SELECT fcode FROM facilities WHERE fcode=%s', (fcode,))
                try:
                        result2 = cur.fetchone()
                except ProgrammingError:
                        result2 = None
                if result2 == None:
                        cur.execute('INSERT INTO facilities(common_name, fcode, location) VALUES(%s, %s, %s)', (common_name,fcode, location))
                        conn.commit()
                        cur.close()
                        conn.close()
                        session['common_name'] = common_name
                        return render_template('valid_facility.html')
                else:
                        conn.commit()
                        cur.close()
                        conn.close()
                        return render_template('invalid_facility.html')
        else:
                conn.commit()
                cur.close()
                conn.close()
                return render_template('invalid_facility.html')
    else:
        conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
        cur = conn.cursor()
        command='SELECT * FROM facilities'
        cur.execute(command)
        res = cur.fetchall()
        processed_data = [] 
        for r in res:
                #print(r)
                processed_data.append( dict(zip(('column_name1', 'column_name2', 'column_name3', 'column_name4'), r)) )  # just making a dict out of the tuples from res
        conn.commit()
        cur.close()
        conn.close()
        session['processed'] = processed_data
        resp = make_response(render_template('add_facility.html'))
        return resp
@app.route('/add_asset', methods = ['GET', 'POST'])
def add_asset():
	conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
	cur = conn.cursor()
	cur.execute('SELECT a.asset_tag, a.alt_description, aa.arrive_dt, aa.depart_dt, \
		f.common_name, f.fcode FROM assets AS a INNER JOIN \
		asset_at AS aa ON aa.asset_fk=a.assets_pk INNER JOIN facilities AS f \
		ON f.facilities_pk=aa.facility_fk ORDER BY aa.arrive_dt ASC;')

	try:
		result = cur.fetchall()
	except ProgrammingError:
		result = None

	asset_report = []
	for r in result:
		asset_report.append(dict(zip(('asset_tag', 'description', 'arrive_dt', 'depart_dt', 'facility_name', 'facility_fcode'), r)) )  


	session['asset_report'] = asset_report
	cur.execute('SELECT common_name FROM facilities;')
	res = cur.fetchall()
	facility_data = [] 
	for r in res:
	        print(r)
	        row=dict()
	        row['common_name']=r[0]
	        facility_data.append(row)
                
	
	session['facility_name'] = facility_data
	
	if request.method == 'POST':
                print('pass 1')
                asset_tag = request.form['asset_tag']
                description = request.form['description']
                facility_name = request.form['common_name']
                arrive_dt = request.form['arrive_dt']
		cur.execute('SELECT asset_tag FROM assets WHERE asset_tag=%s', (asset_tag,))
		try:
                        print('pass 2')
                        res = cur.fetchone()
		except ProgrammingError:
			res = None
		if res == None:
                        print('pass 3')
                        cur.execute('INSERT INTO assets (asset_tag, description) VALUES (%s, %s);', (asset_tag, description))
                        print('pass 4')
                        cur.execute('INSERT INTO asset_at (assets_fk, facility_fk, arrive_dt) VALUES ((SELECT asset_pk FROM assets WHERE asset_tag=%s), \
                                (SELECT facility_pk FROM facilities WHERE facility_common_name=%s), %s);', (asset_tag, name, arrive_dt))
                        conn.commit()
                        cur.close()
                        conn.close()
                        return redirect(url_for('add_asset'))
		else:
			cur.close()
			conn.close()
			return render_template('asset_exists.html')

	return render_template('add_asset.html')


if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=8080)
