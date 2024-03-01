"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint

from openfga_sdk.configuration import Configuration


class ReadAssertionsResponse:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"authorization_model_id": "str", "assertions": "list[Assertion]"}

    attribute_map = {
        "authorization_model_id": "authorization_model_id",
        "assertions": "assertions",
    }

    def __init__(
        self,
        authorization_model_id=None,
        assertions=None,
        local_vars_configuration=None,
    ):
        """ReadAssertionsResponse - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._authorization_model_id = None
        self._assertions = None
        self.discriminator = None

        self.authorization_model_id = authorization_model_id
        if assertions is not None:
            self.assertions = assertions

    @property
    def authorization_model_id(self):
        """Gets the authorization_model_id of this ReadAssertionsResponse.


        :return: The authorization_model_id of this ReadAssertionsResponse.
        :rtype: str
        """
        return self._authorization_model_id

    @authorization_model_id.setter
    def authorization_model_id(self, authorization_model_id):
        """Sets the authorization_model_id of this ReadAssertionsResponse.


        :param authorization_model_id: The authorization_model_id of this ReadAssertionsResponse.
        :type authorization_model_id: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and authorization_model_id is None
        ):
            raise ValueError(
                "Invalid value for `authorization_model_id`, must not be `None`"
            )

        self._authorization_model_id = authorization_model_id

    @property
    def assertions(self):
        """Gets the assertions of this ReadAssertionsResponse.


        :return: The assertions of this ReadAssertionsResponse.
        :rtype: list[Assertion]
        """
        return self._assertions

    @assertions.setter
    def assertions(self, assertions):
        """Sets the assertions of this ReadAssertionsResponse.


        :param assertions: The assertions of this ReadAssertionsResponse.
        :type assertions: list[Assertion]
        """

        self._assertions = assertions

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadAssertionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadAssertionsResponse):
            return True

        return self.to_dict() != other.to_dict()
