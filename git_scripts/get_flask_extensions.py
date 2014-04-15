"""
Pulls content from Flask extensions page and clones all of the
extensions from github. 

Hard coded to git and python 3
"""
import subprocess
import urllib.request
extensions_url = "http://flask.pocoo.org/extensions/"
page = urllib.request.urlopen(extensions_url)
page_content = page.read()

for potential_url in page_content.splitlines():
	if b"http://github.com" in potential_url:
		left_side = potential_url.find(b'"') + 1
		right_side = potential_url.find(b'"', left_side)
		git_url = potential_url[left_side:right_side]
		subprocess.call(['git', 'clone', git_url])
