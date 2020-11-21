from flask import Flask,request
from flask_restful import Api,Resource
from security import auth,identity
from flask_jwt import JWT,jwt_required
from user import SignUp

app = Flask(__name__)
app.secret_key = '#0#'
api = Api(app)
jwt = JWT(app,auth,identity)#/auth
items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #Here we are using get method of rest api to insert the 
        return {'item': item}, 200 if item else 404
    def post(self,name):
        if next(filter(lambda x:x['name'] == name,items),None): #To create the rest api 
            return {'message':'item'+name+'exist'}
        data = request.get_json()
        new_item = {'name':name,'price':data['price']}
        items.append(new_item)
        return new_item
    def delete(self,name): #To delete the element 
        global items
        items = list(filter(lambda x:x['name']!=name,items))
        return items
    def put(self,name): #To put the element in the database 
        data = request.get_json()
        item = next(filter(lambda x:x['name'] == name,items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)

class ItemList(Resource): #Itemlist resources of which table should be created in database
    def get(self):
        return{'item':items}

api.add_resource(Item,'/items/<string:name>') #here we add data to api to jonisify it in the form of api or to give it a structure
api.add_resource(ItemList,'/items')
api.add_resource(SignUp,'/signup')
app.run(port=4000,debug=True)
