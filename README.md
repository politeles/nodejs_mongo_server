# nodejs_mongo_server
this is a REST server in node js  that stores data on mongo db server

How to run it:
-----------------
Go to the folder where the repo is and run
```Shell
npm install
```

Once it is compiled, you can run the server as follows:


```Shell
node server.js
```
The server is configured to listen by default into port 8080.

http://{{host}}:{{port}}/api/users

Where host is your hostname and port is 8080.

you can test the REST api by using POSTMAN (Chrome plugin).
or directly via curl:

```Shell
curl -H "Content-Type: application/json" -X PUT -d '{"userId": "1234","answers": [{"testNo":"1","answerNo":"1","answerValue":"Myanswer1"},{"testNo":"1","answerNo":"2","answerValue":"Myanswer2"}]}' http://localhost:8080/api/users
```
