#!/usr/bin/env python3
#
#  Uses HTML data from c-tracker-content and renders them, using Jinja2, into CTracker/HTMLContent/
#
#  Requirements:
#  - jinja2

import io
import markdown
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader(__name__, 'templates'))
app_template = env.get_template('base.html')

# dump content
def run():
	html_to('content/index.html', "C Tracker", './index.html')
	html_to('c-tracker-content/PrivacyPolicy.html', "Privacy Policy • C Tracker", './PrivacyPolicy.html')
	markdown_to('content/team.md', "The Team • C Tracker", './team.html')
	markdown_to('content/assets.md', "Assets • C Tracker", './assets.html')
	markdown_to('c-tracker-faq/web/FAQ.md', "FAQ • C Tracker", './FAQ.html')


# functions
def html_to(source, title, target):
	content = read_content(source)
	dump_content_to(content, title, target)

def markdown_to(source, title, target):
	raw = read_content(source)
	content = markdown.markdown(raw, output_format='html5')
	dump_content_to(content, title, target)

def read_content(source):
	with io.open(source, 'r', encoding="utf-8") as handle:
		return handle.read()

def dump_content_to(content, title, target):
	app_template.stream(title=title, content=content) \
		.dump(target)

if '__main__' == __name__:
	run()
