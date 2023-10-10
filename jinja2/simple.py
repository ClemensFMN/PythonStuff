from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("."))

template = env.get_template("simple.tmpl")

s = template.render({'var1': 'Hello', 'var2': 'World'})
print(s)

# TODO: How can I raise an error / exception when a variable used in a template is *not* provided?
s = template.render({'var1': 'Hello'})
print(s)

