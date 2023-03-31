#!/bin/bash
# Send a POST request to a URL and display the body of the response
curl -s "$1" -d email="test@gmail.com" -d subject="I will always be here for PLD"
