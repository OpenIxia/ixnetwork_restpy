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


class Tables(Base):
    """Openflow Controller Table Configuration
    The Tables class encapsulates a list of tables resources that are managed by the system.
    A list of resources can be retrieved from the server using the Tables.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "tables"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ChannelIndex": "channelIndex",
        "ChannelRemoteIp": "channelRemoteIp",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Name": "name",
        "NumberOfFlowSet": "numberOfFlowSet",
        "TableId": "tableId",
        "TableName": "tableName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Tables, self).__init__(parent, list_op)

    @property
    def FlowSet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowset_4668cc7c02c6c6c6cb9975c2ed2dbda5.FlowSet): An instance of the FlowSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowset_4668cc7c02c6c6c6cb9975c2ed2dbda5 import (
            FlowSet,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FlowSet", None) is not None:
                return self._properties.get("FlowSet")
        return FlowSet(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def ChannelIndex(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Parent Channel Index
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelIndex"])

    @property
    def ChannelRemoteIp(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The remote IP address of the OF Channel. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelRemoteIp"])

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NumberOfFlowSet(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the number of Flow Set for this controller configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfFlowSet"])

    @NumberOfFlowSet.setter
    def NumberOfFlowSet(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfFlowSet"], value)

    @property
    def TableId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the controller table identifier. Lower numbered tables are consulted first.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TableId"]))

    @property
    def TableName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the name of the controller table.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TableName"]))

    def update(self, Name=None, NumberOfFlowSet=None):
        # type: (str, int) -> Tables
        """Updates tables resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFlowSet (number): Specify the number of Flow Set for this controller configuration.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, NumberOfFlowSet=None):
        # type: (str, int) -> Tables
        """Adds a new tables resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFlowSet (number): Specify the number of Flow Set for this controller configuration.

        Returns
        -------
        - self: This instance with all currently retrieved tables resources using find and the newly added tables resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChannelIndex=None,
        ChannelRemoteIp=None,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NumberOfFlowSet=None,
    ):
        # type: (List[str], List[str], int, str, str, int) -> Tables
        """Finds and retrieves tables resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tables resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tables resources from the server.

        Args
        ----
        - ChannelIndex (list(str)): Parent Channel Index
        - ChannelRemoteIp (list(str)): The remote IP address of the OF Channel. This field is auto-populated and cannot be changed.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFlowSet (number): Specify the number of Flow Set for this controller configuration.

        Returns
        -------
        - self: This instance with matching tables resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tables data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tables resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, TableId=None, TableName=None):
        """Base class infrastructure that gets a list of tables device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - TableId (str): optional regex of tableId
        - TableName (str): optional regex of tableName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
