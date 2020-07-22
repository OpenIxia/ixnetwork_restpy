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


class WriteActionType(Base):
    """NOT DEFINED
    The WriteActionType class encapsulates a required writeActionType resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'writeActionType'
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
        super(WriteActionType, self).__init__(parent)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetQueue'])
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetQueue'], value)

    def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Experimenter=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Updates writeActionType resource on the server.

        Args
        ----
        - CopyTtlIn (bool): NOT DEFINED
        - CopyTtlOut (bool): NOT DEFINED
        - DecrementMplsTtl (bool): NOT DEFINED
        - DecrementNetworkTtl (bool): NOT DEFINED
        - Experimenter (bool): NOT DEFINED
        - Group (bool): NOT DEFINED
        - Output (bool): NOT DEFINED
        - PopMpls (bool): NOT DEFINED
        - PopPbb (bool): NOT DEFINED
        - PopVlan (bool): NOT DEFINED
        - PushMpls (bool): NOT DEFINED
        - PushPbb (bool): NOT DEFINED
        - PushVlan (bool): NOT DEFINED
        - SetField (bool): NOT DEFINED
        - SetMplsTtl (bool): NOT DEFINED
        - SetNetworkTtl (bool): NOT DEFINED
        - SetQueue (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
