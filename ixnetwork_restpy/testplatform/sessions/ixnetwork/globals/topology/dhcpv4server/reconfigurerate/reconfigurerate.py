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


class ReconfigureRate(Base):
    """Parameters used for controlling the rate of actions
    The ReconfigureRate class encapsulates a required reconfigureRate resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'reconfigureRate'

    def __init__(self, parent):
        super(ReconfigureRate, self).__init__(parent)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def Enabled(self):
        """Enabled

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enabled')

    @property
    def Interval(self):
        """The time interval in milliseconds during which the rate is calculated (rate = count/interval)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('interval')

    @property
    def MaxOutstanding(self):
        """The number of triggered instances of an action that are still awaiting a response or completion

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxOutstanding')

    @property
    def Rate(self):
        """Number of times an action is triggered per time interval

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rate')

    @property
    def RowNames(self):
        """Name of rows

        Returns:
            list(str)
        """
        return self._get_attribute('rowNames')

    @property
    def ScaleMode(self):
        """Indicates whether the control is specified per port or per device group.

        Returns:
            str(port|deviceGroup)
        """
        return self._get_attribute('scaleMode')
    @ScaleMode.setter
    def ScaleMode(self, value):
        self._set_attribute('scaleMode', value)

    def update(self, ScaleMode=None):
        """Updates a child instance of reconfigureRate on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ScaleMode (str(port|deviceGroup)): Indicates whether the control is specified per port or per device group.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, Enabled=None, Interval=None, MaxOutstanding=None, Rate=None):
        """Base class infrastructure that gets a list of reconfigureRate device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Enabled (str): optional regex of enabled
            Interval (str): optional regex of interval
            MaxOutstanding (str): optional regex of maxOutstanding
            Rate (str): optional regex of rate

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
