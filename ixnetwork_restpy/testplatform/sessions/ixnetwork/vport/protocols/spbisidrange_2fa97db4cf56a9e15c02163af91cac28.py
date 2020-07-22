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


class SpbIsIdRange(Base):
    """The ISIS ID for SPB Topology Range.
    The SpbIsIdRange class encapsulates a list of spbIsIdRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbIsIdRange.find() method.
    The list can be managed by using the SpbIsIdRange.add() and SpbIsIdRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'spbIsIdRange'
    _SDM_ATT_MAP = {
        'CMacAddressCount': 'cMacAddressCount',
        'CMacAddressStep': 'cMacAddressStep',
        'CVlan': 'cVlan',
        'Enabled': 'enabled',
        'ISid': 'iSid',
        'ITagEthernetType': 'iTagEthernetType',
        'RBit': 'rBit',
        'SVlan': 'sVlan',
        'StartCmacAddress': 'startCmacAddress',
        'TBit': 'tBit',
        'TrafficDestMacAddress': 'trafficDestMacAddress',
        'TransmissionType': 'transmissionType',
        'VlanType': 'vlanType',
    }

    def __init__(self, parent):
        super(SpbIsIdRange, self).__init__(parent)

    @property
    def CMacAddressCount(self):
        """
        Returns
        -------
        - number: The number of C-MAC for each C-MAC range. The default is 1. Maximum value is 4095. The minimum value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressCount'])
    @CMacAddressCount.setter
    def CMacAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressCount'], value)

    @property
    def CMacAddressStep(self):
        """
        Returns
        -------
        - str: The amount to increment each successive C-MAC address from the starting CMAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressStep'])
    @CMacAddressStep.setter
    def CMacAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressStep'], value)

    @property
    def CVlan(self):
        """
        Returns
        -------
        - number: The number of stacked VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])
    @CVlan.setter
    def CVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlan'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the topology range will be part of the simulated network.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ISid(self):
        """
        Returns
        -------
        - number: The I-component Service Instance identifier. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ISid'])
    @ISid.setter
    def ISid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ISid'], value)

    @property
    def ITagEthernetType(self):
        """
        Returns
        -------
        - number: The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagEthernetType'])

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: The Restart State bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RBit'])
    @RBit.setter
    def RBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RBit'], value)

    @property
    def SVlan(self):
        """
        Returns
        -------
        - number: The number of single VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])
    @SVlan.setter
    def SVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlan'], value)

    @property
    def StartCmacAddress(self):
        """
        Returns
        -------
        - str: The starting C-MAC address for the C_MAC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartCmacAddress'])
    @StartCmacAddress.setter
    def StartCmacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartCmacAddress'], value)

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: The external route tag bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])
    @TBit.setter
    def TBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TBit'], value)

    @property
    def TrafficDestMacAddress(self):
        """
        Returns
        -------
        - str: The traffic-destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficDestMacAddress'])
    @TrafficDestMacAddress.setter
    def TrafficDestMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficDestMacAddress'], value)

    @property
    def TransmissionType(self):
        """
        Returns
        -------
        - number: Select the type of packet transmission. Options include Unicast and Multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmissionType'])
    @TransmissionType.setter
    def TransmissionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmissionType'], value)

    @property
    def VlanType(self):
        """
        Returns
        -------
        - number: Select the VLAN type. Options include Single VLAN and Stacked VLAN. Selecting Stacked VLAN activates the C-VLAN options. The Default option is Single VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanType'])
    @VlanType.setter
    def VlanType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanType'], value)

    def update(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Updates spbIsIdRange resource on the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC for each C-MAC range. The default is 1. Maximum value is 4095. The minimum value is 1.
        - CMacAddressStep (str): The amount to increment each successive C-MAC address from the starting CMAC address.
        - CVlan (number): The number of stacked VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - ISid (number): The I-component Service Instance identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - SVlan (number): The number of single VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - StartCmacAddress (str): The starting C-MAC address for the C_MAC range.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): Select the VLAN type. Options include Single VLAN and Stacked VLAN. Selecting Stacked VLAN activates the C-VLAN options. The Default option is Single VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Adds a new spbIsIdRange resource on the server and adds it to the container.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC for each C-MAC range. The default is 1. Maximum value is 4095. The minimum value is 1.
        - CMacAddressStep (str): The amount to increment each successive C-MAC address from the starting CMAC address.
        - CVlan (number): The number of stacked VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - ISid (number): The I-component Service Instance identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - SVlan (number): The number of single VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - StartCmacAddress (str): The starting C-MAC address for the C_MAC range.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): Select the VLAN type. Options include Single VLAN and Stacked VLAN. Selecting Stacked VLAN activates the C-VLAN options. The Default option is Single VLAN.

        Returns
        -------
        - self: This instance with all currently retrieved spbIsIdRange resources using find and the newly added spbIsIdRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbIsIdRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, ITagEthernetType=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Finds and retrieves spbIsIdRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbIsIdRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbIsIdRange resources from the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC for each C-MAC range. The default is 1. Maximum value is 4095. The minimum value is 1.
        - CMacAddressStep (str): The amount to increment each successive C-MAC address from the starting CMAC address.
        - CVlan (number): The number of stacked VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - ISid (number): The I-component Service Instance identifier. The maximum value is 16777215. The minimum value is 0.
        - ITagEthernetType (number): The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        - RBit (bool): The Restart State bit.
        - SVlan (number): The number of single VLAN. The minimum value is 1. The maximum value is 4095. The default is 1.
        - StartCmacAddress (str): The starting C-MAC address for the C_MAC range.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): Select the VLAN type. Options include Single VLAN and Stacked VLAN. Selecting Stacked VLAN activates the C-VLAN options. The Default option is Single VLAN.

        Returns
        -------
        - self: This instance with matching spbIsIdRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbIsIdRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbIsIdRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
