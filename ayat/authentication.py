from flask import Flask, request, make_response,jsonify
from functools import wraps
import jwt
import datetime
from functools import wraps
from ayat      import app





def  token_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message' : 'Token is missing!'}),403

		try:
			data = jwt.decode(token,app.config['SECRET_KEY'])

		except:
			return jsonify({'message' : 'Token is invalid'}),403

		return f(*args,**kwargs)

	return decorated

@app.route('/unprotected')
def unprotected():
	return jsonify({'message' : 'Anyone can view this!'})


@app.route('/protected')
@token_required
def protected():
	return jsonify({'message':'This is only avaliable for people with valid tokens.'})



@app.route('/login')
def login():
	auth=request.authorization

	if auth and auth.username=='username1' and auth.password=='password':
		token = jwt.encode({'user' : auth.username},app.config['SECRET_KEY'])
		return jsonify({'token':token.decode('UTF-8')})

	

	return make_response('Could not verfiy!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})	



