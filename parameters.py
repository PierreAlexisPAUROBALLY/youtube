import json
class Error(Exception):
    """base Error Class"""
    pass


class MissingParametersError(Error):
    """trying to create a new key in gecko_params json file"""


class Parameters():
    def __init__(self, gecko_params="youtube_params.json"):
        self._gecko_params = gecko_params
        with open(self._gecko_params) as file:
            self._p = json.load(file)

        self.video_path = self._p["base_path"]
        self.processed = self.video_path+self._p["processed"]
        self.unprocessed = self.video_path+ self._p["unprocessed"]
        self.splited = self.video_path+self._p["splited"]


    def modifier(self, key, value):
        if key in self._p.keys():
            self._p[key] = value
            self._dump()
        else:
            raise MissingParametersError

    def _dump(self):
        with open(self._gecko_params, "w") as file:
            json.dump(self._p, file)
