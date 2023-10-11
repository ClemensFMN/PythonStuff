from jinja2 import *

# inside the environment, we can define what should happen when a template variable is not provided (default action is to replace with an empty string which may not always be the best option...)
env = Environment(
    loader=FileSystemLoader("."), undefined = StrictUndefined)

template = env.get_template("simple.tmpl")

s = template.render({'var1': 'Hello', 'var2': 'World'})
print(s)

s = template.render({'var1': 'Hello'})
print(s)

