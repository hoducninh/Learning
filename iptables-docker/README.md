# iptables

Warning: 

in the proxy service:

- echo 1 > /proc/sys/net/ipv4/ip_forward
- iptables -F
- iptables -t nat -F
- iptables -X
- iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination <YOUR_SERVER_CONTAINER_IP>:80
- iptables -t nat -A POSTROUTING -j MASQUERADE