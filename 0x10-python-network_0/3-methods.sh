#!/bin/bash
# Request for all HTTP methods a URL's server accepts
curl -sILX OPTIONS | grep "Allow" | cut -d " " -f 2
