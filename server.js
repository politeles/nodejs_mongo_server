// server.js

// BASE SETUP
// =============================================================================

// call the packages we need
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');

// user model from user.js
var User = require('./models/user.js');
// load configuration:
var config = require('./config/config.js');
// configure the connection to db:
var mongoose = require('mongoose');
mongoose.connect('mongodb://'+config.mongo.host+ ":"+config.mongo.port+"/"+config.mongo.database,config.mongo);


// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || config.nodejs.port;        // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });   
});

// more routes for our API will happen here
// user route:
router.route('/users')

	.put(function(req,res){
		var user = new User(req.body);
		//user.userId = req.body.userId;
		//user.answers = req.body.answers;
		console.log("User values: "+user.userId);
		//try to save the user:
		user.save(function (err){
			if(err){
				res.send(err);
			}else{
				res.json({message:"User created"});
			}
		})
		
		// show json  request:
		console.log("Request: "+JSON.stringify(user));
		
		
		
		//save the user:
		
		//sned back a response:
		//res.json({message:'Call ok'});
		
	});

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);