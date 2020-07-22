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


class GlobalTrafficProfileS5S8(Base):
    """
    The GlobalTrafficProfileS5S8 class encapsulates a list of globalTrafficProfileS5S8 resources that are managed by the user.
    A list of resources can be retrieved from the server using the GlobalTrafficProfileS5S8.find() method.
    The list can be managed by using the GlobalTrafficProfileS5S8.add() and GlobalTrafficProfileS5S8.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalTrafficProfileS5S8'
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
        'SPCO_Container': 'sPCO_Container',
        'SPCO_Protocol': 'sPCO_Protocol',
        'STFTFiltersCustom': 'sTFTFiltersCustom',
        'SessionTimeoutValue': 'sessionTimeoutValue',
        'TearDownIndicator': 'tearDownIndicator',
        'UsePredefinedQCI': 'usePredefinedQCI',
        'UsePredefinedTFT': 'usePredefinedTFT',
    }

    def __init__(self, parent):
        super(GlobalTrafficProfileS5S8, self).__init__(parent)

    @property
    def Apn(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApnS5S8): 
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
    def SPCO_Container(self):
        """
        Returns
        -------
        - str: Protocol Configuration Options (Container)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPCO_Container'])
    @SPCO_Container.setter
    def SPCO_Container(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPCO_Container'], value)

    @property
    def SPCO_Protocol(self):
        """
        Returns
        -------
        - str: Protocol Configuration Options (Protocol)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPCO_Protocol'])
    @SPCO_Protocol.setter
    def SPCO_Protocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPCO_Protocol'], value)

    @property
    def STFTFiltersCustom(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['STFTFiltersCustom'])
    @STFTFiltersCustom.setter
    def STFTFiltersCustom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['STFTFiltersCustom'], value)

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
    def UsePredefinedQCI(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePredefinedQCI'])
    @UsePredefinedQCI.setter
    def UsePredefinedQCI(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePredefinedQCI'], value)

    @property
    def UsePredefinedTFT(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePredefinedTFT'])
    @UsePredefinedTFT.setter
    def UsePredefinedTFT(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePredefinedTFT'], value)

    def update(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, Qci=None, RunOnDefaultBearer=None, SPCO_Container=None, SPCO_Protocol=None, STFTFiltersCustom=None, SessionTimeoutValue=None, TearDownIndicator=None, UsePredefinedQCI=None, UsePredefinedTFT=None):
        """Updates globalTrafficProfileS5S8 resource on the server.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApnS5S8)): 
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
        - SPCO_Container (str): Protocol Configuration Options (Container)
        - SPCO_Protocol (str): Protocol Configuration Options (Protocol)
        - STFTFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQCI (bool): 
        - UsePredefinedTFT (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, Qci=None, RunOnDefaultBearer=None, SPCO_Container=None, SPCO_Protocol=None, STFTFiltersCustom=None, SessionTimeoutValue=None, TearDownIndicator=None, UsePredefinedQCI=None, UsePredefinedTFT=None):
        """Adds a new globalTrafficProfileS5S8 resource on the server and adds it to the container.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApnS5S8)): 
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
        - SPCO_Container (str): Protocol Configuration Options (Container)
        - SPCO_Protocol (str): Protocol Configuration Options (Protocol)
        - STFTFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQCI (bool): 
        - UsePredefinedTFT (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved globalTrafficProfileS5S8 resources using find and the newly added globalTrafficProfileS5S8 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained globalTrafficProfileS5S8 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Apn=None, Arp=None, DefaultBearerFallback=None, EnableSessionTimeout=None, Enabled=None, Gbrd=None, Gbru=None, IsMsInitiated=None, Mbrd=None, Mbru=None, Name=None, ObjectId=None, Qci=None, RunOnDefaultBearer=None, SPCO_Container=None, SPCO_Protocol=None, STFTFiltersCustom=None, SessionTimeoutValue=None, TearDownIndicator=None, UsePredefinedQCI=None, UsePredefinedTFT=None):
        """Finds and retrieves globalTrafficProfileS5S8 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalTrafficProfileS5S8 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalTrafficProfileS5S8 resources from the server.

        Args
        ----
        - Apn (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalEgtpApnS5S8)): 
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
        - SPCO_Container (str): Protocol Configuration Options (Container)
        - SPCO_Protocol (str): Protocol Configuration Options (Protocol)
        - STFTFiltersCustom (str): 
        - SessionTimeoutValue (number): Deprecated. Kept for TCL bw compatibility
        - TearDownIndicator (bool): Set tear down indicator flag when deleting context for this activity
        - UsePredefinedQCI (bool): 
        - UsePredefinedTFT (bool): 

        Returns
        -------
        - self: This instance with matching globalTrafficProfileS5S8 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globalTrafficProfileS5S8 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalTrafficProfileS5S8 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
