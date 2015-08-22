var config{};

//create JSON objects for configuration
config.mongo = {};
config.nodejs = {};
// mongoDB configuration with mongoose connect convention:
// see: http://mongoosejs.com/docs/connections.html
config.mongo.host = "localhost";
config.mongo.port = "27017"; // default mongoDB port
config.mongo.database = "users";
config.mongo.user = "adminUser";
config.mongo.pass = "toor";

//node JS server config:
config.nodejs.port = 8080;


//export the modules:
module.exports = config;