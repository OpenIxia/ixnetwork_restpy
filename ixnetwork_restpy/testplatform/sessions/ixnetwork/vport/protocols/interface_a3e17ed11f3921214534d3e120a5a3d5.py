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


class Interface(Base):
    """This object holds the information for a single interface on the LDP router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'AdvertisingMode': 'advertisingMode',
        'AtmVcDirection': 'atmVcDirection',
        'Authentication': 'authentication',
        'BfdOperationMode': 'bfdOperationMode',
        'DiscoveryMode': 'discoveryMode',
        'EnableAtmSession': 'enableAtmSession',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'Enabled': 'enabled',
        'IsLdpLearnedInfoRefreshed': 'isLdpLearnedInfoRefreshed',
        'LabelSpaceId': 'labelSpaceId',
        'Md5Key': 'md5Key',
        'ProtocolInterface': 'protocolInterface',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def AtmLabelRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atmlabelrange_5fbea04d40d1539fb5be94c8185fde05.AtmLabelRange): An instance of the AtmLabelRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atmlabelrange_5fbea04d40d1539fb5be94c8185fde05 import AtmLabelRange
        return AtmLabelRange(self)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_52db08d36d5a12c9945c62ffba44484f.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_52db08d36d5a12c9945c62ffba44484f import LearnedFilter
        return LearnedFilter(self)._select()

    @property
    def LearnedIpv4Label(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4label_23dda3047725208d5616e2a4c9af5b30.LearnedIpv4Label): An instance of the LearnedIpv4Label class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4label_23dda3047725208d5616e2a4c9af5b30 import LearnedIpv4Label
        return LearnedIpv4Label(self)

    @property
    def LearnedIpv4P2mpLables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4p2mplables_901cce4e83bb87ee1a56ea4ee0d8f3c2.LearnedIpv4P2mpLables): An instance of the LearnedIpv4P2mpLables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4p2mplables_901cce4e83bb87ee1a56ea4ee0d8f3c2 import LearnedIpv4P2mpLables
        return LearnedIpv4P2mpLables(self)

    @property
    def LearnedMartiniLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmartinilabel_f9521de52f99cf6c1bc7818345131631.LearnedMartiniLabel): An instance of the LearnedMartiniLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmartinilabel_f9521de52f99cf6c1bc7818345131631 import LearnedMartiniLabel
        return LearnedMartiniLabel(self)

    @property
    def TargetPeer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.targetpeer_609011687593035978eacc673103474b.TargetPeer): An instance of the TargetPeer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.targetpeer_609011687593035978eacc673103474b import TargetPeer
        return TargetPeer(self)

    @property
    def AdvertisingMode(self):
        """
        Returns
        -------
        - str(unsolicited | onDemand): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertisingMode'])
    @AdvertisingMode.setter
    def AdvertisingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertisingMode'], value)

    @property
    def AtmVcDirection(self):
        """
        Returns
        -------
        - str(unidirectional | bidirectional): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AtmVcDirection'])
    @AtmVcDirection.setter
    def AtmVcDirection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AtmVcDirection'], value)

    @property
    def Authentication(self):
        """
        Returns
        -------
        - str(null | md5): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Authentication'])
    @Authentication.setter
    def Authentication(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Authentication'], value)

    @property
    def BfdOperationMode(self):
        """
        Returns
        -------
        - str(singleHop | multiHop): Helps to set the BFD session in terms of hops, one of Single and Multi.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BfdOperationMode'])
    @BfdOperationMode.setter
    def BfdOperationMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BfdOperationMode'], value)

    @property
    def DiscoveryMode(self):
        """
        Returns
        -------
        - str(basic | extended | extendedMartini): The discovery mode used for the interface: basic, extended, or extended Martini.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveryMode'])
    @DiscoveryMode.setter
    def DiscoveryMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscoveryMode'], value)

    @property
    def EnableAtmSession(self):
        """
        Returns
        -------
        - bool: Enables the establishment of ATM sessions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAtmSession'])
    @EnableAtmSession.setter
    def EnableAtmSession(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAtmSession'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: If true, enables BFD registration with LDP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this interface for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IsLdpLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: When enabled, automatically refreshes the LDP learned info (from the DUT).
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLdpLearnedInfoRefreshed'])

    @property
    def LabelSpaceId(self):
        """
        Returns
        -------
        - number: The LDP label space used by this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelSpaceId'])
    @LabelSpaceId.setter
    def LabelSpaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelSpaceId'], value)

    @property
    def Md5Key(self):
        """
        Returns
        -------
        - str: Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5Key'])
    @Md5Key.setter
    def Md5Key(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5Key'], value)

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The protocol interface associated with this LDP interface. There may be more than one protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    def update(self, AdvertisingMode=None, AtmVcDirection=None, Authentication=None, BfdOperationMode=None, DiscoveryMode=None, EnableAtmSession=None, EnableBfdRegistration=None, Enabled=None, LabelSpaceId=None, Md5Key=None, ProtocolInterface=None):
        """Updates interface resource on the server.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertisingMode=None, AtmVcDirection=None, Authentication=None, BfdOperationMode=None, DiscoveryMode=None, EnableAtmSession=None, EnableBfdRegistration=None, Enabled=None, LabelSpaceId=None, Md5Key=None, ProtocolInterface=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertisingMode=None, AtmVcDirection=None, Authentication=None, BfdOperationMode=None, DiscoveryMode=None, EnableAtmSession=None, EnableBfdRegistration=None, Enabled=None, IsLdpLearnedInfoRefreshed=None, LabelSpaceId=None, Md5Key=None, ProtocolInterface=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - IsLdpLearnedInfoRefreshed (bool): When enabled, automatically refreshes the LDP learned info (from the DUT).
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        This exec refreshes the LDP learned information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
