# ~flask_api/resources/routes.py

from .book import BooksApi, BookApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/books')
    api.add_resource(MovieApi, '/api/books/<id>')
