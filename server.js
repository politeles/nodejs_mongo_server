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


//enable Cross Origin Resource Sharing
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
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
		console.log("Request data:"+req.body);
		
		//try to convert to User object:
		try{
			
			var user = new User(req.body);
			console.log("Finding users with id:"+user.idUser);
			//try to find out the user:
			User
			.count({
				idUser: user.idUser
				})
				.exec(
					function(error,results){
					if(error ==null && results!=null){
						// query ok:
						// get the first element of results and update it.
						console.log("Users: "+results);
						if(results == 0 ){
							console.log("no results");
								user.save(function (err){
								if(err){
									//res.send(err);
									res.json({code:"0",userId:req.body.idUser,message:"User can't be saved"});//failed
								}else{
									res.json({code:"1",userId:req.body.idUser,message:"Success"}); //success
								}
								});
						}else{
							console.log("user exist");
							res.json({code:"0",userId:req.body.idUser,message:"User already on db"});//duplicate
						}
					}else{
						console.log("user exist..");
						res.json({code:"0",userId:req.body.idUser,message:"Error"});//error
					}
					
					
					
				});
			
			
		//user.userId = req.body.userId;
		//user.answers = req.body.answers;
		console.log("User values: "+JSON.stringify(user.idUser));
		//try to save the user:
	
			
			
		}catch(error){
			res.json({code:"0",message:"Error: "+error.message});
		}
		
		
		// show json  request:
		//console.log("Request: "+JSON.stringify(user));
		
		
		
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