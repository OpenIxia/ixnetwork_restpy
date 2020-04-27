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


class UserLsa(Base):
    """
    The UserLsa class encapsulates a list of userLsa resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserLsa.find() method.
    The list can be managed by using the UserLsa.add() and UserLsa.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'userLsa'

    def __init__(self, parent):
        super(UserLsa, self).__init__(parent)

    @property
    def AsExternal(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asexternal_fd9b5e29352919ddb5344374a5c1fab0.AsExternal): An instance of the AsExternal class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asexternal_fd9b5e29352919ddb5344374a5c1fab0 import AsExternal
        return AsExternal(self)

    @property
    def InterAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interareaprefix_2546e7ce9c33014e1b97fba5f4b3fa3c.InterAreaPrefix): An instance of the InterAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interareaprefix_2546e7ce9c33014e1b97fba5f4b3fa3c import InterAreaPrefix
        return InterAreaPrefix(self)

    @property
    def InterAreaRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interarearouter_0238fd494b1e4de1d385c53ea6e47643.InterAreaRouter): An instance of the InterAreaRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interarearouter_0238fd494b1e4de1d385c53ea6e47643 import InterAreaRouter
        return InterAreaRouter(self)

    @property
    def IntraAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.intraareaprefix_5b774b390b3423e7b7245a4a8e6fa2bf.IntraAreaPrefix): An instance of the IntraAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.intraareaprefix_5b774b390b3423e7b7245a4a8e6fa2bf import IntraAreaPrefix
        return IntraAreaPrefix(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_f91be640fe4d64015cbd067fec175e7b.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_f91be640fe4d64015cbd067fec175e7b import Link
        return Link(self)

    @property
    def Network(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_6359169f221f6f5d9ea00380b4291ddb.Network): An instance of the Network class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_6359169f221f6f5d9ea00380b4291ddb import Network
        return Network(self)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_a07d67a2b1486caa253b2d7e6c180d8e.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_a07d67a2b1486caa253b2d7e6c180d8e import Router
        return Router(self)

    @property
    def AdvertisingRouterId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('advertisingRouterId')
    @AdvertisingRouterId.setter
    def AdvertisingRouterId(self, value):
        self._set_attribute('advertisingRouterId', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def ExpandIntoLinksOrAttachedRouters(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('expandIntoLinksOrAttachedRouters')
    @ExpandIntoLinksOrAttachedRouters.setter
    def ExpandIntoLinksOrAttachedRouters(self, value):
        self._set_attribute('expandIntoLinksOrAttachedRouters', value)

    @property
    def LinkStateId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('linkStateId')
    @LinkStateId.setter
    def LinkStateId(self, value):
        self._set_attribute('linkStateId', value)

    @property
    def LsaType(self):
        """
        Returns
        -------
        - str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix): 
        """
        return self._get_attribute('lsaType')
    @LsaType.setter
    def LsaType(self, value):
        self._set_attribute('lsaType', value)

    def update(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None):
        """Updates userLsa resource on the server.

        Args
        ----
        - AdvertisingRouterId (str): 
        - Enabled (bool): 
        - ExpandIntoLinksOrAttachedRouters (bool): 
        - LinkStateId (str): 
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None):
        """Adds a new userLsa resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingRouterId (str): 
        - Enabled (bool): 
        - ExpandIntoLinksOrAttachedRouters (bool): 
        - LinkStateId (str): 
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)): 

        Returns
        -------
        - self: This instance with all currently retrieved userLsa resources using find and the newly added userLsa resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained userLsa resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None):
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
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)): 

        Returns
        -------
        - self: This instance with matching userLsa resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

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
