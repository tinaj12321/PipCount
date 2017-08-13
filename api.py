from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class PipCount(Resource):
	def post(self):
		return {'hello': 'world'}

api.add_resource(PipCount, '/')

if __name__ == '__main__':
	app.run(debug=True) 
