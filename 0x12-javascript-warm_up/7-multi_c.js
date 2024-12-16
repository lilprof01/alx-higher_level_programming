#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  x = parseInt(arg);
  while (x > 0) {
    console.log('C is fun');
    x--;
   }
}
