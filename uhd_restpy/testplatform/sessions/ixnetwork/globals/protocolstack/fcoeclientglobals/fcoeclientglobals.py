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


class FcoeClientGlobals(Base):
    """StackManager FCoE Global Settings
    The FcoeClientGlobals class encapsulates a list of fcoeClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcoeClientGlobals.find() method.
    The list can be managed by using the FcoeClientGlobals.add() and FcoeClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeClientGlobals'
    _SDM_ATT_MAP = {
        'AcceptPartialConfig': 'acceptPartialConfig',
        'B2bRxSize': 'b2bRxSize',
        'DcbxTimeout': 'dcbxTimeout',
        'FipAdvertisementPeriod': 'fipAdvertisementPeriod',
        'FipFcfMacListCollection': 'fipFcfMacListCollection',
        'FipFcfMacListCollectionInterval': 'fipFcfMacListCollectionInterval',
        'FipOverrideAdvertisementPeriod': 'fipOverrideAdvertisementPeriod',
        'FipOverrideVnportKeepAlivePeriod': 'fipOverrideVnportKeepAlivePeriod',
        'FipProposeMacInFpma': 'fipProposeMacInFpma',
        'FipResetDiscovery': 'fipResetDiscovery',
        'FipResetNumRetry': 'fipResetNumRetry',
        'FipRestartOnSessionDown': 'fipRestartOnSessionDown',
        'FipSendKeepAlives': 'fipSendKeepAlives',
        'FipVersion': 'fipVersion',
        'FipVlanDiscWithNameId': 'fipVlanDiscWithNameId',
        'FipVnportKeepAlivePeriod': 'fipVnportKeepAlivePeriod',
        'IgnoreDuplicateMacDescriptors': 'ignoreDuplicateMacDescriptors',
        'MaxFcoeSize': 'maxFcoeSize',
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'MaxRetries': 'maxRetries',
        'ObjectId': 'objectId',
        'RetryInterval': 'retryInterval',
        'SetupRate': 'setupRate',
        'TeardownRate': 'teardownRate',
    }

    def __init__(self, parent):
        super(FcoeClientGlobals, self).__init__(parent)

    @property
    def FcoeClientOptionSet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptionset.FcoeClientOptionSet): An instance of the FcoeClientOptionSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientoptionset.fcoeclientoptionset import FcoeClientOptionSet
        return FcoeClientOptionSet(self)

    @property
    def AcceptPartialConfig(self):
        """
        Returns
        -------
        - bool: This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'])
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'], value)

    @property
    def B2bRxSize(self):
        """
        Returns
        -------
        - number: The buffer-to-buffer receive data field size in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['B2bRxSize'])
    @B2bRxSize.setter
    def B2bRxSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['B2bRxSize'], value)

    @property
    def DcbxTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for DCBX to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DcbxTimeout'])
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DcbxTimeout'], value)

    @property
    def FipAdvertisementPeriod(self):
        """
        Returns
        -------
        - number: The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipAdvertisementPeriod'])
    @FipAdvertisementPeriod.setter
    def FipAdvertisementPeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipAdvertisementPeriod'], value)

    @property
    def FipFcfMacListCollection(self):
        """
        Returns
        -------
        - bool: Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipFcfMacListCollection'])
    @FipFcfMacListCollection.setter
    def FipFcfMacListCollection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipFcfMacListCollection'], value)

    @property
    def FipFcfMacListCollectionInterval(self):
        """
        Returns
        -------
        - number: The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipFcfMacListCollectionInterval'])
    @FipFcfMacListCollectionInterval.setter
    def FipFcfMacListCollectionInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipFcfMacListCollectionInterval'], value)

    @property
    def FipOverrideAdvertisementPeriod(self):
        """
        Returns
        -------
        - bool: If enabled, the Discovery Advertisement period will be specified by the application.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipOverrideAdvertisementPeriod'])
    @FipOverrideAdvertisementPeriod.setter
    def FipOverrideAdvertisementPeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipOverrideAdvertisementPeriod'], value)

    @property
    def FipOverrideVnportKeepAlivePeriod(self):
        """
        Returns
        -------
        - bool: If enabled, the VN_Port Keep-Alive period will be specified by the application.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipOverrideVnportKeepAlivePeriod'])
    @FipOverrideVnportKeepAlivePeriod.setter
    def FipOverrideVnportKeepAlivePeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipOverrideVnportKeepAlivePeriod'], value)

    @property
    def FipProposeMacInFpma(self):
        """
        Returns
        -------
        - bool: Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipProposeMacInFpma'])
    @FipProposeMacInFpma.setter
    def FipProposeMacInFpma(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipProposeMacInFpma'], value)

    @property
    def FipResetDiscovery(self):
        """
        Returns
        -------
        - bool: Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipResetDiscovery'])
    @FipResetDiscovery.setter
    def FipResetDiscovery(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipResetDiscovery'], value)

    @property
    def FipResetNumRetry(self):
        """
        Returns
        -------
        - number: The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipResetNumRetry'])
    @FipResetNumRetry.setter
    def FipResetNumRetry(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipResetNumRetry'], value)

    @property
    def FipRestartOnSessionDown(self):
        """
        Returns
        -------
        - bool: If enabled, the port will restart FIP negotiation when the session goes down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipRestartOnSessionDown'])
    @FipRestartOnSessionDown.setter
    def FipRestartOnSessionDown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipRestartOnSessionDown'], value)

    @property
    def FipSendKeepAlives(self):
        """
        Returns
        -------
        - bool: If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipSendKeepAlives'])
    @FipSendKeepAlives.setter
    def FipSendKeepAlives(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipSendKeepAlives'], value)

    @property
    def FipVersion(self):
        """
        Returns
        -------
        - str: The FIP version to use. Auto mode will accept same version as the negotiating party.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipVersion'])
    @FipVersion.setter
    def FipVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipVersion'], value)

    @property
    def FipVlanDiscWithNameId(self):
        """
        Returns
        -------
        - bool: Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipVlanDiscWithNameId'])
    @FipVlanDiscWithNameId.setter
    def FipVlanDiscWithNameId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipVlanDiscWithNameId'], value)

    @property
    def FipVnportKeepAlivePeriod(self):
        """
        Returns
        -------
        - number: The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipVnportKeepAlivePeriod'])
    @FipVnportKeepAlivePeriod.setter
    def FipVnportKeepAlivePeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipVnportKeepAlivePeriod'], value)

    @property
    def IgnoreDuplicateMacDescriptors(self):
        """
        Returns
        -------
        - bool: Ignore duplicate MAC descriptors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IgnoreDuplicateMacDescriptors'])
    @IgnoreDuplicateMacDescriptors.setter
    def IgnoreDuplicateMacDescriptors(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IgnoreDuplicateMacDescriptors'], value)

    @property
    def MaxFcoeSize(self):
        """
        Returns
        -------
        - number: The maximum FCoE frame size in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxFcoeSize'])
    @MaxFcoeSize.setter
    def MaxFcoeSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxFcoeSize'], value)

    @property
    def MaxPacketsPerSecond(self):
        """
        Returns
        -------
        - number: The maximum number of requests transmitted in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'])
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'], value)

    @property
    def MaxRetries(self):
        """
        Returns
        -------
        - number: The number of request retries for each negotiation stage in case of response timeout or error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRetries'])
    @MaxRetries.setter
    def MaxRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRetries'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def RetryInterval(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for a response before sending a new request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryInterval'])
    @RetryInterval.setter
    def RetryInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RetryInterval'], value)

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: The number of interfaces scheduled to be configured in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: The number of interfaces scheduled to be deconfigured in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    def update(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Updates fcoeClientGlobals resource on the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
        - FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
        - FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
        - FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
        - FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
        - FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
        - FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
        - FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
        - FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
        - FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
        - FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
        - FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
        - IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
        - MaxFcoeSize (number): The maximum FCoE frame size in bytes.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Adds a new fcoeClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
        - FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
        - FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
        - FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
        - FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
        - FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
        - FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
        - FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
        - FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
        - FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
        - FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
        - FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
        - IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
        - MaxFcoeSize (number): The maximum FCoE frame size in bytes.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns
        -------
        - self: This instance with all currently retrieved fcoeClientGlobals resources using find and the newly added fcoeClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcoeClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, B2bRxSize=None, DcbxTimeout=None, FipAdvertisementPeriod=None, FipFcfMacListCollection=None, FipFcfMacListCollectionInterval=None, FipOverrideAdvertisementPeriod=None, FipOverrideVnportKeepAlivePeriod=None, FipProposeMacInFpma=None, FipResetDiscovery=None, FipResetNumRetry=None, FipRestartOnSessionDown=None, FipSendKeepAlives=None, FipVersion=None, FipVlanDiscWithNameId=None, FipVnportKeepAlivePeriod=None, IgnoreDuplicateMacDescriptors=None, MaxFcoeSize=None, MaxPacketsPerSecond=None, MaxRetries=None, ObjectId=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves fcoeClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeClientGlobals resources from the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipAdvertisementPeriod (number): The interval in seconds between periodic Discovery Advertisements and ENode FIP Keep-Alive messages.The default value is 8. Valid values are in the range 1 to 90.
        - FipFcfMacListCollection (bool): Allow Ixia emulated ENodes to collect FCF-MAC address info and show details at per-session stats.
        - FipFcfMacListCollectionInterval (number): The amount of time in seconds given to the Ixia emulated ENodes to receive FIP Discovery Advertisements from different FCF-MACs.
        - FipOverrideAdvertisementPeriod (bool): If enabled, the Discovery Advertisement period will be specified by the application.
        - FipOverrideVnportKeepAlivePeriod (bool): If enabled, the VN_Port Keep-Alive period will be specified by the application.
        - FipProposeMacInFpma (bool): Allow Ixia emulated ENodes to propose a non-zero valid MAC address in FPMA FLOGI request.If not enabled, Ixia encodes an all zero MAC address in FPMA FLOGI request.
        - FipResetDiscovery (bool): Allow FIP negotiation to be reinitialized after a specified number of retries has been attempted.
        - FipResetNumRetry (number): The number of normal retries to be attempted before resetting the state machineand continue retrying with alternate FIP VLAN Discovery and FIP Solicitation messages.
        - FipRestartOnSessionDown (bool): If enabled, the port will restart FIP negotiation when the session goes down.
        - FipSendKeepAlives (bool): If enabled, the port will send ENode/VN_Port FIP Keep-Alive messages.
        - FipVersion (str): The FIP version to use. Auto mode will accept same version as the negotiating party.
        - FipVlanDiscWithNameId (bool): Include Name_Identifier Descriptor in FIP VLAN Request messages generated by Ixia emulated ENodes.
        - FipVnportKeepAlivePeriod (number): The interval in seconds between periodic VN_Port FIP Keep-Alive messages.The default value is 90. Valid values are in the range 1 to 3600.
        - IgnoreDuplicateMacDescriptors (bool): Ignore duplicate MAC descriptors.
        - MaxFcoeSize (number): The maximum FCoE frame size in bytes.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - ObjectId (str): Unique identifier for this object
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns
        -------
        - self: This instance with matching fcoeClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
