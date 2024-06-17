"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from datetime import datetime, timedelta
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

import urllib3

from openfga_sdk import rest
from openfga_sdk.configuration import Configuration
from openfga_sdk.credentials import CredentialConfiguration, Credentials
from openfga_sdk.exceptions import AuthenticationError
from openfga_sdk.oauth2 import OAuth2Client


# Helper function to construct mock response
def mock_response(body, status):
    headers = urllib3.response.HTTPHeaderDict({"content-type": "application/json"})
    obj = urllib3.HTTPResponse(body, headers, status, preload_content=False)
    return rest.RESTResponse(obj, obj.data)


class TestOAuth2Client(IsolatedAsyncioTestCase):
    """TestOAuth2Client unit test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    async def test_get_authentication_valid_client_credentials(self):
        """
        Test getting authentication header when method is client credentials
        """
        client = OAuth2Client(None)
        client._access_token = "XYZ123"
        client._access_expiry_time = datetime.now() + timedelta(seconds=60)
        auth_header = await client.get_authentication_header(None)
        self.assertEqual(auth_header, {"Authorization": "Bearer XYZ123"})

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_obtain_client_credentials(self, mock_request):
        """
        Test getting authentication header when method is client credential and we need to obtain token
        """
        response_body = """
{
  "expires_in": 120,
  "access_token": "AABBCCDD"
}
        """
        mock_request.return_value = mock_response(response_body, 200)

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )
        rest_client = rest.RESTClientObject(Configuration())
        current_time = datetime.now()
        client = OAuth2Client(credentials)
        auth_header = await client.get_authentication_header(rest_client)
        self.assertEqual(auth_header, {"Authorization": "Bearer AABBCCDD"})
        self.assertEqual(client._access_token, "AABBCCDD")
        self.assertGreaterEqual(
            client._access_expiry_time, current_time + timedelta(seconds=int(120))
        )
        expected_header = urllib3.response.HTTPHeaderDict(
            {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "openfga-sdk (python) 0.5.0",
            }
        )
        mock_request.assert_called_once_with(
            "POST",
            "https://issuer.fga.example/oauth/token",
            headers=expected_header,
            query_params=None,
            body=None,
            _preload_content=True,
            _request_timeout=None,
            post_params={
                "client_id": "myclientid",
                "client_secret": "mysecret",
                "audience": "myaudience",
                "grant_type": "client_credentials",
            },
        )
        await rest_client.close()

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_obtain_client_credentials_failed(
        self, mock_request
    ):
        """
        Test getting authentication header when method is client credential and we fail to obtain token
        """
        response_body = """
{
  "reason": "Unauthorized"
}
        """
        mock_request.return_value = mock_response(response_body, 403)

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )
        rest_client = rest.RESTClientObject(Configuration())
        client = OAuth2Client(credentials)
        with self.assertRaises(AuthenticationError):
            await client.get_authentication_header(rest_client)
        await rest_client.close()

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_obtain_with_expired_client_credentials_failed(
        self, mock_request
    ):
        """
        Expired token should trigger a new token request
        """

        response_body = """
{
  "reason": "Unauthorized"
}
        """
        mock_request.return_value = mock_response(response_body, 403)

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )
        rest_client = rest.RESTClientObject(Configuration())
        client = OAuth2Client(credentials)

        client._access_token = "XYZ123"
        client._access_expiry_time = datetime.now() - timedelta(seconds=240)

        with self.assertRaises(AuthenticationError):
            await client.get_authentication_header(rest_client)
        await rest_client.close()

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_unexpected_response_fails(self, mock_request):
        """
        Receiving an unexpected response from the server should raise an exception
        """

        response_body = """
This is not a JSON response
        """
        mock_request.return_value = mock_response(response_body, 200)

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )
        rest_client = rest.RESTClientObject(Configuration())
        client = OAuth2Client(credentials)

        with self.assertRaises(AuthenticationError):
            await client.get_authentication_header(rest_client)
        await rest_client.close()

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_erroneous_response_fails(self, mock_request):
        """
        Receiving an erroneous response from the server that's missing properties should raise an exception
        """

        response_body = """
{
  "access_token": "AABBCCDD"
}
        """
        mock_request.return_value = mock_response(response_body, 200)

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )
        rest_client = rest.RESTClientObject(Configuration())
        client = OAuth2Client(credentials)

        with self.assertRaises(AuthenticationError):
            await client.get_authentication_header(rest_client)
        await rest_client.close()

    @patch.object(rest.RESTClientObject, "request")
    async def test_get_authentication_retries_5xx_responses(self, mock_request):
        """
        Receiving a 5xx response from the server should be retried
        """

        error_response_body = """
{
  "code": "rate_limit_exceeded",
  "message": "Rate Limit exceeded"
}
        """

        response_body = """
{
  "expires_in": 120,
  "access_token": "AABBCCDD"
}
        """

        mock_request.side_effect = [
            mock_response(error_response_body, 429),
            mock_response(error_response_body, 429),
            mock_response(error_response_body, 429),
            mock_response(response_body, 200),
        ]

        credentials = Credentials(
            method="client_credentials",
            configuration=CredentialConfiguration(
                client_id="myclientid",
                client_secret="mysecret",
                api_issuer="issuer.fga.example",
                api_audience="myaudience",
            ),
        )

        configuration = Configuration()
        configuration.retry_params.max_retry = 5
        configuration.retry_params.retry_interval = 0

        rest_client = rest.RESTClientObject(configuration)
        client = OAuth2Client(credentials, configuration)

        auth_header = await client.get_authentication_header(rest_client)

        mock_request.assert_called()
        self.assertEqual(mock_request.call_count, 4)  # 3 retries, 1 success
        self.assertEqual(auth_header, {"Authorization": "Bearer AABBCCDD"})

        await rest_client.close()
