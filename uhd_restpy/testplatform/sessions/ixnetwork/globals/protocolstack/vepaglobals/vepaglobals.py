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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class VepaGlobals(Base):
    """Global settings for VEPA protocol.
    The VepaGlobals class encapsulates a list of vepaGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the VepaGlobals.find() method.
    The list can be managed by using the VepaGlobals.add() and VepaGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vepaGlobals'
    _SDM_ATT_MAP = {
        'AllowCvlan0InFilter': 'allowCvlan0InFilter',
        'CdcpSubtype': 'cdcpSubtype',
        'EvbSubtype': 'evbSubtype',
        'GroupVdpTlvs': 'groupVdpTlvs',
        'MaxVdpCommands': 'maxVdpCommands',
        'ObjectId': 'objectId',
        'Oui': 'oui',
        'RetryFailedSessions': 'retryFailedSessions',
        'RetryFailedSessionsInterval': 'retryFailedSessionsInterval',
        'SetupRate': 'setupRate',
        'SuppressEvbTlv': 'suppressEvbTlv',
        'TagDefaultEr': 'tagDefaultEr',
        'TeardownRate': 'teardownRate',
    }

    def __init__(self, parent):
        super(VepaGlobals, self).__init__(parent)

    @property
    def AllowCvlan0InFilter(self):
        """
        Returns
        -------
        - bool: If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowCvlan0InFilter'])
    @AllowCvlan0InFilter.setter
    def AllowCvlan0InFilter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllowCvlan0InFilter'], value)

    @property
    def CdcpSubtype(self):
        """
        Returns
        -------
        - str: 1 byte value used for encapsulating CDCP TLV subtype.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CdcpSubtype'])
    @CdcpSubtype.setter
    def CdcpSubtype(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CdcpSubtype'], value)

    @property
    def EvbSubtype(self):
        """
        Returns
        -------
        - str: 1 byte value used for encapsulating EVB TLV subtype.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvbSubtype'])
    @EvbSubtype.setter
    def EvbSubtype(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EvbSubtype'], value)

    @property
    def GroupVdpTlvs(self):
        """
        Returns
        -------
        - bool: Put multiple VDP TLVs in a single ECP packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupVdpTlvs'])
    @GroupVdpTlvs.setter
    def GroupVdpTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupVdpTlvs'], value)

    @property
    def MaxVdpCommands(self):
        """
        Returns
        -------
        - number: Max Outstanding VDP Commands.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxVdpCommands'])
    @MaxVdpCommands.setter
    def MaxVdpCommands(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxVdpCommands'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Oui(self):
        """
        Returns
        -------
        - str: 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Oui'])
    @Oui.setter
    def Oui(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Oui'], value)

    @property
    def RetryFailedSessions(self):
        """
        Returns
        -------
        - bool: When enabled, keep on retrying sessions that are failed or timed out.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryFailedSessions'])
    @RetryFailedSessions.setter
    def RetryFailedSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RetryFailedSessions'], value)

    @property
    def RetryFailedSessionsInterval(self):
        """
        Returns
        -------
        - number: Retry failed sessions will be made at this value's interval (in miliseconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryFailedSessionsInterval'])
    @RetryFailedSessionsInterval.setter
    def RetryFailedSessionsInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RetryFailedSessionsInterval'], value)

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: Setup rate is the number of VSIs to start in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def SuppressEvbTlv(self):
        """
        Returns
        -------
        - bool: When enabled, the LLDP message containing the EVB TLV will not be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SuppressEvbTlv'])
    @SuppressEvbTlv.setter
    def SuppressEvbTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SuppressEvbTlv'], value)

    @property
    def TagDefaultEr(self):
        """
        Returns
        -------
        - bool: All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TagDefaultEr'])
    @TagDefaultEr.setter
    def TagDefaultEr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TagDefaultEr'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: Teardown rate is the number of VSIs to stop in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    def update(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Updates vepaGlobals resource on the server.

        Args
        ----
        - AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
        - CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
        - EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
        - GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
        - MaxVdpCommands (number): Max Outstanding VDP Commands.
        - Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
        - RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
        - RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
        - SetupRate (number): Setup rate is the number of VSIs to start in each second.
        - SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
        - TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
        - TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Adds a new vepaGlobals resource on the server and adds it to the container.

        Args
        ----
        - AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
        - CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
        - EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
        - GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
        - MaxVdpCommands (number): Max Outstanding VDP Commands.
        - Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
        - RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
        - RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
        - SetupRate (number): Setup rate is the number of VSIs to start in each second.
        - SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
        - TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
        - TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns
        -------
        - self: This instance with all currently retrieved vepaGlobals resources using find and the newly added vepaGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vepaGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, ObjectId=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Finds and retrieves vepaGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vepaGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vepaGlobals resources from the server.

        Args
        ----
        - AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
        - CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
        - EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
        - GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
        - MaxVdpCommands (number): Max Outstanding VDP Commands.
        - ObjectId (str): Unique identifier for this object
        - Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
        - RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
        - RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
        - SetupRate (number): Setup rate is the number of VSIs to start in each second.
        - SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
        - TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
        - TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns
        -------
        - self: This instance with matching vepaGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vepaGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vepaGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
