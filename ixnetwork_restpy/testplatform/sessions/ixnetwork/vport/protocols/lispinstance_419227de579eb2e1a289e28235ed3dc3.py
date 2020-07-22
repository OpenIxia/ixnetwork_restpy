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


class LispInstance(Base):
    """It gives details about the lisp instance
    The LispInstance class encapsulates a list of lispInstance resources that are managed by the user.
    A list of resources can be retrieved from the server using the LispInstance.find() method.
    The list can be managed by using the LispInstance.add() and LispInstance.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lispInstance'
    _SDM_ATT_MAP = {
        'Act': 'act',
        'AllowAllEids': 'allowAllEids',
        'AuthenticationAlgorithm': 'authenticationAlgorithm',
        'AuthoritativeBit': 'authoritativeBit',
        'AutoComposeNegativeMapReply': 'autoComposeNegativeMapReply',
        'Enabled': 'enabled',
        'EtrRegistrationTimeout': 'etrRegistrationTimeout',
        'InstanceId': 'instanceId',
        'InternalMsmrSelectionMode': 'internalMsmrSelectionMode',
        'Key': 'key',
        'MapVersionNumber': 'mapVersionNumber',
        'Reserved': 'reserved',
        'Rsvd': 'rsvd',
        'Ttl': 'ttl',
    }

    def __init__(self, parent):
        super(LispInstance, self).__init__(parent)

    @property
    def ItrRemoteEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.itrremoteeidrange_f713a24feb8e6a2058e9d6f50f614ce6.ItrRemoteEidRange): An instance of the ItrRemoteEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.itrremoteeidrange_f713a24feb8e6a2058e9d6f50f614ce6 import ItrRemoteEidRange
        return ItrRemoteEidRange(self)

    @property
    def LocalEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.localeidrange_dc2d1edbb78f7c9d0e9e72c824fb0a89.LocalEidRange): An instance of the LocalEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.localeidrange_dc2d1edbb78f7c9d0e9e72c824fb0a89 import LocalEidRange
        return LocalEidRange(self)

    @property
    def MapServerResolver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapserverresolver_ad857cfda2776434bb4efa2d2acc6bd3.MapServerResolver): An instance of the MapServerResolver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapserverresolver_ad857cfda2776434bb4efa2d2acc6bd3 import MapServerResolver
        return MapServerResolver(self)

    @property
    def MsAllowedEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msallowedeidrange_d7ef31dcb7d27b4eac8f51adc40c137c.MsAllowedEidRange): An instance of the MsAllowedEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msallowedeidrange_d7ef31dcb7d27b4eac8f51adc40c137c import MsAllowedEidRange
        return MsAllowedEidRange(self)

    @property
    def Act(self):
        """
        Returns
        -------
        - str(noAction | nativelyForward | sendMapRequest | drop): It gives details about the action
        """
        return self._get_attribute(self._SDM_ATT_MAP['Act'])
    @Act.setter
    def Act(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Act'], value)

    @property
    def AllowAllEids(self):
        """
        Returns
        -------
        - bool: It allows all the eids
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowAllEids'])
    @AllowAllEids.setter
    def AllowAllEids(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllowAllEids'], value)

    @property
    def AuthenticationAlgorithm(self):
        """
        Returns
        -------
        - str(sha-1-96 | sha-128-256): It gives details about the authentication algorithm
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationAlgorithm'])
    @AuthenticationAlgorithm.setter
    def AuthenticationAlgorithm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationAlgorithm'], value)

    @property
    def AuthoritativeBit(self):
        """
        Returns
        -------
        - bool: If true, it enables the authoritative bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthoritativeBit'])
    @AuthoritativeBit.setter
    def AuthoritativeBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthoritativeBit'], value)

    @property
    def AutoComposeNegativeMapReply(self):
        """
        Returns
        -------
        - bool: If true, it enables the auto compose negative map reply
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoComposeNegativeMapReply'])
    @AutoComposeNegativeMapReply.setter
    def AutoComposeNegativeMapReply(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoComposeNegativeMapReply'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EtrRegistrationTimeout(self):
        """
        Returns
        -------
        - number: It gives the etr registration timeout
        """
        return self._get_attribute(self._SDM_ATT_MAP['EtrRegistrationTimeout'])
    @EtrRegistrationTimeout.setter
    def EtrRegistrationTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EtrRegistrationTimeout'], value)

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - str: It gives the instance id
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceId'])
    @InstanceId.setter
    def InstanceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstanceId'], value)

    @property
    def InternalMsmrSelectionMode(self):
        """
        Returns
        -------
        - str(allMsmrInSameIxiaPort | custom | none): it gives the details about the internal Msmr selection mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalMsmrSelectionMode'])
    @InternalMsmrSelectionMode.setter
    def InternalMsmrSelectionMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternalMsmrSelectionMode'], value)

    @property
    def Key(self):
        """
        Returns
        -------
        - str: It gives details about the key
        """
        return self._get_attribute(self._SDM_ATT_MAP['Key'])
    @Key.setter
    def Key(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Key'], value)

    @property
    def MapVersionNumber(self):
        """
        Returns
        -------
        - number: It gives details about the map version number
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapVersionNumber'])
    @MapVersionNumber.setter
    def MapVersionNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapVersionNumber'], value)

    @property
    def Reserved(self):
        """
        Returns
        -------
        - number: It gives details about the reserved protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reserved'])
    @Reserved.setter
    def Reserved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Reserved'], value)

    @property
    def Rsvd(self):
        """
        Returns
        -------
        - number: It gives details about the rsvd
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rsvd'])
    @Rsvd.setter
    def Rsvd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rsvd'], value)

    @property
    def Ttl(self):
        """
        Returns
        -------
        - number: It gives details about the ttl
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ttl'])
    @Ttl.setter
    def Ttl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ttl'], value)

    def update(self, Act=None, AllowAllEids=None, AuthenticationAlgorithm=None, AuthoritativeBit=None, AutoComposeNegativeMapReply=None, Enabled=None, EtrRegistrationTimeout=None, InstanceId=None, InternalMsmrSelectionMode=None, Key=None, MapVersionNumber=None, Reserved=None, Rsvd=None, Ttl=None):
        """Updates lispInstance resource on the server.

        Args
        ----
        - Act (str(noAction | nativelyForward | sendMapRequest | drop)): It gives details about the action
        - AllowAllEids (bool): It allows all the eids
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - AuthoritativeBit (bool): If true, it enables the authoritative bit
        - AutoComposeNegativeMapReply (bool): If true, it enables the auto compose negative map reply
        - Enabled (bool): If true, it enables the protocol
        - EtrRegistrationTimeout (number): It gives the etr registration timeout
        - InstanceId (str): It gives the instance id
        - InternalMsmrSelectionMode (str(allMsmrInSameIxiaPort | custom | none)): it gives the details about the internal Msmr selection mode
        - Key (str): It gives details about the key
        - MapVersionNumber (number): It gives details about the map version number
        - Reserved (number): It gives details about the reserved protocols
        - Rsvd (number): It gives details about the rsvd
        - Ttl (number): It gives details about the ttl

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Act=None, AllowAllEids=None, AuthenticationAlgorithm=None, AuthoritativeBit=None, AutoComposeNegativeMapReply=None, Enabled=None, EtrRegistrationTimeout=None, InstanceId=None, InternalMsmrSelectionMode=None, Key=None, MapVersionNumber=None, Reserved=None, Rsvd=None, Ttl=None):
        """Adds a new lispInstance resource on the server and adds it to the container.

        Args
        ----
        - Act (str(noAction | nativelyForward | sendMapRequest | drop)): It gives details about the action
        - AllowAllEids (bool): It allows all the eids
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - AuthoritativeBit (bool): If true, it enables the authoritative bit
        - AutoComposeNegativeMapReply (bool): If true, it enables the auto compose negative map reply
        - Enabled (bool): If true, it enables the protocol
        - EtrRegistrationTimeout (number): It gives the etr registration timeout
        - InstanceId (str): It gives the instance id
        - InternalMsmrSelectionMode (str(allMsmrInSameIxiaPort | custom | none)): it gives the details about the internal Msmr selection mode
        - Key (str): It gives details about the key
        - MapVersionNumber (number): It gives details about the map version number
        - Reserved (number): It gives details about the reserved protocols
        - Rsvd (number): It gives details about the rsvd
        - Ttl (number): It gives details about the ttl

        Returns
        -------
        - self: This instance with all currently retrieved lispInstance resources using find and the newly added lispInstance resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lispInstance resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Act=None, AllowAllEids=None, AuthenticationAlgorithm=None, AuthoritativeBit=None, AutoComposeNegativeMapReply=None, Enabled=None, EtrRegistrationTimeout=None, InstanceId=None, InternalMsmrSelectionMode=None, Key=None, MapVersionNumber=None, Reserved=None, Rsvd=None, Ttl=None):
        """Finds and retrieves lispInstance resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lispInstance resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lispInstance resources from the server.

        Args
        ----
        - Act (str(noAction | nativelyForward | sendMapRequest | drop)): It gives details about the action
        - AllowAllEids (bool): It allows all the eids
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - AuthoritativeBit (bool): If true, it enables the authoritative bit
        - AutoComposeNegativeMapReply (bool): If true, it enables the auto compose negative map reply
        - Enabled (bool): If true, it enables the protocol
        - EtrRegistrationTimeout (number): It gives the etr registration timeout
        - InstanceId (str): It gives the instance id
        - InternalMsmrSelectionMode (str(allMsmrInSameIxiaPort | custom | none)): it gives the details about the internal Msmr selection mode
        - Key (str): It gives details about the key
        - MapVersionNumber (number): It gives details about the map version number
        - Reserved (number): It gives details about the reserved protocols
        - Rsvd (number): It gives details about the rsvd
        - Ttl (number): It gives details about the ttl

        Returns
        -------
        - self: This instance with matching lispInstance resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lispInstance data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lispInstance resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
