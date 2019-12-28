import http.client
import json

class Pushed:
    def __init__(self, app_key, app_secret, pushed_id=None, pushed_apikey=None):
        self.app_key = app_key
        self.app_secret = app_secret
        self.pushed_id = pushed_id
        self.pushed_apikey = pushed_apikey
        self.api_endpoint = "api.pushed.co"
        self.api_port = 443

    def SendRequest(self, type, endpoint_name, payload):
        connection = http.client.HTTPSConnection(self.api_endpoint, self.api_port)
        connection.connect()
        connection.request(type, '/1/'+str(endpoint_name), json.dumps(payload),
          {
            "Content-Type": "application/json"
          }
        )
        result = json.loads(connection.getresponse().read())
        return result

    def GetApps(self):
        json_body = {
            "pushed_id": self.pushed_id,
            "api_key": self.pushed_apikey
        }

        result = self.SendRequest("GET", "app", json_body)
        return result

    def CreateApp(self, name, description, public=False):
        json_body = {
            "pushed_id": self.pushed_id,
            "api_key": self.pushed_apikey,
            "name": name,
            "description": description,
            "public": public
        }
        result = self.SendRequest("PUT", "app", json_body)
        return result

    def GetChannels(self):
        json_body = {
            "pushed_id": self.pushed_id,
            "api_key": self.pushed_apikey
        }

        result = self.SendRequest("GET", "channel", json_body)
        return result

    def CreateChannel(self, app_alias, app_name, public=False):
        json_body = {
            "pushed_id": self.pushed_id,
            "api_key": self.pushed_apikey,
            "app": app_alias,
            "name": app_name,
            "public": public
        }
        result = self.SendRequest("PUT", "app/channel", json_body)
        return result

    def Notification(self, message, url=None):
        json_body = {
          "app_key": self.app_key,
          "app_secret": self.app_secret,
          "target_type": "app",
          "content": message
          }

        if url is not None:
            json_body["content_type"] = "url"
            json_body["content_extra"] = url

        result = self.SendRequest("POST", "push", json_body)
        return result
