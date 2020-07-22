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


class LabelSpace(Base):
    """This object configures the labels for the route range.
    The LabelSpace class encapsulates a required labelSpace resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'labelSpace'
    _SDM_ATT_MAP = {
        'End': 'end',
        'LabelId': 'labelId',
        'Mode': 'mode',
        'Start': 'start',
        'Step': 'step',
    }

    def __init__(self, parent):
        super(LabelSpace, self).__init__(parent)

    @property
    def End(self):
        """
        Returns
        -------
        - number: The last label value available in the label space (range).
        """
        return self._get_attribute(self._SDM_ATT_MAP['End'])
    @End.setter
    def End(self, value):
        self._set_attribute(self._SDM_ATT_MAP['End'], value)

    @property
    def LabelId(self):
        """
        Returns
        -------
        - number: The identifier for the label space.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelId'])
    @LabelId.setter
    def LabelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelId'], value)

    @property
    def Mode(self):
        """
        Returns
        -------
        - str(fixedLabel | incrementLabel): Sets the Label mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def Start(self):
        """
        Returns
        -------
        - number: The first label value available in the label space (range). The default is 16.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Start'])
    @Start.setter
    def Start(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Start'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: The value to add for creating each additional label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    def update(self, End=None, LabelId=None, Mode=None, Start=None, Step=None):
        """Updates labelSpace resource on the server.

        Args
        ----
        - End (number): The last label value available in the label space (range).
        - LabelId (number): The identifier for the label space.
        - Mode (str(fixedLabel | incrementLabel)): Sets the Label mode.
        - Start (number): The first label value available in the label space (range). The default is 16.
        - Step (number): The value to add for creating each additional label value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
