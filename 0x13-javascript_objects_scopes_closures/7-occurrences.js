#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;

  for (let ite = 0; ite <= list.length; ite++) {
    if (list[ite] === searchElement) {
      num++;
    }
  }
  return num;
};
