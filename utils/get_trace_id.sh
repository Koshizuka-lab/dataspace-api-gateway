#!/bin/bash

current_dir=$(dirname "$0")
access_token=$(bash "$current_dir"/get_token.sh | jq -r '.accessToken')

curl -s -X GET -H 'Content-Type: application/json' -H 'apiKey: Sample-APIKey1' \
  -H "Authorization: Bearer $access_token" \
  'http://10.250.4.103:8080/api/v1/datatransport?dataTarget=parts'
