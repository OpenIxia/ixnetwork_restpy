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


class ExtendedCommunity(Base):
    """This object is used to construct an extended community attribute for a route item.
    The ExtendedCommunity class encapsulates a required extendedCommunity resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'extendedCommunity'
    _SDM_ATT_MAP = {
        'ExtendedCommunity': 'extendedCommunity',
    }

    def __init__(self, parent):
        super(ExtendedCommunity, self).__init__(parent)

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | fourOctetAs | opaque | ip],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str)): Associates BGP4 extended community attributes with a route item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCommunity'])
    @ExtendedCommunity.setter
    def ExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtendedCommunity'], value)

    def update(self, ExtendedCommunity=None):
        """Updates extendedCommunity resource on the server.

        Args
        ----
        - ExtendedCommunity (list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | fourOctetAs | opaque | ip],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str))): Associates BGP4 extended community attributes with a route item.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
