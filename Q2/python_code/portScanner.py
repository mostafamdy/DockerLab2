import socket
import argparse

parser = argparse.ArgumentParser(description="port scanner")

parser.add_argument('--ip', type=str, required=True, help='IP Address')
parser.add_argument('--port', type=int, help='Port Number')

args = parser.parse_args()
ip=args.ip
port=args.port


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


print(f"port {port} : {isOpen(ip,port)}")