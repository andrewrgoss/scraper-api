# !/usr/bin/env python
__author__ = 'agoss'

import argparse
import json
import requests
from scraper_api import ScraperAPIClient
import sys


def main():
	parser = argparse.ArgumentParser(description='Parses command line arguments')
	parser.add_argument('--scraper_api_key', type=str, required=True)
	args = parser.parse_args()

	client = ScraperAPIClient(args.scraper_api_key)
	result = json.loads(client.get(url='http://httpbin.org/ip').text)
	print('Rotated proxy IP address = ' + result['origin'])

	urls = [
		client.scrapyGet(url='http://quotes.toscrape.com/page/1/'),
		client.scrapyGet(url='http://quotes.toscrape.com/page/2/'),
	]

	for url in urls:
		r = requests.get(url)
		# add parsing logic here
		print(r.status_code)


try:
	main()
except Exception as err:
	print(err)
	sys.exit(1)
