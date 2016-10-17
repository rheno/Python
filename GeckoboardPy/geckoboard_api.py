# Implement geckoboard dataset API in Python
# See this https://developer.geckoboard.com/api-reference/curl/

import urllib2, base64
import json
import httplib
import constants

class PyGeckoboard:
		
	def auth(self, prefix):
		return self.request(prefix, "", "GET")
		
	def create_dataset(self, prefix, *args, **kwargs):
		data = {}
                unique_by = []

                data = kwargs
                for arg in args:
                        unique_by.append(arg)

                data["unique_by"] = unique_by
		return self.request(prefix, data, "PUT")

	def replace_dataset(self, prefix, *args):

		field = []
		data = {}
		for arg in args :
                	field.append(arg)

		data["data"] = field

		return self.request(prefix, data, "PUT")

	def append_dataset(self, prefix, *args):

                field = []
                data = {}
                for arg in args :
                        field.append(arg)

                data["data"] = field

                return self.request(prefix, data, "POST")


	def delete_dataset(self, prefix):
		return self.request(prefix, "", "DELETE")
		

	
	def request(self, prefix, data, method):
	
		# Get response
		response = ""
		
		# Change dictionary to array
		jsondata = json.dumps(data)

		request = ""

		# Make request
		if method == "POST" or method == "PUT" :
			request = urllib2.Request(constants.URL + "%s"% (prefix), jsondata)
		elif method == "GET" or method == "DELETE" :			
			request = urllib2.Request(constants.URL + "%s"% (prefix))

		base64string = base64.b64encode('%s:%s' % (constants.API_KEY, constants.PASSWORD))

		# Setup Header
		request.add_header("Authorization", "Basic %s" % base64string)
		request.add_header("Content-Type", "application/json")
		request.get_method = lambda:"%s"%method


		# Request and get the response here
		try :
    			resp = urllib2.urlopen(request)
    			response = "Success : "+resp.read()
		except urllib2.HTTPError, e:
    			response = 'HTTPError = %d' % e.code
		except urllib2.URLError, e:
    			response = 'URLError = %s' % str(e.reason)
		except httplib.HTTPException, e:
    			response = 'HTTPException'
		except Exception:
			response = "Parsing Response or Others Error"
		
		return response


p = PyGeckoboard() 	

# print p.create_dataset("/datasets/iseng.bisa", 
#		"tanggal",
#		fields=dict(
#		jumlah=dict(type="number",name="Jumlah"), 
#		tanggal=dict(type="date", name="Tanggal"))
#		)

# print p.delete_dataset("/datasets/iseng.bisa")

print p.append_dataset("/datasets/sales.gross/data", 
			dict(timestamp="2016-01-01T12:00:00Z", amount=877), 
			dict(timestamp="2016-01-29T12:00:00Z", amount=655) 
			)




