#!/usr/bin/env bash
# Copyright (c) 2023 Julian Fechner
# Run with sudo privileges

read -p "Please specify the IP of the box:" IP

ufw enable
ufw default deny incoming
ufw status numbered

read -p "Would you like to delete the old rule (y/n):" ans

if ans==y || ans==Y; then
yes | ufw delete 1
fi

ufw allow from $IP to any
ufw status numbered
