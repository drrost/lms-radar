import http.client
import json

class NetworkManager:
    conn = http.client.HTTPSConnection("lms.ucode.world")
    access_token = ""

    # TODO: Remove the password from here. Read it from an environment variable.
    #
    def getToken(self):
        payload = "username=rdruzhchen&password=arlHX2qbHmfVOMyWvQGdfpxLN1YKl2ne&grant_type=password"
        headers = {
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        self.conn.request("POST", "/api/frontend/o/token", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        response = data.decode("utf-8")
        response_json = json.loads(response)
        return response_json['access_token']

    def getPresence(self):
        if len(self.access_token) == 0:
            self.access_token = self.getToken()
        payload = ''
        headers = {
          'authorization': 'Bearer ' + self.access_token
        }
        self.conn.request("GET", "/api/v0/logtime/active/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        return data.decode("utf-8")