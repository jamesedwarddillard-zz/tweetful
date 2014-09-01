import urlparse

import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

import json

def search(query, result_type, count, auth):
	"""Performs a twitter search for a user"""
	payload = {'q': query, 'result_type': result_type, 'count': count}
	print type(auth)
	response = requests.get(SEARCH_URL, params=payload, auth=auth)
	return response

