import requests
import oauth2

client_key = 'ojz3ckmJbBLRZQjtm99uqDUK2'
client_secret = 'BfIpUP30YLjci5tZSrii5j9IMi6SUDxUkJMXWrKVA9GyzkZoMQ'

access_token = '707272672846225408-igKhPNxj1zzOe90vs1DHv8dcXlHCM22'
token_secret = 'CLpgUfYtJHjkX7QFYXmtn7cfcXvMIZWt3CiknFVRGx7Fg'

url = 'https://api.twitter.com/1.1/followers/list.json'

def oauth_req(url, key, secret, http_method="GET", post_body=b"", http_headers="None"):
    consumer = oauth2.Consumer(key=client_key, secret=client_secret)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    #content = json.loads(content.decode("utf-8"))
    return content

followers = oauth_req(url, access_token, token_secret)
print(followers)
