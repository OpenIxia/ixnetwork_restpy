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
from typing import List, Any, Union


class Static(Base):
    """This object controls the static configuration of ports.
    The Static class encapsulates a required static resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'static'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Static, self).__init__(parent, list_op)

    @property
    def Atm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_9bbaac5d21c0632b71ee4c92d14864c3.Atm): An instance of the Atm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atm_9bbaac5d21c0632b71ee4c92d14864c3 import Atm
        if self._properties.get('Atm', None) is not None:
            return self._properties.get('Atm')
        else:
            return Atm(self)

    @property
    def Fr(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_ebc5d45018c74d53700c88afea530ca2.Fr): An instance of the Fr class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.fr_ebc5d45018c74d53700c88afea530ca2 import Fr
        if self._properties.get('Fr', None) is not None:
            return self._properties.get('Fr')
        else:
            return Fr(self)

    @property
    def InterfaceGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_c2c90e7b7cf8bf4a351e197fc18ccb92.InterfaceGroup): An instance of the InterfaceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interfacegroup_c2c90e7b7cf8bf4a351e197fc18ccb92 import InterfaceGroup
        if self._properties.get('InterfaceGroup', None) is not None:
            return self._properties.get('InterfaceGroup')
        else:
            return InterfaceGroup(self)

    @property
    def Ip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_205717d3d79aa12a8dcea858982c666e.Ip): An instance of the Ip class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ip_205717d3d79aa12a8dcea858982c666e import Ip
        if self._properties.get('Ip', None) is not None:
            return self._properties.get('Ip')
        else:
            return Ip(self)

    @property
    def Lan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_a0c3771a1420d267c519e60205c6a8e6.Lan): An instance of the Lan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_a0c3771a1420d267c519e60205c6a8e6 import Lan
        if self._properties.get('Lan', None) is not None:
            return self._properties.get('Lan')
        else:
            return Lan(self)
