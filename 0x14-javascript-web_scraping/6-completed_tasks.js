#!/usr/bin/node
// Computes the number tasks completed by user id.

const request = require('request');
const URL = process.argv[2];
const completedTasks = {};

request(URL, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const data = JSON.parse(body);

  for (let i = 0; i < data.length; i++) {
    const task = data[i];

    if (task.completed === true) {
      const userID = task.userId;

      if (completedTasks[userID] === undefined) {
        completedTasks[userID] = 1;
      } else {
        completedTasks[userID]++;
      }
    }
  }
  console.log(completedTasks);
});
