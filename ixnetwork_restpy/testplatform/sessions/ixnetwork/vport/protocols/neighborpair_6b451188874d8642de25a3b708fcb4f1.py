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


class NeighborPair(Base):
    """Represents a pair of routers-one is the DUT and the other is simulated by the Ixia protocol server. In addition to some identifying options, it holds two lists for the router: (1)  Destination Ranges-a list of routers which represent the termination point of MPLS tunnels being constructed. (2) Hello TLVs-generalized TLV messages that are included with all HELLO messages.
    The NeighborPair class encapsulates a list of neighborPair resources that are managed by the user.
    A list of resources can be retrieved from the server using the NeighborPair.find() method.
    The list can be managed by using the NeighborPair.add() and NeighborPair.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'neighborPair'
    _SDM_ATT_MAP = {
        'ActualRestartTime': 'actualRestartTime',
        'DutIp': 'dutIp',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableBundleMessageSending': 'enableBundleMessageSending',
        'EnableGracefulRestartHelperMode': 'enableGracefulRestartHelperMode',
        'EnableGracefulRestartingMode': 'enableGracefulRestartingMode',
        'EnableHello': 'enableHello',
        'Enabled': 'enabled',
        'GracefulRestartStartTime': 'gracefulRestartStartTime',
        'GracefulRestartUpTime': 'gracefulRestartUpTime',
        'HelloInterval': 'helloInterval',
        'HelloTimeoutMultiplier': 'helloTimeoutMultiplier',
        'HelloTlvs': 'helloTlvs',
        'IsAssignedInfoRefreshed': 'isAssignedInfoRefreshed',
        'IsLearnedInfoRefreshed': 'isLearnedInfoRefreshed',
        'LabelSpaceEnd': 'labelSpaceEnd',
        'LabelSpaceStart': 'labelSpaceStart',
        'NumberOfGracefulRestarts': 'numberOfGracefulRestarts',
        'OurIp': 'ourIp',
        'RecoveryTimeInterval': 'recoveryTimeInterval',
        'RefreshReduction': 'refreshReduction',
        'RestartTimeInterval': 'restartTimeInterval',
        'SummaryRefreshInterval': 'summaryRefreshInterval',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(NeighborPair, self).__init__(parent)

    @property
    def AssignedLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assignedlabel_a2327011e89aab2956f11aeecbc3b150.AssignedLabel): An instance of the AssignedLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assignedlabel_a2327011e89aab2956f11aeecbc3b150 import AssignedLabel
        return AssignedLabel(self)

    @property
    def DestinationRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.destinationrange_5c4e05197f703fbf3faa01950e5aa3de.DestinationRange): An instance of the DestinationRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.destinationrange_5c4e05197f703fbf3faa01950e5aa3de import DestinationRange
        return DestinationRange(self)

    @property
    def ReceivedLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.receivedlabel_0e6a6ca52ec19120b114d44fa8689e34.ReceivedLabel): An instance of the ReceivedLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.receivedlabel_0e6a6ca52ec19120b114d44fa8689e34 import ReceivedLabel
        return ReceivedLabel(self)

    @property
    def ActualRestartTime(self):
        """
        Returns
        -------
        - number: The time interval after which a hello packet is sent with a new Src Instance Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualRestartTime'])
    @ActualRestartTime.setter
    def ActualRestartTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActualRestartTime'], value)

    @property
    def DutIp(self):
        """
        Returns
        -------
        - str: The IP address for the device under test. This is the RSVP router that the simulated router is directly connected to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutIp'])
    @DutIp.setter
    def DutIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DutIp'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: If true, enables BFD registration with RSVP-TE.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableBundleMessageSending(self):
        """
        Returns
        -------
        - bool: If true, enables the sending of RSVP Bundle Message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBundleMessageSending'])
    @EnableBundleMessageSending.setter
    def EnableBundleMessageSending(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBundleMessageSending'], value)

    @property
    def EnableGracefulRestartHelperMode(self):
        """
        Returns
        -------
        - bool: When checked, enables the graceful restart helper mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'])
    @EnableGracefulRestartHelperMode.setter
    def EnableGracefulRestartHelperMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'], value)

    @property
    def EnableGracefulRestartingMode(self):
        """
        Returns
        -------
        - bool: When checked, enables the graceful restart restarting mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartingMode'])
    @EnableGracefulRestartingMode.setter
    def EnableGracefulRestartingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestartingMode'], value)

    @property
    def EnableHello(self):
        """
        Returns
        -------
        - bool: Enables the transmission of HELLO messages between the simulated router and the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHello'])
    @EnableHello.setter
    def EnableHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHello'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the simulated neighbor pair.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GracefulRestartStartTime(self):
        """
        Returns
        -------
        - number: The time interval after this restart timer is fired, and the neighboring nodes are restarted. During this interval the hello messages are not being sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GracefulRestartStartTime'])
    @GracefulRestartStartTime.setter
    def GracefulRestartStartTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GracefulRestartStartTime'], value)

    @property
    def GracefulRestartUpTime(self):
        """
        Returns
        -------
        - number: The configured interval for which Ixia waits before repeating the Restart cycle, after the Restarting time is over.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GracefulRestartUpTime'])
    @GracefulRestartUpTime.setter
    def GracefulRestartUpTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GracefulRestartUpTime'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: The interval, in seconds, between HELLO messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def HelloTimeoutMultiplier(self):
        """
        Returns
        -------
        - number: The number of Hellos sent without confirmation before the DUT is considered dead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloTimeoutMultiplier'])
    @HelloTimeoutMultiplier.setter
    def HelloTimeoutMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloTimeoutMultiplier'], value)

    @property
    def HelloTlvs(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): Generalized TLV messages that are included with all HELLO messages and built with the rsvpCustomTlv command.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloTlvs'])
    @HelloTlvs.setter
    def HelloTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloTlvs'], value)

    @property
    def IsAssignedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: When enabled, refreshes the assigned label info automatically.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAssignedInfoRefreshed'])

    @property
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: When enabled, refreshes the learned label info automatically.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedInfoRefreshed'])

    @property
    def LabelSpaceEnd(self):
        """
        Returns
        -------
        - number: The last label to be used for RSVP tunnels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelSpaceEnd'])
    @LabelSpaceEnd.setter
    def LabelSpaceEnd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelSpaceEnd'], value)

    @property
    def LabelSpaceStart(self):
        """
        Returns
        -------
        - number: The first label to be used for RSVP tunnels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelSpaceStart'])
    @LabelSpaceStart.setter
    def LabelSpaceStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelSpaceStart'], value)

    @property
    def NumberOfGracefulRestarts(self):
        """
        Returns
        -------
        - number: The number of times the Ixia emulated RSVP neighbor moves to Restarting/Recovering and Up states before stopping the cycle.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfGracefulRestarts'])
    @NumberOfGracefulRestarts.setter
    def NumberOfGracefulRestarts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfGracefulRestarts'], value)

    @property
    def OurIp(self):
        """
        Returns
        -------
        - str: The IP address of the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OurIp'])
    @OurIp.setter
    def OurIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OurIp'], value)

    @property
    def RecoveryTimeInterval(self):
        """
        Returns
        -------
        - number: The configured time interval for which Ixia waits for the DUT to recover the egress LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecoveryTimeInterval'])
    @RecoveryTimeInterval.setter
    def RecoveryTimeInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RecoveryTimeInterval'], value)

    @property
    def RefreshReduction(self):
        """
        Returns
        -------
        - bool: Enables or disables the feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RefreshReduction'])
    @RefreshReduction.setter
    def RefreshReduction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RefreshReduction'], value)

    @property
    def RestartTimeInterval(self):
        """
        Returns
        -------
        - number: This value along with the Recovery Time is advertised in the Hello-packets as part of a Restart-capability object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RestartTimeInterval'])
    @RestartTimeInterval.setter
    def RestartTimeInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RestartTimeInterval'], value)

    @property
    def SummaryRefreshInterval(self):
        """
        Returns
        -------
        - number: The interval between summary refresh messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SummaryRefreshInterval'])
    @SummaryRefreshInterval.setter
    def SummaryRefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SummaryRefreshInterval'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, ActualRestartTime=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartingMode=None, EnableHello=None, Enabled=None, GracefulRestartStartTime=None, GracefulRestartUpTime=None, HelloInterval=None, HelloTimeoutMultiplier=None, HelloTlvs=None, LabelSpaceEnd=None, LabelSpaceStart=None, NumberOfGracefulRestarts=None, OurIp=None, RecoveryTimeInterval=None, RefreshReduction=None, RestartTimeInterval=None, SummaryRefreshInterval=None, TrafficGroupId=None):
        """Updates neighborPair resource on the server.

        Args
        ----
        - ActualRestartTime (number): The time interval after which a hello packet is sent with a new Src Instance Id.
        - DutIp (str): The IP address for the device under test. This is the RSVP router that the simulated router is directly connected to.
        - EnableBfdRegistration (bool): If true, enables BFD registration with RSVP-TE.
        - EnableBundleMessageSending (bool): If true, enables the sending of RSVP Bundle Message.
        - EnableGracefulRestartHelperMode (bool): When checked, enables the graceful restart helper mode.
        - EnableGracefulRestartingMode (bool): When checked, enables the graceful restart restarting mode.
        - EnableHello (bool): Enables the transmission of HELLO messages between the simulated router and the DUT.
        - Enabled (bool): Enables or disables the simulated neighbor pair.
        - GracefulRestartStartTime (number): The time interval after this restart timer is fired, and the neighboring nodes are restarted. During this interval the hello messages are not being sent.
        - GracefulRestartUpTime (number): The configured interval for which Ixia waits before repeating the Restart cycle, after the Restarting time is over.
        - HelloInterval (number): The interval, in seconds, between HELLO messages.
        - HelloTimeoutMultiplier (number): The number of Hellos sent without confirmation before the DUT is considered dead.
        - HelloTlvs (list(dict(arg1:number,arg2:number,arg3:str))): Generalized TLV messages that are included with all HELLO messages and built with the rsvpCustomTlv command.
        - LabelSpaceEnd (number): The last label to be used for RSVP tunnels.
        - LabelSpaceStart (number): The first label to be used for RSVP tunnels.
        - NumberOfGracefulRestarts (number): The number of times the Ixia emulated RSVP neighbor moves to Restarting/Recovering and Up states before stopping the cycle.
        - OurIp (str): The IP address of the simulated router.
        - RecoveryTimeInterval (number): The configured time interval for which Ixia waits for the DUT to recover the egress LSPs.
        - RefreshReduction (bool): Enables or disables the feature.
        - RestartTimeInterval (number): This value along with the Recovery Time is advertised in the Hello-packets as part of a Restart-capability object.
        - SummaryRefreshInterval (number): The interval between summary refresh messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActualRestartTime=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartingMode=None, EnableHello=None, Enabled=None, GracefulRestartStartTime=None, GracefulRestartUpTime=None, HelloInterval=None, HelloTimeoutMultiplier=None, HelloTlvs=None, LabelSpaceEnd=None, LabelSpaceStart=None, NumberOfGracefulRestarts=None, OurIp=None, RecoveryTimeInterval=None, RefreshReduction=None, RestartTimeInterval=None, SummaryRefreshInterval=None, TrafficGroupId=None):
        """Adds a new neighborPair resource on the server and adds it to the container.

        Args
        ----
        - ActualRestartTime (number): The time interval after which a hello packet is sent with a new Src Instance Id.
        - DutIp (str): The IP address for the device under test. This is the RSVP router that the simulated router is directly connected to.
        - EnableBfdRegistration (bool): If true, enables BFD registration with RSVP-TE.
        - EnableBundleMessageSending (bool): If true, enables the sending of RSVP Bundle Message.
        - EnableGracefulRestartHelperMode (bool): When checked, enables the graceful restart helper mode.
        - EnableGracefulRestartingMode (bool): When checked, enables the graceful restart restarting mode.
        - EnableHello (bool): Enables the transmission of HELLO messages between the simulated router and the DUT.
        - Enabled (bool): Enables or disables the simulated neighbor pair.
        - GracefulRestartStartTime (number): The time interval after this restart timer is fired, and the neighboring nodes are restarted. During this interval the hello messages are not being sent.
        - GracefulRestartUpTime (number): The configured interval for which Ixia waits before repeating the Restart cycle, after the Restarting time is over.
        - HelloInterval (number): The interval, in seconds, between HELLO messages.
        - HelloTimeoutMultiplier (number): The number of Hellos sent without confirmation before the DUT is considered dead.
        - HelloTlvs (list(dict(arg1:number,arg2:number,arg3:str))): Generalized TLV messages that are included with all HELLO messages and built with the rsvpCustomTlv command.
        - LabelSpaceEnd (number): The last label to be used for RSVP tunnels.
        - LabelSpaceStart (number): The first label to be used for RSVP tunnels.
        - NumberOfGracefulRestarts (number): The number of times the Ixia emulated RSVP neighbor moves to Restarting/Recovering and Up states before stopping the cycle.
        - OurIp (str): The IP address of the simulated router.
        - RecoveryTimeInterval (number): The configured time interval for which Ixia waits for the DUT to recover the egress LSPs.
        - RefreshReduction (bool): Enables or disables the feature.
        - RestartTimeInterval (number): This value along with the Recovery Time is advertised in the Hello-packets as part of a Restart-capability object.
        - SummaryRefreshInterval (number): The interval between summary refresh messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved neighborPair resources using find and the newly added neighborPair resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained neighborPair resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActualRestartTime=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartingMode=None, EnableHello=None, Enabled=None, GracefulRestartStartTime=None, GracefulRestartUpTime=None, HelloInterval=None, HelloTimeoutMultiplier=None, HelloTlvs=None, IsAssignedInfoRefreshed=None, IsLearnedInfoRefreshed=None, LabelSpaceEnd=None, LabelSpaceStart=None, NumberOfGracefulRestarts=None, OurIp=None, RecoveryTimeInterval=None, RefreshReduction=None, RestartTimeInterval=None, SummaryRefreshInterval=None, TrafficGroupId=None):
        """Finds and retrieves neighborPair resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve neighborPair resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all neighborPair resources from the server.

        Args
        ----
        - ActualRestartTime (number): The time interval after which a hello packet is sent with a new Src Instance Id.
        - DutIp (str): The IP address for the device under test. This is the RSVP router that the simulated router is directly connected to.
        - EnableBfdRegistration (bool): If true, enables BFD registration with RSVP-TE.
        - EnableBundleMessageSending (bool): If true, enables the sending of RSVP Bundle Message.
        - EnableGracefulRestartHelperMode (bool): When checked, enables the graceful restart helper mode.
        - EnableGracefulRestartingMode (bool): When checked, enables the graceful restart restarting mode.
        - EnableHello (bool): Enables the transmission of HELLO messages between the simulated router and the DUT.
        - Enabled (bool): Enables or disables the simulated neighbor pair.
        - GracefulRestartStartTime (number): The time interval after this restart timer is fired, and the neighboring nodes are restarted. During this interval the hello messages are not being sent.
        - GracefulRestartUpTime (number): The configured interval for which Ixia waits before repeating the Restart cycle, after the Restarting time is over.
        - HelloInterval (number): The interval, in seconds, between HELLO messages.
        - HelloTimeoutMultiplier (number): The number of Hellos sent without confirmation before the DUT is considered dead.
        - HelloTlvs (list(dict(arg1:number,arg2:number,arg3:str))): Generalized TLV messages that are included with all HELLO messages and built with the rsvpCustomTlv command.
        - IsAssignedInfoRefreshed (bool): When enabled, refreshes the assigned label info automatically.
        - IsLearnedInfoRefreshed (bool): When enabled, refreshes the learned label info automatically.
        - LabelSpaceEnd (number): The last label to be used for RSVP tunnels.
        - LabelSpaceStart (number): The first label to be used for RSVP tunnels.
        - NumberOfGracefulRestarts (number): The number of times the Ixia emulated RSVP neighbor moves to Restarting/Recovering and Up states before stopping the cycle.
        - OurIp (str): The IP address of the simulated router.
        - RecoveryTimeInterval (number): The configured time interval for which Ixia waits for the DUT to recover the egress LSPs.
        - RefreshReduction (bool): Enables or disables the feature.
        - RestartTimeInterval (number): This value along with the Recovery Time is advertised in the Hello-packets as part of a Restart-capability object.
        - SummaryRefreshInterval (number): The interval between summary refresh messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching neighborPair resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of neighborPair data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the neighborPair resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshAssignedLabelInfo(self):
        """Executes the refreshAssignedLabelInfo operation on the server.

        This exec refreshes the RSVP assigned label information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshAssignedLabelInfo', payload=payload, response_object=None)

    def RefreshReceivedLabelInfo(self):
        """Executes the refreshReceivedLabelInfo operation on the server.

        This exec refreshes the RSVP received label information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshReceivedLabelInfo', payload=payload, response_object=None)

    def RestartNeighbor(self):
        """Executes the restartNeighbor operation on the server.

        This command restarts the specifed RSVP neighbor.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('restartNeighbor', payload=payload, response_object=None)
