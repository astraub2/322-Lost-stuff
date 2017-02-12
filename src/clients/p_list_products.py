# This client can be used to interact with the LOST interface prior to encryption
# implementation

import sys
import json
import datetime

# URL lib parts
from urllib.request import Request, urlopen
from urllib.parse   import urlencode

def main():
    # Check the CLI arguments
    if len(sys.argv)<5 :
        print("Usage: python3 %s <url> <vendor> <description> <compartments>"%sys.argv[0])
        return
    
    # Prep the arguments blob
    args = dict()
    args['timestamp'] = datetime.datetime.utcnow().isoformat()
    if sys.argv[2]=='':
        args['vendor']=''
    else:
        args['vendor']  = sys.argv[2]
    if sys.argv[3]=='':
        args['description'] = ''
    else:
        args['description'] = sys.argv[3]
    if sys.argv[4]=='':
        print("empty list")
        args['compartments'] = list()
    else:
        print("nonempty list --%s--"%sys.argv[4])
        args['compartments'] = sys.argv[4].split(',')


    # Print a message to let the user know what is being tried
    print("Listing items matching:\n\tvendor: %s\n\tdesc: %s\n\tcompart: %s"%(args['vendor'],args['description'],args['compartments']))

    # Setup the data to send
    sargs = dict()
    sargs['arguments']=json.dumps(args)
    sargs['signature']=''
    data = urlencode(sargs)
    
    # Make the resquest
    req = Request(sys.argv[1],data,method='POST')
    res = urlopen(req)
    
    # Parse the response
    resp = json.loads(res.read())
    
    # Print the result code
    #print("Call to LOST returned: %s"%resp['listing'])
    print("Call to LOST returned: %s"%resp)
    

if __name__=='__main__':
    main()
    