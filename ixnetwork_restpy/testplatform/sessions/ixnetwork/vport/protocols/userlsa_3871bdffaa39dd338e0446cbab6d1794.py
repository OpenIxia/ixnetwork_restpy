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


class UserLsa(Base):
    """
    The UserLsa class encapsulates a list of userLsa resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserLsa.find() method.
    The list can be managed by using the UserLsa.add() and UserLsa.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'userLsa'
    _SDM_ATT_MAP = {
        'AdvertisingRouterId': 'advertisingRouterId',
        'Enabled': 'enabled',
        'ExpandIntoLinksOrAttachedRouters': 'expandIntoLinksOrAttachedRouters',
        'LinkStateId': 'linkStateId',
        'LsaType': 'lsaType',
        'OptBitDemandCircuit': 'optBitDemandCircuit',
        'OptBitExternalAttributes': 'optBitExternalAttributes',
        'OptBitExternalRouting': 'optBitExternalRouting',
        'OptBitLsaNoForward': 'optBitLsaNoForward',
        'OptBitMulticast': 'optBitMulticast',
        'OptBitNssaCapability': 'optBitNssaCapability',
        'OptBitTypeOfService': 'optBitTypeOfService',
        'Option': 'option',
    }

    def __init__(self, parent):
        super(UserLsa, self).__init__(parent)

    @property
    def External(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_85a598ac8444d3e9900180267cdd4cc7.External): An instance of the External class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_85a598ac8444d3e9900180267cdd4cc7 import External
        return External(self)

    @property
    def Network(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_955639231e107e0f0d10cb2bc06c7334.Network): An instance of the Network class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_955639231e107e0f0d10cb2bc06c7334 import Network
        return Network(self)

    @property
    def Nssa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_f90f4f11319e2f01d562907fe79a27a5.Nssa): An instance of the Nssa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_f90f4f11319e2f01d562907fe79a27a5 import Nssa
        return Nssa(self)

    @property
    def Opaque(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_69b3d155c040a105eb3fda40e02154f0.Opaque): An instance of the Opaque class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_69b3d155c040a105eb3fda40e02154f0 import Opaque
        return Opaque(self)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_77a71942871e4fa7afe599b051a5f4d8.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_77a71942871e4fa7afe599b051a5f4d8 import Router
        return Router(self)

    @property
    def SummaryIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_42dff126c26ad4a553c5a885bf09e691.SummaryIp): An instance of the SummaryIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_42dff126c26ad4a553c5a885bf09e691 import SummaryIp
        return SummaryIp(self)

    @property
    def AdvertisingRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertisingRouterId'])
    @AdvertisingRouterId.setter
    def AdvertisingRouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertisingRouterId'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExpandIntoLinksOrAttachedRouters(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpandIntoLinksOrAttachedRouters'])
    @ExpandIntoLinksOrAttachedRouters.setter
    def ExpandIntoLinksOrAttachedRouters(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExpandIntoLinksOrAttachedRouters'], value)

    @property
    def LinkStateId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkStateId'])
    @LinkStateId.setter
    def LinkStateId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkStateId'], value)

    @property
    def LsaType(self):
        """
        Returns
        -------
        - str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaType'])
    @LsaType.setter
    def LsaType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaType'], value)

    @property
    def OptBitDemandCircuit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitDemandCircuit'])
    @OptBitDemandCircuit.setter
    def OptBitDemandCircuit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitDemandCircuit'], value)

    @property
    def OptBitExternalAttributes(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitExternalAttributes'])
    @OptBitExternalAttributes.setter
    def OptBitExternalAttributes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitExternalAttributes'], value)

    @property
    def OptBitExternalRouting(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitExternalRouting'])
    @OptBitExternalRouting.setter
    def OptBitExternalRouting(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitExternalRouting'], value)

    @property
    def OptBitLsaNoForward(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitLsaNoForward'])
    @OptBitLsaNoForward.setter
    def OptBitLsaNoForward(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitLsaNoForward'], value)

    @property
    def OptBitMulticast(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitMulticast'])
    @OptBitMulticast.setter
    def OptBitMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitMulticast'], value)

    @property
    def OptBitNssaCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitNssaCapability'])
    @OptBitNssaCapability.setter
    def OptBitNssaCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitNssaCapability'], value)

    @property
    def OptBitTypeOfService(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptBitTypeOfService'])
    @OptBitTypeOfService.setter
    def OptBitTypeOfService(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptBitTypeOfService'], value)

    @property
    def Option(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Option'])
    @Option.setter
    def Option(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Option'], value)

    def update(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
        """Updates userLsa resource on the server.

        Args
        ----
        - AdvertisingRouterId (str): 
        - Enabled (bool): 
        - ExpandIntoLinksOrAttachedRouters (bool): 
        - LinkStateId (str): 
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)): 
        - OptBitDemandCircuit (bool): 
        - OptBitExternalAttributes (bool): 
        - OptBitExternalRouting (bool): 
        - OptBitLsaNoForward (bool): 
        - OptBitMulticast (bool): 
        - OptBitNssaCapability (bool): 
        - OptBitTypeOfService (bool): 
        - Option (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
        """Adds a new userLsa resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingRouterId (str): 
        - Enabled (bool): 
        - ExpandIntoLinksOrAttachedRouters (bool): 
        - LinkStateId (str): 
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)): 
        - OptBitDemandCircuit (bool): 
        - OptBitExternalAttributes (bool): 
        - OptBitExternalRouting (bool): 
        - OptBitLsaNoForward (bool): 
        - OptBitMulticast (bool): 
        - OptBitNssaCapability (bool): 
        - OptBitTypeOfService (bool): 
        - Option (number): 

        Returns
        -------
        - self: This instance with all currently retrieved userLsa resources using find and the newly added userLsa resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained userLsa resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
        """Finds and retrieves userLsa resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve userLsa resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all userLsa resources from the server.

        Args
        ----
        - AdvertisingRouterId (str): 
        - Enabled (bool): 
        - ExpandIntoLinksOrAttachedRouters (bool): 
        - LinkStateId (str): 
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)): 
        - OptBitDemandCircuit (bool): 
        - OptBitExternalAttributes (bool): 
        - OptBitExternalRouting (bool): 
        - OptBitLsaNoForward (bool): 
        - OptBitMulticast (bool): 
        - OptBitNssaCapability (bool): 
        - OptBitTypeOfService (bool): 
        - Option (number): 

        Returns
        -------
        - self: This instance with matching userLsa resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of userLsa data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the userLsa resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
