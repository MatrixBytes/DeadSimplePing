import sys
import socket
import subprocess
import time

config = {
    'ip': '',
    'method': 'icmp',
    'port': '',
    'timeout': '1',
    'interval': '1'
}

args = sys.argv
args.remove(sys.argv[0])

for i in args:
    token = i.split(':')
    config[token[0]] = token[1]

target = socket.gethostbyname(config['ip'])

print(f'PING {config["ip"]}:{config["port"]} ({target})')

if (config['method'] == '') or config['method'] == 'icmp':
    seq = 0
    while True:
        seq += 1
        time.sleep(float(config['interval']))

        start = time.time()

        ping = subprocess.Popen(["ping", "-s", "1", "-W", config['timeout'], "-c", "1", target], stdout = subprocess.PIPE)
        result = ping.communicate()[0].decode()
        end = time.time()

        if '0 received' in result:
            print(f'{config["ip"]}:icmp seq={seq} status=online time={str(start - end)[0:6]} ms')
        if '1 received' in result:
            print(f'{config["ip"]}:icmp seq={seq} status=offline time={str(start - end)[0:6]} ms')

if (config['method'] == 'tcp'):
    seq = 0
    while True:
        seq += 1
        time.sleep(float(config['interval']))

        start = time.time()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(float(config['timeout']))

        try:
            s.connect((target, int(config['port'])))
            end = time.time()
            s.shutdown(socket.SHUT_RD)
            print(f'{config["ip"]}:{config["port"]} seq={seq} status=online time={str(start - end)[1:6]} ms')
        except:
            end = time.time()
            print(f'{config["ip"]}:{config["port"]} seq={seq} status=offline time={str(start - end)[1:6]} ms')
