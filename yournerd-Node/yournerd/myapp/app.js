
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , user = require('./routes/user')
  , test = require('./routes/test')
  , mysql = require('mysql')
  , http = require('http')
  , path = require('path');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(express.cookieParser('your secret here'));
  app.use(express.session());
  //app.use(jquery('/jquery.js'));
  app.use(app.router);
  app.use(require('stylus').middleware(__dirname + '/public'));
  app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

var client = mysql.createConnection({user: 'root', password: ''});
client.connect();

var connection = require("./mysql.js");
connection.setConnection(client);
//client.query("use smartphone;");


app.get('/jade', function(req, res){
  res.render('users');
});

app.get('/rateThumb', function(req, res){
  var feed = "";
  connection.getRateThumb(function(rows){
    rows.forEach(function(entry){
      feed += entry.rate_phrase;
    });
    res.send(feed);
  });
});

app.get("/rateThumb.json", function(req, res){
  connection.getRateThumb(function(rows){
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.write(JSON.stringify(rows));
    res.end();
  });
});

app.get("/insertRateThumb", function (req, res) {
  connection.insertRateThumb(function ("phrase", 5) {
    res.end();
  }


});


http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
