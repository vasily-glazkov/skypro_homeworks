import json
from flask import Flask

with open('candidates.json', encoding='utf-8') as file:
	data = json.load(file)

app = Flask(__name__)


@app.route("/")
def index_page():
	display_string = ""
	for i in data:
		display_string += f"<pre>{i['name']}-\n{i['position']}\n{i['skills']}</pre>"
	return display_string


@app.route("/candidate/<int:x>/")
def candidate_page(x):
	for i in data:
		if i['id'] == x:
			return f"<img src='https://picsum.photos/200'>\n" \
				f"<pre>{i['name']}-\n{i['position']}\n{i['skills']}</pre>"


@app.route("/skill/<x>/")
def search_skill(x):
	display_string = ""
	for i in data:
		if x.lower() in i['skills'] or x in i['skills']:
			display_string += f"<pre>{i['name']}-\n{i['position']}\n{i['skills']}</pre>"
	return display_string


app.run()
