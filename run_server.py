from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from DBManager import DBManager

hostName = "localhost"
serverPort = 8777


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/presence"):
            self.do_presence(self.path)
        else:
            self.do_home()

        # Headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML
        self.s_print("<html><head></head>")
        self.s_print("<p>Request: %s</p>" % self.path)
        self.s_print("<body>")

        rows = self.get_all_users()
        self.print_table(rows)

        self.s_print("</body></html>")

    def do_presence(self, path):
        print("!")
        path_components = urlparse(self.path)
        query = path_components.query
        query_parameters = parse_qs(query)
        xlogin_arr = query_parameters['xlogin']
        if len(xlogin_arr) == 0:
            return
        xlogin = xlogin_arr[0]
        print(xlogin)

        db_manager = DBManager()
        presences = db_manager.presence("2020-07-31 00-00-00", "2020-07-31 23-00-00", xlogin)
        print(presences)

    def do_home(self, path):
        pass

    def s_print(self, str):
        self.wfile.write(bytes(str, "utf-8"))

    def print_table(self, rows):
        self.s_print("<table style=\"width:300px\">")
        self.s_print("<tr><th>xlogin</th></tr>")
        for i, row in enumerate(rows):
            self.s_print("<tr><td>" + str(i + 1) + "</td>")
            self.s_print("<td>" + row[0] + "</td></tr>")
        self.s_print("</table>")

    def get_all_users(self):
        db_manager = DBManager()
        return db_manager.all_users()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
