curl -s -X POST -H 'Content-Type: application/json' -H 'apiKey: Sample-APIKey1' \
  http://10.250.4.103:8081/auth/login \
  --data-raw '{
  "operatorAccountId": "oem_a@example.com",
  "accountPassword": "oemA&user_01"
  }'

