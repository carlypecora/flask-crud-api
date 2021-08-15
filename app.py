# ~flask-api/app.py

from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Book
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/book-api'
}

initialize_db(app)

@app.route('/books')
def get_books():
    books = Book.objects().to_json()
    return Response(books, mimetype="application/json", status=200)

@app.route('/books/<id>')
def get_book(id):
    book = Book.objects.get(id=id).to_json()
    return Response(book, mimetype="application/json", status=200)

@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
    book = Book(**body).save()
    id = book.id
    return {'id': str(id)}, 201

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    body = request.get_json()
    Book.objects.get(id=id).update(**body)
    return '', 200

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    Book.objects.get(id=id).delete()
    return '', 200


app.run()
