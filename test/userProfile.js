process.env.NODE_ENV = "test";

let mongoose = require("mongoose");
let Book = require("../models/UserProfile");

let chai = require("chai");
let chaiHttp = require("chai-http");
let server = require("../index.js").server;
let should = chai.should();

chai.use(chaiHttp);

describe("Status and content of User Registration", function() {
  it("it should POST the user with given details", done => {
    let user = {
      name: "John",
      email: "john@gmail.com",
      location: "Bloomington"
    };
    chai
      .request(server)
      .post("/api/userprofiles")
      .send(user)
      .end((err, res) => {
        res.should.have.status(200);
        res.body.should.be.a("object");
        res.body.should.have.property("name");
        res.body.should.have.property("email");
        res.body.should.have.property("location");
        done();
      });
  });
});

describe("Status and content of Fetching user with specific email", () => {
  afterEach(function() {
    server.close();
  });

  it("it should get the user with given email", done => {
    var email = "john@gmail.com";

    chai
      .request(server)
      .get("/api/userprofiles/fetchByMail/" + "john@gmail.com")
      .end((err, res) => {
        res.should.have.status(200);
        res.body.should.be.a("object");
        res.body.should.have.property("name").eql("John");
        res.body.should.have.property("email").eql("john@gmail.com");
        res.body.should.have.property("location").eql("Bloomington");
        done();
      });
  });
});
