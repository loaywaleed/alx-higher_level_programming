#!/usr/bin/node
/* printing number of argument */

if (process.argv.length === 2) {
	console.log('No argument');
} else if (process.argv === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
