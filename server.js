// server.js

// BASE SETUP
// =============================================================================

// call the packages we need
var express    = require('express');        // call express
var nodeExcel = require('excel-export');    // call excel export
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
	
	// route for processing all users to generate excel file:
	router.route('/process')

	.get(function(req,res){
		 var conf ={};
	// 	 1 step:
	// retrieve all users from db:
	//Array of rows:
	var rowArray = [];
	var colArray = [];
	var colCompleted = false;
	colArray.push({caption:'Codigo',type:'number'});
		User.find({},function(err,users){
		//	console.log("All users:"+JSON.stringify(users));
			if(err==null && users!=null){
			users.forEach(function(user){
				var rA = [];
				
				
				rA.push(user.idUser);
				
				console.log("Id user: "+user.idUser);
				user.answers.forEach(
					function(ans){
					console.log("Answer: "+ans.answerValue);
					rA.push(ans.answerValue);
					
					if(!colCompleted){
						
						var captionValue = "Test: "+ans.testNo+ "Answer: "+ans.answerNo;
						colArray.push({caption:captionValue,type:'text'});
					}
					
				});
				
				rowArray.push(rA);
				colCompleted = true;
				
			});
			}
			
			
			console.log("Showing content");
		 //show row array:
		 rowArray.forEach(function(element){
				element.forEach(function(item){
					console.log("item: "+item);
				});
				
				console.log("showing cols:");
				
				colArray.forEach(function(item){
					console.log("Label: "+JSON.stringify(item));
				});
				
				
			
		 });
		 
		  //  conf.stylesXmlFile = "styles.xml";
    conf.cols = colArray;
	
	
	/*[{
        caption:'Codigo',
        type:'number',
        width:28.7109375
    },{
        caption:'resultados tes1',
        type:'number',
        
    },{
        caption:'bool',
        type:'bool'
    },{
        caption:'number',
         type:'number'              
    }];
	*/
    conf.rows = rowArray;
	/*
	[
        ['pi', new Date(Date.UTC(2013, 4, 1)), true, 3.14],
        ["e", new Date(2012, 4, 1), false, 2.7182],
        ["M&M<>'", new Date(Date.UTC(2013, 6, 9)), false, 1.61803],
        ["null date", null, true, 1.414]  
    ];
	*/
    var result = nodeExcel.execute(conf);
    res.setHeader('Content-Type', 'application/vnd.openxmlformats');
    res.setHeader("Content-Disposition", "attachment; filename=" + "Report.xlsx");
    res.end(result, 'binary');
		 
		 
		 
		 });
		 
		 
		 
		 
		 
		 
		 
 
	});
	
	

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);