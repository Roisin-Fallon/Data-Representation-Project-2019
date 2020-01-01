#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
from flask_cors import CORS
app = Flask(__name__,
            static_url_path='',
            static_folder='../')

CORS(app)

members = [
   {
        "email":"mary@gmail.com",
        "membershipPlan":"Daily",
        "startDate":"20/12/2019",
        "age":18
    },
    {
        "email":"jow@gmail.com",
        "membershipPlan":"Monthly",
        "startDate":"30/01/2020",
        "age":20
    },
    {
        "email":"david@gmail.com",
        "membershipPlan":"Annually",
        "startDate":"06/01/2020",
        "age":40
    },
]

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify( {'members':members})
# curl -i http://localhost:5000/members

@app.route('/members/<string:memberID>', methods =['GET'])
def get_member(memberID):
    foundMembers = list(filter(lambda t : t['memberID'] == memberID , members))
    if len(foundMembers) == 0:
        return jsonify( { 'member' : '' }),204
    return jsonify( { 'member' : foundMembers[0] })
#curl -i http://localhost:5000/members/test

@app.route('/members', methods=['POST'])
def create_member():
    if not request.json:
        abort(400)
    if not 'name' in request.json:
        abort(400)
    member={
		"memberID":  request.json['memberID'],
        "name":  request.json['name'],
        "email": request.json['email'],
        "favouriteClass":request.json['favouriteClass'],
	    "weeklyGoal":request.json['weeklyGoal'],
        "budget":request.json['budget']
    }
    members.append(member)
    return jsonify( {'member':member}),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"memberID\":\"006\",\"name\":\"Sinead Andrews\",\"email\":\"sineadandrews@gmail.com\",\"favouriteClass\":\"HIT\",\"weeklyGoal\":\"Tone up \",\"budget\":50}" http://localhost:5000/members

@app.route('/members/<string:memberID>', methods =['PUT'])
def update_member(memberID):
	foundMembers=list(filter(lambda t : t['memberID'] ==memberID, members))
	if len(foundMembers) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) is not str:
		abort(400)
	if 'email' in request.json and type(request.json['email']) is not str:
		abort(400)
	if 'favouriteClass' in request.json and type(request.json['favouriteClass']) != str:
		abort(400)
	if 'weeklyGoal' in request.json and type(request.json['weeklyGoal']) != str:
		abort(400)
	if 'budget' in request.json and type(request.json['budget']) is not int:
		abort(400)
	foundMembers[0]['name']  = request.json.get('name', foundMembers[0]['name'])
	foundMembers[0]['email'] =request.json.get('email', foundMembers[0]['email'])
	foundMembers[0]['favouriteClass']  = request.json.get('favouriteClass', foundMembers[0]['favouriteClass'])
	foundMembers[0]['weeklyGoal'] =request.json.get('weeklyGoal', foundMembers[0]['weeklyGoal'])
	foundMembers[0]['budget'] =request.json.get('budget', foundMembers[0]['budget'])
	return jsonify( {'member':foundMembers[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"favouriteClass\":\"Abs Blast\"}" http://localhost:5000/members/181%20G%201234

@app.route('/members/<string:memberID>', methods =['DELETE'])
def delete_member(memberID):
    foundMembers = list(filter (lambda t : t['memberID'] == memberID, members))
    if len(foundMembers) == 0:
        abort(404)
    members.remove(foundMembers[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)