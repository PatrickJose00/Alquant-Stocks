const express = require("express");
const path = require("path");

const port = process.env.PORT || 8080;
const app = express();

// Set the static folder path
const staticFolderPath = path.join(__dirname, "dist");
app.use(express.static(staticFolderPath));

app.get("/*", function(req, res) {
  res.sendFile(path.join(staticFolderPath, "index.html"));
});

app.listen(port, function() {
  console.log("Server started on port", port);
});