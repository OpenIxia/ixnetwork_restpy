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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class Esmc(Base):
    """ESMC global and per-port settings
    The Esmc class encapsulates a required esmc resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'esmc'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'RowNames': 'rowNames',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Esmc, self).__init__(parent, list_op)

    @property
    def StartRateAndFlowControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.startrateandflowcontrol.startrateandflowcontrol_585d8f39c08d7894b1219834ab4ac841.StartRateAndFlowControl): An instance of the StartRateAndFlowControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.startrateandflowcontrol.startrateandflowcontrol_585d8f39c08d7894b1219834ab4ac841 import StartRateAndFlowControl
        if self._properties.get('StartRateAndFlowControl', None) is not None:
            return self._properties.get('StartRateAndFlowControl')
        else:
            return StartRateAndFlowControl(self)._select()

    @property
    def StopRateAndFlowControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.stoprateandflowcontrol.stoprateandflowcontrol_1859cdc6da8001544275aa8ebcd9d250.StopRateAndFlowControl): An instance of the StopRateAndFlowControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.stoprateandflowcontrol.stoprateandflowcontrol_1859cdc6da8001544275aa8ebcd9d250 import StopRateAndFlowControl
        if self._properties.get('StopRateAndFlowControl', None) is not None:
            return self._properties.get('StopRateAndFlowControl')
        else:
            return StopRateAndFlowControl(self)._select()

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    def update(self, Name=None):
        # type: (str) -> Esmc
        """Updates esmc resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
