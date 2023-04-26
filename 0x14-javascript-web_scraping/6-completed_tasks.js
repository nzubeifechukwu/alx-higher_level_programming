#!/usr/bin/node
/**
 * For a given API url (https://jsonplaceholder.typicode.com/todos), passed as
 * the first argument, compute the number of tasks completed by user id
 * (print only users with at least one completed task).
 */
const process = require('process');
const request = require('request');

const url = process.argv[2];

request({ url: url, json: true }, function (error, response, body) {
  if (!error) {
    let taskCount = 0;
    const tasksByUser = {};
    const userIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    for (const id of userIds) {
      for (const task of body) {
        if (id === task.userId && task.completed === true) {
          taskCount++;
        }
      }
      if (taskCount > 0) {
        tasksByUser[id] = taskCount;
      }
      taskCount = 0;
    }
    console.log(tasksByUser);
  }
});
