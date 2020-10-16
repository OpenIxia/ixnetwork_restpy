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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class SbfdInitiator(Base):
    """
    The SbfdInitiator class encapsulates a required sbfdInitiator resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'sbfdInitiator'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestIPAddr': 'destIPAddr',
        'MplsLabelCount': 'mplsLabelCount',
        'MyDiscriminator': 'myDiscriminator',
        'Name': 'name',
        'PeerDiscriminator': 'peerDiscriminator',
        'SessionInfo': 'sessionInfo',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TxInterval': 'txInterval',
    }

    def __init__(self, parent):
        super(SbfdInitiator, self).__init__(parent)

    @property
    def MplsLabelList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.mplslabellist_37213b54082ea2315b262cbc86661827.MplsLabelList): An instance of the MplsLabelList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.mplslabellist_37213b54082ea2315b262cbc86661827 import MplsLabelList
        return MplsLabelList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DestIPAddr(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Destination IP address in SBFD Packet,which is sent to Responder. Should be in 127 subnet as defined in specification.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestIPAddr']))

    @property
    def MplsLabelCount(self):
        """
        Returns
        -------
        - number: Number of MPLS Labels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsLabelCount'])
    @MplsLabelCount.setter
    def MplsLabelCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsLabelCount'], value)

    @property
    def MyDiscriminator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The value to be used for My Discriminator in S-BFD packets sent to the Responder by this Initiator. Should be unique in sessions from a single Initiator.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MyDiscriminator']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PeerDiscriminator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configured Peer Discriminator which should match the configured Local or My Discriminator on the target Responder.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerDiscriminator']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[adminDown | down | up]): Current state of the S-BFD Initiator Session. It is normally Up or Down depending on whether Responder is responding correctly or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If packets are not recieved within the negotiated transmit Interval * this value , session is brought down and Flap Count is increased in statistics.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    @property
    def TxInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tx Interval in Milli Seconds. Note: Initial transmission interval is set to maximum of 1s and configured Tx Interval. Once session comes up, the timer will auto-transition to the negotiated value i.e. maximum of local Tx Interval and recieved Rx Interval from Responder.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxInterval']))

    def update(self, MplsLabelCount=None, Name=None):
        """Updates sbfdInitiator resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - MplsLabelCount (number): Number of MPLS Labels.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, DestIPAddr=None, MyDiscriminator=None, PeerDiscriminator=None, TimeoutMultiplier=None, TxInterval=None):
        """Base class infrastructure that gets a list of sbfdInitiator device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - DestIPAddr (str): optional regex of destIPAddr
        - MyDiscriminator (str): optional regex of myDiscriminator
        - PeerDiscriminator (str): optional regex of peerDiscriminator
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier
        - TxInterval (str): optional regex of txInterval

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
