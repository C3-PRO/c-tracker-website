#!/usr/bin/env python3
#
#  Uses HTML data from c-tracker-content and renders them, using Jinja2, into CTracker/HTMLContent/
#
#  Requirements:
#  - jinja2

import io
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader(__name__, 'templates'))
app_template = env.get_template('base.html')

# index
with io.open('content/index.html', 'r', encoding="utf-8") as handle:
	content = handle.read()
	app_template.stream(title="C Tracker", content=content) \
		.dump('./index.html')

# team
with io.open('content/team.html', 'r', encoding="utf-8") as handle:
	content = handle.read()
	app_template.stream(title="The Team • C Tracker", content=content) \
		.dump('./team.html')

# Privacy Policy
with io.open('c-tracker-content/PrivacyPolicy.html', 'r', encoding="utf-8") as handle:
	content = handle.read()
	app_template.stream(title="Privacy Policy • C Tracker", content=content) \
		.dump('./PrivacyPolicy.html')
