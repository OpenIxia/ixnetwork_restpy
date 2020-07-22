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


class MapServerCacheInfo(Base):
    """It gives details about the map server cache info
    The MapServerCacheInfo class encapsulates a list of mapServerCacheInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the MapServerCacheInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'mapServerCacheInfo'
    _SDM_ATT_MAP = {
        'Action': 'action',
        'EidPrefix': 'eidPrefix',
        'EidPrefixAfi': 'eidPrefixAfi',
        'EidPrefixLength': 'eidPrefixLength',
        'EtrIp': 'etrIp',
        'ExpiresAfter': 'expiresAfter',
        'InstanceId': 'instanceId',
        'Ipv4ErrorMapRegisterRx': 'ipv4ErrorMapRegisterRx',
        'Ipv4MapNotifyTx': 'ipv4MapNotifyTx',
        'Ipv4MapRegisterRx': 'ipv4MapRegisterRx',
        'Ipv4MapRequestDropped': 'ipv4MapRequestDropped',
        'Ipv6ErrorMapRegisterRx': 'ipv6ErrorMapRegisterRx',
        'Ipv6MapNotifyTx': 'ipv6MapNotifyTx',
        'Ipv6MapRegisterRx': 'ipv6MapRegisterRx',
        'Ipv6MapRequestDropped': 'ipv6MapRequestDropped',
        'Key': 'key',
        'MapVersionNumber': 'mapVersionNumber',
        'ProxyMapReply': 'proxyMapReply',
        'WantMapNotify': 'wantMapNotify',
    }

    def __init__(self, parent):
        super(MapServerCacheInfo, self).__init__(parent)

    @property
    def RemoteLocators(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_96410d05b977962f780a8f3077813cee.RemoteLocators): An instance of the RemoteLocators class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_96410d05b977962f780a8f3077813cee import RemoteLocators
        return RemoteLocators(self)

    @property
    def Action(self):
        """
        Returns
        -------
        - str: It gives details about the action (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Action'])

    @property
    def EidPrefix(self):
        """
        Returns
        -------
        - str: It gives details about the eid prefix (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefix'])

    @property
    def EidPrefixAfi(self):
        """
        Returns
        -------
        - str: It gives details about the eid prefix Afi (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefixAfi'])

    @property
    def EidPrefixLength(self):
        """
        Returns
        -------
        - number: It gives details about the eid prefix Length (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefixLength'])

    @property
    def EtrIp(self):
        """
        Returns
        -------
        - str: It gives details about the etrlp (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EtrIp'])

    @property
    def ExpiresAfter(self):
        """
        Returns
        -------
        - str: It gives details about the expiration details (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpiresAfter'])

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - number: It gives details about the instance id (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceId'])

    @property
    def Ipv4ErrorMapRegisterRx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv4 Error Map register at receivers end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4ErrorMapRegisterRx'])

    @property
    def Ipv4MapNotifyTx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv4 Map notify at transmitters end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapNotifyTx'])

    @property
    def Ipv4MapRegisterRx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv4 Map register at receivers end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRegisterRx'])

    @property
    def Ipv4MapRequestDropped(self):
        """
        Returns
        -------
        - number: It gives details about the ipv4 Map Request dropped (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRequestDropped'])

    @property
    def Ipv6ErrorMapRegisterRx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv6 Error Map register at receivers end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ErrorMapRegisterRx'])

    @property
    def Ipv6MapNotifyTx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv6 Map notify at transmitters end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapNotifyTx'])

    @property
    def Ipv6MapRegisterRx(self):
        """
        Returns
        -------
        - number: It gives details about the ipv6 Map register at receivers end (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRegisterRx'])

    @property
    def Ipv6MapRequestDropped(self):
        """
        Returns
        -------
        - number: It gives details about the ipv6 Map Request dropped (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRequestDropped'])

    @property
    def Key(self):
        """
        Returns
        -------
        - str: It gives details about the key (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Key'])

    @property
    def MapVersionNumber(self):
        """
        Returns
        -------
        - number: It gives details map version number
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapVersionNumber'])

    @property
    def ProxyMapReply(self):
        """
        Returns
        -------
        - bool: It gives details about the proxy map reply(Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProxyMapReply'])

    @property
    def WantMapNotify(self):
        """
        Returns
        -------
        - bool: It gives details about the Map notify
        """
        return self._get_attribute(self._SDM_ATT_MAP['WantMapNotify'])

    def find(self, Action=None, EidPrefix=None, EidPrefixAfi=None, EidPrefixLength=None, EtrIp=None, ExpiresAfter=None, InstanceId=None, Ipv4ErrorMapRegisterRx=None, Ipv4MapNotifyTx=None, Ipv4MapRegisterRx=None, Ipv4MapRequestDropped=None, Ipv6ErrorMapRegisterRx=None, Ipv6MapNotifyTx=None, Ipv6MapRegisterRx=None, Ipv6MapRequestDropped=None, Key=None, MapVersionNumber=None, ProxyMapReply=None, WantMapNotify=None):
        """Finds and retrieves mapServerCacheInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mapServerCacheInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mapServerCacheInfo resources from the server.

        Args
        ----
        - Action (str): It gives details about the action (Read-Only)
        - EidPrefix (str): It gives details about the eid prefix (Read-Only)
        - EidPrefixAfi (str): It gives details about the eid prefix Afi (Read-Only)
        - EidPrefixLength (number): It gives details about the eid prefix Length (Read-Only)
        - EtrIp (str): It gives details about the etrlp (Read-Only)
        - ExpiresAfter (str): It gives details about the expiration details (Read-Only)
        - InstanceId (number): It gives details about the instance id (Read-Only)
        - Ipv4ErrorMapRegisterRx (number): It gives details about the ipv4 Error Map register at receivers end (Read-Only)
        - Ipv4MapNotifyTx (number): It gives details about the ipv4 Map notify at transmitters end (Read-Only)
        - Ipv4MapRegisterRx (number): It gives details about the ipv4 Map register at receivers end (Read-Only)
        - Ipv4MapRequestDropped (number): It gives details about the ipv4 Map Request dropped (Read-Only)
        - Ipv6ErrorMapRegisterRx (number): It gives details about the ipv6 Error Map register at receivers end (Read-Only)
        - Ipv6MapNotifyTx (number): It gives details about the ipv6 Map notify at transmitters end (Read-Only)
        - Ipv6MapRegisterRx (number): It gives details about the ipv6 Map register at receivers end (Read-Only)
        - Ipv6MapRequestDropped (number): It gives details about the ipv6 Map Request dropped (Read-Only)
        - Key (str): It gives details about the key (Read-only)
        - MapVersionNumber (number): It gives details map version number
        - ProxyMapReply (bool): It gives details about the proxy map reply(Read-Only)
        - WantMapNotify (bool): It gives details about the Map notify

        Returns
        -------
        - self: This instance with matching mapServerCacheInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mapServerCacheInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mapServerCacheInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
