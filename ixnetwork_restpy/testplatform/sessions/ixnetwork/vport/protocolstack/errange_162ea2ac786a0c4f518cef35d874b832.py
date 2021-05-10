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


class ErRange(Base):
    """Manages a range of Edge Relays.
    The ErRange class encapsulates a list of erRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the ErRange.find() method.
    The list can be managed by using the ErRange.add() and ErRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'erRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'EcpAckTimerInit': 'ecpAckTimerInit',
        'EcpMaxRetries': 'ecpMaxRetries',
        'Enabled': 'enabled',
        'ErMode': 'erMode',
        'EvbMode': 'evbMode',
        'EvbRka': 'evbRka',
        'EvbRwd': 'evbRwd',
        'Name': 'name',
        'ObjectId': 'objectId',
        'SchannelId': 'schannelId',
        'SchannelIdMac': 'schannelIdMac',
        'SchannelVlanId': 'schannelVlanId',
    }

    def __init__(self, parent):
        super(ErRange, self).__init__(parent)

    @property
    def VsiRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vsirange_89147b4a94e33164f96e37b09ee46b58.VsiRange): An instance of the VsiRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vsirange_89147b4a94e33164f96e37b09ee46b58 import VsiRange
        return VsiRange(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of ERs in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def EcpAckTimerInit(self):
        """
        Returns
        -------
        - number: This value is used by the ECP state machine to compute the timeout value for the ACK messages (milliseconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EcpAckTimerInit'])
    @EcpAckTimerInit.setter
    def EcpAckTimerInit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EcpAckTimerInit'], value)

    @property
    def EcpMaxRetries(self):
        """
        Returns
        -------
        - number: The number of times ECP will try to resend the VDP packages before failing.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EcpMaxRetries'])
    @EcpMaxRetries.setter
    def EcpMaxRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EcpMaxRetries'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ErMode(self):
        """
        Returns
        -------
        - str: Dropdown box containing the ER Modes: -VEB: An edge relay that requires reflective relay service to be disabled on the station-facing Bridge Port (SBP) of the attached Bridge; -VEPA: An edge relay that always forwards frames through its uplink relay port (URP) and that can make use of reflective relay service provided by the station-facing Bridge Port (SBP) of the attached Bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErMode'])
    @ErMode.setter
    def ErMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ErMode'], value)

    @property
    def EvbMode(self):
        """
        Returns
        -------
        - str: EVB Range's Mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvbMode'])
    @EvbMode.setter
    def EvbMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvbMode'], value)

    @property
    def EvbRka(self):
        """
        Returns
        -------
        - number: This value is used by the VDP state machine to compute the value of reinitKeepAlive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvbRka'])
    @EvbRka.setter
    def EvbRka(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvbRka'], value)

    @property
    def EvbRwd(self):
        """
        Returns
        -------
        - number: This value is used by the VDP state machine to compute the value of resourceWaitDelay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvbRwd'])
    @EvbRwd.setter
    def EvbRwd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvbRwd'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SchannelId(self):
        """
        Returns
        -------
        - number: Service Channel ID used by ER in CDCP TLV. This field isn't editable for the default ER.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SchannelId'])
    @SchannelId.setter
    def SchannelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SchannelId'], value)

    @property
    def SchannelIdMac(self):
        """
        Returns
        -------
        - str: Uplink Relay Port MAC Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SchannelIdMac'])
    @SchannelIdMac.setter
    def SchannelIdMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SchannelIdMac'], value)

    @property
    def SchannelVlanId(self):
        """
        Returns
        -------
        - number: Service VLAN ID used by ER in CDCP TLV(if 0, ER will request S-VLAN from EVB Bridge). This field isn't editable for the default ER.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SchannelVlanId'])
    @SchannelVlanId.setter
    def SchannelVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SchannelVlanId'], value)

    def update(self, Count=None, EcpAckTimerInit=None, EcpMaxRetries=None, Enabled=None, ErMode=None, EvbMode=None, EvbRka=None, EvbRwd=None, Name=None, SchannelId=None, SchannelIdMac=None, SchannelVlanId=None):
        """Updates erRange resource on the server.

        Args
        ----
        - Count (number): The number of ERs in the range.
        - EcpAckTimerInit (number): This value is used by the ECP state machine to compute the timeout value for the ACK messages (milliseconds).
        - EcpMaxRetries (number): The number of times ECP will try to resend the VDP packages before failing.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ErMode (str): Dropdown box containing the ER Modes: -VEB: An edge relay that requires reflective relay service to be disabled on the station-facing Bridge Port (SBP) of the attached Bridge; -VEPA: An edge relay that always forwards frames through its uplink relay port (URP) and that can make use of reflective relay service provided by the station-facing Bridge Port (SBP) of the attached Bridge.
        - EvbMode (str): EVB Range's Mode.
        - EvbRka (number): This value is used by the VDP state machine to compute the value of reinitKeepAlive.
        - EvbRwd (number): This value is used by the VDP state machine to compute the value of resourceWaitDelay.
        - Name (str): Name of range
        - SchannelId (number): Service Channel ID used by ER in CDCP TLV. This field isn't editable for the default ER.
        - SchannelIdMac (str): Uplink Relay Port MAC Address.
        - SchannelVlanId (number): Service VLAN ID used by ER in CDCP TLV(if 0, ER will request S-VLAN from EVB Bridge). This field isn't editable for the default ER.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, EcpAckTimerInit=None, EcpMaxRetries=None, Enabled=None, ErMode=None, EvbMode=None, EvbRka=None, EvbRwd=None, Name=None, SchannelId=None, SchannelIdMac=None, SchannelVlanId=None):
        """Adds a new erRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The number of ERs in the range.
        - EcpAckTimerInit (number): This value is used by the ECP state machine to compute the timeout value for the ACK messages (milliseconds).
        - EcpMaxRetries (number): The number of times ECP will try to resend the VDP packages before failing.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ErMode (str): Dropdown box containing the ER Modes: -VEB: An edge relay that requires reflective relay service to be disabled on the station-facing Bridge Port (SBP) of the attached Bridge; -VEPA: An edge relay that always forwards frames through its uplink relay port (URP) and that can make use of reflective relay service provided by the station-facing Bridge Port (SBP) of the attached Bridge.
        - EvbMode (str): EVB Range's Mode.
        - EvbRka (number): This value is used by the VDP state machine to compute the value of reinitKeepAlive.
        - EvbRwd (number): This value is used by the VDP state machine to compute the value of resourceWaitDelay.
        - Name (str): Name of range
        - SchannelId (number): Service Channel ID used by ER in CDCP TLV. This field isn't editable for the default ER.
        - SchannelIdMac (str): Uplink Relay Port MAC Address.
        - SchannelVlanId (number): Service VLAN ID used by ER in CDCP TLV(if 0, ER will request S-VLAN from EVB Bridge). This field isn't editable for the default ER.

        Returns
        -------
        - self: This instance with all currently retrieved erRange resources using find and the newly added erRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained erRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, EcpAckTimerInit=None, EcpMaxRetries=None, Enabled=None, ErMode=None, EvbMode=None, EvbRka=None, EvbRwd=None, Name=None, ObjectId=None, SchannelId=None, SchannelIdMac=None, SchannelVlanId=None):
        """Finds and retrieves erRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve erRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all erRange resources from the server.

        Args
        ----
        - Count (number): The number of ERs in the range.
        - EcpAckTimerInit (number): This value is used by the ECP state machine to compute the timeout value for the ACK messages (milliseconds).
        - EcpMaxRetries (number): The number of times ECP will try to resend the VDP packages before failing.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - ErMode (str): Dropdown box containing the ER Modes: -VEB: An edge relay that requires reflective relay service to be disabled on the station-facing Bridge Port (SBP) of the attached Bridge; -VEPA: An edge relay that always forwards frames through its uplink relay port (URP) and that can make use of reflective relay service provided by the station-facing Bridge Port (SBP) of the attached Bridge.
        - EvbMode (str): EVB Range's Mode.
        - EvbRka (number): This value is used by the VDP state machine to compute the value of reinitKeepAlive.
        - EvbRwd (number): This value is used by the VDP state machine to compute the value of resourceWaitDelay.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - SchannelId (number): Service Channel ID used by ER in CDCP TLV. This field isn't editable for the default ER.
        - SchannelIdMac (str): Uplink Relay Port MAC Address.
        - SchannelVlanId (number): Service VLAN ID used by ER in CDCP TLV(if 0, ER will request S-VLAN from EVB Bridge). This field isn't editable for the default ER.

        Returns
        -------
        - self: This instance with matching erRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of erRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the erRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
