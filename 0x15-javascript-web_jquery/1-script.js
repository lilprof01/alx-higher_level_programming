#!/usr/bin/node
/**
  * script updates text color of the <header> element to red
*/
const $ = window.$;
$(document).ready(function () {
  $('header').css('color', '#FF0000');
});
