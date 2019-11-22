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


class VepaGlobals(Base):
    """Global settings for VEPA protocol.
    The VepaGlobals class encapsulates a list of vepaGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VepaGlobals.find() method.
    The list can be managed by the user by using the VepaGlobals.add() and VepaGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vepaGlobals'

    def __init__(self, parent):
        super(VepaGlobals, self).__init__(parent)

    @property
    def AllowCvlan0InFilter(self):
        """If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.

        Returns:
            bool
        """
        return self._get_attribute('allowCvlan0InFilter')
    @AllowCvlan0InFilter.setter
    def AllowCvlan0InFilter(self, value):
        self._set_attribute('allowCvlan0InFilter', value)

    @property
    def CdcpSubtype(self):
        """1 byte value used for encapsulating CDCP TLV subtype.

        Returns:
            str
        """
        return self._get_attribute('cdcpSubtype')
    @CdcpSubtype.setter
    def CdcpSubtype(self, value):
        self._set_attribute('cdcpSubtype', value)

    @property
    def EvbSubtype(self):
        """1 byte value used for encapsulating EVB TLV subtype.

        Returns:
            str
        """
        return self._get_attribute('evbSubtype')
    @EvbSubtype.setter
    def EvbSubtype(self, value):
        self._set_attribute('evbSubtype', value)

    @property
    def GroupVdpTlvs(self):
        """Put multiple VDP TLVs in a single ECP packet.

        Returns:
            bool
        """
        return self._get_attribute('groupVdpTlvs')
    @GroupVdpTlvs.setter
    def GroupVdpTlvs(self, value):
        self._set_attribute('groupVdpTlvs', value)

    @property
    def MaxVdpCommands(self):
        """Max Outstanding VDP Commands.

        Returns:
            number
        """
        return self._get_attribute('maxVdpCommands')
    @MaxVdpCommands.setter
    def MaxVdpCommands(self, value):
        self._set_attribute('maxVdpCommands', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Oui(self):
        """3 byte value used for encapsulating LLDP packets for CDCP and EVB.

        Returns:
            str
        """
        return self._get_attribute('oui')
    @Oui.setter
    def Oui(self, value):
        self._set_attribute('oui', value)

    @property
    def RetryFailedSessions(self):
        """When enabled, keep on retrying sessions that are failed or timed out.

        Returns:
            bool
        """
        return self._get_attribute('retryFailedSessions')
    @RetryFailedSessions.setter
    def RetryFailedSessions(self, value):
        self._set_attribute('retryFailedSessions', value)

    @property
    def RetryFailedSessionsInterval(self):
        """Retry failed sessions will be made at this value's interval (in miliseconds).

        Returns:
            number
        """
        return self._get_attribute('retryFailedSessionsInterval')
    @RetryFailedSessionsInterval.setter
    def RetryFailedSessionsInterval(self, value):
        self._set_attribute('retryFailedSessionsInterval', value)

    @property
    def SetupRate(self):
        """Setup rate is the number of VSIs to start in each second.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def SuppressEvbTlv(self):
        """When enabled, the LLDP message containing the EVB TLV will not be sent.

        Returns:
            bool
        """
        return self._get_attribute('suppressEvbTlv')
    @SuppressEvbTlv.setter
    def SuppressEvbTlv(self, value):
        self._set_attribute('suppressEvbTlv', value)

    @property
    def TagDefaultEr(self):
        """All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.

        Returns:
            bool
        """
        return self._get_attribute('tagDefaultEr')
    @TagDefaultEr.setter
    def TagDefaultEr(self, value):
        self._set_attribute('tagDefaultEr', value)

    @property
    def TeardownRate(self):
        """Teardown rate is the number of VSIs to stop in each second.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Updates a child instance of vepaGlobals on the server.

        Args:
            AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
            CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
            EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
            GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
            RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
            RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
            TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Adds a new vepaGlobals node on the server and retrieves it in this instance.

        Args:
            AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
            CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
            EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
            GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
            RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
            RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
            TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns:
            self: This instance with all currently retrieved vepaGlobals data using find and the newly added vepaGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vepaGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AllowCvlan0InFilter=None, CdcpSubtype=None, EvbSubtype=None, GroupVdpTlvs=None, MaxVdpCommands=None, ObjectId=None, Oui=None, RetryFailedSessions=None, RetryFailedSessionsInterval=None, SetupRate=None, SuppressEvbTlv=None, TagDefaultEr=None, TeardownRate=None):
        """Finds and retrieves vepaGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve vepaGlobals data from the server.
        By default the find method takes no parameters and will retrieve all vepaGlobals data from the server.

        Args:
            AllowCvlan0InFilter (bool): If checked, VDP will send the exact VDP filter list, as configured in applicoation. If unchecked, VDP will detect Filters with multiple entries that contain C-VLAN 0 and will replace the entire filter list with C-VLAN 0, as specified in 802.1Qbg standard.
            CdcpSubtype (str): 1 byte value used for encapsulating CDCP TLV subtype.
            EvbSubtype (str): 1 byte value used for encapsulating EVB TLV subtype.
            GroupVdpTlvs (bool): Put multiple VDP TLVs in a single ECP packet.
            MaxVdpCommands (number): Max Outstanding VDP Commands.
            ObjectId (str): Unique identifier for this object
            Oui (str): 3 byte value used for encapsulating LLDP packets for CDCP and EVB.
            RetryFailedSessions (bool): When enabled, keep on retrying sessions that are failed or timed out.
            RetryFailedSessionsInterval (number): Retry failed sessions will be made at this value's interval (in miliseconds).
            SetupRate (number): Setup rate is the number of VSIs to start in each second.
            SuppressEvbTlv (bool): When enabled, the LLDP message containing the EVB TLV will not be sent.
            TagDefaultEr (bool): All packets originated from default ER are tagged with VLAN 1 when option is checked and untagged when option is unchecked.
            TeardownRate (number): Teardown rate is the number of VSIs to stop in each second.

        Returns:
            self: This instance with matching vepaGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vepaGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vepaGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
