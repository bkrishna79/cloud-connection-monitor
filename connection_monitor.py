import ssl
import socket
import threading
import time

# ================= CONFIGURATION =================
TARGET_HOST = "example.com"   # Replace with your endpoint
PORT = 443
HOST_HEADER = "example.com"

TOTAL_CONN = 1000        # Safe default
TARGET_CPS = 50          # Connections per second
KEEPALIVE_INTERVAL = 5   # Seconds between keepalive
BATCH_SIZE = 200         # Batch processing size
# =================================================

connections = []
lock = threading.Lock()


def create_conn(i):
    """Create a single TCP/TLS connection and send initial request."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.settimeout(5)

        sock.connect((TARGET_HOST, PORT))

        context = ssl._create_unverified_context()
        ssock = context.wrap_socket(sock, server_hostname=HOST_HEADER)
        ssock.setblocking(False)

        req = f"HEAD / HTTP/1.1\r\nHost: {HOST_HEADER}\r\nConnection: keep-alive\r\n\r\n"
        ssock.sendall(req.encode())

        with lock:
            connections.append(ssock)

        print(f"[+] Conn {i} ESTABLISHED")

    except Exception as e:
        print(f"[!] Conn {i} FAILED: {e}")


def keepalive_loop():
    """Send periodic keepalive requests and track connection health."""
    while True:
        time.sleep(KEEPALIVE_INTERVAL)

        sent = 0
        dropped = 0

        with lock:
            total = len(connections)

        print(f"\n[INFO] Running keepalive on {total} connections")

        for i in range(0, total, BATCH_SIZE):
            batch = connections[i:i + BATCH_SIZE]

            for conn in batch:
                try:
                    req = f"HEAD / HTTP/1.1\r\nHost: {HOST_HEADER}\r\nConnection: keep-alive\r\n\r\n"
                    conn.sendall(req.encode())
                    sent += 1

                    try:
                        conn.recv(4096)
                    except BlockingIOError:
                        pass

                except Exception:
                    dropped += 1
                    try:
                        conn.close()
                    except:
                        pass

                    with lock:
                        if conn in connections:
                            connections.remove(conn)

        print(f"[STATS] Active={len(connections)} Sent={sent} Dropped={dropped}")


def main():
    print(f"Starting connection monitor → target={TARGET_HOST}:{PORT}, total={TOTAL_CONN}, cps={TARGET_CPS}")

    threads = []

    for i in range(TOTAL_CONN):
        start = time.time()

        t = threading.Thread(target=create_conn, args=(i,))
        t.start()
        threads.append(t)

        elapsed = time.time() - start
        sleep_time = max(0, (1 / TARGET_CPS) - elapsed)
        time.sleep(sleep_time)

    for t in threads:
        t.join()

    print("[INFO] All connections established")

    threading.Thread(target=keepalive_loop, daemon=True).start()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
