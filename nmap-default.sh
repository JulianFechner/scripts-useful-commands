#!/bin/bash
read -p "Enter target IP: " target_ip
sudo nmap -sS -sV $target_ip
