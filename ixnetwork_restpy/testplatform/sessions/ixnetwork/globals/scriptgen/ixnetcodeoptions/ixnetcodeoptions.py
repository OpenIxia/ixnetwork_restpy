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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IxNetCodeOptions(Base):
    """Contains the ixNet code generation options
    The IxNetCodeOptions class encapsulates a required ixNetCodeOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ixNetCodeOptions'
    _SDM_ATT_MAP = {
        'IncludeAvailableHardware': 'includeAvailableHardware',
        'IncludeConnect': 'includeConnect',
        'IncludeDefaultValues': 'includeDefaultValues',
        'IncludeQuickTest': 'includeQuickTest',
        'IncludeStatistic': 'includeStatistic',
        'IncludeTAPSettings': 'includeTAPSettings',
        'IncludeTestComposer': 'includeTestComposer',
        'IncludeTraffic': 'includeTraffic',
        'IncludeTrafficFlowGroup': 'includeTrafficFlowGroup',
        'IncludeTrafficStack': 'includeTrafficStack',
    }

    def __init__(self, parent):
        super(IxNetCodeOptions, self).__init__(parent)

    @property
    def IncludeAvailableHardware(self):
        """
        Returns
        -------
        - bool: Flag to include available hardware nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeAvailableHardware'])
    @IncludeAvailableHardware.setter
    def IncludeAvailableHardware(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeAvailableHardware'], value)

    @property
    def IncludeConnect(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Flag to include the connect command
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeConnect'])
    @IncludeConnect.setter
    def IncludeConnect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeConnect'], value)

    @property
    def IncludeDefaultValues(self):
        """
        Returns
        -------
        - bool: Flag to include attributes that have values which are default
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeDefaultValues'])
    @IncludeDefaultValues.setter
    def IncludeDefaultValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeDefaultValues'], value)

    @property
    def IncludeQuickTest(self):
        """
        Returns
        -------
        - bool: Flag to include quickTest nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeQuickTest'])
    @IncludeQuickTest.setter
    def IncludeQuickTest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeQuickTest'], value)

    @property
    def IncludeStatistic(self):
        """
        Returns
        -------
        - bool: Flag to include statistic view nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeStatistic'])
    @IncludeStatistic.setter
    def IncludeStatistic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeStatistic'], value)

    @property
    def IncludeTAPSettings(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTAPSettings'])
    @IncludeTAPSettings.setter
    def IncludeTAPSettings(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTAPSettings'], value)

    @property
    def IncludeTestComposer(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Flag to include test composer code
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTestComposer'])
    @IncludeTestComposer.setter
    def IncludeTestComposer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTestComposer'], value)

    @property
    def IncludeTraffic(self):
        """
        Returns
        -------
        - bool: Flag to include traffic item nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTraffic'])
    @IncludeTraffic.setter
    def IncludeTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTraffic'], value)

    @property
    def IncludeTrafficFlowGroup(self):
        """
        Returns
        -------
        - bool: Flag to include traffic item high level stream nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTrafficFlowGroup'])
    @IncludeTrafficFlowGroup.setter
    def IncludeTrafficFlowGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTrafficFlowGroup'], value)

    @property
    def IncludeTrafficStack(self):
        """
        Returns
        -------
        - bool: Flag to include high level stream stack nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTrafficStack'])
    @IncludeTrafficStack.setter
    def IncludeTrafficStack(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTrafficStack'], value)

    def update(self, IncludeAvailableHardware=None, IncludeConnect=None, IncludeDefaultValues=None, IncludeQuickTest=None, IncludeStatistic=None, IncludeTAPSettings=None, IncludeTestComposer=None, IncludeTraffic=None, IncludeTrafficFlowGroup=None, IncludeTrafficStack=None):
        """Updates ixNetCodeOptions resource on the server.

        Args
        ----
        - IncludeAvailableHardware (bool): Flag to include available hardware nodes
        - IncludeConnect (bool): Flag to include the connect command
        - IncludeDefaultValues (bool): Flag to include attributes that have values which are default
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
