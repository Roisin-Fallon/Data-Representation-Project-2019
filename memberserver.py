from flask import Flask, jsonify, request, abort
from memberDAO import memberDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/members"
@app.route('/members')
def getAll():
    #print("in getall")
    results = memberDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/members/2"
@app.route('/members/<int:id>')
def findById(id):
    foundMember = memberDAO.findByID(id)

    return jsonify(foundMember)


#curl  -i -H "Content-Type:application/json" -X POST -d "{\"email\":\"georgedeleaney@yahoo.com\",\"membershipPlan\":\"Daily\",\"startDate\":\"2019-11-12\" ,\"age\":22}" http://127.0.0.1:5000/members
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"id\":7,\"email\":\"jackjones@gmail.com\",\"membershipPlan\":\"Monthly\",\"startDate\":\"2019-10-11\" ,\"age\":30}" http://127.0.0.1:5000/members

@app.route('/members', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    member = {
        "email": request.json['email'],
        "membershipPlan": request.json['membershipPlan'],
        "startDate": request.json['startDate'],
        "age": request.json['age'],
    }
    values =(member['email'], member['membershipPlan'], member['startDate'], member['age'])
    newId = memberDAO.create(values)
    member['id'] = newId
    return jsonify(member)

# curl  -i -H "Content-Type:application/json" -X PUT -d "{\"email\":\"marygarciak@gmail.com\",\"membershipPlan\":\"Monthly\",\"startDate\":\"2020-03-01\" ,\"age\":22}" http://127.0.0.1:5000/members/1
@app.route('/members/<int:id>', methods=['PUT'])
def update(id):
    foundMember = memberDAO.findByID(id)
    if not foundMember:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age' in reqJson and type(reqJson['age']) is not int:
        abort(400)

    if 'email' in reqJson:
        foundMember['email'] = reqJson['email']
    if 'membershipPlan' in reqJson:
        foundMember['membershipPlan'] = reqJson['membershipPlan']
    if 'startDate' in reqJson:
        foundMember['startDate'] = reqJson['startDate']
    if 'age' in reqJson:
        foundMember['age'] = reqJson['age']
    values = (foundMember['email'], foundMember['membershipPlan'], foundMember['startDate'], foundMember['age'], foundMember['id'])
    memberDAO.update(values)
    return jsonify(foundMember)
        
#  curl -X DELETE http://localhost:5000/members/7
@app.route('/members/<int:id>' , methods=['DELETE'])
def delete(id):
    memberDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)