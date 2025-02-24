#!/usr/bin/node
/**
  * script toggles the class of the <header>element
  * when the user clicks on tag DIV#toggle_header
  */
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
