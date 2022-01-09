#!/bin/bash
# cURL to the end
curl -sI "$1" | grep -i content-length | awk '{print $2}'
