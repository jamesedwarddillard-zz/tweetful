import argparse
import sys

def make_parser():
	"""Constructing the command line parser"""
	description = "A twitter app that pulls down a users timeline, searches and posts"
	parser = argparse.ArgumentParser(description=description)