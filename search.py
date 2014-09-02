import urlparse

import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

import json

def json_decoder(json_response):
	"""
	Takes a json response and decodes it 
	"""
	encoded = json.dumps(json_response.json(), encoding='utf-8')
	decoded = json.loads(encoded, encoding='utf-8')
	return decoded


def search(query, result_type, count, auth):
	"""Performs a twitter search for a user"""
	payload = {'q': query, 'result_type': result_type, 'count': count}
	response = requests.get(SEARCH_URL, params=payload, auth=auth)
	decoded_response = json_decoder(response)
	return decoded_response

