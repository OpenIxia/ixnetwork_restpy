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


class GlobalTrafficProfiles(Base):
    """
    The GlobalTrafficProfiles class encapsulates a list of globalTrafficProfiles resources that are managed by the user.
    A list of resources can be retrieved from the server using the GlobalTrafficProfiles.find() method.
    The list can be managed by using the GlobalTrafficProfiles.add() and GlobalTrafficProfiles.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalTrafficProfiles'
    _SDM_ATT_MAP = {
        'Apn': 'apn',
        'Arp': 'arp',
        'DefaultBearerFallback': 'defaultBearerFallback',
        'EnableSessionTimeout': 'enableSessionTimeout',
        'Enabled': 'enabled',
        'Gbrd': 'gbrd',
        'Gbru': 'gbru',
        'IsMsInitiated': 'isMsInitiated',
        'Mbrd': 'mbrd',
        'Mbru': 'mbru',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Qci': 'qci',
        'RunOnDefaultBearer': 'runOnDefaultBearer',
        'STftFiltersCustom': 'sTftFiltersCustom',
        'SessionTimeoutValue': 'sessionTimeoutValue',
        'SpcoContainer': 'spcoContainer',
        'SpcoProtocol': 'spcoProtocol',
        'TearDownIndicator': 'tearDownIndicator',
        'UsePredefinedQci': 'usePredefinedQci',
        'UsePredefinedTft': 'usePredefinedTft',
    }

    def __init__(self, parent):
        super(GlobalTrafficProfiles, self).__init__(parent)

    @property
    def Apn(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApn): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Apn'])
    @Apn.setter
    def Apn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Apn'], value)

    @property
    def Arp(self):
        """
        Returns
        -------
        - number: Priority of allocation and retention
        """
        return self._get_attribute(self._SDM_ATT_MAP['Arp'])
    @Arp.setter
    def Arp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Arp'], value)

    @property
    def DefaultBearerFallback(self):
        """
        Returns
        -------
        - bool: Fallback on default bearer if no dedicated bearer was created for this activity.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultBearerFallback'])
    @DefaultBearerFallback.setter
    def DefaultBearerFallback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DefaultBearerFallback'], value)

    @property
    def EnableSessionTimeout(self):
        """
        Returns
        -------
        - bool: Deprecated. Kept for TCL bw compatibility
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSessionTimeout'])
    @EnableSessionTimeout.setter
    def EnableSessionTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSessionTimeout'], value)

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
    def Gbrd(self):
        """
        Returns
        -------
        - number: Guaranteed bitrate for downlink (kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gbrd'])
    @Gbrd.setter
    def Gbrd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gbrd'], value)

    @property
    def Gbru(self):
        """
        Returns
        -------
        - number: Guaranteed bitrate for uplink (kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gbru'])
    @Gbru.setter
    def Gbru(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gbru'], value)

    @property
    def IsMsInitiated(self):
        """
        Returns
        -------
        - bool: UE initiated service request for this activity. Execute Bearer Resource Command with TFT operation set to Create New. This option will be taken in consideration if no active bearer was found with matching TFT and QoS.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMsInitiated'])
    @IsMsInitiated.setter
    def IsMsInitiated(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsMsInitiated'], value)

    @property
    def Mbrd(self):
        """
        Returns
        -------
        - number: Maximum bitrate for downlink (kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mbrd'])
    @Mbrd.setter
    def Mbrd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mbrd'], value)

    @property
    def Mbru(self):
        """
        Returns
        -------
        - number: Maximum bitrate for uplink (kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mbru'])
    @Mbru.setter
    def Mbru(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mbru'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: GTP needs the name of the activity
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
    def Qci(self):
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP['Qci'])
    @Qci.setter
    def Qci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Qci'], value)

    @property
    def RunOnDefaultBearer(self):
        """
        Returns
        -------
        - bool: Run activity on default bearer only
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunOnDefaultBearer'])
    @RunOnDefaultBearer.setter
    def RunOnDefaultBearer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RunOnDefaultBearer'], value)

    @property
    def STftFiltersCustom(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['STftFiltersCustom'])
    @STftFiltersCustom.setter
    def STftFiltersCustom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['STftFiltersCustom'], value)

    @property
    def SessionTimeoutValue(self):
        """
        Returns
        -------
        - number: Deprecated. Kept for TCL bw compatibility
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionTimeoutValue'])
    @SessionTimeoutValue.setter
    def SessionTimeoutValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SessionTimeoutValue'], value)

    @property
    def SpcoContainer(self):
        """
        Returns
        -------
        - str: Protocol Configuration Options (Container)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpcoContainer'])
    @SpcoContainer.setter
    def SpcoContainer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpcoContainer'], value)

    @property
    def SpcoProtocol(self):
        """
        Returns
        -------
        - str: Protocol Configuration Options (Protocol)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpcoProtocol'])
    @SpcoProtocol.setter
    def SpcoProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpcoProtocol'], value)

    @property
    def TearDownIndicator(self):
        """
        Returns
        -------
        - bool: Set tear down indicator flag when deleting context for this activity
        """
        return self._get_attribute(self._SDM_ATT_MAP['TearDownIndicator'])
    @TearDownIndicator.setter
    def TearDownIndicator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TearDownIndicator'], value)

    @property
    def UsePredefinedQci(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePredefinedQci'])
    @UsePredefinedQci.setter
    def UsePredefinedQci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePredefinedQci'], value)

    @property
    def UsePredefinedTft(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePredefinedTft'])
    @UsePredefinedTft.setter
    def UsePredefinedTft(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePredefinedTft'], value)

    def update(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, Qci=None, RunOnDefaultBearer=None, STftFiltersCustom=None, SessionTimeoutValue=None, SpcoContainer=None, SpcoProtocol=None, TearDownIndicator=None, UsePredefinedQci=None, UsePredefinedTft=None):
        """Updates globalTrafficProfiles resource on the server.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApn)): 
        - Arp (number): Priority of allocation and retention
        - DefaultBearerFallback (bool): Fallback on default bearer if no dedicated bearer was created for this activity.
        - EnableSessionTimeout (bool): Deprecated. Kept for TCL bw compatibility
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink (kbps)
        - Gbru (number): Guaranteed bitrate for uplink (kbps)
        - IsMsInitiated (bool): UE initiated service request for this activity. Execute Bearer Resource Command with TFT operation set to Create New. This option will be taken in consideration if no active bearer was found with matching TFT and QoS.
        - Mbrd (number): Maximum bitrate for downlink (kbps)
        - Mbru (number): Maximum bitrate for uplink (kbps)
        - Name (str): GTP needs the name of the activity
        - Qci (number): QoS Class Identifier
        - RunOnDefaultBearer (bool): Run activity on default bearer only
        - STftFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - SpcoContainer (str): Protocol Configuration Options (Container)
        - SpcoProtocol (str): Protocol Configuration Options (Protocol)
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQci (bool): 
        - UsePredefinedTft (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, Qci=None, RunOnDefaultBearer=None, STftFiltersCustom=None, SessionTimeoutValue=None, SpcoContainer=None, SpcoProtocol=None, TearDownIndicator=None, UsePredefinedQci=None, UsePredefinedTft=None):
        """Adds a new globalTrafficProfiles resource on the server and adds it to the container.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApn)): 
        - Arp (number): Priority of allocation and retention
        - DefaultBearerFallback (bool): Fallback on default bearer if no dedicated bearer was created for this activity.
        - EnableSessionTimeout (bool): Deprecated. Kept for TCL bw compatibility
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink (kbps)
        - Gbru (number): Guaranteed bitrate for uplink (kbps)
        - IsMsInitiated (bool): UE initiated service request for this activity. Execute Bearer Resource Command with TFT operation set to Create New. This option will be taken in consideration if no active bearer was found with matching TFT and QoS.
        - Mbrd (number): Maximum bitrate for downlink (kbps)
        - Mbru (number): Maximum bitrate for uplink (kbps)
        - Name (str): GTP needs the name of the activity
        - Qci (number): QoS Class Identifier
        - RunOnDefaultBearer (bool): Run activity on default bearer only
        - STftFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - SpcoContainer (str): Protocol Configuration Options (Container)
        - SpcoProtocol (str): Protocol Configuration Options (Protocol)
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQci (bool): 
        - UsePredefinedTft (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved globalTrafficProfiles resources using find and the newly added globalTrafficProfiles resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained globalTrafficProfiles resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, ObjectId=None, Qci=None, RunOnDefaultBearer=None, STftFiltersCustom=None, SessionTimeoutValue=None, SpcoContainer=None, SpcoProtocol=None, TearDownIndicator=None, UsePredefinedQci=None, UsePredefinedTft=None):
        """Finds and retrieves globalTrafficProfiles resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalTrafficProfiles resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalTrafficProfiles resources from the server.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApn)): 
        - Arp (number): Priority of allocation and retention
        - DefaultBearerFallback (bool): Fallback on default bearer if no dedicated bearer was created for this activity.
        - EnableSessionTimeout (bool): Deprecated. Kept for TCL bw compatibility
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink (kbps)
        - Gbru (number): Guaranteed bitrate for uplink (kbps)
        - IsMsInitiated (bool): UE initiated service request for this activity. Execute Bearer Resource Command with TFT operation set to Create New. This option will be taken in consideration if no active bearer was found with matching TFT and QoS.
        - Mbrd (number): Maximum bitrate for downlink (kbps)
        - Mbru (number): Maximum bitrate for uplink (kbps)
        - Name (str): GTP needs the name of the activity
        - ObjectId (str): Unique identifier for this object
        - Qci (number): QoS Class Identifier
        - RunOnDefaultBearer (bool): Run activity on default bearer only
        - STftFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - SpcoContainer (str): Protocol Configuration Options (Container)
        - SpcoProtocol (str): Protocol Configuration Options (Protocol)
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQci (bool): 
        - UsePredefinedTft (bool): 

        Returns
        -------
        - self: This instance with matching globalTrafficProfiles resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globalTrafficProfiles data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalTrafficProfiles resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
