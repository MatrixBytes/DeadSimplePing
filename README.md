# DeadSimplePing
Dead simple pinger that supports TCP and ICMP \
Usage Examples: 
  ```
  python3 paping.py interval:0.1 ip:1.1.1.1 method:tcp port:80 # ping 1.1.1.1 via tcp on port 80 with an interval of 0.1 
  python3 paping.py ip:www.google.com # ping google with default config. (method=icmp, timeout=1, interval=1) 
  python3 paping.py ip:www.google.com interval:0.01 # ping google with default config and a interval of 0.01 
```
