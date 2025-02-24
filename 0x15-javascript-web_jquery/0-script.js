#!/usr/bin/node
/**
  * script updates the color of the <header> element to red
*/

window.onload = function updateColor () {
  const h = document.querySelector('header');
  h.style.color = 'red';
};
