from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

"""hello world"""
class PipCount(Resource):
	def post(self):
		return {'hello': 'world'}

api.add_resource(PipCount, '/')

"""taking in an image"""
	def import_data(self, request)
		try:
			if 'image' in request.files:
				filename=images.save(request.files['image'])
				self.image_filename = filename
				self.image_url = images.url(filename)
			except KeyError as e:
				raise ValidationError('Invalid image: missing ' + e.args[0])
			return self;			

if __name__ == '__main__':
	app.run(debug=True) 

