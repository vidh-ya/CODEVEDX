import requests

def sql_injection_test(url, payloads):
    results = []
    for payload in payloads:
        try:
            # இங்கே timeout சேர்க்க வேண்டும்
            response = requests.get(url, params={"id": payload}, timeout=5)

            if "error" in response.text.lower():
                print(f"[!] Possible SQL Injection with payload: {payload}")
                results.append(payload)

        except requests.exceptions.Timeout:
            print(f"[x] Timeout occurred for payload: {payload}")
        except requests.exceptions.ConnectionError:
            print(f"[x] Connection error for payload: {payload}")

    return results
