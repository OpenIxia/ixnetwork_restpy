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


class LearnedFilter(Base):
    """This object contains criteria for filtering the learned routes.
    The LearnedFilter class encapsulates a required learnedFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedFilter'

    def __init__(self, parent):
        super(LearnedFilter, self).__init__(parent)

    @property
    def Capabilities(self):
        """An instance of the Capabilities class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_754497d1ff7b22c18e1ee34bf909c096.Capabilities)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_754497d1ff7b22c18e1ee34bf909c096 import Capabilities
        return Capabilities(self)._select()

    @property
    def Prefix(self):
        """An instance of the Prefix class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.prefix_70a4504d7e1406e26725789a953f84b5.Prefix)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.prefix_70a4504d7e1406e26725789a953f84b5 import Prefix
        return Prefix(self)._select()

    @property
    def Afi(self):
        """Address Family Identifier value. Identifies the network layer protocol to be used with these routes.

        Returns:
            number
        """
        return self._get_attribute('afi')
    @Afi.setter
    def Afi(self, value):
        self._set_attribute('afi', value)

    @property
    def EnableAfiSafi(self):
        """If enabled, allows the user to set values to be used for BGP-MP - the user-specified AFI and SAFI values for the BGP MP_REACH_NLRI.

        Returns:
            bool
        """
        return self._get_attribute('enableAfiSafi')
    @EnableAfiSafi.setter
    def EnableAfiSafi(self, value):
        self._set_attribute('enableAfiSafi', value)

    @property
    def EnablePrefix(self):
        """If enabled, BGP Prefix Filters configured in this dialog will be used to filter for routes that match those filter entries. Only those routes will be stored in the routing table. If disabled, all learned BGP routes will be stored.

        Returns:
            bool
        """
        return self._get_attribute('enablePrefix')
    @EnablePrefix.setter
    def EnablePrefix(self, value):
        self._set_attribute('enablePrefix', value)

    @property
    def Safi(self):
        """Subsequent Address Family Identifier value. Used with, and provides additional information about, the AFI in the NLRI, per RFC 2858.

        Returns:
            number
        """
        return self._get_attribute('safi')
    @Safi.setter
    def Safi(self, value):
        self._set_attribute('safi', value)

    def update(self, Afi=None, EnableAfiSafi=None, EnablePrefix=None, Safi=None):
        """Updates a child instance of learnedFilter on the server.

        Args:
            Afi (number): Address Family Identifier value. Identifies the network layer protocol to be used with these routes.
            EnableAfiSafi (bool): If enabled, allows the user to set values to be used for BGP-MP - the user-specified AFI and SAFI values for the BGP MP_REACH_NLRI.
            EnablePrefix (bool): If enabled, BGP Prefix Filters configured in this dialog will be used to filter for routes that match those filter entries. Only those routes will be stored in the routing table. If disabled, all learned BGP routes will be stored.
            Safi (number): Subsequent Address Family Identifier value. Used with, and provides additional information about, the AFI in the NLRI, per RFC 2858.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
