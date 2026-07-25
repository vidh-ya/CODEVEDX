import requests

def xss_test(url, payloads):
    results = []
    for payload in payloads:
        response = requests.get(url, params={"q": payload})
        if payload in response.text:
            print(f"[!] Possible XSS with payload: {payload}")
            results.append(payload)
    return results
