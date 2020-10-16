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


class EapoUdpGlobals(Base):
    """
    The EapoUdpGlobals class encapsulates a list of eapoUdpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the EapoUdpGlobals.find() method.
    The list can be managed by using the EapoUdpGlobals.add() and EapoUdpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'eapoUdpGlobals'
    _SDM_ATT_MAP = {
        'ChangeStatusQuery': 'changeStatusQuery',
        'CookieSize': 'cookieSize',
        'FragmentSize': 'fragmentSize',
        'MaxClientsPerSecond': 'maxClientsPerSecond',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'Port': 'port',
        'Timeout': 'timeout',
        'TriggerCount': 'triggerCount',
        'TriggerOrigin': 'triggerOrigin',
        'TriggerType': 'triggerType',
        'WaitBeforeRun': 'waitBeforeRun',
        'WaitForCompletion': 'waitForCompletion',
    }

    def __init__(self, parent):
        super(EapoUdpGlobals, self).__init__(parent)

    @property
    def CertInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.certinfo.certinfo.CertInfo): An instance of the CertInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.certinfo.certinfo import CertInfo
        return CertInfo(self)._select()

    @property
    def NacSettings(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nacsettings.NacSettings): An instance of the NacSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nacsettings import NacSettings
        return NacSettings(self)._select()

    @property
    def ChangeStatusQuery(self):
        """
        Returns
        -------
        - number: After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChangeStatusQuery'])
    @ChangeStatusQuery.setter
    def ChangeStatusQuery(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChangeStatusQuery'], value)

    @property
    def CookieSize(self):
        """
        Returns
        -------
        - number: The size of the cookie we send.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CookieSize'])
    @CookieSize.setter
    def CookieSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CookieSize'], value)

    @property
    def FragmentSize(self):
        """
        Returns
        -------
        - number: Size of the frame sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FragmentSize'])
    @FragmentSize.setter
    def FragmentSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FragmentSize'], value)

    @property
    def MaxClientsPerSecond(self):
        """
        Returns
        -------
        - number: The number of interfaces to setup per second. Zero value means maximum with no limit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxClientsPerSecond'])
    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxClientsPerSecond'], value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'])
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Port(self):
        """
        Returns
        -------
        - number: Port on which we start listening for UDP messages for this plugin.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Port'])
    @Port.setter
    def Port(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Port'], value)

    @property
    def Timeout(self):
        """
        Returns
        -------
        - number: After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Timeout'])
    @Timeout.setter
    def Timeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Timeout'], value)

    @property
    def TriggerCount(self):
        """
        Returns
        -------
        - number: How many triggers are sent when a client is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerCount'])
    @TriggerCount.setter
    def TriggerCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerCount'], value)

    @property
    def TriggerOrigin(self):
        """
        Returns
        -------
        - str: The trigger source can be external (outside port) or internal (another plugin or application).
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerOrigin'])
    @TriggerOrigin.setter
    def TriggerOrigin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerOrigin'], value)

    @property
    def TriggerType(self):
        """
        Returns
        -------
        - str: Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerType'])
    @TriggerType.setter
    def TriggerType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerType'], value)

    @property
    def WaitBeforeRun(self):
        """
        Returns
        -------
        - number: Time to wait before running this protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitBeforeRun'])
    @WaitBeforeRun.setter
    def WaitBeforeRun(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WaitBeforeRun'], value)

    @property
    def WaitForCompletion(self):
        """
        Returns
        -------
        - bool: If true the configuration will end after all interfaces are configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitForCompletion'])
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WaitForCompletion'], value)

    def update(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Updates eapoUdpGlobals resource on the server.

        Args
        ----
        - ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
        - CookieSize (number): The size of the cookie we send.
        - FragmentSize (number): Size of the frame sent.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - Port (number): Port on which we start listening for UDP messages for this plugin.
        - Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
        - TriggerCount (number): How many triggers are sent when a client is started.
        - TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
        - TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Adds a new eapoUdpGlobals resource on the server and adds it to the container.

        Args
        ----
        - ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
        - CookieSize (number): The size of the cookie we send.
        - FragmentSize (number): Size of the frame sent.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - Port (number): Port on which we start listening for UDP messages for this plugin.
        - Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
        - TriggerCount (number): How many triggers are sent when a client is started.
        - TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
        - TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns
        -------
        - self: This instance with all currently retrieved eapoUdpGlobals resources using find and the newly added eapoUdpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained eapoUdpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, ObjectId=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Finds and retrieves eapoUdpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eapoUdpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eapoUdpGlobals resources from the server.

        Args
        ----
        - ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
        - CookieSize (number): The size of the cookie we send.
        - FragmentSize (number): Size of the frame sent.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - ObjectId (str): Unique identifier for this object
        - Port (number): Port on which we start listening for UDP messages for this plugin.
        - Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
        - TriggerCount (number): How many triggers are sent when a client is started.
        - TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
        - TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns
        -------
        - self: This instance with matching eapoUdpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eapoUdpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eapoUdpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
