#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) console.log(err);
  else console.log(data);
});
