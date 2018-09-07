var express = require("express");
var app = express();
const bodyparser = require("body-parser");
app.use(bodyparser.json());

var MongoClient = require("mongodb").MongoClient;
var url = "mongodb://localhost:27017/mydb";
var myUser = [
  {
    userid: 1,
    userName: "Smith"
  },
  {
    userid: 2,
    userName: "Mohan"
  },
  {
    userid: 3,
    userName: "Joe"
  }
];

MongoClient.connect(
  url,
  { useNewUrlParser: true },
  function(err, db) {
    if (err) throw err;
    var dbo = db.db("usnaukri");
    var myobj = { name: "Company Inc", address: "Highway 37" };
    dbo.createCollection("users", function(err, res) {
      if (err) throw err;
      console.log("Collection created!");
      dbo.collection("users").insertMany(myUser, function(err, res) {
        if (err) throw err;
        console.log(" documents inserted");
      });
      db.close();
    });
  }
);

var port = process.env.PORT || 3000;

app.listen(port);
