import csv
from flask import Flask
from flask_restful import Resource, Api
from Dane.movies import Movies

app = Flask(__name__)
api = Api(app)

movies_list = list()

with open('dane/movies.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)
    for i, row in enumerate(spamreader):
        movie = Movies(row[0], row[1], row[2])
        movies_list.append(movie.__dict__)




class TodoSimple(Resource):
    def get(self):
        return movies_list


class HelloWorld(Resource):
    def get(self):
        return {'Witaj': 'user'}


api.add_resource(TodoSimple, '/movies')
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
