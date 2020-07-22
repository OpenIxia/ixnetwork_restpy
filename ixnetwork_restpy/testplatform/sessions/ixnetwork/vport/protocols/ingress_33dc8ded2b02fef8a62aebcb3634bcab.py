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


class Ingress(Base):
    """Sets the default behavior and configuration of ingress router destination route ranges.
    The Ingress class encapsulates a required ingress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ingress'
    _SDM_ATT_MAP = {
        'EnableEro': 'enableEro',
        'Ero': 'ero',
        'PrefixLength': 'prefixLength',
        'PrependDutToEro': 'prependDutToEro',
        'ReservationErrorTlv': 'reservationErrorTlv',
        'Rro': 'rro',
        'SendRro': 'sendRro',
        'TunnelIdsCount': 'tunnelIdsCount',
        'TunnelIdsStart': 'tunnelIdsStart',
    }

    def __init__(self, parent):
        super(Ingress, self).__init__(parent)

    @property
    def SenderRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.senderrange_15dfd9e6673a6986869f84e8c22d0879.SenderRange): An instance of the SenderRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.senderrange_15dfd9e6673a6986869f84e8c22d0879 import SenderRange
        return SenderRange(self)

    @property
    def EnableEro(self):
        """
        Returns
        -------
        - bool: Enables use of the ERO option in Ingress mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEro'])
    @EnableEro.setter
    def EnableEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEro'], value)

    @property
    def Ero(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ip | as],arg2:str,arg3:number,arg4:bool)): Enables use of the ERO option in Ingress mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ero'])
    @Ero.setter
    def Ero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ero'], value)

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: If the DUT's address is to be prepended to the ERO list, this indicates what prefix length is to be used for the entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixLength'], value)

    @property
    def PrependDutToEro(self):
        """
        Returns
        -------
        - str(none | prependLoose | prependStrict): Enables the user to insert the DUT address at the beginning of the list of hops in the path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrependDutToEro'])
    @PrependDutToEro.setter
    def PrependDutToEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrependDutToEro'], value)

    @property
    def ReservationErrorTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): a set of custom TLVs to be included in RESV ERR messages. These may only be used for ingress routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationErrorTlv'])
    @ReservationErrorTlv.setter
    def ReservationErrorTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReservationErrorTlv'], value)

    @property
    def Rro(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ip | label],arg2:str,arg3:bool,arg4:bool,arg5:number,arg6:bool,arg7:bool,arg8:bool)): If enabled, an RRO is reflected back to the originating router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rro'])
    @Rro.setter
    def Rro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rro'], value)

    @property
    def SendRro(self):
        """
        Returns
        -------
        - bool: When the destination range is used in Ingress mode, this indicates that a SEND RRO option is to be included in RSVP messages sent downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendRro'])
    @SendRro.setter
    def SendRro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendRro'], value)

    @property
    def TunnelIdsCount(self):
        """
        Returns
        -------
        - number: The number of destination routers. Each router's address is one greater than the previous one's.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdsCount'])
    @TunnelIdsCount.setter
    def TunnelIdsCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdsCount'], value)

    @property
    def TunnelIdsStart(self):
        """
        Returns
        -------
        - number: Sets the start of the range of Tunnel IDs to be used in simulations.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIdsStart'])
    @TunnelIdsStart.setter
    def TunnelIdsStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIdsStart'], value)

    def update(self, EnableEro=None, Ero=None, PrefixLength=None, PrependDutToEro=None, ReservationErrorTlv=None, Rro=None, SendRro=None, TunnelIdsCount=None, TunnelIdsStart=None):
        """Updates ingress resource on the server.

        Args
        ----
        - EnableEro (bool): Enables use of the ERO option in Ingress mode.
        - Ero (list(dict(arg1:str[ip | as],arg2:str,arg3:number,arg4:bool))): Enables use of the ERO option in Ingress mode.
        - PrefixLength (number): If the DUT's address is to be prepended to the ERO list, this indicates what prefix length is to be used for the entry.
        - PrependDutToEro (str(none | prependLoose | prependStrict)): Enables the user to insert the DUT address at the beginning of the list of hops in the path.
        - ReservationErrorTlv (list(dict(arg1:number,arg2:number,arg3:str))): a set of custom TLVs to be included in RESV ERR messages. These may only be used for ingress routers.
        - Rro (list(dict(arg1:str[ip | label],arg2:str,arg3:bool,arg4:bool,arg5:number,arg6:bool,arg7:bool,arg8:bool))): If enabled, an RRO is reflected back to the originating router.
        - SendRro (bool): When the destination range is used in Ingress mode, this indicates that a SEND RRO option is to be included in RSVP messages sent downstream.
        - TunnelIdsCount (number): The number of destination routers. Each router's address is one greater than the previous one's.
        - TunnelIdsStart (number): Sets the start of the range of Tunnel IDs to be used in simulations.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
