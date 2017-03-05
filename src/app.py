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
                        return redirect(url_for('add_facility'))
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
        if request.method == 'POST':
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                asset_tag = request.form['asset_tag']
                #print('pass 1')
                description = request.form['description']
                facility_name = request.form['common_name']
                arrive_dt = request.form['arrive_dt']
                cur.execute('SELECT asset_tag FROM assets WHERE asset_tag=%s', (asset_tag,))
                try:
                        res = cur.fetchone()
                        #print('pass 2')
                except ProgrammingError:
                        res = None
                if res == None:
                        cur.execute('INSERT INTO assets (asset_tag, alt_description) VALUES (%s, %s);', (asset_tag, description))
                        #print('pass 3')

                        cur.execute('INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES ((SELECT assets_pk FROM assets WHERE asset_tag=%s), \
                                (SELECT facilities_pk FROM facilities WHERE common_name=%s), %s);', (asset_tag, facility_name, arrive_dt))
                        #print('pass 4')
                        conn.commit()
                        cur.close()
                        conn.close()
                        return redirect(url_for('add_asset'))
                else:
                        cur.close()
                        conn.close()
                        return render_template('asset_exists.html')
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
        

        return render_template('add_asset.html')
@app.route('/dispose_asset', methods = ['GET', 'POST'])
def dispose_asset():
        if request.method == 'POST':
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                asset_tag = request.form['asset_tag']
                dispose_dt = request.form['dispose_dt']
                cur.execute('SELECT disposed_dt FROM assets WHERE asset_tag=%s', (asset_tag,))
                try:
                        res = cur.fetchone()
                except ProgrammingError:
                        res = None
                if res == None:
                        cur.close()
                        conn.close()
                        return render_template('asset_DNE.html')
                if res[0] != None:
                        cur.close()
                        conn.close()
                        return render_template('asset_AD.html')
                
                else:
                        
                        #update dispose on asset and change asset_at
                        cur.execute('UPDATE assets SET disposed_dt=%s WHERE asset_tag=%s;', (dispose_dt, asset_tag))
                        cur.execute('UPDATE asset_at SET depart_dt=%s WHERE asset_fk=(SELECT assets_pk FROM assets WHERE asset_tag=%s)', (dispose_dt, asset_tag))
                        conn.commit()
                        cur.close()
                        conn.close()
                        return redirect(url_for('dashboard'))
                        
        else:
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                username=session['username']
                cur.execute('SELECT role_name FROM users JOIN roles ON users.role_fk=roles.role_pk WHERE username=%s', (username,))
                try:
                        result = cur.fetchone()
                except ProgrammingError:
                        result = None

                if result != ('Logistics Officer',):
                        #print (result)
                        return render_template('invalid_credentials.html')
                else:
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
                                #print(r)
                                row=dict()
                                row['common_name']=r[0]
                                facility_data.append(row)
                                
                        
                        session['facility_name'] = facility_data
                        

                        return render_template('dispose_asset.html')
                        
@app.route('/asset_report', methods = ['GET', 'POST'])
def asset_report():    
        if request.method == 'POST':
                date = request.form['dt']
                
                facility = request.form['facility']
                
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                if facility== '':
                        #no specified facility
                        cur.execute('SELECT a.asset_tag, a.alt_description, aa.arrive_dt, aa.depart_dt, f.common_name, f.fcode FROM assets AS a INNER JOIN asset_at AS aa ON a.assets_pk=aa.asset_fk \
                        INNER JOIN facilities AS f ON f.facilities_pk=aa.facility_fk WHERE aa.arrive_dt<=%s AND (aa.depart_dt>=%s OR aa.depart_dt IS NULL);', (date, date))

                        try:
                                result = cur.fetchall()
                        except ProgrammingError:
                                result = None

                        asset_rreport = []
                        for r in result:
                                asset_rreport.append(dict(zip(('asset_tag', 'description', 'arrive_dt', 'depart_dt', 'facility_name', 'facility_fcode'), r)) )  
                        session['asset_rreport'] = asset_rreport
                        cur.execute('SELECT common_name FROM facilities;')
                        res = cur.fetchall()
                        facility_data = [] 
                        for r in res:
                                row=dict()
                                row['common_name']=r[0]
                                facility_data.append(row)
                        session['facility_name'] = facility_data
                        cur.close()
                        conn.close()
                        return render_template('asset_report.html')
                else:
                        #specified facility
                        
                        cur.execute('SELECT a.asset_tag, a.alt_description, aa.arrive_dt, aa.depart_dt, f.common_name, f.fcode FROM assets AS a INNER JOIN asset_at AS aa ON a.assets_pk=aa.asset_fk \
                        INNER JOIN facilities AS f ON f.facilities_pk=aa.facility_fk WHERE aa.arrive_dt<=%s AND (aa.depart_dt>=%s OR aa.depart_dt IS NULL) AND f.common_name=%s;', (date, date, facility))
                        try:
                                result = cur.fetchall()
                        except ProgrammingError:
                                result = None

                        asset_rreport = []
                        for r in result:
                                asset_rreport.append(dict(zip(('asset_tag', 'description', 'arrive_dt', 'depart_dt', 'facility_name', 'facility_fcode'), r)) )  
                        session['asset_rreport'] = asset_rreport
                        cur.execute('SELECT common_name FROM facilities;')
                        res = cur.fetchall()
                        facility_data = [] 
                        for r in res:
                                row=dict()
                                row['common_name']=r[0]
                                facility_data.append(row)
                        session['facility_name'] = facility_data
                        cur.close()
                        conn.close()
                        return render_template('asset_report.html')
                
        if request.method == 'GET':
                asset_rreport = []
                session['asset_rreport'] = asset_rreport
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                cur.execute('SELECT common_name FROM facilities;')
                res = cur.fetchall()
                facility_data = [] 
                for r in res:
                        row=dict()
                        row['common_name']=r[0]
                        facility_data.append(row)
                        

                session['facility_name'] = facility_data
                conn.commit()
                cur.close()
                conn.close()
                return render_template('asset_report.html')

                
@app.route('/transit_request', methods = ['GET', 'POST'])
def transit_request():
        if request.method == 'POST':
                asset_tag=request.form['asset_tag']
                date = request.form['dispose_dt']
                source = request.form['source']
                destination=request.form['destination']
                username=session['username']
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                  
                ##add transitrequest to DB
                cur.execute('INSERT INTO transfer (asset_fk, requestor_fk, request_dt, source_fk, destination_fk) VALUES\
                            ((SELECT assets.assets_pk FROM assets WHERE asset_tag= %s), (SELECT users.user_pk FROM users WHERE username=%s),\
                            %s, (SELECT facilities.facilities_pk FROM facilities WHERE common_name=%s), (SELECT facilities.facilities_pk FROM facilities WHERE common_name=%s))\
                            ;', (asset_tag, username, date, source, destination))
                conn.commit()
                cur.close()
                conn.close()
                session['transfer_asset']=asset_tag
                return render_template('successful_request.html')
                
        else:
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                username=session['username']
                cur.execute('SELECT role_name FROM users JOIN roles ON users.role_fk=roles.role_pk WHERE username=%s', (username,))
                try:
                        result = cur.fetchone()
                except ProgrammingError:
                        result = None

                if result != ('Logistics Officer',):
                        #print (result)
                        return render_template('invalid_credentials.html')
                else:
                        cur.execute('SELECT asset_tag FROM assets;')
                        res = cur.fetchall()
                        asset_tag = [] 
                        for r in res:
                                row=dict()
                                row['tag']=r[0]
                                asset_tag.append(r)
                                

                        session['asset_tags'] = asset_tag
                        return render_template('transit_request.html')
@app.route('/approve_req', methods = ['GET', 'POST'])
def approve_req():
        if request.method == 'POST':
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                response_dt=request.form['response_dt']
                request_id = request.form['request_id']
                session['request_approval'] = request_id
                approval = request.form['approval']
                username=session['username']
                cur.execute('SELECT transfer_pk FROM transfer WHERE transfer_pk=%s', (request_id,))
                try:
                        result = cur.fetchone()
                except ProgrammingError:
                        result = None

                if result ==None:
                        return render_template('transit_reqDNE.html')
                else:
                        if approval=='Confirm':
                                cur.execute('INSERT INTO transit (asset_fk, transfer_fk, source_fk, destination_fk) VALUES\
                                            ((SELECT asset_fk FROM transfer WHERE transfer_pk=%s), %s, (SELECT source_fk FROM transfer WHERE transfer_pk=%s)\
                                            , %s)', (request_id, request_id,request_id,request_id))
                                cur.execute('UPDATE transfer SET approver_fk=(SELECT users.user_pk FROM users WHERE username=%s)\
                                            ,approve_dt=%s WHERE transfer_pk=%s;',(username, response_dt, request_id))          

                                
                                conn.commit()
                                cur.close()
                                conn.close()
                                return render_template('dashboard.html')
                        else:
                                cur.execute('DELETE FROM transfer WHERE transfer_pk=%s', (request_id,))
                                conn.commit()
                                cur.close()
                                conn.close()
                                return render_template('dashboard.html')
                        
        else:
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                username=session['username']
                cur.execute('SELECT role_name FROM users JOIN roles ON users.role_fk=roles.role_pk WHERE username=%s', (username,))
                try:
                        result = cur.fetchone()
                except ProgrammingError:
                        result = None

                if result != ('Facilities Officer',):
                        return render_template('invalid_credentials2.html')
                else:
                        
                        cur.execute('SELECT transfer_pk, asset_fk, requestor_fk, source_fk, destination_fk, request_dt FROM transfer WHERE approve_dt IS NULL ;')
                        try:
                                result = cur.fetchall()
                        except ProgrammingError:
                                result = None

                        current_req = []
                        for r in result:
                                current_req.append(dict(zip(('req_tag', 'asset_id', 'requestor', 'source', 'destination', 'request_dt'), r)) )  
                        session['current_req'] = current_req
                        conn.commit()
                        cur.close()
                        conn.close()
                        return render_template('approve_req.html')
@app.route('/update_transit', methods = ['GET', 'POST'])
def update_transit():
        if request.method == 'POST':
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
        else:
                conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
                cur = conn.cursor()
                username=session['username']
                cur.execute('SELECT role_name FROM users JOIN roles ON users.role_fk=roles.role_pk WHERE username=%s', (username,))
                try:
                        result = cur.fetchone()
                except ProgrammingError:
                        result = None

                if result != ('Logistics Officer',):
                        #print (result)
                        return render_template('invalid_credentials.html')
                else:
                        cur.execute('SELECT asset_tag FROM assets JOIN transit WHERE asset_pk=asset_fk WHERE transit.unload_dt IS NULL;')
                        res = cur.fetchall()
                        transit_tag = [] 
                        for r in res:
                                row=dict()
                                row['tag']=r[0]
                                transit_tag.append(r)
                                

                        session['transit_tags'] = transit_tag
                        return render_template('update_transit.html')
        
        
                        




                

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=8080)
