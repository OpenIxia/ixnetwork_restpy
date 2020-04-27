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


class EgtpClientGlobals(Base):
    """
    The EgtpClientGlobals class encapsulates a list of egtpClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the EgtpClientGlobals.find() method.
    The list can be managed by using the EgtpClientGlobals.add() and EgtpClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpClientGlobals'

    def __init__(self, parent):
        super(EgtpClientGlobals, self).__init__(parent)

    @property
    def EnableDynamicQosCtrl(self):
        """
        Returns
        -------
        - bool: Enable Dynamic QoS Enforcement
        """
        return self._get_attribute('enableDynamicQosCtrl')
    @EnableDynamicQosCtrl.setter
    def EnableDynamicQosCtrl(self, value):
        self._set_attribute('enableDynamicQosCtrl', value)

    @property
    def EnableGatewayArp(self):
        """
        Returns
        -------
        - bool: When enabled, every IP address will ARP the specified gateway.
        """
        return self._get_attribute('enableGatewayArp')
    @EnableGatewayArp.setter
    def EnableGatewayArp(self, value):
        self._set_attribute('enableGatewayArp', value)

    @property
    def EnablePartialNegotiation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enablePartialNegotiation')
    @EnablePartialNegotiation.setter
    def EnablePartialNegotiation(self, value):
        self._set_attribute('enablePartialNegotiation', value)

    @property
    def GatewayArpRequestRate(self):
        """
        Returns
        -------
        - number: Maximum ARP request rate
        """
        return self._get_attribute('gatewayArpRequestRate')
    @GatewayArpRequestRate.setter
    def GatewayArpRequestRate(self, value):
        self._set_attribute('gatewayArpRequestRate', value)

    @property
    def MaxMbrUAndD(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('maxMbrUAndD')
    @MaxMbrUAndD.setter
    def MaxMbrUAndD(self, value):
        self._set_attribute('maxMbrUAndD', value)

    @property
    def MaxOutstandingGatewayArpRequests(self):
        """
        Returns
        -------
        - number: Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
        """
        return self._get_attribute('maxOutstandingGatewayArpRequests')
    @MaxOutstandingGatewayArpRequests.setter
    def MaxOutstandingGatewayArpRequests(self, value):
        self._set_attribute('maxOutstandingGatewayArpRequests', value)

    @property
    def MaxOutstandingReleases(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def SendOneArpFromEachInterface(self):
        """
        Returns
        -------
        - bool: When set, each interface will send one ARP request.
        """
        return self._get_attribute('sendOneArpFromEachInterface')
    @SendOneArpFromEachInterface.setter
    def SendOneArpFromEachInterface(self, value):
        self._set_attribute('sendOneArpFromEachInterface', value)

    @property
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: Initial setup rate
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def TeardownRateInitial(self):
        """
        Returns
        -------
        - number: Initial teardown rate
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    @property
    def TsSpec(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('tsSpec')
    @TsSpec.setter
    def TsSpec(self, value):
        self._set_attribute('tsSpec', value)

    @property
    def UseMaxRatesForDcp(self):
        """
        Returns
        -------
        - bool: Use default rates (DCP mode)
        """
        return self._get_attribute('useMaxRatesForDcp')
    @UseMaxRatesForDcp.setter
    def UseMaxRatesForDcp(self, value):
        self._set_attribute('useMaxRatesForDcp', value)

    def update(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Updates egtpClientGlobals resource on the server.

        Args
        ----
        - EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
        - EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
        - EnablePartialNegotiation (bool): 
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - MaxMbrUAndD (number): 
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
        - MaxOutstandingReleases (number): 
        - MaxOutstandingRequests (number): 
        - SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate
        - TsSpec (str): 
        - UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Adds a new egtpClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
        - EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
        - EnablePartialNegotiation (bool): 
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - MaxMbrUAndD (number): 
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
        - MaxOutstandingReleases (number): 
        - MaxOutstandingRequests (number): 
        - SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate
        - TsSpec (str): 
        - UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Returns
        -------
        - self: This instance with all currently retrieved egtpClientGlobals resources using find and the newly added egtpClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained egtpClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableDynamicQosCtrl=None, EnableGatewayArp=None, EnablePartialNegotiation=None, GatewayArpRequestRate=None, MaxMbrUAndD=None, MaxOutstandingGatewayArpRequests=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, SendOneArpFromEachInterface=None, SetupRateInitial=None, TeardownRateInitial=None, TsSpec=None, UseMaxRatesForDcp=None):
        """Finds and retrieves egtpClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpClientGlobals resources from the server.

        Args
        ----
        - EnableDynamicQosCtrl (bool): Enable Dynamic QoS Enforcement
        - EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
        - EnablePartialNegotiation (bool): 
        - GatewayArpRequestRate (number): Maximum ARP request rate
        - MaxMbrUAndD (number): 
        - MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
        - MaxOutstandingReleases (number): 
        - MaxOutstandingRequests (number): 
        - ObjectId (str): Unique identifier for this object
        - SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate
        - TsSpec (str): 
        - UseMaxRatesForDcp (bool): Use default rates (DCP mode)

        Returns
        -------
        - self: This instance with matching egtpClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of egtpClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
