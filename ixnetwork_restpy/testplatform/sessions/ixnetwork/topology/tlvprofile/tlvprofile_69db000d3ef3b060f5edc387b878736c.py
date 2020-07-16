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


class TlvProfile(Base):
    """Tlv profile functionality is contained under this node
    The TlvProfile class encapsulates a list of tlvProfile resources that are managed by the system.
    A list of resources can be retrieved from the server using the TlvProfile.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'tlvProfile'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(TlvProfile, self).__init__(parent)

    @property
    def DefaultTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.defaulttlv_8e41257d3d01ec013783dd0fd6697862.DefaultTlv): An instance of the DefaultTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.defaulttlv_8e41257d3d01ec013783dd0fd6697862 import DefaultTlv
        return DefaultTlv(self)

    @property
    def Tlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlv_d2b702d35a057ccb264f716c5f342298.Tlv): An instance of the Tlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlv_d2b702d35a057ccb264f716c5f342298 import Tlv
        return Tlv(self)

    def find(self):
        """Finds and retrieves tlvProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tlvProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tlvProfile resources from the server.

        Returns
        -------
        - self: This instance with matching tlvProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tlvProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tlvProfile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CopyTlv(self, *args, **kwargs):
        """Executes the copyTlv operation on the server.

        Copy a template tlv to a topology tlv profile

        copyTlv(Arg2=href)href
        ----------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/globals/.../topology)): An object reference to a source template tlv
        - Returns str(None): An object reference to the newly created topology tlv as a result of the copy operation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('copyTlv', payload=payload, response_object=None)
