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


class ECpriRec(Base):
    """eCRPI Port Specific Data
    The ECpriRec class encapsulates a required eCpriRec resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'eCpriRec'

    def __init__(self, parent):
        super(ECpriRec, self).__init__(parent)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def ECpriProtocolRevision(self):
        """eCPRI protocol revision to be used by all eCPRI messages.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eCpriProtocolRevision')

    @property
    def ECpriUdpDestinationPort(self):
        """UDP Destination port to be used by all eCPRI messages in this port.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eCpriUdpDestinationPort')

    @property
    def EcpriProtocolRevision(self):
        """DEPRECATED eCPRI protocol revision to be used by all eCPRI messages.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ecpriProtocolRevision')

    @property
    def EcpriUdpDestinationPort(self):
        """DEPRECATED UDP Destination port to be used by all eCPRI messages in this port.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ecpriUdpDestinationPort')

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
    def RowNames(self):
        """Name of rows

        Returns:
            list(str)
        """
        return self._get_attribute('rowNames')

    def update(self, Name=None):
        """Updates a child instance of eCpriRec on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, ECpriProtocolRevision=None, ECpriUdpDestinationPort=None, EcpriProtocolRevision=None, EcpriUdpDestinationPort=None):
        """Base class infrastructure that gets a list of eCpriRec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            ECpriProtocolRevision (str): optional regex of eCpriProtocolRevision
            ECpriUdpDestinationPort (str): optional regex of eCpriUdpDestinationPort
            EcpriProtocolRevision (str): optional regex of ecpriProtocolRevision
            EcpriUdpDestinationPort (str): optional regex of ecpriUdpDestinationPort

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
