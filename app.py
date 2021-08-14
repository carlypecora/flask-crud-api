# ~flask-api/app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

@app.route('/')
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return {'id': books.index(book)}, 200

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    book = request.get_json()
    books[index] = book
    return jsonify(books[index]), 200

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    books.pop(index)
    return 'None', 200


app.run()
