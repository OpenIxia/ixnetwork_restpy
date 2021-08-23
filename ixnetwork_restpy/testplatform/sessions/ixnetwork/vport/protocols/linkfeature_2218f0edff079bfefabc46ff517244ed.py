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
from typing import List, Any, Union


class LinkFeature(Base):
    """NOT DEFINED
    The LinkFeature class encapsulates a required linkFeature resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'linkFeature'
    _SDM_ATT_MAP = {
        'OfppfAutoNegotiation': 'ofppfAutoNegotiation',
        'OfppfPause': 'ofppfPause',
        'OfppfPauseAsym': 'ofppfPauseAsym',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(LinkFeature, self).__init__(parent, list_op)

    @property
    def OfppfAutoNegotiation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OfppfAutoNegotiation'])
    @OfppfAutoNegotiation.setter
    def OfppfAutoNegotiation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OfppfAutoNegotiation'], value)

    @property
    def OfppfPause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OfppfPause'])
    @OfppfPause.setter
    def OfppfPause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OfppfPause'], value)

    @property
    def OfppfPauseAsym(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OfppfPauseAsym'])
    @OfppfPauseAsym.setter
    def OfppfPauseAsym(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OfppfPauseAsym'], value)

    def update(self, OfppfAutoNegotiation=None, OfppfPause=None, OfppfPauseAsym=None):
        # type: (bool, bool, bool) -> LinkFeature
        """Updates linkFeature resource on the server.

        Args
        ----
        - OfppfAutoNegotiation (bool): NOT DEFINED
        - OfppfPause (bool): NOT DEFINED
        - OfppfPauseAsym (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
