import os, sys, json, urllib3, requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = os.getenv("DASHBOARD_URL", "https://wazuh.example.com")
API_USER = os.getenv("API_USER")
API_PASS = os.getenv("API_PASS")

def main():
    # Manager API URL is proxied only if Traefik is configured to do so.
    # For a direct health probe, hit the dashboard root to ensure 200 OK.
    try:
        r = requests.get(URL, timeout=20, verify=False)
        print("Status:", r.status_code)
        assert r.status_code in (200, 302)
        print("OK")
    except Exception as e:
        print("Probe failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
