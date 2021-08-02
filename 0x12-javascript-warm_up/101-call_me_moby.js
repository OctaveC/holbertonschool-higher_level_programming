#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let ite = 0; ite < x; ite++) {
    theFunction();
  }
};
