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


class Bgp(Base):
    """Simulates one or more BGP4 routers in a network of routers.
    The Bgp class encapsulates a required bgp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgp'
    _SDM_ATT_MAP = {
        'AutoFillUpDutIp': 'autoFillUpDutIp',
        'DisableReceivedUpdateValidation': 'disableReceivedUpdateValidation',
        'EVpnAfi': 'eVpnAfi',
        'EVpnSafi': 'eVpnSafi',
        'EnableAdVplsPrefixLengthInBits': 'enableAdVplsPrefixLengthInBits',
        'EnableExternalActiveConnect': 'enableExternalActiveConnect',
        'EnableInternalActiveConnect': 'enableInternalActiveConnect',
        'EnableLabelExchangeOverLsp': 'enableLabelExchangeOverLsp',
        'EnableVpnLabelExchangeOverLsp': 'enableVpnLabelExchangeOverLsp',
        'Enabled': 'enabled',
        'EsImportRouteTargetSubType': 'esImportRouteTargetSubType',
        'EsImportRouteTargetType': 'esImportRouteTargetType',
        'EsiLabelExtendedCommunitySubType': 'esiLabelExtendedCommunitySubType',
        'EsiLabelExtendedCommunityType': 'esiLabelExtendedCommunityType',
        'EvpnIpAddressLengthUnit': 'evpnIpAddressLengthUnit',
        'ExternalRetries': 'externalRetries',
        'ExternalRetryDelay': 'externalRetryDelay',
        'InternalRetries': 'internalRetries',
        'InternalRetryDelay': 'internalRetryDelay',
        'MacMobilityExtendedCommunitySubType': 'macMobilityExtendedCommunitySubType',
        'MacMobilityExtendedCommunityType': 'macMobilityExtendedCommunityType',
        'MldpP2mpFecType': 'mldpP2mpFecType',
        'RunningState': 'runningState',
        'Tester4ByteAsForIbgp': 'tester4ByteAsForIbgp',
        'TesterAsForIbgp': 'testerAsForIbgp',
        'TriggerVplsPwInitiation': 'triggerVplsPwInitiation',
        'VrfRouteImportExtendedCommunitySubType': 'vrfRouteImportExtendedCommunitySubType',
    }

    def __init__(self, parent):
        super(Bgp, self).__init__(parent)

    @property
    def NeighborRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborrange_26f40d15635b26e83238aa3bcab182ab.NeighborRange): An instance of the NeighborRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborrange_26f40d15635b26e83238aa3bcab182ab import NeighborRange
        return NeighborRange(self)

    @property
    def AutoFillUpDutIp(self):
        """
        Returns
        -------
        - bool: If true, automatically fills up the IP of the DUT
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoFillUpDutIp'])
    @AutoFillUpDutIp.setter
    def AutoFillUpDutIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoFillUpDutIp'], value)

    @property
    def DisableReceivedUpdateValidation(self):
        """
        Returns
        -------
        - bool: If true, disables any update validation request from the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableReceivedUpdateValidation'])
    @DisableReceivedUpdateValidation.setter
    def DisableReceivedUpdateValidation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableReceivedUpdateValidation'], value)

    @property
    def EVpnAfi(self):
        """
        Returns
        -------
        - number: AFI to support EVPN. Default value is 25. Minimum valus is 0 and maximum value is 0xFFFF
        """
        return self._get_attribute(self._SDM_ATT_MAP['EVpnAfi'])
    @EVpnAfi.setter
    def EVpnAfi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EVpnAfi'], value)

    @property
    def EVpnSafi(self):
        """
        Returns
        -------
        - number: SAFI to support EVPN. Default value is 70. Minimum valus is 0 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EVpnSafi'])
    @EVpnSafi.setter
    def EVpnSafi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EVpnSafi'], value)

    @property
    def EnableAdVplsPrefixLengthInBits(self):
        """
        Returns
        -------
        - bool: If true, enables the AdVpls length in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdVplsPrefixLengthInBits'])
    @EnableAdVplsPrefixLengthInBits.setter
    def EnableAdVplsPrefixLengthInBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdVplsPrefixLengthInBits'], value)

    @property
    def EnableExternalActiveConnect(self):
        """
        Returns
        -------
        - bool: Causes a HELLO message to be actively sent when BGP testing starts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExternalActiveConnect'])
    @EnableExternalActiveConnect.setter
    def EnableExternalActiveConnect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExternalActiveConnect'], value)

    @property
    def EnableInternalActiveConnect(self):
        """
        Returns
        -------
        - bool: Causes a HELLO message to be actively sent when BGP testing starts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableInternalActiveConnect'])
    @EnableInternalActiveConnect.setter
    def EnableInternalActiveConnect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableInternalActiveConnect'], value)

    @property
    def EnableLabelExchangeOverLsp(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Enables the ability to exchange labels over LSP for VPNs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLabelExchangeOverLsp'])
    @EnableLabelExchangeOverLsp.setter
    def EnableLabelExchangeOverLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLabelExchangeOverLsp'], value)

    @property
    def EnableVpnLabelExchangeOverLsp(self):
        """
        Returns
        -------
        - bool: If true, enables the exchange of VPN exchange over LSP
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVpnLabelExchangeOverLsp'])
    @EnableVpnLabelExchangeOverLsp.setter
    def EnableVpnLabelExchangeOverLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVpnLabelExchangeOverLsp'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated BGP router in the emulated BGP network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EsImportRouteTargetSubType(self):
        """
        Returns
        -------
        - number: This is a new transitive Route Target extended community carried with the Ethernet Segment route in EVPN. When used, it enables all the PEs connected to the same multi-homed site to import the Ethernet Segment routes. Default value is 2. Minimum value is 1 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsImportRouteTargetSubType'])
    @EsImportRouteTargetSubType.setter
    def EsImportRouteTargetSubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsImportRouteTargetSubType'], value)

    @property
    def EsImportRouteTargetType(self):
        """
        Returns
        -------
        - number: This is a new transitive Route Target extended community carried with the Ethernet Segment route in EVPN. When used, it enables all the PEs connected to the same multi-homed site to import the Ethernet Segment routes. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsImportRouteTargetType'])
    @EsImportRouteTargetType.setter
    def EsImportRouteTargetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsImportRouteTargetType'], value)

    @property
    def EsiLabelExtendedCommunitySubType(self):
        """
        Returns
        -------
        - number: This is a new transitive extended community in EVPN. It may be advertised along with Ethernet Auto-Discovery routes and it enables split-horizon procedures for multi-homed sites. Default value is 1. Minimum value is 1 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsiLabelExtendedCommunitySubType'])
    @EsiLabelExtendedCommunitySubType.setter
    def EsiLabelExtendedCommunitySubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsiLabelExtendedCommunitySubType'], value)

    @property
    def EsiLabelExtendedCommunityType(self):
        """
        Returns
        -------
        - number: This is a new transitive extended community in EVPN. It may be advertised along with Ethernet Auto-Discovery routes and it enables split-horizon procedures for multi-homed sites. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EsiLabelExtendedCommunityType'])
    @EsiLabelExtendedCommunityType.setter
    def EsiLabelExtendedCommunityType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EsiLabelExtendedCommunityType'], value)

    @property
    def EvpnIpAddressLengthUnit(self):
        """
        Returns
        -------
        - str(bit | byte): The unit of the IP address length field in MAC Advertisement route packet, can be bits or bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvpnIpAddressLengthUnit'])
    @EvpnIpAddressLengthUnit.setter
    def EvpnIpAddressLengthUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvpnIpAddressLengthUnit'], value)

    @property
    def ExternalRetries(self):
        """
        Returns
        -------
        - number: The number of times to attempt an OPEN connection with the DUT router(s) before giving up.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRetries'])
    @ExternalRetries.setter
    def ExternalRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRetries'], value)

    @property
    def ExternalRetryDelay(self):
        """
        Returns
        -------
        - number: When retries are necessary, the delay between retries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRetryDelay'])
    @ExternalRetryDelay.setter
    def ExternalRetryDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRetryDelay'], value)

    @property
    def InternalRetries(self):
        """
        Returns
        -------
        - number: The number of times to attempt an OPEN connection with the DUT router(s) before giving up.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalRetries'])
    @InternalRetries.setter
    def InternalRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternalRetries'], value)

    @property
    def InternalRetryDelay(self):
        """
        Returns
        -------
        - number: When retries are necessary, the delay between retries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalRetryDelay'])
    @InternalRetryDelay.setter
    def InternalRetryDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternalRetryDelay'], value)

    @property
    def MacMobilityExtendedCommunitySubType(self):
        """
        Returns
        -------
        - number: This is a new transitive extended community used in EVPN. It may be advertised along with MAC Advertisement routes to support MAC mobility. Default value is 0. Minimum value is 0 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacMobilityExtendedCommunitySubType'])
    @MacMobilityExtendedCommunitySubType.setter
    def MacMobilityExtendedCommunitySubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacMobilityExtendedCommunitySubType'], value)

    @property
    def MacMobilityExtendedCommunityType(self):
        """
        Returns
        -------
        - number: This is a new transitive extended community used in EVPN. It may be advertised along with MAC Advertisement routes to support MAC mobility. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacMobilityExtendedCommunityType'])
    @MacMobilityExtendedCommunityType.setter
    def MacMobilityExtendedCommunityType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacMobilityExtendedCommunityType'], value)

    @property
    def MldpP2mpFecType(self):
        """
        Returns
        -------
        - number: The MLDP P2MP FEC type value in hexadecimal.LOCAL EXECS
        """
        return self._get_attribute(self._SDM_ATT_MAP['MldpP2mpFecType'])
    @MldpP2mpFecType.setter
    def MldpP2mpFecType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MldpP2mpFecType'], value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the BGP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def Tester4ByteAsForIbgp(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tester4ByteAsForIbgp'])
    @Tester4ByteAsForIbgp.setter
    def Tester4ByteAsForIbgp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tester4ByteAsForIbgp'], value)

    @property
    def TesterAsForIbgp(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TesterAsForIbgp'])
    @TesterAsForIbgp.setter
    def TesterAsForIbgp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TesterAsForIbgp'], value)

    @property
    def TriggerVplsPwInitiation(self):
        """
        Returns
        -------
        - bool: Enable to initiate a trigger a VPLS PW initation that is a BGP-LDP communication.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerVplsPwInitiation'])
    @TriggerVplsPwInitiation.setter
    def TriggerVplsPwInitiation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerVplsPwInitiation'], value)

    @property
    def VrfRouteImportExtendedCommunitySubType(self):
        """
        Returns
        -------
        - number: Extended Community Sub Type to be used in VRF Route Import Extended Community.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VrfRouteImportExtendedCommunitySubType'])
    @VrfRouteImportExtendedCommunitySubType.setter
    def VrfRouteImportExtendedCommunitySubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VrfRouteImportExtendedCommunitySubType'], value)

    def update(self, AutoFillUpDutIp=None, DisableReceivedUpdateValidation=None, EVpnAfi=None, EVpnSafi=None, EnableAdVplsPrefixLengthInBits=None, EnableExternalActiveConnect=None, EnableInternalActiveConnect=None, EnableLabelExchangeOverLsp=None, EnableVpnLabelExchangeOverLsp=None, Enabled=None, EsImportRouteTargetSubType=None, EsImportRouteTargetType=None, EsiLabelExtendedCommunitySubType=None, EsiLabelExtendedCommunityType=None, EvpnIpAddressLengthUnit=None, ExternalRetries=None, ExternalRetryDelay=None, InternalRetries=None, InternalRetryDelay=None, MacMobilityExtendedCommunitySubType=None, MacMobilityExtendedCommunityType=None, MldpP2mpFecType=None, Tester4ByteAsForIbgp=None, TesterAsForIbgp=None, TriggerVplsPwInitiation=None, VrfRouteImportExtendedCommunitySubType=None):
        """Updates bgp resource on the server.

        Args
        ----
        - AutoFillUpDutIp (bool): If true, automatically fills up the IP of the DUT
        - DisableReceivedUpdateValidation (bool): If true, disables any update validation request from the DUT.
        - EVpnAfi (number): AFI to support EVPN. Default value is 25. Minimum valus is 0 and maximum value is 0xFFFF
        - EVpnSafi (number): SAFI to support EVPN. Default value is 70. Minimum valus is 0 and maximum value is 0xFF.
        - EnableAdVplsPrefixLengthInBits (bool): If true, enables the AdVpls length in bits.
        - EnableExternalActiveConnect (bool): Causes a HELLO message to be actively sent when BGP testing starts.
        - EnableInternalActiveConnect (bool): Causes a HELLO message to be actively sent when BGP testing starts.
        - EnableLabelExchangeOverLsp (bool): Enables the ability to exchange labels over LSP for VPNs.
        - EnableVpnLabelExchangeOverLsp (bool): If true, enables the exchange of VPN exchange over LSP
        - Enabled (bool): Enables or disables the use of this emulated BGP router in the emulated BGP network. (default = disabled)
        - EsImportRouteTargetSubType (number): This is a new transitive Route Target extended community carried with the Ethernet Segment route in EVPN. When used, it enables all the PEs connected to the same multi-homed site to import the Ethernet Segment routes. Default value is 2. Minimum value is 1 and maximum value is 0xFF.
        - EsImportRouteTargetType (number): This is a new transitive Route Target extended community carried with the Ethernet Segment route in EVPN. When used, it enables all the PEs connected to the same multi-homed site to import the Ethernet Segment routes. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        - EsiLabelExtendedCommunitySubType (number): This is a new transitive extended community in EVPN. It may be advertised along with Ethernet Auto-Discovery routes and it enables split-horizon procedures for multi-homed sites. Default value is 1. Minimum value is 1 and maximum value is 0xFF.
        - EsiLabelExtendedCommunityType (number): This is a new transitive extended community in EVPN. It may be advertised along with Ethernet Auto-Discovery routes and it enables split-horizon procedures for multi-homed sites. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        - EvpnIpAddressLengthUnit (str(bit | byte)): The unit of the IP address length field in MAC Advertisement route packet, can be bits or bytes
        - ExternalRetries (number): The number of times to attempt an OPEN connection with the DUT router(s) before giving up.
        - ExternalRetryDelay (number): When retries are necessary, the delay between retries.
        - InternalRetries (number): The number of times to attempt an OPEN connection with the DUT router(s) before giving up.
        - InternalRetryDelay (number): When retries are necessary, the delay between retries.
        - MacMobilityExtendedCommunitySubType (number): This is a new transitive extended community used in EVPN. It may be advertised along with MAC Advertisement routes to support MAC mobility. Default value is 0. Minimum value is 0 and maximum value is 0xFF.
        - MacMobilityExtendedCommunityType (number): This is a new transitive extended community used in EVPN. It may be advertised along with MAC Advertisement routes to support MAC mobility. Default value is 6. Minimum value is 1 and maximum value is 0xFF.
        - MldpP2mpFecType (number): The MLDP P2MP FEC type value in hexadecimal.LOCAL EXECS
        - Tester4ByteAsForIbgp (number): NOT DEFINED
        - TesterAsForIbgp (number): NOT DEFINED
        - TriggerVplsPwInitiation (bool): Enable to initiate a trigger a VPLS PW initation that is a BGP-LDP communication.
        - VrfRouteImportExtendedCommunitySubType (number): Extended Community Sub Type to be used in VRF Route Import Extended Community.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self):
        """Executes the start operation on the server.

        This function allows to Start BGP on a group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This function allows to Stop BGP on a group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
