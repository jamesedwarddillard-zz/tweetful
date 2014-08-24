import argparse
import sys

def make_parser():
	"""Constructing the command line parser"""
	description = "A twitter app that shows a user their follower rank and saves searches"
	parser = argparse.ArgumentParser(description=description)

	subparser = parser.add_subparsers(help="Available commands")

	#Subparser for the rank command
	timeline_parser = subparser.add_parser("timeline", help = "See your timeline")


	#Subparser for the search command


