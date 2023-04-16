#!/usr/bin/env bash
# Copyright (c) 2023 Julian Fechner
# Run with sudo privileges

options="Usage: ovpn.sh [OPTIONS]
	Options:
	--thm			Connect to THM via OVPN
	--htb-machines 		Connect to HTB machines via OVPN
	--htb-seasonal 		Connect to HTB seasonal machinesvia OVPN"

if [[ $@ == "--thm" ]]
then
	openvpn --config "/home/kali/Documents/vpn/thm/N30n.ovpn"
elif [[ $@ == "--htb-machines" ]]
then
	openvpn --config "/home/kali/Documents/vpn/htb/lab_xn30n.ovpn"
elif [[ $@ == "--htb-seasonal" ]]
then
	openvpn --config "/home/kali/Documents/vpn/htb/competitive_xn30n.ovpn"
else
	# Removes unnessecary indentation
	sed 's/^[[:space:]]*//' <<< "$options"
fi
