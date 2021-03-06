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

var UserSchema   = new Schema({
    idUser: Number,
    time:Date,
    tests:[{
    	testNo: Number,
    	result: Number
    }],
	answers:[{
		testNo: Number,
		answerNo: Number,
		answerValue: String
		}]
	
});

module.exports = mongoose.model('User', UserSchema);