import os
import re

# ================= CONFIG =================
RESULTS_DIR = "distributed_network_validator/results"
# ==========================================

def parse_packet_loss(content):
    """
    Extract packet loss percentage from fping / ping output
    Example: '10 packets transmitted, 9 received, 10% packet loss'
    """
    match = re.search(r"(\d+)%\s*packet loss", content)
    if match:
        return int(match.group(1))
    return None


def parse_iperf_loss(content):
    """
    Extract UDP loss from iperf3 output (if available)
    Example: '0.0-10.0 sec  ...  0/1000 (0%)'
    """
    match = re.search(r"\((\d+)%\)", content)
    if match:
        return int(match.group(1))
    return None


def analyze_file(filepath):
    with open(filepath, "r") as f:
        data = f.read()

    loss = parse_packet_loss(data)

    if loss is None:
        loss = parse_iperf_loss(data)

    return loss


def main():
    print("\n🔍 Packet Loss Analysis\n")

    if not os.path.exists(RESULTS_DIR):
        print(f"[ERROR] Results directory not found: {RESULTS_DIR}")
        return

    files = os.listdir(RESULTS_DIR)

    if not files:
        print("[INFO] No result files found.")
        return

    total_files = 0
    total_loss = 0
    failed = 0

    for file in files:
        filepath = os.path.join(RESULTS_DIR, file)

        if not os.path.isfile(filepath):
            continue

        loss = analyze_file(filepath)

        if loss is not None:
            print(f"[FILE] {file} → Packet Loss: {loss}%")

            total_files += 1
            total_loss += loss

            if loss > 0:
                failed += 1
        else:
            print(f"[FILE] {file} → No packet loss data found")

    print("\n📊 Summary")
    print("-" * 40)

    if total_files > 0:
        avg_loss = total_loss / total_files
        print(f"Total Files Analyzed : {total_files}")
        print(f"Average Packet Loss  : {avg_loss:.2f}%")
        print(f"Files with Loss > 0  : {failed}")
    else:
        print("No valid data found.")


if __name__ == "__main__":
    main()
