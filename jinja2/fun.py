# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:58:47 2023

@author: 700001473
"""

from jinja2 import Environment, FileSystemLoader, StrictUndefined, meta

# inside the environment, we can define what should happen when a template variable is not provided (default action is to replace with an empty string which may not always be the best option...)
env = Environment(
    loader=FileSystemLoader("."), undefined = StrictUndefined)

template = env.get_template("fun.tmpl")

dct = {'v1': 3, 'v2': 10}

s = template.render({'var1': 'Hello',
                     'dct': dct,
                     'lst': [1,4,10,2],
                     'flag': True})
print(s)




# We want to extract all template variables
# get the source first
source, filename, uptodate = env.loader.get_source(env, "fun.tmpl")
ast = env.parse(source)
variables = meta.find_undeclared_variables(ast)
print("Variables in the template:", variables)

