#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];

  for (const ite of list) {
    rev.unshift(ite);
  }

  return rev;
};
