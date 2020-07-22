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


class ApplyActions(Base):
    """Select the type of apply action instructions that the table flow entry will support.
    The ApplyActions class encapsulates a required applyActions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'applyActions'
    _SDM_ATT_MAP = {
        'CopyTtlIn': 'copyTtlIn',
        'CopyTtlOut': 'copyTtlOut',
        'DecrementMplsTtl': 'decrementMplsTtl',
        'DecrementNetworkTtl': 'decrementNetworkTtl',
        'Experimenter': 'experimenter',
        'Group': 'group',
        'Output': 'output',
        'PopMpls': 'popMpls',
        'PopPbb': 'popPbb',
        'PopVlan': 'popVlan',
        'PushMpls': 'pushMpls',
        'PushPbb': 'pushPbb',
        'PushVlan': 'pushVlan',
        'SetField': 'setField',
        'SetMplsTtl': 'setMplsTtl',
        'SetNetworkTtl': 'setNetworkTtl',
        'SetQueue': 'setQueue',
    }

    def __init__(self, parent):
        super(ApplyActions, self).__init__(parent)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL In Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CopyTtlIn'])
    @CopyTtlIn.setter
    def CopyTtlIn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CopyTtlIn'], value)

    @property
    def CopyTtlOut(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL Out Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CopyTtlOut'])
    @CopyTtlOut.setter
    def CopyTtlOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CopyTtlOut'], value)

    @property
    def DecrementMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement MPLS TTL Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DecrementMplsTtl'])
    @DecrementMplsTtl.setter
    def DecrementMplsTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DecrementMplsTtl'], value)

    @property
    def DecrementNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement Network TTL Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'])
    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'], value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - bool: If selected, table supports Experimenter Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def Group(self):
        """
        Returns
        -------
        - bool: If selected, table supports Group Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Group'])
    @Group.setter
    def Group(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Group'], value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: If selected, table supports Output Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Output'])
    @Output.setter
    def Output(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Output'], value)

    @property
    def PopMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop MPLS Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopMpls'])
    @PopMpls.setter
    def PopMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopMpls'], value)

    @property
    def PopPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop PBB Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopPbb'])
    @PopPbb.setter
    def PopPbb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopPbb'], value)

    @property
    def PopVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop VLAN Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopVlan'])
    @PopVlan.setter
    def PopVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopVlan'], value)

    @property
    def PushMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push MPLS Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushMpls'])
    @PushMpls.setter
    def PushMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushMpls'], value)

    @property
    def PushPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push PBB Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushPbb'])
    @PushPbb.setter
    def PushPbb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushPbb'], value)

    @property
    def PushVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push VLAN Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushVlan'])
    @PushVlan.setter
    def PushVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushVlan'], value)

    @property
    def SetField(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Field Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetField'])
    @SetField.setter
    def SetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetField'], value)

    @property
    def SetMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set MPLS TTL Apply Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetMplsTtl'])
    @SetMplsTtl.setter
    def SetMplsTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetMplsTtl'], value)

    @property
    def SetNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Network TTL Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetNetworkTtl'])
    @SetNetworkTtl.setter
    def SetNetworkTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetNetworkTtl'], value)

    @property
    def SetQueue(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Queue Write Actions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetQueue'])
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetQueue'], value)

    def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Experimenter=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Updates applyActions resource on the server.

        Args
        ----
        - CopyTtlIn (bool): If selected, table supports Copy TTL In Apply Actions.
        - CopyTtlOut (bool): If selected, table supports Copy TTL Out Apply Actions.
        - DecrementMplsTtl (bool): If selected, table supports Decrement MPLS TTL Apply Actions.
        - DecrementNetworkTtl (bool): If selected, table supports Decrement Network TTL Write Actions.
        - Experimenter (bool): If selected, table supports Experimenter Write Actions.
        - Group (bool): If selected, table supports Group Write Actions.
        - Output (bool): If selected, table supports Output Apply Actions.
        - PopMpls (bool): If selected, table supports Pop MPLS Apply Actions.
        - PopPbb (bool): If selected, table supports Pop PBB Write Actions.
        - PopVlan (bool): If selected, table supports Pop VLAN Apply Actions.
        - PushMpls (bool): If selected, table supports Push MPLS Apply Actions.
        - PushPbb (bool): If selected, table supports Push PBB Write Actions.
        - PushVlan (bool): If selected, table supports Push VLAN Apply Actions.
        - SetField (bool): If selected, table supports Set Field Write Actions.
        - SetMplsTtl (bool): If selected, table supports Set MPLS TTL Apply Actions.
        - SetNetworkTtl (bool): If selected, table supports Set Network TTL Write Actions.
        - SetQueue (bool): If selected, table supports Set Queue Write Actions.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
