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


class IgmpQuerierRange(Base):
    """
    The IgmpQuerierRange class encapsulates a list of igmpQuerierRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpQuerierRange.find() method.
    The list can be managed by using the IgmpQuerierRange.add() and IgmpQuerierRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "igmpQuerierRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "GeneralQueryInterval": "generalQueryInterval",
        "GeneralQueryResponseInterval": "generalQueryResponseInterval",
        "Name": "name",
        "ObjectId": "objectId",
        "RobustnessVariable": "robustnessVariable",
        "RouterAlert": "routerAlert",
        "SpecificQueryResponseCount": "specificQueryResponseCount",
        "SpecificQueryResponseInterval": "specificQueryResponseInterval",
        "StartupQueryCount": "startupQueryCount",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpQuerierRange, self).__init__(parent, list_op)

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
    def GeneralQueryInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueryInterval"])

    @GeneralQueryInterval.setter
    def GeneralQueryInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueryInterval"], value)

    @property
    def GeneralQueryResponseInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueryResponseInterval"])

    @GeneralQueryResponseInterval.setter
    def GeneralQueryResponseInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueryResponseInterval"], value)

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
    def RobustnessVariable(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RobustnessVariable"])

    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RobustnessVariable"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, sets the Send Router Alert bit in the IP header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SpecificQueryResponseCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpecificQueryResponseCount"])

    @SpecificQueryResponseCount.setter
    def SpecificQueryResponseCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpecificQueryResponseCount"], value)

    @property
    def SpecificQueryResponseInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpecificQueryResponseInterval"])

    @SpecificQueryResponseInterval.setter
    def SpecificQueryResponseInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpecificQueryResponseInterval"], value)

    @property
    def StartupQueryCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of general query messages sent at startup.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartupQueryCount"])

    @StartupQueryCount.setter
    def StartupQueryCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartupQueryCount"], value)

    @property
    def Version(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IGMP/MLD protocol version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    def update(
        self,
        Enabled=None,
        GeneralQueryInterval=None,
        GeneralQueryResponseInterval=None,
        Name=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SpecificQueryResponseCount=None,
        SpecificQueryResponseInterval=None,
        StartupQueryCount=None,
        Version=None,
    ):
        # type: (bool, int, int, str, int, bool, int, int, int, str) -> IgmpQuerierRange
        """Updates igmpQuerierRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
        - GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
        - Name (str): Name of range
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
        - StartupQueryCount (number): The number of general query messages sent at startup.
        - Version (str): IGMP/MLD protocol version.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        GeneralQueryInterval=None,
        GeneralQueryResponseInterval=None,
        Name=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SpecificQueryResponseCount=None,
        SpecificQueryResponseInterval=None,
        StartupQueryCount=None,
        Version=None,
    ):
        # type: (bool, int, int, str, int, bool, int, int, int, str) -> IgmpQuerierRange
        """Adds a new igmpQuerierRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
        - GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
        - Name (str): Name of range
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
        - StartupQueryCount (number): The number of general query messages sent at startup.
        - Version (str): IGMP/MLD protocol version.

        Returns
        -------
        - self: This instance with all currently retrieved igmpQuerierRange resources using find and the newly added igmpQuerierRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpQuerierRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        GeneralQueryInterval=None,
        GeneralQueryResponseInterval=None,
        Name=None,
        ObjectId=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SpecificQueryResponseCount=None,
        SpecificQueryResponseInterval=None,
        StartupQueryCount=None,
        Version=None,
    ):
        # type: (bool, int, int, str, str, int, bool, int, int, int, str) -> IgmpQuerierRange
        """Finds and retrieves igmpQuerierRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpQuerierRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpQuerierRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
        - GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
        - StartupQueryCount (number): The number of general query messages sent at startup.
        - Version (str): IGMP/MLD protocol version.

        Returns
        -------
        - self: This instance with matching igmpQuerierRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpQuerierRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpQuerierRange resources from the server available through an iterator or index

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
