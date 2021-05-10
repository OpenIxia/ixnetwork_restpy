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


class BandTypes(Base):
    """Select the band types supported.
    The BandTypes class encapsulates a required bandTypes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bandTypes'
    _SDM_ATT_MAP = {
        'Drop': 'drop',
        'DscpRemark': 'dscpRemark',
    }

    def __init__(self, parent):
        super(BandTypes, self).__init__(parent)

    @property
    def Drop(self):
        """
        Returns
        -------
        - bool: This indicates that packets which exceed the band rate value are dropped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Drop'])
    @Drop.setter
    def Drop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Drop'], value)

    @property
    def DscpRemark(self):
        """
        Returns
        -------
        - bool: This indicates that the drop precedence of the DSCP field is remarked in the IP header of the packets that exceed the band rate value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DscpRemark'])
    @DscpRemark.setter
    def DscpRemark(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DscpRemark'], value)

    def update(self, Drop=None, DscpRemark=None):
        """Updates bandTypes resource on the server.

        Args
        ----
        - Drop (bool): This indicates that packets which exceed the band rate value are dropped.
        - DscpRemark (bool): This indicates that the drop precedence of the DSCP field is remarked in the IP header of the packets that exceed the band rate value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
