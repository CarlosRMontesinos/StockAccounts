import json
import webapp2
import model
import string

WEB_SITE = """<!doctype html> 
<html> 
  
  <body>  
    <h1 style="width: 100%; text-align: center;" >Josue's Stock Account</h1> 

    <h1 style="width: 100%; text-align: center;" > APPLE </h1>
    <h2 style="width: 100%; text-align: center;" > Quantity: {quatity} </h2>
    <h2 style="width: 100%; text-align: center;" > Last Price: {last_price} </h2>
    <h2 style="width: 100%; text-align: center;" > Current Value: {current_value} </h2> 

  </body>
</html>"""

# Get data from DB

# Look for tockens and replace
UPDATED_WEB_SITE = string.replace(WEB_SITE, "{quatity}", "WE ROCK")
UPDATED_WEB_SITE = string.replace(UPDATED_WEB_SITE, "{last_price}", "WE ROCK")
UPDATED_WEB_SITE = string.replace(UPDATED_WEB_SITE, "{current_value}", "WE ROCK")


# Serve website
UPDATE_STRING = "UPDATING...!!!"

class RestHandler(webapp2.RequestHandler):
    
    def get(self):
     	# Serve the website
    	self.response.write( UPDATED_WEB_SITE )

APP = webapp2.WSGIApplication([
    ('/', RestHandler),
], debug=True)
