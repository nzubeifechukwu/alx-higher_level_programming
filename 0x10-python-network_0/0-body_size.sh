#!/usr/bin/bash
# This script accepts a url, sends a request to the url and displays the size of the body response in bytes
curl -sI "$1" | grep "Connection-Length" | cut -d " " -f 2
