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


class Source(Base):
    """A set of register addresses to be included in this interface.
    The Source class encapsulates a list of source resources that are managed by the user.
    A list of resources can be retrieved from the server using the Source.find() method.
    The list can be managed by using the Source.add() and Source.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'source'

    def __init__(self, parent):
        super(Source, self).__init__(parent)

    @property
    def LearnedSgState(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedsgstate_22f05535b079eacdfa9fbf735a92387f.LearnedSgState): An instance of the LearnedSgState class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedsgstate_22f05535b079eacdfa9fbf735a92387f import LearnedSgState
        return LearnedSgState(self)

    @property
    def DiscardSgJoinStates(self):
        """
        Returns
        -------
        - bool: If enabled, the learned join states sent by the RP (DUT) in response to this specific register message will be discarded.
        """
        return self._get_attribute('discardSgJoinStates')
    @DiscardSgJoinStates.setter
    def DiscardSgJoinStates(self, value):
        self._set_attribute('discardSgJoinStates', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this source entry for use in PIM-SM register messages.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 multicast group address in the range of group addresses included in this register message.
        """
        return self._get_attribute('groupAddress')
    @GroupAddress.setter
    def GroupAddress(self, value):
        self._set_attribute('groupAddress', value)

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - number: The number of group addresses to be included in this register message.
        """
        return self._get_attribute('groupCount')
    @GroupCount.setter
    def GroupCount(self, value):
        self._set_attribute('groupCount', value)

    @property
    def GroupMappingMode(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): Controls the mapping from sources to groups during advertisement.
        """
        return self._get_attribute('groupMappingMode')
    @GroupMappingMode.setter
    def GroupMappingMode(self, value):
        self._set_attribute('groupMappingMode', value)

    @property
    def GroupMaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask used with the group address.
        """
        return self._get_attribute('groupMaskWidth')
    @GroupMaskWidth.setter
    def GroupMaskWidth(self, value):
        self._set_attribute('groupMaskWidth', value)

    @property
    def MulticastDataLength(self):
        """
        Returns
        -------
        - number: The length of the multicast data, in bytes.
        """
        return self._get_attribute('multicastDataLength')
    @MulticastDataLength.setter
    def MulticastDataLength(self, value):
        self._set_attribute('multicastDataLength', value)

    @property
    def RegisterProbeTime(self):
        """
        Returns
        -------
        - number: Part of the register-stop timer (RST (S,G). Used to control the time intervals for the transmission of null-register messages from the source's DR to the RP. Prior to expiration of the register suppression time of the RST, a null-register message is sent to probe the RP, as a reminder to the RP to send a new register-stop message and maintain the state. If the RP does not respond with a new register-stop message, the source's DR will start sending register-encapsulated data again. The default is 5 seconds.Note: This value must be less than half of the register suppression time value.
        """
        return self._get_attribute('registerProbeTime')
    @RegisterProbeTime.setter
    def RegisterProbeTime(self, value):
        self._set_attribute('registerProbeTime', value)

    @property
    def RpAddress(self):
        """
        Returns
        -------
        - str: The IP address of the rendezvous point (RP) router - the root of the RPT (rendezvous point tree).
        """
        return self._get_attribute('rpAddress')
    @RpAddress.setter
    def RpAddress(self, value):
        self._set_attribute('rpAddress', value)

    @property
    def SendNullRegAtBegin(self):
        """
        Returns
        -------
        - bool: If checked, a null register packet will be sent by the Ixia-emulated designated router (DR)/source range to the RP to start the message exchange. (A null register packet contains no data.)
        """
        return self._get_attribute('sendNullRegAtBegin')
    @SendNullRegAtBegin.setter
    def SendNullRegAtBegin(self, value):
        self._set_attribute('sendNullRegAtBegin', value)

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 source address to be included in this register message. (IPv4 Multicast addresses are not valid for sources.)
        """
        return self._get_attribute('sourceAddress')
    @SourceAddress.setter
    def SourceAddress(self, value):
        self._set_attribute('sourceAddress', value)

    @property
    def SourceCount(self):
        """
        Returns
        -------
        - number: The number of source addresses to be included in the register message.
        """
        return self._get_attribute('sourceCount')
    @SourceCount.setter
    def SourceCount(self, value):
        self._set_attribute('sourceCount', value)

    @property
    def SuppressionTime(self):
        """
        Returns
        -------
        - number: Part of the register-stop timer (RST (S,G). The amount of time, following receipt of a register-stop message, that the DR will NOT send register-encapsulated data to the rendezvous point (RP).
        """
        return self._get_attribute('suppressionTime')
    @SuppressionTime.setter
    def SuppressionTime(self, value):
        self._set_attribute('suppressionTime', value)

    @property
    def SwitchOverInterval(self):
        """
        Returns
        -------
        - number: The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.
        """
        return self._get_attribute('switchOverInterval')
    @SwitchOverInterval.setter
    def SwitchOverInterval(self, value):
        self._set_attribute('switchOverInterval', value)

    @property
    def TxIterationGap(self):
        """
        Returns
        -------
        - number: The gap between each iteration of the register range (in milliseconds) . The default is 60,000 ms (= 60 seconds). (Does not apply to NULL Registers, which contain no data.)
        """
        return self._get_attribute('txIterationGap')
    @TxIterationGap.setter
    def TxIterationGap(self, value):
        self._set_attribute('txIterationGap', value)

    @property
    def UdpDstPort(self):
        """
        Returns
        -------
        - number: The number of UDP destination ports in the receiving multicast group.The default is 3000 UDP destination ports.
        """
        return self._get_attribute('udpDstPort')
    @UdpDstPort.setter
    def UdpDstPort(self, value):
        self._set_attribute('udpDstPort', value)

    @property
    def UdpSrcPort(self):
        """
        Returns
        -------
        - number: The number of UDP source ports sending encapsulated UDP packets to multicast groups (via register messages to the RP). The default is 3000 UDP source ports.
        """
        return self._get_attribute('udpSrcPort')
    @UdpSrcPort.setter
    def UdpSrcPort(self, value):
        self._set_attribute('udpSrcPort', value)

    def update(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Updates source resource on the server.

        Args
        ----
        - DiscardSgJoinStates (bool): If enabled, the learned join states sent by the RP (DUT) in response to this specific register message will be discarded.
        - Enabled (bool): Enables this source entry for use in PIM-SM register messages.
        - GroupAddress (str): The first IPv4 or IPv6 multicast group address in the range of group addresses included in this register message.
        - GroupCount (number): The number of group addresses to be included in this register message.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Controls the mapping from sources to groups during advertisement.
        - GroupMaskWidth (number): The number of bits in the network mask used with the group address.
        - MulticastDataLength (number): The length of the multicast data, in bytes.
        - RegisterProbeTime (number): Part of the register-stop timer (RST (S,G). Used to control the time intervals for the transmission of null-register messages from the source's DR to the RP. Prior to expiration of the register suppression time of the RST, a null-register message is sent to probe the RP, as a reminder to the RP to send a new register-stop message and maintain the state. If the RP does not respond with a new register-stop message, the source's DR will start sending register-encapsulated data again. The default is 5 seconds.Note: This value must be less than half of the register suppression time value.
        - RpAddress (str): The IP address of the rendezvous point (RP) router - the root of the RPT (rendezvous point tree).
        - SendNullRegAtBegin (bool): If checked, a null register packet will be sent by the Ixia-emulated designated router (DR)/source range to the RP to start the message exchange. (A null register packet contains no data.)
        - SourceAddress (str): The first IPv4 or IPv6 source address to be included in this register message. (IPv4 Multicast addresses are not valid for sources.)
        - SourceCount (number): The number of source addresses to be included in the register message.
        - SuppressionTime (number): Part of the register-stop timer (RST (S,G). The amount of time, following receipt of a register-stop message, that the DR will NOT send register-encapsulated data to the rendezvous point (RP).
        - SwitchOverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.
        - TxIterationGap (number): The gap between each iteration of the register range (in milliseconds) . The default is 60,000 ms (= 60 seconds). (Does not apply to NULL Registers, which contain no data.)
        - UdpDstPort (number): The number of UDP destination ports in the receiving multicast group.The default is 3000 UDP destination ports.
        - UdpSrcPort (number): The number of UDP source ports sending encapsulated UDP packets to multicast groups (via register messages to the RP). The default is 3000 UDP source ports.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Adds a new source resource on the server and adds it to the container.

        Args
        ----
        - DiscardSgJoinStates (bool): If enabled, the learned join states sent by the RP (DUT) in response to this specific register message will be discarded.
        - Enabled (bool): Enables this source entry for use in PIM-SM register messages.
        - GroupAddress (str): The first IPv4 or IPv6 multicast group address in the range of group addresses included in this register message.
        - GroupCount (number): The number of group addresses to be included in this register message.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Controls the mapping from sources to groups during advertisement.
        - GroupMaskWidth (number): The number of bits in the network mask used with the group address.
        - MulticastDataLength (number): The length of the multicast data, in bytes.
        - RegisterProbeTime (number): Part of the register-stop timer (RST (S,G). Used to control the time intervals for the transmission of null-register messages from the source's DR to the RP. Prior to expiration of the register suppression time of the RST, a null-register message is sent to probe the RP, as a reminder to the RP to send a new register-stop message and maintain the state. If the RP does not respond with a new register-stop message, the source's DR will start sending register-encapsulated data again. The default is 5 seconds.Note: This value must be less than half of the register suppression time value.
        - RpAddress (str): The IP address of the rendezvous point (RP) router - the root of the RPT (rendezvous point tree).
        - SendNullRegAtBegin (bool): If checked, a null register packet will be sent by the Ixia-emulated designated router (DR)/source range to the RP to start the message exchange. (A null register packet contains no data.)
        - SourceAddress (str): The first IPv4 or IPv6 source address to be included in this register message. (IPv4 Multicast addresses are not valid for sources.)
        - SourceCount (number): The number of source addresses to be included in the register message.
        - SuppressionTime (number): Part of the register-stop timer (RST (S,G). The amount of time, following receipt of a register-stop message, that the DR will NOT send register-encapsulated data to the rendezvous point (RP).
        - SwitchOverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.
        - TxIterationGap (number): The gap between each iteration of the register range (in milliseconds) . The default is 60,000 ms (= 60 seconds). (Does not apply to NULL Registers, which contain no data.)
        - UdpDstPort (number): The number of UDP destination ports in the receiving multicast group.The default is 3000 UDP destination ports.
        - UdpSrcPort (number): The number of UDP source ports sending encapsulated UDP packets to multicast groups (via register messages to the RP). The default is 3000 UDP source ports.

        Returns
        -------
        - self: This instance with all currently retrieved source resources using find and the newly added source resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained source resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscardSgJoinStates=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMappingMode=None, GroupMaskWidth=None, MulticastDataLength=None, RegisterProbeTime=None, RpAddress=None, SendNullRegAtBegin=None, SourceAddress=None, SourceCount=None, SuppressionTime=None, SwitchOverInterval=None, TxIterationGap=None, UdpDstPort=None, UdpSrcPort=None):
        """Finds and retrieves source resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve source resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all source resources from the server.

        Args
        ----
        - DiscardSgJoinStates (bool): If enabled, the learned join states sent by the RP (DUT) in response to this specific register message will be discarded.
        - Enabled (bool): Enables this source entry for use in PIM-SM register messages.
        - GroupAddress (str): The first IPv4 or IPv6 multicast group address in the range of group addresses included in this register message.
        - GroupCount (number): The number of group addresses to be included in this register message.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Controls the mapping from sources to groups during advertisement.
        - GroupMaskWidth (number): The number of bits in the network mask used with the group address.
        - MulticastDataLength (number): The length of the multicast data, in bytes.
        - RegisterProbeTime (number): Part of the register-stop timer (RST (S,G). Used to control the time intervals for the transmission of null-register messages from the source's DR to the RP. Prior to expiration of the register suppression time of the RST, a null-register message is sent to probe the RP, as a reminder to the RP to send a new register-stop message and maintain the state. If the RP does not respond with a new register-stop message, the source's DR will start sending register-encapsulated data again. The default is 5 seconds.Note: This value must be less than half of the register suppression time value.
        - RpAddress (str): The IP address of the rendezvous point (RP) router - the root of the RPT (rendezvous point tree).
        - SendNullRegAtBegin (bool): If checked, a null register packet will be sent by the Ixia-emulated designated router (DR)/source range to the RP to start the message exchange. (A null register packet contains no data.)
        - SourceAddress (str): The first IPv4 or IPv6 source address to be included in this register message. (IPv4 Multicast addresses are not valid for sources.)
        - SourceCount (number): The number of source addresses to be included in the register message.
        - SuppressionTime (number): Part of the register-stop timer (RST (S,G). The amount of time, following receipt of a register-stop message, that the DR will NOT send register-encapsulated data to the rendezvous point (RP).
        - SwitchOverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.
        - TxIterationGap (number): The gap between each iteration of the register range (in milliseconds) . The default is 60,000 ms (= 60 seconds). (Does not apply to NULL Registers, which contain no data.)
        - UdpDstPort (number): The number of UDP destination ports in the receiving multicast group.The default is 3000 UDP destination ports.
        - UdpSrcPort (number): The number of UDP source ports sending encapsulated UDP packets to multicast groups (via register messages to the RP). The default is 3000 UDP source ports.

        Returns
        -------
        - self: This instance with matching source resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of source data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the source resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
