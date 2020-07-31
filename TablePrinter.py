from typing import BinaryIO

class TablePrinter:
    wfile: BinaryIO

    def __init__(self, wfile):
        self.wfile = wfile

    def __s_print(self, str):
        self.wfile.write(bytes(str, "utf-8"))

    def __print_td(self, str):
        self.__s_print("<td>" + str + "</td>")

    def __print_tr(self, i, row):
        self.__s_print("<tr>")
        self.__print_td(str(i + 1))
        for td in row:
            self.__print_td(td)
        self.__s_print("</tr>")

    def __print_titles(self, titles):
        self.__s_print("<tr>")
        for title in titles:
            self.__s_print("<th>" + title + "</th>")
        self.__s_print("</tr>")

    def __print_rows(self, rows):
        for i, row in enumerate(rows):
            self.__print_tr(i, row)

    def print_table(self, titles, rows):
        self.__s_print("<style>table, th, td {border: 1px solid black;}</style>")
        self.__s_print("<table style=\"width:50%\">")
        self.__print_titles(titles)
        self.__print_rows(rows)
        self.__s_print("</table>")
