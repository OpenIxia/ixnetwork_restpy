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


class SwitchFlow131TriggerAttributes(Base):
    """This object allows to configure the switch Flow 131 Trigger Attributes.
    The SwitchFlow131TriggerAttributes class encapsulates a required switchFlow131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'switchFlow131TriggerAttributes'
    _SDM_ATT_MAP = {
        'OutGroup': 'outGroup',
        'OutGroupInputMode': 'outGroupInputMode',
        'OutPort': 'outPort',
        'OutPortInputMode': 'outPortInputMode',
        'TableId': 'tableId',
        'TableIdInputMode': 'tableIdInputMode',
    }

    def __init__(self, parent):
        super(SwitchFlow131TriggerAttributes, self).__init__(parent)

    @property
    def OutGroup(self):
        """
        Returns
        -------
        - number: This describes the out group value. It requires matching entries to include this as an output group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutGroup'])
    @OutGroup.setter
    def OutGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutGroup'], value)

    @property
    def OutGroupInputMode(self):
        """
        Returns
        -------
        - str(allGroups | anyGroup | outGroupCustom): This describes the input mode of the out group value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutGroupInputMode'])
    @OutGroupInputMode.setter
    def OutGroupInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutGroupInputMode'], value)

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: This describes the out port value. It requires matching entries to include this as an output port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPort'])
    @OutPort.setter
    def OutPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPort'], value)

    @property
    def OutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom): This describes the input mode of the out port value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortInputMode'])
    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPortInputMode'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])
    @TableId.setter
    def TableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableId'], value)

    @property
    def TableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | custom): This describes the input mode of the Table Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableIdInputMode'])
    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableIdInputMode'], value)

    def update(self, OutGroup=None, OutGroupInputMode=None, OutPort=None, OutPortInputMode=None, TableId=None, TableIdInputMode=None):
        """Updates switchFlow131TriggerAttributes resource on the server.

        Args
        ----
        - OutGroup (number): This describes the out group value. It requires matching entries to include this as an output group.
        - OutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): This describes the input mode of the out group value.
        - OutPort (number): This describes the out port value. It requires matching entries to include this as an output port.
        - OutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): This describes the input mode of the out port value.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | custom)): This describes the input mode of the Table Identifier.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
