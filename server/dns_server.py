# server/dns_server.py
from dnslib import *
from dnslib.server import DNSServer, BaseResolver
import base64
import time

class ChatDNSResolver(BaseResolver):
    def decode(self, qname):
        try:
            encoded = str(qname).split('.')[0]
            padded = encoded + '=' * (-len(encoded) % 4)
            return base64.urlsafe_b64decode(padded.encode()).decode()
        except Exception as e:
            return f"[Error decoding] {e}"

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        message = self.decode(qname)
        print(f"Received from client: {message}")
        reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT("Received: " + message), ttl=60))
        return reply

if __name__ == "__main__":
    resolver = ChatDNSResolver()
    udp_server = DNSServer(resolver, port=5353, address="0.0.0.0", tcp=False)
    tcp_server = DNSServer(resolver, port=5353, address="0.0.0.0", tcp=True)

    print("DNS Server running on port 5353 (TCP and UDP)...")
    udp_server.start_thread()
    tcp_server.start_thread()

    while True:
        time.sleep(1)
