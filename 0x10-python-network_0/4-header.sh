#!/bin/bash
# Send a GET request, with a new header variable set, and display the body of the response
curl -s "$1" -H "X-School-User-Id:98"
