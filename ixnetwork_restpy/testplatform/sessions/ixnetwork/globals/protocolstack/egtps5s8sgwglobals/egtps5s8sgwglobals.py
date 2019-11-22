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


class EgtpS5S8SgwGlobals(Base):
    """
    The EgtpS5S8SgwGlobals class encapsulates a list of egtpS5S8SgwGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the EgtpS5S8SgwGlobals.find() method.
    The list can be managed by the user by using the EgtpS5S8SgwGlobals.add() and EgtpS5S8SgwGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpS5S8SgwGlobals'

    def __init__(self, parent):
        super(EgtpS5S8SgwGlobals, self).__init__(parent)

    @property
    def GlobalEgtpApnS5S8(self):
        """An instance of the GlobalEgtpApnS5S8 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.globalegtpapns5s8.globalegtpapns5s8.GlobalEgtpApnS5S8)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.globalegtpapns5s8.globalegtpapns5s8 import GlobalEgtpApnS5S8
        return GlobalEgtpApnS5S8(self)

    @property
    def GlobalTrafficProfileS5S8(self):
        """An instance of the GlobalTrafficProfileS5S8 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.globaltrafficprofiles5s8.globaltrafficprofiles5s8.GlobalTrafficProfileS5S8)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.globaltrafficprofiles5s8.globaltrafficprofiles5s8 import GlobalTrafficProfileS5S8
        return GlobalTrafficProfileS5S8(self)

    @property
    def EnableDynamicQosCtrl(self):
        """Enable Dynamic QoS Enforcement

        Returns:
            bool
        """
        return self._get_attribute('enableDynamicQosCtrl')
    @EnableDynamicQosCtrl.setter
    def EnableDynamicQosCtrl(self, value):
        self._set_attribute('enableDynamicQosCtrl', value)

    @property
    def EnableGatewayArp(self):
        """When enabled, every IP address will ARP the specified gateway.

        Returns:
            bool
        """
        return self._get_attribute('enableGatewayArp')
    @EnableGatewayArp.setter
    def EnableGatewayArp(self, value):
        self._set_attribute('enableGatewayArp', value)

    @property
    def EnablePartialNegotiation(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('enablePartialNegotiation')
    @EnablePartialNegotiation.setter
    def EnablePartialNegotiation(self, value):
        self._set_attribute('enablePartialNegotiation', value)

    @property
    def GatewayArpRequestRate(self):
        """Maximum ARP request rate

        Returns:
            number
        """
        return self._get_attribute('gatewayArpRequestRate')
    @GatewayArpRequestRate.setter
    def GatewayArpRequestRate(self, value):
        self._set_attribute('gatewayArpRequestRate', value)

    @property
    def MaxMbrUAndD(self):
        """

        Returns:
            number
        """
        return self._get_attribute('maxMbrUAndD')
    @MaxMbrUAndD.setter
    def MaxMbrUAndD(self, value):
        self._set_attribute('maxMbrUAndD', value)

    @property
    def MaxOutstandingGatewayArpRequests(self):
        """Threshold at which the plugin begins throttling back the number of new ARP requests sent out.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingGatewayArpRequests')
    @MaxOutstandingGatewayArpRequests.setter
    def MaxOutstandingGatewayArpRequests(self, value):
        self._set_attribute('maxOutstandingGatewayArpRequests', value)

    @property
    def MaxOutstandingReleases(self):
        """

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SendOneArpFromEachInterface(self):
        """When set, each interface will send one ARP request.

        Returns:
            bool
        """
        return self._get_attribute('sendOneArpFromEachInterface')
    @SendOneArpFromEachInterface.setter
    def SendOneArpFromEachInterface(self, value):
        self._set_attribute('sendOneArpFromEachInterface', value)

    @property
    def SetupRateInitial(self):
        """Initial setup rate

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def TeardownRateInitial(self):
        """Initial teardown rate

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    @property
    def TsSpec(self):
        """

        Returns:
            str
        """
        return self._get_attribute('tsSpec')
    @TsSpec.setter
    def TsSpec(self, value):
        self._set_attribute('tsSpec', value)

    @property
    def UseMaxRatesForDcp(self):
        """Use default rates (DCP mode)

        Returns:
            bool
        """
        return self._get_attribute('useMaxRatesForDcp')
    @UseMaxRatesForDcp.setter
    def UseMaxRatesForDcp(self, value):
        self._set_attribute('useMaxRatesForDcp', value)

    def update(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Updates a child instance of egtpS5S8SgwGlobals on the server.

        Args:
            EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            EnablePartialNegotiation (bool): 
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxMbrUAndD (number): 
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            MaxOutstandingReleases (number): 
            MaxOutstandingRequests (number): 
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate
            TsSpec (str): 
            UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Adds a new egtpS5S8SgwGlobals node on the server and retrieves it in this instance.

        Args:
            EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            EnablePartialNegotiation (bool): 
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxMbrUAndD (number): 
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            MaxOutstandingReleases (number): 
            MaxOutstandingRequests (number): 
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate
            TsSpec (str): 
            UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Returns:
            self: This instance with all currently retrieved egtpS5S8SgwGlobals data using find and the newly added egtpS5S8SgwGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the egtpS5S8SgwGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Finds and retrieves egtpS5S8SgwGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve egtpS5S8SgwGlobals data from the server.
        By default the find method takes no parameters and will retrieve all egtpS5S8SgwGlobals data from the server.

        Args:
            EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            EnablePartialNegotiation (bool): 
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxMbrUAndD (number): 
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            MaxOutstandingReleases (number): 
            MaxOutstandingRequests (number): 
            ObjectId (str): Unique identifier for this object
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate
            TsSpec (str): 
            UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Returns:
            self: This instance with matching egtpS5S8SgwGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of egtpS5S8SgwGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the egtpS5S8SgwGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
