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


class AtoiTLVList(Base):
    """PTP IEEE ATOI TLV related configuration
    The AtoiTLVList class encapsulates a required atoiTLVList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'atoiTLVList'

    def __init__(self, parent):
        super(AtoiTLVList, self).__init__(parent)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def CurrentOffset(self):
        """'Current Offset' shall be the current offset of the local time, in seconds.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('currentOffset')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DisplayName(self):
        """'Display Name' shall be the text name of the alternate timescale.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('displayName')

    @property
    def JumpSeconds(self):
        """'Jump Seconds' shall be 0 when the local time does not use Daylight Saving Time (DST), else shall be Nx900 with N, an integer greater or less than 0.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('jumpSeconds')

    @property
    def KeyField(self):
        """keyField shall be >0 when the offset is valid, else 0.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('keyField')

    @property
    def MvActive(self):
        """Activate/Deactivate Configuration.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvActive')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def TimeOfNextJump(self):
        """When not zero, 'Time Of Next Jump' shall be the second portion of the PTP time at the next DST event, OR the next leap second.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeOfNextJump')

    def update(self, Name=None):
        """Updates a child instance of atoiTLVList on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, CurrentOffset=None, DisplayName=None, JumpSeconds=None, KeyField=None, MvActive=None, TimeOfNextJump=None):
        """Base class infrastructure that gets a list of atoiTLVList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            CurrentOffset (str): optional regex of currentOffset
            DisplayName (str): optional regex of displayName
            JumpSeconds (str): optional regex of jumpSeconds
            KeyField (str): optional regex of keyField
            MvActive (str): optional regex of mvActive
            TimeOfNextJump (str): optional regex of timeOfNextJump

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
