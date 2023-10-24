#!/usr/bin/node
// obtaining number of tasks completed by users

const request = require('request');
const url = process.argv[2];

const tasksByUser = {};
const completedPerUser = Array(11).fill(0);

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const arrayOfTasks = JSON.parse(body);
  for (let i = 0; i < arrayOfTasks.length; i++) {
    for (let j = 0; j < 11; j++) {
      if (arrayOfTasks[i].userId === j) {
        if (arrayOfTasks[i].completed === true) {
          completedPerUser[j]++;
          tasksByUser[j] = completedPerUser[j];
        }
      }
    }
  }
  console.log(tasksByUser);
}
);
