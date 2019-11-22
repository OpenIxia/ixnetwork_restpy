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


class Flapping(Base):
    """This object controls route flapping for the route range.
    The Flapping class encapsulates a required flapping resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'flapping'

    def __init__(self, parent):
        super(Flapping, self).__init__(parent)

    @property
    def Delay(self):
        """The setting for a timer that must elapse before a route range is advertised. It allows the user to specify a pause time between the sending of route ranges.

        Returns:
            number
        """
        return self._get_attribute('delay')
    @Delay.setter
    def Delay(self, value):
        self._set_attribute('delay', value)

    @property
    def DownTime(self):
        """During flapping, the amount of time during which the routes in the route range are withdrawn/down.

        Returns:
            number
        """
        return self._get_attribute('downTime')
    @DownTime.setter
    def DownTime(self, value):
        self._set_attribute('downTime', value)

    @property
    def EnablePartialFlap(self):
        """Enables partial flapping, based on the Flap From and To Route Index settings.

        Returns:
            bool
        """
        return self._get_attribute('enablePartialFlap')
    @EnablePartialFlap.setter
    def EnablePartialFlap(self, value):
        self._set_attribute('enablePartialFlap', value)

    @property
    def Enabled(self):
        """If true, enables route flapping.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def RoutesToFlapFrom(self):
        """The index of the first generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)

        Returns:
            number
        """
        return self._get_attribute('routesToFlapFrom')
    @RoutesToFlapFrom.setter
    def RoutesToFlapFrom(self, value):
        self._set_attribute('routesToFlapFrom', value)

    @property
    def RoutesToFlapTo(self):
        """The index of the last generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)

        Returns:
            number
        """
        return self._get_attribute('routesToFlapTo')
    @RoutesToFlapTo.setter
    def RoutesToFlapTo(self, value):
        self._set_attribute('routesToFlapTo', value)

    @property
    def UpTime(self):
        """During flapping, the amount of time during which the routes in the route range are up.

        Returns:
            number
        """
        return self._get_attribute('upTime')
    @UpTime.setter
    def UpTime(self, value):
        self._set_attribute('upTime', value)

    def update(self, Delay=None, DownTime=None, EnablePartialFlap=None, Enabled=None, RoutesToFlapFrom=None, RoutesToFlapTo=None, UpTime=None):
        """Updates a child instance of flapping on the server.

        Args:
            Delay (number): The setting for a timer that must elapse before a route range is advertised. It allows the user to specify a pause time between the sending of route ranges.
            DownTime (number): During flapping, the amount of time during which the routes in the route range are withdrawn/down.
            EnablePartialFlap (bool): Enables partial flapping, based on the Flap From and To Route Index settings.
            Enabled (bool): If true, enables route flapping.
            RoutesToFlapFrom (number): The index of the first generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
            RoutesToFlapTo (number): The index of the last generated route to be flapped (starting at 0). (Flap and Partial Flap must be enabled.)
            UpTime (number): During flapping, the amount of time during which the routes in the route range are up.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
