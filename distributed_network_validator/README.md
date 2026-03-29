# Distributed Network Validator

## 🚀 Overview
Automates multi-node network testing across virtual servers using Ansible.

Supports TCP, UDP, and ICMP validation and collects results centrally for analysis.

---

## 📂 Structure

- playbooks/
  - tcp_test.yml
  - udp_test.yml
  - icmp_test.yml
- inventory/
  - inventory.ini
- results/

---

## 🧪 Tests Covered

- TCP throughput (iperf3)
- UDP performance (iperf3)
- ICMP reachability (fping)

---

## ▶️ Usage

```bash
ansible-playbook -i inventory/inventory.ini playbooks/tcp_test.yml
ansible-playbook -i inventory/inventory.ini playbooks/udp_test.yml
ansible-playbook -i inventory/inventory.ini playbooks/icmp_test.yml
```
## 📊 Output

All results are collected under:

results/

## 📌 Use Cases
Cloud network validation
Multi-zone performance testing
Packet loss detection
Customer PoC environments



