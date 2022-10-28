# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class EapoUdpRange(Base):
    """
    The EapoUdpRange class encapsulates a list of eapoUdpRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the EapoUdpRange.find() method.
    The list can be managed by using the EapoUdpRange.add() and EapoUdpRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "eapoUdpRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "ExpectedSystemToken": "expectedSystemToken",
        "FastInnerMethod": "fastInnerMethod",
        "FastProvisionMode": "fastProvisionMode",
        "FastStatelessResume": "fastStatelessResume",
        "NacSequence": "nacSequence",
        "Name": "name",
        "ObjectId": "objectId",
        "Protocol": "protocol",
        "ResponseType": "responseType",
        "UserName": "userName",
        "UserPassword": "userPassword",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EapoUdpRange, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ExpectedSystemToken(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Expected System Token.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExpectedSystemToken"])

    @ExpectedSystemToken.setter
    def ExpectedSystemToken(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExpectedSystemToken"], value)

    @property
    def FastInnerMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str: FAST Inner Method.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastInnerMethod"])

    @FastInnerMethod.setter
    def FastInnerMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastInnerMethod"], value)

    @property
    def FastProvisionMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: FAST Provision Mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastProvisionMode"])

    @FastProvisionMode.setter
    def FastProvisionMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastProvisionMode"], value)

    @property
    def FastStatelessResume(self):
        # type: () -> str
        """
        Returns
        -------
        - str: FAST Stateless Resume.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastStatelessResume"])

    @FastStatelessResume.setter
    def FastStatelessResume(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastStatelessResume"], value)

    @property
    def NacSequence(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/eapoUdpGlobals/nacSettings/nacSequence): Nac Sequence used by this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NacSequence"])

    @NacSequence.setter
    def NacSequence(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NacSequence"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def Protocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Authentification Protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Protocol"])

    @Protocol.setter
    def Protocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Protocol"], value)

    @property
    def ResponseType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Messages types to responde.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResponseType"])

    @ResponseType.setter
    def ResponseType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResponseType"], value)

    @property
    def UserName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The UserName used to authentificate the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserName"])

    @UserName.setter
    def UserName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserName"], value)

    @property
    def UserPassword(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The UserPassword used to authentificate the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPassword"])

    @UserPassword.setter
    def UserPassword(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPassword"], value)

    def update(
        self,
        Enabled=None,
        ExpectedSystemToken=None,
        FastInnerMethod=None,
        FastProvisionMode=None,
        FastStatelessResume=None,
        NacSequence=None,
        Name=None,
        Protocol=None,
        ResponseType=None,
        UserName=None,
        UserPassword=None,
    ):
        # type: (bool, str, str, str, str, str, str, str, str, str, str) -> EapoUdpRange
        """Updates eapoUdpRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ExpectedSystemToken (str): Expected System Token.
        - FastInnerMethod (str): FAST Inner Method.
        - FastProvisionMode (str): FAST Provision Mode.
        - FastStatelessResume (str): FAST Stateless Resume.
        - NacSequence (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/eapoUdpGlobals/nacSettings/nacSequence)): Nac Sequence used by this range.
        - Name (str): Name of range
        - Protocol (str): Authentification Protocol.
        - ResponseType (str): Messages types to responde.
        - UserName (str): The UserName used to authentificate the port.
        - UserPassword (str): The UserPassword used to authentificate the port.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        ExpectedSystemToken=None,
        FastInnerMethod=None,
        FastProvisionMode=None,
        FastStatelessResume=None,
        NacSequence=None,
        Name=None,
        Protocol=None,
        ResponseType=None,
        UserName=None,
        UserPassword=None,
    ):
        # type: (bool, str, str, str, str, str, str, str, str, str, str) -> EapoUdpRange
        """Adds a new eapoUdpRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ExpectedSystemToken (str): Expected System Token.
        - FastInnerMethod (str): FAST Inner Method.
        - FastProvisionMode (str): FAST Provision Mode.
        - FastStatelessResume (str): FAST Stateless Resume.
        - NacSequence (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/eapoUdpGlobals/nacSettings/nacSequence)): Nac Sequence used by this range.
        - Name (str): Name of range
        - Protocol (str): Authentification Protocol.
        - ResponseType (str): Messages types to responde.
        - UserName (str): The UserName used to authentificate the port.
        - UserPassword (str): The UserPassword used to authentificate the port.

        Returns
        -------
        - self: This instance with all currently retrieved eapoUdpRange resources using find and the newly added eapoUdpRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained eapoUdpRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        ExpectedSystemToken=None,
        FastInnerMethod=None,
        FastProvisionMode=None,
        FastStatelessResume=None,
        NacSequence=None,
        Name=None,
        ObjectId=None,
        Protocol=None,
        ResponseType=None,
        UserName=None,
        UserPassword=None,
    ):
        # type: (bool, str, str, str, str, str, str, str, str, str, str, str) -> EapoUdpRange
        """Finds and retrieves eapoUdpRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eapoUdpRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eapoUdpRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ExpectedSystemToken (str): Expected System Token.
        - FastInnerMethod (str): FAST Inner Method.
        - FastProvisionMode (str): FAST Provision Mode.
        - FastStatelessResume (str): FAST Stateless Resume.
        - NacSequence (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/eapoUdpGlobals/nacSettings/nacSequence)): Nac Sequence used by this range.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Protocol (str): Authentification Protocol.
        - ResponseType (str): Messages types to responde.
        - UserName (str): The UserName used to authentificate the port.
        - UserPassword (str): The UserPassword used to authentificate the port.

        Returns
        -------
        - self: This instance with matching eapoUdpRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eapoUdpRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eapoUdpRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
