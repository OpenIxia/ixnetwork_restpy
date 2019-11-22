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


class CustomDelayVariation(Base):
    """Specifies custom delay variation as a histogram.  Can only be used on one enabled profile at a time.  Can only be used on a profile which has delay and delayVariation disabled.
    The CustomDelayVariation class encapsulates a required customDelayVariation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'customDelayVariation'

    def __init__(self, parent):
        super(CustomDelayVariation, self).__init__(parent)

    @property
    def CustomValue(self):
        """An instance of the CustomValue class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.customdelayvariation.customvalue.customvalue.CustomValue)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.customdelayvariation.customvalue.customvalue import CustomValue
        return CustomValue(self)

    @property
    def Enabled(self):
        """If true, vary the packet delay.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Name(self):
        """Descriptive name of custom value list.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    def update(self, Enabled=None, Name=None):
        """Updates a child instance of customDelayVariation on the server.

        Args:
            Enabled (bool): If true, vary the packet delay.
            Name (str): Descriptive name of custom value list.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
