const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const UserProfileSchema = new Schema({
  name: {
    type: String
  },
  email: {
    type: String
  },
  location: {
    type: String
  },
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = UserProfile = mongoose.model("UserProfile", UserProfileSchema);
