import time
import random

# ================= CONFIG =================
OUTPUT_FILE = "metrics.log"
INTERVAL = 5
# ==========================================

def generate_metrics():
    # Dummy values (can be replaced with real integration later)
    active = random.randint(900, 1000)
    dropped = random.randint(0, 10)

    return active, dropped


def write_metrics(active, dropped):
    timestamp = int(time.time())

    line = f"timestamp={timestamp} active={active} dropped={dropped}\n"

    with open(OUTPUT_FILE, "a") as f:
        f.write(line)


def main():
    print("Starting Metrics Logger...\n")

    while True:
        active, dropped = generate_metrics()

        write_metrics(active, dropped)

        print(f"[INFO] Active={active} Dropped={dropped} (written to {OUTPUT_FILE})")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
