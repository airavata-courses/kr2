const express = require("express");
const router = express.Router();

//UserProfile Model
const UserProfile = require("../../models/UserProfile");

//@route  GET api/users
router.get("/", (req, res) => {
  UserProfile.find()
    .sort({ date: -1 })
    .then(userprofiles => res.json(userprofiles));
});

//@route  POST api/users
router.post("/", (req, res) => {
  console.log("At server" + JSON.stringify(req.body));
  const newUser = new UserProfile({
    name: req.body.name
  });
  console.log("At server" + req);
  newUser.save().then(item => res.json(item));
});
module.exports = router;
