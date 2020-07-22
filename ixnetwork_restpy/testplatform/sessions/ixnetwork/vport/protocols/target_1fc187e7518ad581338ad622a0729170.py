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


class Target(Base):
    """This object controls the configuration of L3 Site targets.
    The Target class encapsulates a required target resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'target'
    _SDM_ATT_MAP = {
        'TargetList': 'targetList',
        'TargetListEx': 'targetListEx',
    }

    def __init__(self, parent):
        super(Target, self).__init__(parent)

    @property
    def TargetList(self):
        """DEPRECATED 
        Returns
        -------
        - list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number)): Configures a target attribute to be associated with advertised L3 VPN route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetList'])
    @TargetList.setter
    def TargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetList'], value)

    @property
    def TargetListEx(self):
        """
        Returns
        -------
        - list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str)): Configures a list of export targets to be associated with advertised L3 VPN route ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetListEx'])
    @TargetListEx.setter
    def TargetListEx(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetListEx'], value)

    def update(self, TargetList=None, TargetListEx=None):
        """Updates target resource on the server.

        Args
        ----
        - TargetList (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number))): Configures a target attribute to be associated with advertised L3 VPN route ranges.
        - TargetListEx (list(dict(arg1:str[as | ip | asNumber2],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str))): Configures a list of export targets to be associated with advertised L3 VPN route ranges.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
