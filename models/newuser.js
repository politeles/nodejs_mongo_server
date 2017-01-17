/*
* Database schema.
* On this example we have the following schema on mongo:
* {"userId":"userIdValue",
* answers:[
* {"idUser":1111,"testNo":1,"answerNo":2,"answerValue":"answer1"},
* {"idUser":1111,"testNo":1,"answerNo":2,"answerValue":"answer1"}
* ]}
*/
var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var NewUserSchema   = new Schema({
    id: Number,
    time:Date
	
});

module.exports = mongoose.model('NewUser', NewUserSchema);