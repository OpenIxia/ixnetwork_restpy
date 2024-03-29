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


class AppLibFlow(Base):
    """This object specifies the particular application library flow related properties.
    The AppLibFlow class encapsulates a list of appLibFlow resources that are managed by the system.
    A list of resources can be retrieved from the server using the AppLibFlow.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "appLibFlow"
    _SDM_ATT_MAP = {
        "ConfigId": "configId",
        "ConnectionCount": "connectionCount",
        "Description": "description",
        "FlowId": "flowId",
        "FlowSize": "flowSize",
        "Name": "name",
        "Parameters": "parameters",
        "Percentage": "percentage",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AppLibFlow, self).__init__(parent, list_op)

    @property
    def Connection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection.Connection): An instance of the Connection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection import (
            Connection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Connection", None) is not None:
                return self._properties.get("Connection")
        return Connection(self)

    @property
    def Parameter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter.Parameter): An instance of the Parameter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter import (
            Parameter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Parameter", None) is not None:
                return self._properties.get("Parameter")
        return Parameter(self)

    @property
    def ConfigId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The internal config id asociated with this flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigId"])

    @property
    def ConnectionCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of connections in this flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectionCount"])

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Brief description of what the flow does.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @property
    def FlowId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The identifier of the flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowId"])

    @property
    def FlowSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The size of the flow in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowSize"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the Flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @property
    def Parameters(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Array containing configurable parameters per flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Parameters"])

    @property
    def Percentage(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of traffic generated for this flows.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Percentage"])

    @Percentage.setter
    def Percentage(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Percentage"], value)

    def update(self, Percentage=None):
        # type: (int) -> AppLibFlow
        """Updates appLibFlow resource on the server.

        Args
        ----
        - Percentage (number): The amount of traffic generated for this flows.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Percentage=None):
        # type: (int) -> AppLibFlow
        """Adds a new appLibFlow resource on the json, only valid with batch add utility

        Args
        ----
        - Percentage (number): The amount of traffic generated for this flows.

        Returns
        -------
        - self: This instance with all currently retrieved appLibFlow resources using find and the newly added appLibFlow resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ConfigId=None,
        ConnectionCount=None,
        Description=None,
        FlowId=None,
        FlowSize=None,
        Name=None,
        Parameters=None,
        Percentage=None,
    ):
        # type: (int, int, str, str, int, str, List[str], int) -> AppLibFlow
        """Finds and retrieves appLibFlow resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve appLibFlow resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all appLibFlow resources from the server.

        Args
        ----
        - ConfigId (number): The internal config id asociated with this flow.
        - ConnectionCount (number): Number of connections in this flow.
        - Description (str): Brief description of what the flow does.
        - FlowId (str): The identifier of the flow.
        - FlowSize (number): The size of the flow in bytes.
        - Name (str): The name of the Flow.
        - Parameters (list(str)): Array containing configurable parameters per flow.
        - Percentage (number): The amount of traffic generated for this flows.

        Returns
        -------
        - self: This instance with matching appLibFlow resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of appLibFlow data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the appLibFlow resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
