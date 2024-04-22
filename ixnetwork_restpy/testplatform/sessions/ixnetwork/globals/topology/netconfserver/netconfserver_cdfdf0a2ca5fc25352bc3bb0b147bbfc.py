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


class NetconfServer(Base):
    """Per Port Netconf Server configuration
    The NetconfServer class encapsulates a required netconfServer resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "netconfServer"
    _SDM_ATT_MAP = {
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Name": "name",
        "RowNames": "rowNames",
        "YangArchive": "yangArchive",
        "YangSourceDirectory": "yangSourceDirectory",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(NetconfServer, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import (
            StartRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StartRate", None) is not None:
                return self._properties.get("StartRate")
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import (
            StopRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopRate", None) is not None:
                return self._properties.get("StopRate")
        return StopRate(self)._select()

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
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    @property
    def YangArchive(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Archived file where YANG modules are present.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["YangArchive"]))

    @property
    def YangSourceDirectory(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory where YANG modules are present.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["YangSourceDirectory"])
        )

    def update(self, Name=None):
        # type: (str) -> NetconfServer
        """Updates netconfServer resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        # type: (int, str, str, List[str]) -> NetconfServer
        """Finds and retrieves netconfServer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netconfServer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netconfServer resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching netconfServer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netconfServer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netconfServer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self, PortNames=None, YangArchive=None, YangSourceDirectory=None
    ):
        """Base class infrastructure that gets a list of netconfServer device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - YangArchive (str): optional regex of yangArchive
        - YangSourceDirectory (str): optional regex of yangSourceDirectory

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
