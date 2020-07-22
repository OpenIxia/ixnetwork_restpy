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


class Egress(Base):
    """Sets the behavior and values for egress router destination route ranges.
    The Egress class encapsulates a required egress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egress'
    _SDM_ATT_MAP = {
        'Bandwidth': 'bandwidth',
        'EgressBehavior': 'egressBehavior',
        'EnableFixedLabelForResv': 'enableFixedLabelForResv',
        'LabelValue': 'labelValue',
        'PathErrorTlv': 'pathErrorTlv',
        'ReflectRro': 'reflectRro',
        'RefreshInterval': 'refreshInterval',
        'ReservationStyle': 'reservationStyle',
        'ReservationTearTlv': 'reservationTearTlv',
        'ReservationTlv': 'reservationTlv',
        'Rro': 'rro',
        'SendResvConfirmation': 'sendResvConfirmation',
        'TimeoutMultiplier': 'timeoutMultiplier',
    }

    def __init__(self, parent):
        super(Egress, self).__init__(parent)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - number: The requested bandwidth for the tunnel, expressed in kbits per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bandwidth'])
    @Bandwidth.setter
    def Bandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bandwidth'], value)

    @property
    def EgressBehavior(self):
        """
        Returns
        -------
        - str(alwaysUseConfiguredStyle | useSeWhenIndicatedInSessionAttribute): Dictates the RSVP reservation style when the value of behavior is rsvpEgress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressBehavior'])
    @EgressBehavior.setter
    def EgressBehavior(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EgressBehavior'], value)

    @property
    def EnableFixedLabelForResv(self):
        """
        Returns
        -------
        - bool: Enables the use of a fixed label in RESV messages while in Egress mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFixedLabelForResv'])
    @EnableFixedLabelForResv.setter
    def EnableFixedLabelForResv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFixedLabelForResv'], value)

    @property
    def LabelValue(self):
        """
        Returns
        -------
        - str: RSVP label for IPV4 and IPv6 RSVP related routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelValue'])
    @LabelValue.setter
    def LabelValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelValue'], value)

    @property
    def PathErrorTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): When signaling fails in the head-end area, a path error message is sent to the head-end.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathErrorTlv'])
    @PathErrorTlv.setter
    def PathErrorTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathErrorTlv'], value)

    @property
    def ReflectRro(self):
        """
        Returns
        -------
        - bool: Enables the reflection of a received RRO object for Egress mode destination ranges. When selected, any RRO items added with addRroItem are ignored. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReflectRro'])
    @ReflectRro.setter
    def ReflectRro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReflectRro'], value)

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - number: When the destination range is used in Egress mode, this indicates the time, in seconds, between the simulated router's message to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RefreshInterval'])
    @RefreshInterval.setter
    def RefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RefreshInterval'], value)

    @property
    def ReservationStyle(self):
        """
        Returns
        -------
        - str(se | ff | wf): The reservation style desired. One of the following options: rsvpFF (fixed filtered mode) or rsvpSE (shared explicit mode).
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationStyle'])
    @ReservationStyle.setter
    def ReservationStyle(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReservationStyle'], value)

    @property
    def ReservationTearTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): a set of custom TLVs to be included in RESV TEAR messages. These may only be used for egress routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationTearTlv'])
    @ReservationTearTlv.setter
    def ReservationTearTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReservationTearTlv'], value)

    @property
    def ReservationTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): a set of custom TLVs to be included in RESV messages. These may only be used for egress routers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReservationTlv'])
    @ReservationTlv.setter
    def ReservationTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReservationTlv'], value)

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
    def SendResvConfirmation(self):
        """
        Returns
        -------
        - bool: Enables the generation of RESV Confirmation messages for received RESV messages which contain a RESV Confirmation Class object. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendResvConfirmation'])
    @SendResvConfirmation.setter
    def SendResvConfirmation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendResvConfirmation'], value)

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - number: The number of Hellos before a router is declared dead.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'])
    @TimeoutMultiplier.setter
    def TimeoutMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'], value)

    def update(self, Bandwidth=None, EgressBehavior=None, EnableFixedLabelForResv=None, LabelValue=None, PathErrorTlv=None, ReflectRro=None, RefreshInterval=None, ReservationStyle=None, ReservationTearTlv=None, ReservationTlv=None, Rro=None, SendResvConfirmation=None, TimeoutMultiplier=None):
        """Updates egress resource on the server.

        Args
        ----
        - Bandwidth (number): The requested bandwidth for the tunnel, expressed in kbits per second.
        - EgressBehavior (str(alwaysUseConfiguredStyle | useSeWhenIndicatedInSessionAttribute)): Dictates the RSVP reservation style when the value of behavior is rsvpEgress.
        - EnableFixedLabelForResv (bool): Enables the use of a fixed label in RESV messages while in Egress mode.
        - LabelValue (str): RSVP label for IPV4 and IPv6 RSVP related routes.
        - PathErrorTlv (list(dict(arg1:number,arg2:number,arg3:str))): When signaling fails in the head-end area, a path error message is sent to the head-end.
        - ReflectRro (bool): Enables the reflection of a received RRO object for Egress mode destination ranges. When selected, any RRO items added with addRroItem are ignored. (default = true)
        - RefreshInterval (number): When the destination range is used in Egress mode, this indicates the time, in seconds, between the simulated router's message to the DUT.
        - ReservationStyle (str(se | ff | wf)): The reservation style desired. One of the following options: rsvpFF (fixed filtered mode) or rsvpSE (shared explicit mode).
        - ReservationTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): a set of custom TLVs to be included in RESV TEAR messages. These may only be used for egress routers.
        - ReservationTlv (list(dict(arg1:number,arg2:number,arg3:str))): a set of custom TLVs to be included in RESV messages. These may only be used for egress routers.
        - Rro (list(dict(arg1:str[ip | label],arg2:str,arg3:bool,arg4:bool,arg5:number,arg6:bool,arg7:bool,arg8:bool))): If enabled, an RRO is reflected back to the originating router.
        - SendResvConfirmation (bool): Enables the generation of RESV Confirmation messages for received RESV messages which contain a RESV Confirmation Class object. (default = false)
        - TimeoutMultiplier (number): The number of Hellos before a router is declared dead.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
