# Distributed Network Validator

## 🚀 Overview
The Distributed Network Validator is an Ansible-based framework designed to execute large-scale network validation across multiple virtual machines.

It automates TCP, UDP, and ICMP testing between nodes, collects results centrally, and enables analysis of performance and packet loss.

This tool is built based on real-world cloud validation and customer PoC scenarios.

---

## 🎯 Key Capabilities

- Multi-node network testing across distributed environments  
- Automated orchestration using Ansible  
- TCP throughput validation using iperf3  
- UDP performance and loss analysis  
- ICMP reachability testing using fping  
- Centralized result collection from all nodes  
- Scalable to tens or hundreds of virtual machines  

---

## 🧩 Architecture

        Ansible Controller
                │
        ┌───────┴────────┐
        │                │
   Client Nodes     Server Nodes
        │                │
        └───────┬────────┘
                │
        Test Execution (TCP / UDP / ICMP)
                │
        Result Collection (fetch)
                │
        Centralized Analysis

---

## 📂 Directory Structure

distributed_network_validator/
 ├── playbooks/
 │    ├── tcp_test.yml
 │    ├── udp_test.yml
 │    ├── icmp_test.yml
 ├── inventory/
 │    ├── inventory_sample.ini
 ├── results/

---

## ⚙️ Prerequisites

- Ansible installed on control node  
- SSH access to all target nodes  
- Python3 installed on all nodes  
- iperf3 installed (or installed via playbook)  
- fping installed for ICMP testing  

---

## 🔧 Inventory Setup

A sample inventory is provided:

inventory/inventory_sample.ini

Example:

[clients]
client1 ansible_host=10.0.0.10

[servers]
server1 ansible_host=10.0.0.20

[all:vars]
ansible_user=root
ansible_ssh_private_key_file=~/.ssh/id_rsa

Note: Use your own inventory for real environments. Do not commit sensitive data.

---

## ▶️ Usage

Run TCP Test:
ansible-playbook -i inventory/inventory_sample.ini playbooks/tcp_test.yml

Run UDP Test:
ansible-playbook -i inventory/inventory_sample.ini playbooks/udp_test.yml

Run ICMP Test:
ansible-playbook -i inventory/inventory_sample.ini playbooks/icmp_test.yml

---

## 📊 Output

- Results are collected from all nodes  
- Stored under:

results/

- Each file represents test output from a node or node pair  

---

## 📌 Use Cases

- Multi-node cloud network validation  
- Customer PoC testing environments  
- Throughput benchmarking (TCP/UDP)  
- Packet loss detection  
- Network stability validation across zones  
- Large-scale VSI connectivity testing  

---

## 🔍 Observability & Analysis

Collected results can be:
- Parsed using Python scripts  
- Integrated with monitoring tools (Telegraf, InfluxDB, Grafana)  
- Used for identifying packet loss and performance bottlenecks  

---

## ⚠️ Security Considerations

- Do not expose real IP addresses in public repositories  
- Use sanitized inventory files  
- Protect SSH private keys  
- Ensure proper authorization before running tests  

---

## 🔭 Future Enhancements

- Automated result parsing and reporting  
- Packet loss and latency dashboards  
- Integration with Prometheus/Grafana  
- Parallel execution optimization  
- Multi-region testing support  

---

## 👨‍💻 Author

Radhakrishnan Balasubramanian  
Cloud & Networking Engineer | CCIE | Security Enthusiast (CEH / CPENT)

