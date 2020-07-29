from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from DBManager import DBManager

hostName = "localhost"
serverPort = 8777

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML
        self.s_print("<html><head></head>")
        self.s_print("<p>Request: %s</p>" % self.path)
        self.s_print("<body>")

        rows = self.fetch_data()
        self.print_table(rows)

        self.s_print("</body></html>")

    def s_print(self, str):
        self.wfile.write(bytes(str, "utf-8"))

    def print_table(self, rows):
        self.s_print("<table style=\"width:300px\">")
        self.s_print("<tr><th>xlogin</th></tr>")
        for i, row in enumerate(rows):
            self.s_print("<tr><td>" + str(i + 1) + "</td>")
            self.s_print("<td>" + row[0] + "</td></tr>")
        self.s_print("</table>")

    def fetch_data(self):
        db_manager = DBManager()
        return db_manager.fetch_data()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
