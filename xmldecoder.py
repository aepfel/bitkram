#!/usr/bin/python

import sys
import xml.dom.minidom as dom

def _knoten_auslesen(knoten):
	return eval("%s('%s')" % (knoten.getAttribute("typ"),knoten.firstChild.data.strip()))
