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


class GroupCapabilities(Base):
    """Specify the group capabilities supported by Switch.
    The GroupCapabilities class encapsulates a required groupCapabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'groupCapabilities'
    _SDM_ATT_MAP = {
        'Chaining': 'chaining',
        'ChainingChecks': 'chainingChecks',
        'SelectLiveness': 'selectLiveness',
        'SelectWeight': 'selectWeight',
    }

    def __init__(self, parent):
        super(GroupCapabilities, self).__init__(parent)

    @property
    def Chaining(self):
        """
        Returns
        -------
        - bool: Chaining groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Chaining'])
    @Chaining.setter
    def Chaining(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Chaining'], value)

    @property
    def ChainingChecks(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChainingChecks'])
    @ChainingChecks.setter
    def ChainingChecks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChainingChecks'], value)

    @property
    def SelectLiveness(self):
        """
        Returns
        -------
        - bool: Liveness for select groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectLiveness'])
    @SelectLiveness.setter
    def SelectLiveness(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectLiveness'], value)

    @property
    def SelectWeight(self):
        """
        Returns
        -------
        - bool: Weight for select groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectWeight'])
    @SelectWeight.setter
    def SelectWeight(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectWeight'], value)

    def update(self, Chaining=None, ChainingChecks=None, SelectLiveness=None, SelectWeight=None):
        """Updates groupCapabilities resource on the server.

        Args
        ----
        - Chaining (bool): Chaining groups.
        - ChainingChecks (bool): NOT DEFINED
        - SelectLiveness (bool): Liveness for select groups.
        - SelectWeight (bool): Weight for select groups.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
