def api_request(endpoint, method="GET", *, timeout=10, retry_cout=3, headers=None, params=None):
    request_info = f"Making a {method} request to {endpoint} with timeout {timeout}s and {retry_cout} retries."
    if headers:
        request_info += f" Headers: {headers}"
    print(request_info)