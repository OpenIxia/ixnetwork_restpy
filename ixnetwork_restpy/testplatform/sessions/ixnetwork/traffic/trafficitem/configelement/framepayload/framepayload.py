# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class FramePayload(Base):
    """This object provides different options for the Frame Payload.
    The FramePayload class encapsulates a required framePayload resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'framePayload'

    def __init__(self, parent):
        super(FramePayload, self).__init__(parent)

    @property
    def CustomPattern(self):
        """If Frame Payload type is Custom, then this attribute specifies a string in hex format.

        Returns:
            str
        """
        return self._get_attribute('customPattern')
    @CustomPattern.setter
    def CustomPattern(self, value):
        self._set_attribute('customPattern', value)

    @property
    def CustomRepeat(self):
        """If true, Custom Pattern is repeated.

        Returns:
            bool
        """
        return self._get_attribute('customRepeat')
    @CustomRepeat.setter
    def CustomRepeat(self, value):
        self._set_attribute('customRepeat', value)

    @property
    def Type(self):
        """The types of Frame Payload.

        Returns:
            str(CJPAT|CRPAT|custom|decrementByte|decrementWord|incrementByte|incrementWord|random)
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    def update(self, CustomPattern=None, CustomRepeat=None, Type=None):
        """Updates a child instance of framePayload on the server.

        Args:
            CustomPattern (str): If Frame Payload type is Custom, then this attribute specifies a string in hex format.
            CustomRepeat (bool): If true, Custom Pattern is repeated.
            Type (str(CJPAT|CRPAT|custom|decrementByte|decrementWord|incrementByte|incrementWord|random)): The types of Frame Payload.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
