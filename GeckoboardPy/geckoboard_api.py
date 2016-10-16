# Implement geckoboard dataset API in Python
# See this https://developer.geckoboard.com/api-reference/curl/

import urllib2, base64
import json
import httplib

# Put your url datasets, API_KEY, and Password (Not used in my case)
URL = "https://api.geckoboard.com/datasets/sales.gross/data"
API_KEY = "API_KEY"
PASSWORD = ""

# Python Dictionary (You can modify this to get data from database or other sources)
pydict = {'data': [{"timestamp" : "2016-01-01T12:00:00Z", "amount" : 219}, {"timestamp" : "2016-01-02T12:00:00Z", "amount" : 900}]}

# Change dictionary to array
jsondata = json.dumps(pydict)

# Make request
request = urllib2.Request(URL, jsondata)
base64string = base64.b64encode('%s:%s' % (API_KEY, PASSWORD))

# Setup Header
request.add_header("Authorization", "Basic %s" % base64string)   
request.add_header("Content-Type", "application/json")


# Request and get the response here
try :
    response = urllib2.urlopen(request)
    print "Success : "+response.read()
except urllib2.HTTPError, e:
    print 'HTTPError = %d'%e.code
except urllib2.URLError, e:
    print 'URLError = '.str(e.reason)
except httplib.HTTPException, e:
    print 'HTTPException'
except Exception:
    print "Parsing Response or Others Error"
