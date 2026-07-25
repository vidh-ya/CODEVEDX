from sql_injection_test import sql_injection_test
from xss_test import xss_test
from csrf_test import csrf_test

def main():
    print("=== Web Application Penetration Testing Tool ===")
    target = input("Enter Target URL (example: http://testphp.vulnweb.com): ")

    print("\n[+] Starting SQL Injection Test...")
    sql_payloads = ["' OR '1'='1", "' UNION SELECT null,null--"]
    sql_results = sql_injection_test(target, sql_payloads)

    print("\n[+] Starting XSS Test...")
    xss_payloads = ["<script>alert('XSS')</script>", "\" onmouseover=\"alert('XSS')"]
    xss_results = xss_test(target, xss_payloads)

    print("\n[+] Starting CSRF Test...")
    csrf_results = csrf_test(target)

    print("\n=== Scan Completed ===")
    print("SQL Injection Results:", sql_results)
    print("XSS Results:", xss_results)
    print("CSRF Results:", csrf_results)

if __name__ == "__main__":
    main()
