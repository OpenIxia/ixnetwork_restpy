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


class FlowRangeAction(Base):
    """Indicates the description of the Flow Range action.
    The FlowRangeAction class encapsulates a list of flowRangeAction resources that are managed by the user.
    A list of resources can be retrieved from the server using the FlowRangeAction.find() method.
    The list can be managed by using the FlowRangeAction.add() and FlowRangeAction.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'flowRangeAction'
    _SDM_ATT_MAP = {
        'EthDestination': 'ethDestination',
        'EthSource': 'ethSource',
        'IpDscp': 'ipDscp',
        'Ipv4Destination': 'ipv4Destination',
        'Ipv4Source': 'ipv4Source',
        'MaxByteLength': 'maxByteLength',
        'OutputPort': 'outputPort',
        'QueueId': 'queueId',
        'TransportDestination': 'transportDestination',
        'TransportSource': 'transportSource',
        'TypeOfAction': 'typeOfAction',
        'TypeOfOutPort': 'typeOfOutPort',
        'VendorData': 'vendorData',
        'VendorDataLength': 'vendorDataLength',
        'VendorId': 'vendorId',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(FlowRangeAction, self).__init__(parent)

    @property
    def EthDestination(self):
        """
        Returns
        -------
        - str: Specifies the destination address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetDst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthDestination'])
    @EthDestination.setter
    def EthDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthDestination'], value)

    @property
    def EthSource(self):
        """
        Returns
        -------
        - str: Specifies the source address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetSrc.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthSource'])
    @EthSource.setter
    def EthSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthSource'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - number: Specifies the IP DSCP value. This attribute value is applicable only when the typeOfAction selected is setIpv4TosBits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - str: Specifies the destination IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4DstAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Destination'])
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Destination'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: Specifies the source IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4SrcAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def MaxByteLength(self):
        """
        Returns
        -------
        - number: Indicates the maximum length in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxByteLength'])
    @MaxByteLength.setter
    def MaxByteLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxByteLength'], value)

    @property
    def OutputPort(self):
        """
        Returns
        -------
        - number: Specifies the number of Output ports used. This attribute value is applicable only when the typeOfOutPort selected is ofppManual.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPort'])
    @OutputPort.setter
    def OutputPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutputPort'], value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: Indicates the Queue ID for this Flow Range. This attribute value is applicable only when the typeOfAction selected is enqueue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueId'], value)

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - number: Specifies the transport destination address. This attribute value is applicable only when the typeOfAction selected is setTransportDestination.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestination'])
    @TransportDestination.setter
    def TransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportDestination'], value)

    @property
    def TransportSource(self):
        """
        Returns
        -------
        - number: Specifies the Transport source address. This attribute value is applicable only when the typeOfAction selected is setTransportSource.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportSource'])
    @TransportSource.setter
    def TransportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportSource'], value)

    @property
    def TypeOfAction(self):
        """
        Returns
        -------
        - str(none | output | enqueue | setVlanId | setVlanPriority | stripVlanHeader | setEthernetSrc | setEthernetDst | setIpv4TosBits | setIpv4SrcAddress | setIpv4DstAddress | setTransportSource | setTransportDestination | setVendorAction): Indicates the action type associated with this Flow Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeOfAction'])
    @TypeOfAction.setter
    def TypeOfAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeOfAction'], value)

    @property
    def TypeOfOutPort(self):
        """
        Returns
        -------
        - str(ofppManual | ofppAll | ofppController | ofppInPort | ofppLocal | ofppNormal | ofppFlood): Specifies the Output Port Type for this Flow Range. This attribute value is applicable only when the typeOfAction selected is output
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeOfOutPort'])
    @TypeOfOutPort.setter
    def TypeOfOutPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeOfOutPort'], value)

    @property
    def VendorData(self):
        """
        Returns
        -------
        - str: Specifies the data of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorData'])
    @VendorData.setter
    def VendorData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorData'], value)

    @property
    def VendorDataLength(self):
        """
        Returns
        -------
        - number: Specifies the data length of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorDataLength'])
    @VendorDataLength.setter
    def VendorDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorDataLength'], value)

    @property
    def VendorId(self):
        """
        Returns
        -------
        - number: Specifies the unique Vendor identifier. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorId'])
    @VendorId.setter
    def VendorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorId'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: Specifies the unique VLAN Identifier for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanId.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: Specifies the User Priority for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanPriority.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, EthDestination=None, EthSource=None, IpDscp=None, Ipv4Destination=None, Ipv4Source=None, MaxByteLength=None, OutputPort=None, QueueId=None, TransportDestination=None, TransportSource=None, TypeOfAction=None, TypeOfOutPort=None, VendorData=None, VendorDataLength=None, VendorId=None, VlanId=None, VlanPriority=None):
        """Updates flowRangeAction resource on the server.

        Args
        ----
        - EthDestination (str): Specifies the destination address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetDst.
        - EthSource (str): Specifies the source address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetSrc.
        - IpDscp (number): Specifies the IP DSCP value. This attribute value is applicable only when the typeOfAction selected is setIpv4TosBits.
        - Ipv4Destination (str): Specifies the destination IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4DstAddress.
        - Ipv4Source (str): Specifies the source IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4SrcAddress.
        - MaxByteLength (number): Indicates the maximum length in bytes.
        - OutputPort (number): Specifies the number of Output ports used. This attribute value is applicable only when the typeOfOutPort selected is ofppManual.
        - QueueId (number): Indicates the Queue ID for this Flow Range. This attribute value is applicable only when the typeOfAction selected is enqueue.
        - TransportDestination (number): Specifies the transport destination address. This attribute value is applicable only when the typeOfAction selected is setTransportDestination.
        - TransportSource (number): Specifies the Transport source address. This attribute value is applicable only when the typeOfAction selected is setTransportSource.
        - TypeOfAction (str(none | output | enqueue | setVlanId | setVlanPriority | stripVlanHeader | setEthernetSrc | setEthernetDst | setIpv4TosBits | setIpv4SrcAddress | setIpv4DstAddress | setTransportSource | setTransportDestination | setVendorAction)): Indicates the action type associated with this Flow Range.
        - TypeOfOutPort (str(ofppManual | ofppAll | ofppController | ofppInPort | ofppLocal | ofppNormal | ofppFlood)): Specifies the Output Port Type for this Flow Range. This attribute value is applicable only when the typeOfAction selected is output
        - VendorData (str): Specifies the data of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorDataLength (number): Specifies the data length of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorId (number): Specifies the unique Vendor identifier. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VlanId (number): Specifies the unique VLAN Identifier for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanId.
        - VlanPriority (number): Specifies the User Priority for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanPriority.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EthDestination=None, EthSource=None, IpDscp=None, Ipv4Destination=None, Ipv4Source=None, MaxByteLength=None, OutputPort=None, QueueId=None, TransportDestination=None, TransportSource=None, TypeOfAction=None, TypeOfOutPort=None, VendorData=None, VendorDataLength=None, VendorId=None, VlanId=None, VlanPriority=None):
        """Adds a new flowRangeAction resource on the server and adds it to the container.

        Args
        ----
        - EthDestination (str): Specifies the destination address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetDst.
        - EthSource (str): Specifies the source address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetSrc.
        - IpDscp (number): Specifies the IP DSCP value. This attribute value is applicable only when the typeOfAction selected is setIpv4TosBits.
        - Ipv4Destination (str): Specifies the destination IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4DstAddress.
        - Ipv4Source (str): Specifies the source IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4SrcAddress.
        - MaxByteLength (number): Indicates the maximum length in bytes.
        - OutputPort (number): Specifies the number of Output ports used. This attribute value is applicable only when the typeOfOutPort selected is ofppManual.
        - QueueId (number): Indicates the Queue ID for this Flow Range. This attribute value is applicable only when the typeOfAction selected is enqueue.
        - TransportDestination (number): Specifies the transport destination address. This attribute value is applicable only when the typeOfAction selected is setTransportDestination.
        - TransportSource (number): Specifies the Transport source address. This attribute value is applicable only when the typeOfAction selected is setTransportSource.
        - TypeOfAction (str(none | output | enqueue | setVlanId | setVlanPriority | stripVlanHeader | setEthernetSrc | setEthernetDst | setIpv4TosBits | setIpv4SrcAddress | setIpv4DstAddress | setTransportSource | setTransportDestination | setVendorAction)): Indicates the action type associated with this Flow Range.
        - TypeOfOutPort (str(ofppManual | ofppAll | ofppController | ofppInPort | ofppLocal | ofppNormal | ofppFlood)): Specifies the Output Port Type for this Flow Range. This attribute value is applicable only when the typeOfAction selected is output
        - VendorData (str): Specifies the data of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorDataLength (number): Specifies the data length of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorId (number): Specifies the unique Vendor identifier. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VlanId (number): Specifies the unique VLAN Identifier for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanId.
        - VlanPriority (number): Specifies the User Priority for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanPriority.

        Returns
        -------
        - self: This instance with all currently retrieved flowRangeAction resources using find and the newly added flowRangeAction resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained flowRangeAction resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EthDestination=None, EthSource=None, IpDscp=None, Ipv4Destination=None, Ipv4Source=None, MaxByteLength=None, OutputPort=None, QueueId=None, TransportDestination=None, TransportSource=None, TypeOfAction=None, TypeOfOutPort=None, VendorData=None, VendorDataLength=None, VendorId=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves flowRangeAction resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowRangeAction resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowRangeAction resources from the server.

        Args
        ----
        - EthDestination (str): Specifies the destination address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetDst.
        - EthSource (str): Specifies the source address of the Ethernet port. This attribute value is applicable only when the typeOfAction selected is setEthernetSrc.
        - IpDscp (number): Specifies the IP DSCP value. This attribute value is applicable only when the typeOfAction selected is setIpv4TosBits.
        - Ipv4Destination (str): Specifies the destination IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4DstAddress.
        - Ipv4Source (str): Specifies the source IPv4 address for this flow range. This attribute value is applicable only when the typeOfAction selected is setIpv4SrcAddress.
        - MaxByteLength (number): Indicates the maximum length in bytes.
        - OutputPort (number): Specifies the number of Output ports used. This attribute value is applicable only when the typeOfOutPort selected is ofppManual.
        - QueueId (number): Indicates the Queue ID for this Flow Range. This attribute value is applicable only when the typeOfAction selected is enqueue.
        - TransportDestination (number): Specifies the transport destination address. This attribute value is applicable only when the typeOfAction selected is setTransportDestination.
        - TransportSource (number): Specifies the Transport source address. This attribute value is applicable only when the typeOfAction selected is setTransportSource.
        - TypeOfAction (str(none | output | enqueue | setVlanId | setVlanPriority | stripVlanHeader | setEthernetSrc | setEthernetDst | setIpv4TosBits | setIpv4SrcAddress | setIpv4DstAddress | setTransportSource | setTransportDestination | setVendorAction)): Indicates the action type associated with this Flow Range.
        - TypeOfOutPort (str(ofppManual | ofppAll | ofppController | ofppInPort | ofppLocal | ofppNormal | ofppFlood)): Specifies the Output Port Type for this Flow Range. This attribute value is applicable only when the typeOfAction selected is output
        - VendorData (str): Specifies the data of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorDataLength (number): Specifies the data length of the Vendor. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VendorId (number): Specifies the unique Vendor identifier. This attribute value is applicable only when the typeOfAction selected is setVendorAction.
        - VlanId (number): Specifies the unique VLAN Identifier for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanId.
        - VlanPriority (number): Specifies the User Priority for this VLAN. This attribute value is applicable only when the typeOfAction selected is setVlanPriority.

        Returns
        -------
        - self: This instance with matching flowRangeAction resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowRangeAction data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowRangeAction resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
