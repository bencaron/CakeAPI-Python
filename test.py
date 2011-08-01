# -*- coding: UTF-8 -*-

from cakeapi import API
import json # Not needed. Used only for pretty printing the JSON object

# Initialize the API Object by parsing your API Key
apiobj = API('YourApiKey')

# Log in
login_params = {
    'email'     :   'some@email.com', 
    'password'  :   'abc123'
}

# Pass the params to the API as an array['Class','Method'] and a dictionary with params
response = apiobj.call(['User', 'login'], login_params)
print json.dumps(response, indent=2)

# Subscribing an email to a list with custom fields
subscribe_params = {
    'user_key'          :   'theUserKey',
    'list_id'           :   'theListId',
    'client_id'         :   'theClientId',
    'email'             :   'theEmailToSusbcribe',
    'data[First Name]'  :   'FirstName',
    'data[Last Name]'   :   'LastName',
    'data[Phone #]'     :   '514826936',
    'data[Endereço]'    :   '1234 Rnd Street'
}

response = apiobj.call(['List', 'subscribeEmail'], subscribe_params)
print json.dumps(response, indent=2)