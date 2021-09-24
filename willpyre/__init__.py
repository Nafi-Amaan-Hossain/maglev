from . import router, app, structure
import json

__all__ = ['JSONResponse', 'TextResponse', 'Router', 'App']

Router, App, Cookie = router.Router, app.App, structure.Cookie


class JSONResponse(structure.Response):
    def __init__(
        self,
        data,
        status=200,
            content_type="application/json",
            headers=dict(),
            cookies=dict()):
        super().__init__(headers=headers, cookies=cookies,
                         content_type=content_type, status=status)
        self.body = json.dumps(data)


class TextResponse(structure.Response):
    def __init__(
        self,
        data,
        status=200,
            content_type="text/plain",
            headers=dict(),
            cookies=dict()):
        super().__init__(headers=headers, cookies=cookies,
                         content_type=content_type, status=status)
        self.body = data