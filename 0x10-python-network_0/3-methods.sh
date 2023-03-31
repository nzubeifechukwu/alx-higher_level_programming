#!/bin/bash
# Request for all HTTP methods a URL's server accepts
curl -sIL "$1" -X OPTIONS | grep "Allow" | cut -c 8-
