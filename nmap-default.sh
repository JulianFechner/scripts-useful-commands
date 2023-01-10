#!usr/bin/env bash
read -p "Enter target IP: " target_ip
sudo nmap -sS -sV -sV $target_ip
