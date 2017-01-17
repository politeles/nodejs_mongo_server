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
var NewUser = require('./models/newuser.js');
var NewAnswer = require('./models/newanswer.js');
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

	router.route('/new_user')

	.put(function(req,res){
		console.log("Request data:"+req.body);

		//try to convert to User object:
		try{

			var user = new NewUser(req.body);
			console.log("Finding users with id:"+user.idUser);
			//try to find out the user:
			NewUser
			.count({
				id: user.id
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
									res.json({code:"0",id:req.body.idUser,message:"User can't be saved"});//failed
								}else{
									res.json({code:"1",id:req.body.idUser,message:"Success"}); //success
								}
								});
						}else{
							console.log("user exist");
							res.json({code:"0",id:req.body.idUser,message:"User already on db"});//duplicate
						}
					}else{
						console.log("user exist..");
						res.json({code:"0",id:req.body.idUser,message:"Error"});//error
					}



				});


		//user.userId = req.body.userId;
		//user.answers = req.body.answers;
		console.log("User values: "+JSON.stringify(user.id));
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
router.route('/new_answer')

	.put(function(req,res){
		console.log("Request data:"+req.body);

		//try to convert to User object:
		try{

			var answer = new NewAnswer(req.body);
			console.log("Finding users with id:"+answer.idUser);
			//try to find out the user:
			NewAnswer.save(function (err){
								if(err){
									//res.send(err);
									res.json({code:"0",idUser:req.body.idUser,message:"User can't be saved"});//failed
								}else{
									res.json({code:"1",idUser:req.body.idUser,message:"Success"}); //success
								}
								});





		//user.userId = req.body.userId;
		//user.answers = req.body.answers;
		console.log("User values: "+JSON.stringify(answer.idUser));
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
		 var conf = [];
		 conf.push(new Object());
		 conf.push(new Object());
	// 	 1 step:
	// retrieve all users from db:
	//Array of rows:
	var rowArray = [];
	var rowArray1 = [];
	var colArray1 = [
		{caption:"Codigo",type:"number",key:"code"},
		{caption:"Fecha",type:"datetime",key:"timestamp"},
		{caption:"Test 1",type:"text",key:"r1"},
		{caption:"Test 2",type:"text",key:"r2"},
		{caption:"Test 3",type:"text",key:"r3"},
		{caption:"Test de los ojos",type:"text",key:"r4"},
		];
	var colArray = [
		{caption:"Codigo",type:"number",key:"code"},
		{caption:"Fecha",type:"datetime",key:"timestamp"},
		{caption:"Test 1 - item 1",type:"text",key:"3-1"},
		{caption:"Test 1 - item 2",type:"text",key:"3-2"},
		{caption:"Test 1 - item 3",type:"text",key:"3-3"},
		{caption:"Test 1 - item 4",type:"text",key:"3-4"},
		{caption:"Test 1 - item 5",type:"text",key:"3-5"},
		{caption:"Test 1 - item 6",type:"text",key:"3-6"},
		{caption:"Test 1 - item 7",type:"text",key:"3-7"},
		{caption:"Test 1 - item 8",type:"text",key:"3-8"},
		{caption:"Test 1 - item 9",type:"text",key:"3-9"},
		{caption:"Test 1 - item 10",type:"text",key:"3-10"},
		{caption:"Test 1 - item 11",type:"text",key:"3-11"},
		{caption:"Test 1 - item 12",type:"text",key:"3-12"},
		{caption:"Test 1 - item 13",type:"text",key:"3-13"},
		{caption:"Test 1 - item 14",type:"text",key:"3-14"},
		{caption:"Test 1 - item 15",type:"text",key:"3-15"},
		{caption:"Test 2 - item 0",type:"text",key:"2-0"},
		{caption:"Test 2 - item 1",type:"text",key:"2-1"},
		{caption:"Test 2 - item 2",type:"text",key:"2-2"},
		{caption:"Test 2 - item 3",type:"text",key:"2-3"},
		{caption:"Test 2 - item 4",type:"text",key:"2-4"},
		{caption:"Test 2 - item 5",type:"text",key:"2-5"},
		{caption:"Test 2 - item 6",type:"text",key:"2-6"},
		{caption:"Test 2 - item 7",type:"text",key:"2-7"},
		{caption:"Test 2 - item 8",type:"text",key:"2-8"},
		{caption:"Test 2 - item 9",type:"text",key:"2-9"},
		{caption:"Test 2 - item 10",type:"text",key:"2-10"},
		{caption:"Test 2 - item 11",type:"text",key:"2-11"},
		{caption:"Test 2 - item 12",type:"text",key:"2-12"},
		{caption:"Test 2 - item 13",type:"text",key:"2-13"},
		{caption:"Test 2 - item 14",type:"text",key:"2-14"},
		{caption:"Test 2 - item 15",type:"text",key:"2-15"},
		{caption:"Test 2 - item 16",type:"text",key:"2-16"},
		{caption:"Test 2 - item 17",type:"text",key:"2-17"},
		{caption:"Test 2 - item 18",type:"text",key:"2-18"},
		{caption:"Test 2 - item 19",type:"text",key:"2-19"},
		{caption:"Test 2 - item 20",type:"text",key:"2-20"},
		{caption:"Test 2 - item 21",type:"text",key:"2-21"},
		{caption:"Test 2 - item 22",type:"text",key:"2-22"},
		{caption:"Test 2 - item 23",type:"text",key:"2-23"},
		{caption:"Test 2 - item 24",type:"text",key:"2-24"},
		{caption:"Test 2 - item 25",type:"text",key:"2-25"},
		{caption:"Test 2 - item 26",type:"text",key:"2-26"},
		{caption:"Test 2 - item 27",type:"text",key:"2-27"},
		{caption:"Test 2 - item 28",type:"text",key:"2-28"},
		{caption:"Test 2 - item 29",type:"text",key:"2-29"},
		{caption:"Test 2 - item 30",type:"text",key:"2-30"},
		{caption:"Test 2 - item 31",type:"text",key:"2-31"},
		{caption:"Test 3 - item 1",type:"text",key:"1-1"},
		{caption:"Test 3 - item 2",type:"text",key:"1-2"},
		{caption:"Test 3 - item 3",type:"text",key:"1-3"},
		{caption:"Test 3 - item 4",type:"text",key:"1-4"},
		{caption:"Test 3 - item 5",type:"text",key:"1-5"},
		{caption:"Test 3 - item 6",type:"text",key:"1-6"},
		{caption:"Test 3 - item 7",type:"text",key:"1-7"},
		{caption:"Test 3 - item 8",type:"text",key:"1-8"},
		{caption:"Test 3 - item 9",type:"text",key:"1-9"},
		{caption:"Test 3 - item 10",type:"text",key:"1-10"},
		{caption:"Test 3 - item 11",type:"text",key:"1-11"},
		{caption:"Test 3 - item 12",type:"text",key:"1-12"},
		{caption:"Test 3 - item 13",type:"text",key:"1-13"},
		{caption:"Test 3 - item 14",type:"text",key:"1-14"},
		{caption:"Test 3 - item 15",type:"text",key:"1-15"},
		{caption:"Test 3 - item 16",type:"text",key:"1-16"},
		{caption:"Test 3 - item 17",type:"text",key:"1-17"},
		{caption:"Test 3 - item 18",type:"text",key:"1-18"},
		{caption:"Test 3 - item 19",type:"text",key:"1-19"},
		{caption:"Test 3 - item 20",type:"text",key:"1-20"},
		{caption:"Test 3 - item 21",type:"text",key:"1-21"},
		{caption:"Test 3 - item 22",type:"text",key:"1-22"},
		{caption:"Test 3 - item 23",type:"text",key:"1-23"},
		{caption:"Test 3 - item 24",type:"text",key:"1-24"},
		{caption:"Test 3 - item 25",type:"text",key:"1-25"},
		{caption:"Test 3 - item 26",type:"text",key:"1-26"},
		{caption:"Test 3 - item 27",type:"text",key:"1-27"},
		{caption:"Test 3 - item 28",type:"text",key:"1-28"},
		{caption:"Test 3 - item 29",type:"text",key:"1-29"},
		{caption:"Test 3 - item 30",type:"text",key:"1-30"},
		{caption:"Test 3 - item 31",type:"text",key:"1-31"},
		{caption:"Test 3 - item 32",type:"text",key:"1-32"},
		{caption:"Test 3 - item 33",type:"text",key:"1-33"},
		{caption:"Test de los ojos - item 0",type:"text",key:"4-0"},
		{caption:"Test de los ojos - item 1",type:"text",key:"4-1"},
		{caption:"Test de los ojos - item 2",type:"text",key:"4-2"},
		{caption:"Test de los ojos - item 3",type:"text",key:"4-3"},
		{caption:"Test de los ojos - item 4",type:"text",key:"4-4"},
		{caption:"Test de los ojos - item 5",type:"text",key:"4-5"},
		{caption:"Test de los ojos - item 6",type:"text",key:"4-6"},
		{caption:"Test de los ojos - item 7",type:"text",key:"4-7"},
		{caption:"Test de los ojos - item 8",type:"text",key:"4-8"},
		{caption:"Test de los ojos - item 9",type:"text",key:"4-9"},
		{caption:"Test de los ojos - item 10",type:"text",key:"4-10"},
		{caption:"Test de los ojos - item 11",type:"text",key:"4-11"},
		{caption:"Test de los ojos - item 12",type:"text",key:"4-12"},
		{caption:"Test de los ojos - item 13",type:"text",key:"4-13"},
		{caption:"Test de los ojos - item 14",type:"text",key:"4-14"},
		{caption:"Test de los ojos - item 15",type:"text",key:"4-15"},
		{caption:"Test de los ojos - item 16",type:"text",key:"4-16"},
		{caption:"Test de los ojos - item 17",type:"text",key:"4-17"},
		{caption:"Test de los ojos - item 18",type:"text",key:"4-18"},
		{caption:"Test de los ojos - item 19",type:"text",key:"4-19"},
		{caption:"Test de los ojos - item 20",type:"text",key:"4-20"},
		{caption:"Test de los ojos - item 21",type:"text",key:"4-21"},
		{caption:"Test de los ojos - item 22",type:"text",key:"4-22"},
		{caption:"Test de los ojos - item 23",type:"text",key:"4-23"},
		{caption:"Test de los ojos - item 24",type:"text",key:"4-24"},
		{caption:"Test de los ojos - item 25",type:"text",key:"4-25"},
		{caption:"Test de los ojos - item 26",type:"text",key:"4-26"},
		{caption:"Test de los ojos - item 27",type:"text",key:"4-27"},
		{caption:"Test de los ojos - item 28",type:"text",key:"4-28"},
		{caption:"Test de los ojos - item 29",type:"text",key:"4-29"},
		{caption:"Test de los ojos - item 30",type:"text",key:"4-30"},
		{caption:"Test de los ojos - item 31",type:"text",key:"4-31"},
		{caption:"Test de los ojos - item 32",type:"text",key:"4-32"},
		{caption:"Test de los ojos - item 33",type:"text",key:"4-33"},
		{caption:"Test de los ojos - item 34",type:"text",key:"4-34"},
		{caption:"Test de los ojos - item 35",type:"text",key:"4-35"},
		{caption:"Test de los ojos - item 36",type:"text",key:"4-36"}


	];
	//var colCompleted = false;
	//colArray.push({caption:'Codigo',type:'number'});
		User.find({},function(err,users){
		//	console.log("All users:"+JSON.stringify(users));
			if(err==null && users!=null){
			users.forEach(function(user){
				var rA = [];
				var rA1 = [];


			//	rA.push(user.idUser);

				//console.log("Id user: "+user.idUser);

				var dic = {};
				var dic1 = {};

					user.answers.forEach(
					function(ans){
					//console.log("Answer: "+ans.answerValue);

					if(ans!=null && typeof ans.answerValue != 'undefined'){
						dic[ans.testNo.toString()+"-"+ans.answerNo.toString()] = ans.answerValue;

					}

					//console.log("Key: "+ans.testNo.toString()+"-"+ans.answerNo.toString());
					//rA.push(ans.answerValue);

					/*if(!colCompleted){

						var captionValue = "Test: "+ans.testNo+ "Answer: "+ans.answerNo;
					//	colArray.push({caption:captionValue,type:'text'});
					}*/

				});

					user.tests.forEach(function(ans){
						if(ans!=null && typeof ans.testNo != 'undefined'){
							dic1["r"+ans.testNo.toString()] = ans.result.toString();
							//console.log("store: "+ans.testNo.toString()+" value: ")
						}
					});


			//	colCompleted = true;



			dic["code"] = 	user.idUser;
			dic["timestamp"] = user.time;
			dic1["code"] = 	user.idUser;
			dic1["timestamp"] = user.time;

				colArray.forEach(
					function(colItem){
						var storedVal = "";


						if(dic[colItem.key]!=null&& typeof dic[colItem.key] !='undefined'){
						storedVal = dic[colItem.key];

							//console.log("key: "+colItem.key+" value: "+storedVal);

						}
						rA.push(storedVal);





					});

					//console.log("Vector rA: ");
					//before push the array:
					//rA.forEach(function(item){
					//	console.log("Item: "+item)
					//});
			rowArray.push(rA);

			colArray1.forEach(
					function(colItem){
						var storedVal = "";


						if(dic1[colItem.key]!=null&& typeof dic1[colItem.key] !='undefined'){
						storedVal = dic1[colItem.key];

							//console.log("key: "+colItem.key+" value: "+storedVal);

						}
						rA1.push(storedVal);





					});

					//console.log("Vector rA: ");
					//before push the array:
					//rA1.forEach(function(item){
					//	console.log("Item: "+item)
					//});
			rowArray1.push(rA1);

	/*		console.log("Showing content");
		 //show row array:
		 rowArray.forEach(function(element){
				element.forEach(function(item){
					console.log("item: "+item);
				});

				console.log("showing cols:");

				colArray.forEach(function(item){
					console.log("Label: "+JSON.stringify(item));
				});

				*/

		 });

		  //  conf.stylesXmlFile = "styles.xml";
    conf[0].cols = colArray;
    conf[1].cols = colArray1;


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
    conf[0].rows = rowArray;
    conf[1].rows = rowArray1;
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



			}

		 });








	});





// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
