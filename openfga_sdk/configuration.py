# coding: utf-8

"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

import copy
import logging
import sys
from urllib.parse import urlparse

import urllib3
import six
from six.moves import http_client as httplib

from openfga_sdk.exceptions import FgaValidationException, ApiValueError
from openfga_sdk.validation import is_well_formed_ulid_string


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}


class RetryParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator

    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    Retry configuration in case of HTTP too many request

    :param max_retry: Maximum number of retry
    :param min_wait_in_ms: Minimum wait (in ms) between retry
    """

    def __init__(self, max_retry=15, min_wait_in_ms=100):
        self._max_retry = max_retry
        self._min_wait_in_ms = min_wait_in_ms

    @property
    def max_retry(self):
        """
        Return the maximum number of retry
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, value):
        """
        Update the maximum number of retry
        """
        self._max_retry = value

    @property
    def min_wait_in_ms(self):
        """
        Return the minimum wait (in ms) in between retry
        """
        return self._min_wait_in_ms

    @min_wait_in_ms.setter
    def min_wait_in_ms(self, value):
        """
        Update the minimum wait (in ms) in between retry
        """
        self._min_wait_in_ms = value


class Configuration(object):
    """NOTE: This class is auto generated by OpenAPI Generator

    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param api_scheme: Whether connection is 'https' or 'http'. Default as 'https'
        .. deprecated:: 0.4.1
            Use `api_url` instead.
    :param api_host: Base url
        .. deprecated:: 0.4.1
            Use `api_url` instead.
    :param store_id: ID of store for API
    :param credentials: Configuration for obtaining authentication credential
    :param retry_params: Retry parameters upon HTTP too many request
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer)
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication
    :param password: Password for HTTP basic authentication
    :param discard_unknown_keys: Boolean value indicating whether to discard
      unknown properties. A server may send a response that includes additional
      properties that are not known by the client in the following scenarios:
      1. The OpenAPI document is incomplete, i.e. it does not match the server
         implementation.
      2. The client was generated using an older version of the OpenAPI document
         and the server has been upgraded since then.
      If a schema in the OpenAPI document defines the additionalProperties attribute,
      then all undeclared properties received by the server are injected into the
      additional properties map. In that case, there are undeclared properties, and
      nothing to discard.
    :param disabled_client_side_validations (string): Comma-separated list of
      JSON schema validation keywords to disable JSON schema structural validation
      rules. The following keywords may be specified: multipleOf, maximum,
      exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, pattern,
      maxItems, minItems.
      By default, the validation is performed for data generated locally by the client
      and data received from the server, independent of any validation performed by
      the server side. If the input data does not satisfy the JSON schema validation
      rules specified in the OpenAPI document, an exception is raised.
      If disabled_client_side_validations is set, structural validation is
      disabled. This can be useful to troubleshoot data validation problem, such as
      when the OpenAPI document validation rules do not match the actual API data
      received by the server.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format
    :param api_url: str - the URL of the FGA server
    """

    _default = None

    def __init__(self, api_scheme="https", api_host=None,
                 store_id=None,
                 credentials=None,
                 retry_params=None,
                 api_key=None, api_key_prefix=None,
                 username=None, password=None,
                 discard_unknown_keys=False,
                 disabled_client_side_validations="",
                 server_index=None, server_variables=None,
                 server_operation_index=None, server_operation_variables=None,
                 ssl_ca_cert=None,
                 api_url=None,  # TODO: restructure when removing api_scheme/api_host
                 ):
        """Constructor
        """
        self._url = api_url
        self._scheme = api_scheme
        self._base_path = api_host
        self._store_id = store_id
        self._credentials = credentials
        if retry_params is not None:
            self._retry_params = retry_params
        else:
            # use the default parameters
            self._retry_params = RetryParams()
        """Default Base url
        """
        self.server_index = 0
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.discard_unknown_keys = discard_unknown_keys
        self.disabled_client_side_validations = disabled_client_side_validations
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("openfga_sdk")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """

        self.connection_pool_maxsize = 100
        """This value is passed to the aiohttp to limit simultaneous connections.
           Default values is 100, None means no-limit.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'disabled_client_side_validations':
            s = set(filter(None, value.split(',')))
            for v in s:
                if v not in JSON_SCHEMA_VALIDATION_KEYWORDS:
                    raise ApiValueError(
                        "Invalid keyword: '{0}''".format(v))
            self._disabled_client_side_validations = s

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = copy.deepcopy(default)

    @classmethod
    def get_default_copy(cls):
        """Return new instance of configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration passed by the set_default method.

        :return: The configuration object.
        """
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return Configuration()

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 0.1\n"\
               "SDK Package Version: 0.4.1".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    def is_valid(self):
        """
        Verify the configuration is valid.
        Note that we are only doing basic validation to ensure input is sane.
        """
        combined_url = self.api_url
        if self.api_url is None:
            if self.api_host is None or self.api_host == '':
                raise FgaValidationException('api_host is required but not configured.')
            if self.api_scheme is None or self.api_scheme == '':
                raise FgaValidationException('api_scheme is required but not configured.')
            combined_url = self.api_scheme + '://' + self.api_host
        parsed_url = None
        try:
            parsed_url = urlparse(combined_url)
        except ValueError:
            if self.api_url is None:
                raise ApiValueError('Either api_scheme `{}` or api_host `{}` is invalid'.format(
                    self.api_scheme, self.api_host))
            else:
                raise ApiValueError('api_url `{}` is invalid'.format(
                    self.api_url))
        if self.api_url is None:
            if (parsed_url.scheme != 'http' and parsed_url.scheme != 'https'):
                raise ApiValueError(
                    'api_scheme `{}` must be either `http` or `https`'.format(self.api_scheme))
            if (parsed_url.netloc == ''):
                raise ApiValueError('api_host `{}` is invalid'.format(self.api_host))
            if (parsed_url.path != ''):
                raise ApiValueError(
                    'api_host `{}` is not expected to have path specified'.format(self.api_scheme))
            if (parsed_url.query != ''):
                raise ApiValueError(
                    'api_host `{}` is not expected to have query specified'.format(self.api_scheme))

        if self.store_id is not None and self.store_id != "" and is_well_formed_ulid_string(self.store_id) is False:
            raise FgaValidationException(
                "store_id ('%s') is not in a valid ulid format" % self.store_id)

        if self._credentials is not None:
            self._credentials.validate_credentials_config()

    @property
    def api_scheme(self):
        """Return connection is https or http."""
        return self._scheme

    @api_scheme.setter
    def api_scheme(self, value):
        """Update connection scheme (https or http)."""
        self._scheme = value

    @property
    def api_host(self):
        """Return api_host."""
        return self._base_path

    @api_host.setter
    def api_host(self, value):
        """Update configured host"""
        self._base_path = value

    @property
    def api_url(self):
        """Return api_url"""
        return self._url

    @api_url.setter
    def api_url(self, value):
        """Update configured api_url"""
        self._url = value

    @property
    def store_id(self):
        """Return store id."""
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        """Update store id."""
        self._store_id = value

    @property
    def credentials(self):
        """
        Return configured credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        """Update credentials"""
        self._credentials = value

    @property
    def retry_params(self):
        """
        Return retry parameters
        """
        return self._retry_params

    @retry_params.setter
    def retry_params(self, value):
        """
        Update retry parameters
        """
        self._retry_params = value
