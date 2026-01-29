import logging
from functools import cached_property

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.helpers import serialize_object
from zeep.transports import Transport


SPEDION_SOAP_USER = 'SimpexWSKSGmbH2'
SPEDION_SOAP_PASSWORD = 'h#pN5HWecrJ8z7g'

logger = logging.getLogger(__name__)


class BaseRestException(Exception):
    """ Exception with a customizable status code, error code, and message. """
    TEMPLATE_MESSAGE = ''
    ERROR_CODE = ''
    STATUS_CODE = None

    def __init__(self, message=None, error_code=None, details=None,
                 status_code=None, *args, **kwargs):
        if message is None and self.TEMPLATE_MESSAGE == '':
            msg = 'message must be passed or TEMPLATE_MESSAGE must be filled'
            raise ValueError(msg)

        if status_code is None and self.STATUS_CODE is None:
            msg = 'status_code must be passed or STATUS_CODE must be filled'
            raise ValueError(msg)

        self.message = message or self.TEMPLATE_MESSAGE.format(**kwargs)
        self.error_code = (
                error_code or
                self.ERROR_CODE or
                self.__class__.__name__
        )
        self.details = details
        self.status = status_code or self.STATUS_CODE
        super().__init__(*args)


class SpedionException(BaseRestException):
    """Base exception for Spedion API errors"""
    STATUS_CODE = 418


class SpedionSoapClient(Client):
    """Spedion SOAP client"""

    WSDL_URL = (
        'https://simpex.spedion.de/simpex/3.1/Services/'
        'MessageService.asmx?WSDL'
    )

    def __init__(self, wsse=None, service_name=None, port_name=None, plugins=None, settings=None):
        super().__init__(
            self.WSDL_URL,
            wsse,
            self._get_auth_transport(),
            service_name, port_name, plugins, settings
        )

    def _do_request(self, method, *args, **kwargs):
        """Make a SOAP request and handle errors"""
        response = serialize_object(method(*args, **kwargs))
        self._ensure_not_error(response)
        return response

    @staticmethod
    def _ensure_not_error(response):
        """Ensure that the SOAP response does not contain an error"""
        if response is None:
            return

        if 'Code' in response and 'ErrorCode' in response['Code']:
            logger.error(response)
            raise SpedionException(
                message=response['Description'],
                error_code=response['ErrorDesc'],
                details={
                    'error_code': response['ErrorCode'],
                },
            )

    @cached_property
    def _auth_session(self):
        """Create a session for Spedion SOAP client"""
        username = SPEDION_SOAP_USER
        password = SPEDION_SOAP_PASSWORD

        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        return session

    def _get_auth_transport(self):
        """Get authentication transport for Spedion SOAP client"""
        transport = Transport(session=self._auth_session)
        return transport


spideon_clients = SpedionSoapClient()
