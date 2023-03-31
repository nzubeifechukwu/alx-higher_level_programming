#!/bin/bash
# Request for all HTTP methods a URL's server accepts
curl -sILX OPTIONS "$1" | grep "Allow" | cut -c 2
