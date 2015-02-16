from random import randint

from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class DiceSingle(restful.Resource):
    def get(self, num_sides):
        results = [ randint(1, num_sides) ]
        return {
            'number_of_rolls': 1,
            'number_of_sides': num_sides,
            'rolls': results,
            'total': sum(results),
        }


class DiceMulti(restful.Resource):
    def get(self, num_sides, num_rolls):
        results = [ randint(1, num_sides) for i in range(num_rolls) ]
        return {
            'number_of_rolls': 1,
            'number_of_sides': num_sides,
            'rolls': results,
            'total': sum(results),
        }


api.add_resource(DiceSingle, '/dice/<int:num_sides>')
api.add_resource(DiceMulti, '/dice/<int:num_sides>/<int:num_rolls>')

if __name__ == '__main__':
    app.run(debug=True)