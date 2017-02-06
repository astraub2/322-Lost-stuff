from flask import Flask,make_response, render_template, session, redirect, url_for, escape, request
import psycopg2
app = Flask(__name__)
import traceback
#app.run(host='0.0.0.0', port=8080)
#app.debug = False
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
       
       resp = make_response(render_template('intransrep.html'))
       resp.set_cookie('tdate', tdate)
       transbuilder(tdate);
   
    return resp
    
@app.route('/inventoryrep', methods = ['POST', 'GET'])
def inventoryrep():
    if request.method == 'POST':
       idate = request.form['idate']
       facility= request.form['facility']
       resp = make_response(render_template('inventoryrep.html'))
       resp.set_cookie('idate', idate)
       resp.set_cookie('facility', facility)
       invenbuilder(idate, facility)
   
    return resp


def transbuilder(tdate):
    #command="SELECT * FROM transit WHERE date=%s"(tdate)
    try:
        conn = psycopg2.connect("dbname=lost, dbhost='/tmp'")
    except psycopg2.Error as e:
        print ("I am unable to connect to the database")
        print (e)
        print (e.pgcode)
        print (e.pgerror)
        print (traceback.format_exc())
    cur = conn.cursor()
    cur.execute("""SELECT * FROM transit""")
    rows = cur.fetchall()
    for row in rows:
        print ("   ", row[0])




def invenbuilder(idate, facility):
    command="SELECT assets.assets_pk, asset_at.facility_fk, assets.alt_description,asset_at.arrive_dt FROM asset_at LEFT JOIN assets ON asset_at.assets=assets.assets_pk WHERE asset_at.facility_fk=(SELECT facilities_pk FROM facilities WHERE common_name='%s')"%(facility)
    try:
        conn = psycopg2.connect("dbname=lost, dbhost='/tmp'")
    except psycopg2.Error as e:
        print ("I am unable to connect to the database")
        print (e)
        print (e.pgcode)
        print (e.pgerror)
        print (traceback.format_exc())
        
    cur = conn.cursor()
    cur.execute(command)
##    rows = cur.fetchall()
##    for row in rows:
##        print ("   ", row[0])





@app.route('/logout')
def logout():
    return render_template('logout.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
