#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg === 1) {
  console.log(arg + ' is undefined');
} else {
  console.log(arg[0] + ' is ' + arg[1]);
}
