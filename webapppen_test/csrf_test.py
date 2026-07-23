import requests

def csrf_test(url):
    try:
        response = requests.get(url)
        if "csrf" not in response.text.lower():
            print("[!] CSRF protection missing!")
            return "No CSRF protection"
        else:
            print("[+] CSRF protection detected.")
            return "CSRF protection enabled"
    except Exception as e:
        return f"Error: {e}"
