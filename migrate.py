# Python script to migrate new answers to answers format.
import yaml
from pymongo import MongoClient
import pprint

f = open('config.yaml')

config = yaml.safe_load(f)
f.close()

client = MongoClient('172.17.0.9', 27017)
db = client.users
collection = db.newanswers
# 	answers:[{
#		testNo: Number,
#		answerNo: Number,
#		answerValue: String
#		}]
#
#var NewAnswer   = new Schema({
#		id: Number,
#		idUser: Number,
#		testNo: Number,
#		answerNo: Number,
#		answerValue: String
#	
# });
#
#

pp = pprint.PrettyPrinter()

cursor = collection.find({'idUser':{'$gt':700}}).sort([('idUser',1)])
force = False
users = {}
for answer in cursor:
	#pp.pprint(answer)
	#pp.pprint(answer['idUser'])
	if answer['idUser'] not in users.keys():
		users[answer['idUser']] = {}
		users[answer['idUser']]['answers'] = []
	users[answer['idUser']]['answers'].append(answer)
#pp.pprint(users)
#insert in mongo	



for user in users:
	print("user",user)
	pp.pprint(users[user]['answers'])
	db.users.update({'idUser': user},{'$set': {"answers": users[user]['answers']}},upsert = False)

