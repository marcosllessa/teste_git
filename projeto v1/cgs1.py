import pandas as pd
import json
import requests
import numpy as np
import random
import urllib.request as url
from requests.auth import HTTPBasicAuth
from urllib.error import URLError, HTTPError
from pandas.io.json import json_normalize


class CGS1:
    
    def __init__(self):
    
        self.servidor_post = 'https://api.gs1br.org/oauth/access-token'
        self.servidor_get = 'https://api.gs1br.org/gs1/v0/products/'
        self.headers = {'Content-Type':'application/json'}
        self.data_post = {
            'grant_type': 'password',
            'username': 'toni.pimentel@compsis.com.br',
            'password': 'api@gs1'
        }
        
        self.client_id = 'b37493c1-3043-3bde-92c9-8a05ae2f953a'
        self.pw = '7b5c4fc9-a556-35e0-824c-2106cb40fe9f'
        
        self.data_get = {
            'client_id': self.client_id,
            'access_token': '',
            'Content-type': 'application/json'
        }


    def get_post(self):
        server_return = requests.post(self.servidor_post, 
                                      headers=self.headers, 
                                      auth=HTTPBasicAuth(self.client_id, self.pw), data=json.dumps(self.data_post))
        ret = server_return.json()        
        self.data_get = {
            'client_id': self.client_id,
            'access_token': ret['access_token'],
            'Content-type': 'application/json'
        }
        
        return server_return

    def get_gtin(self,gtin):
        ret = requests.get(self.servidor_get + gtin, headers=(self.data_get))
        if(ret.status_code == 401):
            ret = self.get_post()
            if((ret.status_code == 200) |(ret.status_code == 201)):
                ret = requests.get(self.servidor_get + gtin, headers=(self.data_get))
        return ret
