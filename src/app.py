from flask import Flask,make_response, render_template, session, redirect, url_for, escape, request
from config import dbname, dbhost, dbport, lost_priv, lost_pub, user_pub, prod_pub
import json
import psycopg2
app = Flask(__name__)
import traceback
#app.run(host='0.0.0.0', port=8080)
#app.debug = False
app.secret_key = "super secret key"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/reportfs', methods = ['POST', 'GET'])
def reportfs():
   if request.method == 'POST':
       user = request.form['nm']
       
       resp = make_response(render_template('reportfs.html'))
       resp.set_cookie('userID', user)
   
   return resp

@app.route('/getinven')
def getinven():
   date = request.cookies.get('idate')
   facility = request.cookies.get('facility')
   return '<h1>Date: '+date+'</h1>' '<br><h1>Facility: '+facility+'</h1>'

@app.route('/gettrans')
def gettrans():
   date = request.cookies.get('idate')
   return '<h1>Date: '+date+'</h1>'

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return ('<h1>Username: '+name+
    '</h1>' '<br><button type="button" onclick="javascript:history.back()">Back</button>')
   
@app.route('/login')
def loginagain():
    return render_template('login.html')

@app.route('/intransrep', methods = ['POST', 'GET'])
def intransrep():
    if request.method == 'POST':
       tdate = request.form['tdate']
    if(tdate==''):
        command="SELECT * FROM asset_on"
        try:
            conn = psycopg2.connect("dbname=lost host='/tmp/'")
        except psycopg2.Error as e:
            print ("I am unable to connect to the database")
        cur = conn.cursor()
        cur.execute(command)
        res = cur.fetchall()  # this is the result of the database query "SELECT column_name1, column_name2 FROM some_table"
        processed2_data = []   # this is the processed result I'll stick in the session (or pass to the template)
        for r in res:
            print(r)
            processed2_data.append( dict(zip(('column_name5', 'column_name6', 'column_name7', 'column_name8', 'column_name9'), r)) )  # just making a dict out of the tuples from res
        session['processed_data_trans'] = processed2_data
        resp = make_response(render_template('intransrep.html'))
    else:
        command="SELECT * FROM asset_on WHERE load_dt<=%s"(tdate)
        try:
            conn = psycopg2.connect("dbname=lost host='/tmp/'")
        except psycopg2.Error as e:
            print ("I am unable to connect to the database")
        cur = conn.cursor()
        cur.execute(command)
        res = cur.fetchall()  # this is the result of the database query "SELECT column_name1, column_name2 FROM some_table"
        processed2_data = []   # this is the processed result I'll stick in the session (or pass to the template)
        for r in res:
            print(res)
            processed2_data.append( dict(zip(('column_name5', 'column_name6', 'column_name7', 'column_name8', 'column_name9'), r)) )  # just making a dict out of the tuples from res
        session['processed_data_trans'] = processed2_data
        resp = make_response(render_template('intransrep.html'))
 
    return resp
    
@app.route('/inventoryrep', methods = ['POST', 'GET'])
def inventoryrep():
    if request.method == 'POST':
        idate = request.form['idate']
        facility= request.form['facility']
        if(idate==''):
            command="SELECT assets.assets_pk, asset_at.facility_fk, assets.alt_description,asset_at.arrive_dt FROM asset_at LEFT JOIN assets ON asset_at.asset_fk=assets.assets_pk WHERE asset_at.facility_fk=(SELECT facilities_pk FROM facilities WHERE common_name='%s')"%(facility)
            try:
                conn = psycopg2.connect("dbname=lost host='/tmp/'")
            except psycopg2.Error as e:
                print ("I am unable to connect to the database")
                   
            cur = conn.cursor()
            cur.execute(command)
            res = cur.fetchall()  # this is the result of the database query "SELECT column_name1, column_name2 FROM some_table"
            processed_data = []   # this is the processed result I'll stick in the session (or pass to the template)
            for r in res:
                processed_data.append( dict(zip(('column_name1', 'column_name2', 'column_name3', 'column_name4'), r)) )  # just making a dict out of the tuples from res
                session['processed_data_session_name'] = processed_data
                resp = make_response(render_template('inventoryrep.html'))



        else:
            command="SELECT assets.assets_pk, asset_at.facility_fk, assets.alt_description,asset_at.arrive_dt FROM asset_at LEFT JOIN assets ON asset_at.asset_fk=assets.assets_pk WHERE asset_at.arrive_dt<='%s' AND asset_at.facility_fk=(SELECT facilities_pk FROM facilities WHERE common_name='%s')"%(idate, facility)
            try:
                conn = psycopg2.connect("dbname=lost host='/tmp/'")
            except psycopg2.Error as e:
                print ("I am unable to connect to the database")
                    
            cur = conn.cursor()
            cur.execute(command)
            res = cur.fetchall()  # this is the result of the database query "SELECT column_name1, column_name2 FROM some_table"
            processed_data = []   # this is the processed result I'll stick in the session (or pass to the template)
            for r in res:
                processed_data.append( dict(zip(('column_name1', 'column_name2', 'column_name3', 'column_name4'), r)) )  # just making a dict out of the tuples from res
            session['processed_data_session_name'] = processed_data
            resp = make_response(render_template('inventoryrep.html'))
   


   
    return resp


def transbuilder(tdate):
    if(tdate==''):
        command="SELECT * FROM asset_on"
        try:
            conn = psycopg2.connect("dbname=lost host='/tmp/'")
        except psycopg2.Error as e:
            print ("I am unable to connect to the database")
            print (e)
            print (e.pgcode)
            print (e.pgerror)
            print (traceback.format_exc())
        cur = conn.cursor()
        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            print ("   ", row[0])
    else:
        command="SELECT * FROM asset_on WHERE load_dt<=%s"(tdate)
        try:
            conn = psycopg2.connect("dbname=lost host='/tmp/'")
        except psycopg2.Error as e:
            print ("I am unable to connect to the database")
            print (e)
            print (e.pgcode)
            print (e.pgerror)
            print (traceback.format_exc())
        cur = conn.cursor()
        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            print ("   ", row[0])





def invenbuilder(idate, facility):
    command="SELECT assets.assets_pk, asset_at.facility_fk, assets.alt_description,asset_at.arrive_dt FROM asset_at LEFT JOIN assets ON asset_at.asset_fk=assets.assets_pk WHERE asset_at.facility_fk=(SELECT facilities_pk FROM facilities WHERE common_name='%s')"%(facility)
    try:
        conn = psycopg2.connect("dbname=lost host='/tmp/'")
    except psycopg2.Error as e:
        print ("I am unable to connect to the database")
        print (e)
        print (e.pgcode)
        print (e.pgerror)
        print (traceback.format_exc())
        
    cur = conn.cursor()
    cur.execute(command)
    res = cur.fetchall()  # this is the result of the database query "SELECT column_name1, column_name2 FROM some_table"
    processed_data = []   # this is the processed result I'll stick in the session (or pass to the template)
    for r in res:
        processed_data.append( dict(zip(('column_name1', 'column_name2'), r)) )  # just making a dict out of the tuples from res
    session['processed_data_session_name'] = processed_data
    





@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/rest')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html',dbname=dbname,dbhost=dbhost,dbport=dbport)

@app.route('/rest/list_products', methods=('POST',))
def list_products():
    """This function is huge... much of it should be broken out into other supporting
        functions"""
    
    # Check maybe process as plaintext
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    # Unmatched, take the user somewhere else
    else:
        redirect('rest')
    
    # Setup a connection to the database
    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    # If execution gets here we have request json to work with
    # Do I need to handle compartments in this query?
    if len(req['compartments'])==0:
        print("have not compartment")
        # Just handle vendor and description
        SQLstart = """select vendor,description,string_agg(c.abbrv||':'||l.abbrv,',')
from products p
left join security_tags t on p.product_pk=t.product_fk
left join sec_compartments c on t.compartment_fk=c.compartment_pk
left join sec_levels l on t.level_fk=l.level_pk"""
        if req['vendor']=='' and req['description']=='':
            # No filters, add the group by and query is ready to go
            SQLstart += " group by vendor,description"
            cur.execute(SQLstart)
        else:
            if not req['vendor']=='' and not req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                req['description']="%"+req['description']+"%"
                SQLstart += " where description ilike %s and vendor ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['description'],req['vendor']))
            elif req['vendor']=='':
                req['description']="%"+req['description']+"%"
                SQLstart += " where description ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['description'],))
            elif req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                SQLstart += " where vendor ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['vendor'],))
    else:
        print("have compartment %s"%len(req['compartments']))
        # Need to handle compartments too
        SQLstart = """select vendor,description,string_agg(c.abbrv||':'||l.abbrv,',')
from security_tags t
left join sec_compartments c on t.compartment_fk=c.compartment_pk
left join sec_levels l on t.level_fk=l.level_pk
left join products p on t.product_fk=p.product_pk
where product_fk is not NULL and c.abbrv||':'||l.abbrv = ANY(%s)"""
        if req['vendor']=='' and req['description']=='':
            # No filters, add the group by and query is ready to go
            SQLstart += " group by vendor,description,product_fk having count(*)=%s"
            cur.execute(SQLstart,(req['compartments'],len(req['compartments'])))
        else:
            if not req['vendor']=='' and not req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                req['description']="%"+req['description']+"%"
                SQLstart += " and description ilike %s and vendor ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['description'],req['vendor'],len(req['compartments'])))
            elif req['vendor']=='':
                req['description']="%"+req['description']+"%"
                SQLstart += " and description ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['description'],len(req['compartments'])))
            elif req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                SQLstart += " and vendor ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['vendor'],len(req['compartments'])))
    
    # One of the 8 cases should've run... process the results
    dbres = cur.fetchall()
    listing = list()
    for row in dbres:
        e = dict()
        e['vendor'] = row[0]
        e['description'] = row[1]
        if row[2] is None:
            e['compartments'] = list()
        else:
            e['compartments'] = row[2].split(',')
        listing.append(e)
    
    # Prepare the response
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['listing'] = listing
    data = json.dumps(dat)
    
    conn.close()
    return data
@app.route('/rest/lost_key', methods=('POST',))
def lost_key():
    if request.method=='POST' and 'arguments' in request.form:
        req='key'	
	    
@app.route('/rest/suspend_user', methods=('POST',))
def suspend_user():
    # Try to handle as plaintext
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])

    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data
@app.route('/rest/activate_user', methods=('POST',))
def activate_user():
	# Try to handle as plaintext
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])

    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data

@app.route('/rest/add_asset')
def add_asset():
	if request.method == "POST" and "arguments" in request.form:
		req = json.loads(request.form["arguments"])
		dat = dict()
		dat["timestamp"] = req["timestamp"]
		##TODO
		dat["result"] = "OK"
		data = json.dumps(dat)
		return data
	    
@app.route('/goodbye')
def goodbye():
    if request.method=='GET' and 'mytext' in request.args:
        return render_template('goodbye.html',data=request.args.get('mytext'))

    # request.form is only populated for POST messages
    if request.method=='POST' and 'mytext' in request.form:
        return render_template('goodbye.html',data=request.form['mytext'])
    return render_template('index.html')



if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=8080)
