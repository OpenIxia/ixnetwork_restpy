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


class FramePreemption(Base):
    """
    The FramePreemption class encapsulates a required framePreemption resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'framePreemption'
    _SDM_ATT_MAP = {
        'IsFramePreemptionEnabled': 'isFramePreemptionEnabled',
        'IsSmdVREnabled': 'isSmdVREnabled',
    }

    def __init__(self, parent):
        super(FramePreemption, self).__init__(parent)

    @property
    def IsFramePreemptionEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsFramePreemptionEnabled'])
    @IsFramePreemptionEnabled.setter
    def IsFramePreemptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsFramePreemptionEnabled'], value)

    @property
    def IsSmdVREnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSmdVREnabled'])
    @IsSmdVREnabled.setter
    def IsSmdVREnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSmdVREnabled'], value)

    def update(self, IsFramePreemptionEnabled=None, IsSmdVREnabled=None):
        """Updates framePreemption resource on the server.

        Args
        ----
        - IsFramePreemptionEnabled (bool): 
        - IsSmdVREnabled (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
