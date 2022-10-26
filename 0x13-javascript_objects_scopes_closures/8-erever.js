#!/bin/usr/node
exports.esrever = function (list) {
	const invertedList = [];
	for (const e of list) invertedList.unshift(e);
	return invertedList;
};
