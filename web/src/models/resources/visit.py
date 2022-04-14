from pymongo import MongoClient
from flask_restful import Resource

# instanciando mongoClient na porta default
client = MongoClient("localhost", 27017)
# novo database de nome aNewDB
db = client.aNewDB
# nova colecttion de nome UserNum
UserNum = db.UserNum
if (db.userNum == None):
  UserNum.insert_one({'num_of_users': 0})

#criar resource
class Visit(Resource):
  def get(self):
    prev_num = UserNum.find_one({})['num_of_users']
    new_num = prev_num + 1
    UserNum.update_one({}, {"$set": {"num_of_users": new_num}})
    return str("Ola user " + str(new_num))