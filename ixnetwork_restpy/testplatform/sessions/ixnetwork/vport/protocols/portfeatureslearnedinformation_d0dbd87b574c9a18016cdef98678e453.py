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


class PortFeaturesLearnedInformation(Base):
    """This object allows to configure the portFeaturesLearnedInformation ports.
    The PortFeaturesLearnedInformation class encapsulates a list of portFeaturesLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the PortFeaturesLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "portFeaturesLearnedInformation"
    _SDM_ATT_MAP = {
        "AdvertisedFeatures": "advertisedFeatures",
        "Config": "config",
        "CurrentFeatures": "currentFeatures",
        "CurrentSpeed": "currentSpeed",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "ErrorCode": "errorCode",
        "ErrorType": "errorType",
        "EthernetAddress": "ethernetAddress",
        "Latency": "latency",
        "LocalIp": "localIp",
        "MaxSpeed": "maxSpeed",
        "Name": "name",
        "NegotiatedVersion": "negotiatedVersion",
        "PeerAdvertisedFeatures": "peerAdvertisedFeatures",
        "PortNumber": "portNumber",
        "RemoteIp": "remoteIp",
        "ReplyState": "replyState",
        "State": "state",
        "SupportedFeatures": "supportedFeatures",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PortFeaturesLearnedInformation, self).__init__(parent, list_op)

    @property
    def AdvertisedFeatures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The current features, like link modes, link types, and link features that the port advertises.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertisedFeatures"])

    @property
    def Config(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the configuration supported by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Config"])

    @property
    def CurrentFeatures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The current features like the link modes, link types, and link features that the port supports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentFeatures"])

    @property
    def CurrentSpeed(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The current speed of the port in kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentSpeed"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def ErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The error code of the received error.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorCode"])

    @property
    def ErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorType"])

    @property
    def EthernetAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Ethernet address of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetAddress"])

    @property
    def Latency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The latency measurement for the OpenFlow channel in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Latency"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the local IP of the Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def MaxSpeed(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum speed of the port in kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxSpeed"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the name of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def NegotiatedVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

    @property
    def PeerAdvertisedFeatures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The current features, like, link modes, link types, and link features, that the peer advertises.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerAdvertisedFeatures"])

    @property
    def PortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The port number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNumber"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The state of reply for the Open Flow channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyState"])

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the states supported by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def SupportedFeatures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The features like link modes, link types, and link features that is supported by the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportedFeatures"])

    def add(self):
        """Adds a new portFeaturesLearnedInformation resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved portFeaturesLearnedInformation resources using find and the newly added portFeaturesLearnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AdvertisedFeatures=None,
        Config=None,
        CurrentFeatures=None,
        CurrentSpeed=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        ErrorCode=None,
        ErrorType=None,
        EthernetAddress=None,
        Latency=None,
        LocalIp=None,
        MaxSpeed=None,
        Name=None,
        NegotiatedVersion=None,
        PeerAdvertisedFeatures=None,
        PortNumber=None,
        RemoteIp=None,
        ReplyState=None,
        State=None,
        SupportedFeatures=None,
    ):
        # type: (str, str, str, int, str, str, str, str, str, int, str, int, str, str, str, int, str, str, str, str) -> PortFeaturesLearnedInformation
        """Finds and retrieves portFeaturesLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portFeaturesLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portFeaturesLearnedInformation resources from the server.

        Args
        ----
        - AdvertisedFeatures (str): The current features, like link modes, link types, and link features that the port advertises.
        - Config (str): Signifies the configuration supported by the port.
        - CurrentFeatures (str): The current features like the link modes, link types, and link features that the port supports.
        - CurrentSpeed (number): The current speed of the port in kbps.
        - DataPathId (str): The Data Path identifier of the OpenFlow switch.
        - DataPathIdAsHex (str): The Data Path identifier of the OpenFlow switch in hexadecimal format.
        - ErrorCode (str): The error code of the received error.
        - ErrorType (str): The type of the error received.
        - EthernetAddress (str): The Ethernet address of the switch.
        - Latency (number): The latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): Indicates the local IP of the Controller.
        - MaxSpeed (number): The maximum speed of the port in kbps.
        - Name (str): Signifies the name of the port.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - PeerAdvertisedFeatures (str): The current features, like, link modes, link types, and link features, that the peer advertises.
        - PortNumber (number): The port number.
        - RemoteIp (str): The Remote IP address of the selected interface.
        - ReplyState (str): The state of reply for the Open Flow channel.
        - State (str): Signifies the states supported by the port.
        - SupportedFeatures (str): The features like link modes, link types, and link features that is supported by the switch.

        Returns
        -------
        - self: This instance with matching portFeaturesLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portFeaturesLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portFeaturesLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the addRecordForTrigger operation on the server.

        NOT DEFINED

        addRecordForTrigger(async_operation=bool)bool
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "addRecordForTrigger", payload=payload, response_object=None
        )
