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


class LispInstance(Base):
    """It gives details about the lisp instance
    The LispInstance class encapsulates a list of lispInstance resources that are managed by the user.
    A list of resources can be retrieved from the server using the LispInstance.find() method.
    The list can be managed by using the LispInstance.add() and LispInstance.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lispInstance'

    def __init__(self, parent):
        super(LispInstance, self).__init__(parent)

    @property
    def ItrRemoteEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.itrremoteeidrange_52da09c5d85a9714cdfc8193b118f1ca.ItrRemoteEidRange): An instance of the ItrRemoteEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.itrremoteeidrange_52da09c5d85a9714cdfc8193b118f1ca import ItrRemoteEidRange
        return ItrRemoteEidRange(self)

    @property
    def LocalEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.localeidrange_c70c39ff6c1dafcbb8b3452542238044.LocalEidRange): An instance of the LocalEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.localeidrange_c70c39ff6c1dafcbb8b3452542238044 import LocalEidRange
        return LocalEidRange(self)

    @property
    def MapServerResolver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapserverresolver_0b082fe96a080b425b8ce968386c7dda.MapServerResolver): An instance of the MapServerResolver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapserverresolver_0b082fe96a080b425b8ce968386c7dda import MapServerResolver
        return MapServerResolver(self)

    @property
    def MsAllowedEidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msallowedeidrange_914a04e5d41b69640f681c05be1957cb.MsAllowedEidRange): An instance of the MsAllowedEidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msallowedeidrange_914a04e5d41b69640f681c05be1957cb import MsAllowedEidRange
        return MsAllowedEidRange(self)

    @property
    def Act(self):
        """
        Returns
        -------
        - str(noAction | nativelyForward | sendMapRequest | drop): It gives details about the action
        """
        return self._get_attribute('act')
    @Act.setter
    def Act(self, value):
        self._set_attribute('act', value)

    @property
    def AllowAllEids(self):
        """
        Returns
        -------
        - bool: It allows all the eids
        """
        return self._get_attribute('allowAllEids')
    @AllowAllEids.setter
    def AllowAllEids(self, value):
        self._set_attribute('allowAllEids', value)

    @property
    def AuthenticationAlgorithm(self):
        """
        Returns
        -------
        - str(sha-1-96 | sha-128-256): It gives details about the authentication algorithm
        """
        return self._get_attribute('authenticationAlgorithm')
    @AuthenticationAlgorithm.setter
    def AuthenticationAlgorithm(self, value):
        self._set_attribute('authenticationAlgorithm', value)

    @property
    def AuthoritativeBit(self):
        """
        Returns
        -------
        - bool: If true, it enables the authoritative bit
        """
        return self._get_attribute('authoritativeBit')
    @AuthoritativeBit.setter
    def AuthoritativeBit(self, value):
        self._set_attribute('authoritativeBit', value)

    @property
    def AutoComposeNegativeMapReply(self):
        """
        Returns
        -------
        - bool: If true, it enables the auto compose negative map reply
        """
        return self._get_attribute('autoComposeNegativeMapReply')
    @AutoComposeNegativeMapReply.setter
    def AutoComposeNegativeMapReply(self, value):
        self._set_attribute('autoComposeNegativeMapReply', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the protocol
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def EtrRegistrationTimeout(self):
        """
        Returns
        -------
        - number: It gives the etr registration timeout
        """
        return self._get_attribute('etrRegistrationTimeout')
    @EtrRegistrationTimeout.setter
    def EtrRegistrationTimeout(self, value):
        self._set_attribute('etrRegistrationTimeout', value)

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - str: It gives the instance id
        """
        return self._get_attribute('instanceId')
    @InstanceId.setter
    def InstanceId(self, value):
        self._set_attribute('instanceId', value)

    @property
    def InternalMsmrSelectionMode(self):
        """
        Returns
        -------
        - str(allMsmrInSameIxiaPort | custom | none): it gives the details about the internal Msmr selection mode
        """
        return self._get_attribute('internalMsmrSelectionMode')
    @InternalMsmrSelectionMode.setter
    def InternalMsmrSelectionMode(self, value):
        self._set_attribute('internalMsmrSelectionMode', value)

    @property
    def Key(self):
        """
        Returns
        -------
        - str: It gives details about the key
        """
        return self._get_attribute('key')
    @Key.setter
    def Key(self, value):
        self._set_attribute('key', value)

    @property
    def MapVersionNumber(self):
        """
        Returns
        -------
        - number: It gives details about the map version number
        """
        return self._get_attribute('mapVersionNumber')
    @MapVersionNumber.setter
    def MapVersionNumber(self, value):
        self._set_attribute('mapVersionNumber', value)

    @property
    def Reserved(self):
        """
        Returns
        -------
        - number: It gives details about the reserved protocols
        """
        return self._get_attribute('reserved')
    @Reserved.setter
    def Reserved(self, value):
        self._set_attribute('reserved', value)

    @property
    def Rsvd(self):
        """
        Returns
        -------
        - number: It gives details about the rsvd
        """
        return self._get_attribute('rsvd')
    @Rsvd.setter
    def Rsvd(self, value):
        self._set_attribute('rsvd', value)

    @property
    def Ttl(self):
        """
        Returns
        -------
        - number: It gives details about the ttl
        """
        return self._get_attribute('ttl')
    @Ttl.setter
    def Ttl(self, value):
        self._set_attribute('ttl', value)

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
        return self._update(locals())

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
        return self._create(locals())

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
        return self._select(locals())

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
