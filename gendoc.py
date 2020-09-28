#!/usr/bin/env python

from appy.pod.renderer import Renderer
import json
from sys import argv

filename = argv[1] # You should pass exactly one argument
variables = json.load(open(f'{filename}.json', 'r'))
renderer = Renderer(f'{filename}-template.odt', variables, f'{filename}.odt', overwriteExisting=True)
renderer.run()
