""""
This is my most recent educationIn the first request, the auth_token = 347sd6yk8iu2, which is not in the list of given tokens, so the request is INVALID. The string to be returned is "INVALID".

In the second request, the auth_token = safh34ywb0p5, which is in the list of valid tokens, so the request is VALID. The request parameters are - name = sam. The string to be returned is "VALID,name,sam".

In the third request, the auth_token = safh34ywb0p5, which is in the list of valid tokens, but since the request is a POST request, it must have a valid CSRF token. Since the given request doesn't have a CSRF token, the request is INVALID. The string to be returned is "INVALID".

In the fourth request, the auth_token = safh34ywb0p5, which is in the list of valid tokens, but since the request is a POST request, it must have a valid CSRF token. CSRF_token = ak2sh32dy. It is an alphanumeric string with length 9 (>=8), so the given request is VALID. The request parameters are - name = chris. The string to be returned is "VALID,name,chris".

The responses returned are ["INVALID", "VALID,name,sam", "INVALID", "VALID,name,chris"].

string valid_auth_tokens[m]:  The list of valid authentication tokens the requests

string requests[n][2]: The list of requests made, their types and the associated URLs.

swap
"""

valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
# requests = [["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"], 
#             ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"], 
#             ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
#             ["POST”, "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]] 
 
           
def getResponses(valid_auth_tokens, requests):
    for token in valid_auth_tokens:
        for request in requests:
            if re