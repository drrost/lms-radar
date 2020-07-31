from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from DBManager import DBManager
from TablePrinter import TablePrinter

hostName = "localhost"
serverPort = 8777

class MyServer(BaseHTTPRequestHandler):
    tablePrinter: TablePrinter

    def do_GET(self):
        self.tablePrinter = TablePrinter(self.wfile)
        if self.path.startswith("/presence"):
            self.do_presence(self.path)
        else:
            self.do_home(self.path)

    def do_presence(self, path):
        path_components = urlparse(self.path)
        query = path_components.query
        query_parameters = parse_qs(query)
        xlogin_arr = query_parameters['xlogin']
        if len(xlogin_arr) == 0:
            return
        xlogin = xlogin_arr[0]

        db_manager = DBManager()
        presences = db_manager.presence("2020-07-31 00-00-00", "2020-07-31 23-00-00", xlogin)

        # Headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML
        self.__s_print("<html><head></head><body>")

        titles = ["#", "xlogin", "workspace", "date_time"]
        self.tablePrinter.print_table(titles, presences)

        self.__s_print("</body></html>")

    def do_home(self, path):
        # Headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML
        self.__s_print("<html><head></head>")
        self.__s_print("<body>")

        rows = self.__get_all_users()
        titles = ["#", "xlogin"]
        self.tablePrinter.print_table(titles, rows)

        self.__s_print("</body></html>")


    def __get_all_users(self):
        db_manager = DBManager()
        return db_manager.all_users()

    def __s_print(self, str):
        self.wfile.write(bytes(str, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
