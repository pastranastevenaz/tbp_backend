# Backend for Teamname by Proxy site

### AWS ambda entpoints
ROOT
https://9374efz9mk.execute-api.us-west-1.amazonaws.com/dev/
EXCEPTION FORM
https://9374efz9mk.execute-api.us-west-1.amazonaws.com/dev/sendex

### Licence
GNU GENERAL PUBLIC LICENSE



#### Notes
Sending AWS POST Requests (Example)
curl -H "Content-Type: application/json" -X POST -d "{\"na
me\": \"User\"}" https://9374efz9mk.execute-api.us-west-1.amazonaws.com/dev/sendex