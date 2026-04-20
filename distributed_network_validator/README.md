# Cloud Connection Monitoring & Network Validation Toolkit

## 🚀 Overview
This repository provides a set of tools to simulate, monitor, and validate network behavior in cloud environments.

It combines:
- Persistent connection testing  
- Endpoint validation  
- Metrics generation  
- Distributed multi-node network testing using Ansible  
- Packet loss analysis and outage detection  

The toolkit is built based on real-world customer PoC and cloud validation scenarios.

---

## 🔧 Toolkit Components

### 🔹 Connection Monitor
- Simulates large-scale persistent TCP/TLS connections  
- Maintains connections using keepalive (HTTP HEAD)  
- Tracks connection health and drops  

File:
connection_monitor.py

---

### 🔹 Endpoint Validator
- Continuously validates HTTP endpoints  
- Measures latency and HTTP response status  

File:
endpoint_validator.py

---

### 🔹 Metrics Logger
- Generates and logs metrics  
- Can integrate with Telegraf / InfluxDB / Grafana  

File:
metrics_logger.py

---

### 🔹 Packet Loss Analyzer ⭐
- Parses fping and iperf outputs  
- Detects packet loss events across nodes  
- Identifies outage windows (start/end time)  
- Calculates outage duration  

File:
packet_loss_analyzer.py

---

### 🔹 Distributed Network Validator (Ansible)

Automates network testing across multiple virtual machines.

#### Capabilities
- TCP testing using iperf3  
- UDP performance validation  
- ICMP reachability testing (fping)  
- Centralized result collection  

#### Structure
distributed_network_validator/
 ├── playbooks/
 ├── inventory/
 ├── results/

---

## 🎯 Key Capabilities

- Persistent connection simulation at scale  
- Endpoint health and latency monitoring  
- Metrics generation for observability pipelines  
- Distributed network validation across multiple nodes  
- TCP, UDP, and ICMP testing support  
- Packet loss detection and outage analysis  

---

## ❗ Problem Statement

Traditional tools like `wrk` and `iperf` focus on short-lived throughput testing and do not provide visibility into:

- Long-lived connection stability  
- Keepalive behavior  
- Distributed network validation  
- Packet loss trends and outage duration  

This toolkit addresses these gaps with both connection-level and system-level validation.

---

## 🧩 Architecture

Connection Monitor → Persistent Sessions  
        ↓  
Endpoint Validator → HTTP Health Checks  
        ↓  
Metrics Logger → Observability Data  
        ↓  
Distributed Validator → Multi-node Testing  
        ↓  
Packet Loss Analyzer → Outage Detection  

---

## 📊 Sample Output

[INFO] Running keepalive on 1000 connections  
[STATS] Active=998 Dropped=2  

[OK] https://example.com | Status=200 | Latency=25ms  

Packet Loss Report  
Source: 10.0.0.1 → Dest: 10.0.0.2 → Duration: 5s  

---

## 📌 Use Cases

- Cloud Object Storage (COS) validation  
- Customer PoC environments  
- Multi-zone network validation  
- Large-scale connection stability testing  
- Packet loss and outage detection  
- Observability pipeline validation  

---

## ⚠️ Security Note

- Sample inventory files are provided  
- Do NOT commit real infrastructure details or SSH keys  
- Always use sanitized configurations  

---

## 🔭 Future Enhancements

- Telegraf integration  
- InfluxDB support  
- Grafana dashboards  
- Automated result analysis  
- Multi-region distributed execution  

---

## 👨‍💻 Author

Radhakrishnan Balasubramanian  
Cloud & Networking Engineer | CCIE | Security Enthusiast (CEH / CPENT)

