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

router.get("/fetchByMail/:emailId", (req, res) => {
  var emailId = req.params.emailId;

  UserProfile.findOne({ email: emailId }).then(userprofiles =>
    res.json(userprofiles)
  );
});

//@route  POST api/users
router.post("/", (req, res) => {
  let newUser = new UserProfile({
    name: req.body.name,
    email: req.body.email,
    location: req.body.location
  });

  newUser.save().then(item => res.json(item));
});
module.exports = router;
