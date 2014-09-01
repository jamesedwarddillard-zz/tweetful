import argparse
import sys

def make_parser():
	"""Constructing the command line parser"""
	description = "A twitter app that searches on behalf of a user"
	parser = argparse.ArgumentParser(description=description)

	subparser = parser.add_subparsers(help="Available commands")

	#Subparser for the search command
	search_parser = subparser.add_parser("search", help = "Search Twitter for things you care about")
	search_parser.add_argument("query", help="The term you're searching for")
	search_parser.add_argument("result_type", default="*recent", nargs="?", help="The type of search you're performing: recent, popular or mixed")
	search_parser.add_argument("count", default=3, nargs="?", help="The number of results your search will return")
	search_parser.set_defaults(command = "search")

	return parser


