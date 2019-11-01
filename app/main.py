from flask import Flask, request, render_template
import pymongo

app = Flask(__name__)
db_client = pymongo.MongoClient('mongodb://18.188.243.182:27017,18.188.243.182:27017,18.219.98.242:27017/?replicaSet=lab9')
db = db_client['chat']

@app.route('/')
def main_page():
	return render_template('index.html', messages=get_messages())


@app.route('/', methods=['POST'])
def get_form():
	message = request.form['Message']
	tudor = request.form['Author']

	collection = db['messages']
	collection.insert_one({'author': tudor, 'content': message})

	return render_template('index.html', messages=get_messages())


def get_messages():
	collection = db['messages']
	messages = collection.find({}, {'_id': 0})
	return messages


if __name__ == '__main__':
	app.run(host='0.0.0.0')
