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


class FcoeClientGlobals(Base):
    """StackManager FCoE Global Settings
    The FcoeClientGlobals class encapsulates a list of fcoeClientGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the FcoeClientGlobals.find() method.
    The list can be managed by the user by using the FcoeClientGlobals.add() and FcoeClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeClientGlobals'

    def __init__(self, parent):
        super(FcoeClientGlobals, self).__init__(parent)

    @property
    def FcoeClientOptionSet(self):
        """An instance of the FcoeClientOptionSet class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptionset.FcoeClientOptionSet)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptionset import FcoeClientOptionSet
        return FcoeClientOptionSet(self)

    @property
    def AcceptPartialConfig(self):
        """This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.

        Returns:
            bool
        """
        return self._get_attribute('acceptPartialConfig')
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute('acceptPartialConfig', value)

    @property
    def B2bRxSize(self):
        """The buffer-to-buffer receive data field size in bytes.

        Returns:
            number
        """
        return self._get_attribute('b2bRxSize')
    @B2bRxSize.setter
    def B2bRxSize(self, value):
        self._set_attribute('b2bRxSize', value)

    @property
    def DcbxTimeout(self):
        """The number of seconds to wait for DCBX to negotiate.

        Returns:
            number
        """
        return self._get_attribute('dcbxTimeout')
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute('dcbxTimeout', value)

    @property
    def FipAdvertisementPeriod(self):
        """The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.

        Returns:
            number
        """
        return self._get_attribute('fipAdvertisementPeriod')
    @FipAdvertisementPeriod.setter
    def FipAdvertisementPeriod(self, value):
        self._set_attribute('fipAdvertisementPeriod', value)

    @property
    def FipFcfMacListCollection(self):
        """Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.

        Returns:
            bool
        """
        return self._get_attribute('fipFcfMacListCollection')
    @FipFcfMacListCollection.setter
    def FipFcfMacListCollection(self, value):
        self._set_attribute('fipFcfMacListCollection', value)

    @property
    def FipFcfMacListCollectionInterval(self):
        """The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.

        Returns:
            number
        """
        return self._get_attribute('fipFcfMacListCollectionInterval')
    @FipFcfMacListCollectionInterval.setter
    def FipFcfMacListCollectionInterval(self, value):
        self._set_attribute('fipFcfMacListCollectionInterval', value)

    @property
    def FipOverrideAdvertisementPeriod(self):
        """If enabled, the Discovery Advertisement period will be specified by the application.

        Returns:
            bool
        """
        return self._get_attribute('fipOverrideAdvertisementPeriod')
    @FipOverrideAdvertisementPeriod.setter
    def FipOverrideAdvertisementPeriod(self, value):
        self._set_attribute('fipOverrideAdvertisementPeriod', value)

    @property
    def FipOverrideVnportKeepAlivePeriod(self):
        """If enabled, the VN_Port Keep-Alive period will be specified by the application.

        Returns:
            bool
        """
        return self._get_attribute('fipOverrideVnportKeepAlivePeriod')
    @FipOverrideVnportKeepAlivePeriod.setter
    def FipOverrideVnportKeepAlivePeriod(self, value):
        self._set_attribute('fipOverrideVnportKeepAlivePeriod', value)

    @property
    def FipProposeMacInFpma(self):
        """Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.

        Returns:
            bool
        """
        return self._get_attribute('fipProposeMacInFpma')
    @FipProposeMacInFpma.setter
    def FipProposeMacInFpma(self, value):
        self._set_attribute('fipProposeMacInFpma', value)

    @property
    def FipResetDiscovery(self):
        """Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.

        Returns:
            bool
        """
        return self._get_attribute('fipResetDiscovery')
    @FipResetDiscovery.setter
    def FipResetDiscovery(self, value):
        self._set_attribute('fipResetDiscovery', value)

    @property
    def FipResetNumRetry(self):
        """The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.

        Returns:
            number
        """
        return self._get_attribute('fipResetNumRetry')
    @FipResetNumRetry.setter
    def FipResetNumRetry(self, value):
        self._set_attribute('fipResetNumRetry', value)

    @property
    def FipRestartOnSessionDown(self):
        """If enabled, the port will restart FIP negotiation when the session goes down.

        Returns:
            bool
        """
        return self._get_attribute('fipRestartOnSessionDown')
    @FipRestartOnSessionDown.setter
    def FipRestartOnSessionDown(self, value):
        self._set_attribute('fipRestartOnSessionDown', value)

    @property
    def FipSendKeepAlives(self):
        """If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.

        Returns:
            bool
        """
        return self._get_attribute('fipSendKeepAlives')
    @FipSendKeepAlives.setter
    def FipSendKeepAlives(self, value):
        self._set_attribute('fipSendKeepAlives', value)

    @property
    def FipVersion(self):
        """The FIP version to use. Auto mode will accept same version as the negotiating party.

        Returns:
            str
        """
        return self._get_attribute('fipVersion')
    @FipVersion.setter
    def FipVersion(self, value):
        self._set_attribute('fipVersion', value)

    @property
    def FipVlanDiscWithNameId(self):
        """Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.

        Returns:
            bool
        """
        return self._get_attribute('fipVlanDiscWithNameId')
    @FipVlanDiscWithNameId.setter
    def FipVlanDiscWithNameId(self, value):
        self._set_attribute('fipVlanDiscWithNameId', value)

    @property
    def FipVnportKeepAlivePeriod(self):
        """The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.

        Returns:
            number
        """
        return self._get_attribute('fipVnportKeepAlivePeriod')
    @FipVnportKeepAlivePeriod.setter
    def FipVnportKeepAlivePeriod(self, value):
        self._set_attribute('fipVnportKeepAlivePeriod', value)

    @property
    def IgnoreDuplicateMacDescriptors(self):
        """Ignore duplicate MAC descriptors.

        Returns:
            bool
        """
        return self._get_attribute('ignoreDuplicateMacDescriptors')
    @IgnoreDuplicateMacDescriptors.setter
    def IgnoreDuplicateMacDescriptors(self, value):
        self._set_attribute('ignoreDuplicateMacDescriptors', value)

    @property
    def MaxFcoeSize(self):
        """The maximum FCoE frame size in bytes.

        Returns:
            number
        """
        return self._get_attribute('maxFcoeSize')
    @MaxFcoeSize.setter
    def MaxFcoeSize(self, value):
        self._set_attribute('maxFcoeSize', value)

    @property
    def MaxPacketsPerSecond(self):
        """The maximum number of requests transmitted in each second.

        Returns:
            number
        """
        return self._get_attribute('maxPacketsPerSecond')
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute('maxPacketsPerSecond', value)

    @property
    def MaxRetries(self):
        """The number of request retries for each negotiation stage in case of response timeout or error.

        Returns:
            number
        """
        return self._get_attribute('maxRetries')
    @MaxRetries.setter
    def MaxRetries(self, value):
        self._set_attribute('maxRetries', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def RetryInterval(self):
        """The number of seconds to wait for a response before sending a new request.

        Returns:
            number
        """
        return self._get_attribute('retryInterval')
    @RetryInterval.setter
    def RetryInterval(self, value):
        self._set_attribute('retryInterval', value)

    @property
    def SetupRate(self):
        """The number of interfaces scheduled to be configured in each second.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def TeardownRate(self):
        """The number of interfaces scheduled to be deconfigured in each second.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Updates a child instance of fcoeClientGlobals on the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
            B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
            FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
            FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
            FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
            FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
            FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
            FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
            FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
            FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
            FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
            FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
            FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
            FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
            IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
            MaxFcoeSize (number): The maximum FCoE frame size in bytes.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.
            SetupRate (number): The number of interfaces scheduled to be configured in each second.
            TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Adds a new fcoeClientGlobals node on the server and retrieves it in this instance.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
            B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
            FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
            FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
            FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
            FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
            FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
            FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
            FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
            FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
            FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
            FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
            FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
            FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
            IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
            MaxFcoeSize (number): The maximum FCoE frame size in bytes.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.
            SetupRate (number): The number of interfaces scheduled to be configured in each second.
            TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns:
            self: This instance with all currently retrieved fcoeClientGlobals data using find and the newly added fcoeClientGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the fcoeClientGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, ObjectId=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves fcoeClientGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve fcoeClientGlobals data from the server.
        By default the find method takes no parameters and will retrieve all fcoeClientGlobals data from the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
            B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
            FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
            FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
            FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
            FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
            FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
            FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
            FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
            FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
            FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
            FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
            FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
            FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
            IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
            MaxFcoeSize (number): The maximum FCoE frame size in bytes.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            ObjectId (str): Unique identifier for this object
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.
            SetupRate (number): The number of interfaces scheduled to be configured in each second.
            TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns:
            self: This instance with matching fcoeClientGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of fcoeClientGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the fcoeClientGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
