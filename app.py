from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosophe\'s Store',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    },
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def get_books():
    response_object = {'status': 'Success'}
    if request.method == 'POST':
        BOOKS.append({
            'title': request.form['title'],
            'author': request.form['author'],
            'read': request.form['read'],
        })
        response_object['message'] = 'Books Added'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
