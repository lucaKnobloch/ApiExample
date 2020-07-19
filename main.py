import dataFile
import random

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(dataFile.ai_quotes), 200
        for quote in dataFile.ai_quotes:
            if quote["id"] == id:
                return quote, 200
        return "Quote not found", 404


def post(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in dataFile.ai_quotes:
        if id == quote["id"]:
            return f"Quote with id {id} already exists", 400
    quote = {
        "id": int(id),
        "author": params["author"],
        "quote": params["quote"]
    }
    dataFile.ai_quotes.append(quote)
    return quote, 201


def put(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in dataFile.ai_quotes:
        if id == quote["id"]:
            quote["author"] = params["author"]
            quote["quote"] = params["quote"]
            return quote, 200

    quote = {
        "id": id,
        "author": params["author"],
        "quote": params["quote"]
    }

    dataFile.ai_quotes.append(quote)
    return quote, 201


def delete(self, id):
    global ai_quotes
    ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
    return f"Quote with id {id} is deleted.", 200


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
