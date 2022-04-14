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


class IxNetCodeOptions(Base):
    """Contains the ixNet code generation options
    The IxNetCodeOptions class encapsulates a required ixNetCodeOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ixNetCodeOptions"
    _SDM_ATT_MAP = {
        "IncludeAvailableHardware": "includeAvailableHardware",
        "IncludeConnect": "includeConnect",
        "IncludeDefaultValues": "includeDefaultValues",
        "IncludeQuickTest": "includeQuickTest",
        "IncludeStatistic": "includeStatistic",
        "IncludeTAPSettings": "includeTAPSettings",
        "IncludeTestComposer": "includeTestComposer",
        "IncludeTraffic": "includeTraffic",
        "IncludeTrafficFlowGroup": "includeTrafficFlowGroup",
        "IncludeTrafficStack": "includeTrafficStack",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IxNetCodeOptions, self).__init__(parent, list_op)

    @property
    def IncludeAvailableHardware(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include available hardware nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeAvailableHardware"])

    @IncludeAvailableHardware.setter
    def IncludeAvailableHardware(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeAvailableHardware"], value)

    @property
    def IncludeConnect(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Flag to include the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeConnect"])

    @IncludeConnect.setter
    def IncludeConnect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeConnect"], value)

    @property
    def IncludeDefaultValues(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include attributes that have values which are defaul
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeDefaultValues"])

    @IncludeDefaultValues.setter
    def IncludeDefaultValues(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeDefaultValues"], value)

    @property
    def IncludeQuickTest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include quickTest nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeQuickTest"])

    @IncludeQuickTest.setter
    def IncludeQuickTest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeQuickTest"], value)

    @property
    def IncludeStatistic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include statistic view nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeStatistic"])

    @IncludeStatistic.setter
    def IncludeStatistic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeStatistic"], value)

    @property
    def IncludeTAPSettings(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTAPSettings"])

    @IncludeTAPSettings.setter
    def IncludeTAPSettings(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTAPSettings"], value)

    @property
    def IncludeTestComposer(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Flag to include test composer code
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTestComposer"])

    @IncludeTestComposer.setter
    def IncludeTestComposer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTestComposer"], value)

    @property
    def IncludeTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include traffic item nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTraffic"])

    @IncludeTraffic.setter
    def IncludeTraffic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTraffic"], value)

    @property
    def IncludeTrafficFlowGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include traffic item high level stream nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficFlowGroup"])

    @IncludeTrafficFlowGroup.setter
    def IncludeTrafficFlowGroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficFlowGroup"], value)

    @property
    def IncludeTrafficStack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to include high level stream stack nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficStack"])

    @IncludeTrafficStack.setter
    def IncludeTrafficStack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficStack"], value)

    def update(
        self,
        IncludeAvailableHardware=None,
        IncludeConnect=None,
        IncludeDefaultValues=None,
        IncludeQuickTest=None,
        IncludeStatistic=None,
        IncludeTAPSettings=None,
        IncludeTestComposer=None,
        IncludeTraffic=None,
        IncludeTrafficFlowGroup=None,
        IncludeTrafficStack=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IxNetCodeOptions
        """Updates ixNetCodeOptions resource on the server.

        Args
        ----
        - IncludeAvailableHardware (bool): Flag to include available hardware nodes
        - IncludeConnect (bool): Flag to include the connect command
        - IncludeDefaultValues (bool): Flag to include attributes that have values which are defaul
        - IncludeQuickTest (bool): Flag to include quickTest nodes
        - IncludeStatistic (bool): Flag to include statistic view nodes
        - IncludeTAPSettings (bool):
        - IncludeTestComposer (bool): Flag to include test composer code
        - IncludeTraffic (bool): Flag to include traffic item nodes
        - IncludeTrafficFlowGroup (bool): Flag to include traffic item high level stream nodes
        - IncludeTrafficStack (bool): Flag to include high level stream stack nodes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        IncludeAvailableHardware=None,
        IncludeConnect=None,
        IncludeDefaultValues=None,
        IncludeQuickTest=None,
        IncludeStatistic=None,
        IncludeTAPSettings=None,
        IncludeTestComposer=None,
        IncludeTraffic=None,
        IncludeTrafficFlowGroup=None,
        IncludeTrafficStack=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IxNetCodeOptions
        """Finds and retrieves ixNetCodeOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ixNetCodeOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ixNetCodeOptions resources from the server.

        Args
        ----
        - IncludeAvailableHardware (bool): Flag to include available hardware nodes
        - IncludeConnect (bool): Flag to include the connect command
        - IncludeDefaultValues (bool): Flag to include attributes that have values which are defaul
        - IncludeQuickTest (bool): Flag to include quickTest nodes
        - IncludeStatistic (bool): Flag to include statistic view nodes
        - IncludeTAPSettings (bool):
        - IncludeTestComposer (bool): Flag to include test composer code
        - IncludeTraffic (bool): Flag to include traffic item nodes
        - IncludeTrafficFlowGroup (bool): Flag to include traffic item high level stream nodes
        - IncludeTrafficStack (bool): Flag to include high level stream stack nodes

        Returns
        -------
        - self: This instance with matching ixNetCodeOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ixNetCodeOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ixNetCodeOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
