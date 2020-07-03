#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:19:50 2019

@author: clnovak
"""

# based on
# https://stackoverflow.com/questions/2506932/how-do-i-forward-a-request-to-a-different-url-in-python


import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', 'http://www.google.at')
       self.end_headers()

HTTPServer(("", 8080), Redirect).serve_forever()
