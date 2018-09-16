const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const UserProfiles = require("./routes/api/UserProfiles");

const app = express();

//body parser middleware
app.use(bodyParser.json());

//db URI
const db = require("./config/keys").mongoURI;

//connect to MONGO
mongoose
  .connect(
    db,
    { useNewUrlParser: true }
  )
  .then(() => console.log("MongoDB connected....."))
  .catch(err => console.log(err));

//Use Routes
app.use("/api/UserProfiles", UserProfiles);

const port = process.env.PORT || 4000;

app.listen(port, () => console.log(`Server started on port ${port}`));

module.exports = app;
