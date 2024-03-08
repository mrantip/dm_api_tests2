from requests import session, Response
import structlog


class RestClient:

    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')


    def post(self, path: str, **kwargs):
        return self._send_request('POST', path, **kwargs)