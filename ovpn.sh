#!/usr/bin/env bash
# Copyright (c) 2023 Julian Fechner
# Run with sudo privileges

options="Usage: ovpn.sh [OPTIONS]
	Options:
	--thm          Connect to THM via OVPN
	--htb          Connect to HTB via OVPN"

if [[ $@ == "--thm" ]]
then
	openvpn --config "/home/kali/Documents/vpn/thm/N30n.ovpn"
elif [[ $@ == "--htb" ]]
then
	openvpn --config "/home/kali/Documents/vpn/htb/xn30n.ovpn"
else
	# Removes unnessecary indentation
	sed 's/^[[:space:]]*//' <<< "$options"
fi
