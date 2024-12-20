#!/usr/bin/node

const fs = require('fs');
const path = require('path');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const data1 = fs.readFileSync(path.join(__dirname, sourceFile1));
const data2 = fs.readFileSync(path.join(__dirname, sourceFile2));

fs.writeFileSync(path.join(__dirname, destinationFile), data1 + data2);
