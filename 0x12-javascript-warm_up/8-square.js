#!/usr/bin/node
const b = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < x; a++) {
    let y = 0;
    let myVar = '';

    while (y < b) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
