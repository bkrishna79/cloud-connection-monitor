import requests
import time

# ================= CONFIG =================
URLS = [
    "https://example.com",
    "https://www.google.com"
]

INTERVAL = 5  # seconds
# ==========================================

def check_endpoint(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        latency = (time.time() - start) * 1000

        print(f"[OK] {url} | Status={response.status_code} | Latency={latency:.2f} ms")

    except Exception as e:
        print(f"[ERROR] {url} | {e}")


def main():
    print("Starting Endpoint Validator...\n")

    while True:
        for url in URLS:
            check_endpoint(url)

        print("-" * 50)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
