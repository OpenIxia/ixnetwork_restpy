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


class DedicatedBearersS5S8Pgw(Base):
    """Bearer
    The DedicatedBearersS5S8Pgw class encapsulates a list of dedicatedBearersS5S8Pgw resources that is be managed by the user.
    A list of resources can be retrieved from the server using the DedicatedBearersS5S8Pgw.find() method.
    The list can be managed by the user by using the DedicatedBearersS5S8Pgw.add() and DedicatedBearersS5S8Pgw.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dedicatedBearersS5S8Pgw'

    def __init__(self, parent):
        super(DedicatedBearersS5S8Pgw, self).__init__(parent)

    @property
    def ApnAmbrUpdateValue(self):
        """APN_AMBR update value (in %).

        Returns:
            number
        """
        return self._get_attribute('apnAmbrUpdateValue')
    @ApnAmbrUpdateValue.setter
    def ApnAmbrUpdateValue(self, value):
        self._set_attribute('apnAmbrUpdateValue', value)

    @property
    def Arp(self):
        """OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.

        Returns:
            number
        """
        return self._get_attribute('arp')
    @Arp.setter
    def Arp(self, value):
        self._set_attribute('arp', value)

    @property
    def Custom_tft(self):
        """

        Returns:
            str
        """
        return self._get_attribute('custom_tft')
    @Custom_tft.setter
    def Custom_tft(self, value):
        self._set_attribute('custom_tft', value)

    @property
    def EnableLifetime(self):
        """Enable bearer lifetime control

        Returns:
            bool
        """
        return self._get_attribute('enableLifetime')
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute('enableLifetime', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Gbrd(self):
        """Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('gbrd')
    @Gbrd.setter
    def Gbrd(self, value):
        self._set_attribute('gbrd', value)

    @property
    def Gbru(self):
        """Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('gbru')
    @Gbru.setter
    def Gbru(self, value):
        self._set_attribute('gbru', value)

    @property
    def Lifetime(self):
        """Bearer lifetime (seconds)

        Returns:
            number
        """
        return self._get_attribute('lifetime')
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute('lifetime', value)

    @property
    def Mbrd(self):
        """Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('mbrd')
    @Mbrd.setter
    def Mbrd(self, value):
        self._set_attribute('mbrd', value)

    @property
    def Mbru(self):
        """Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('mbru')
    @Mbru.setter
    def Mbru(self, value):
        self._set_attribute('mbru', value)

    @property
    def Mode(self):
        """A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure

        Returns:
            str
        """
        return self._get_attribute('mode')
    @Mode.setter
    def Mode(self, value):
        self._set_attribute('mode', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PreemptionCapability(self):
        """If true preemption capability is enabled

        Returns:
            bool
        """
        return self._get_attribute('preemptionCapability')
    @PreemptionCapability.setter
    def PreemptionCapability(self, value):
        self._set_attribute('preemptionCapability', value)

    @property
    def PreemptionVulnerability(self):
        """If true preemption vulnerability is enabled

        Returns:
            bool
        """
        return self._get_attribute('preemptionVulnerability')
    @PreemptionVulnerability.setter
    def PreemptionVulnerability(self, value):
        self._set_attribute('preemptionVulnerability', value)

    @property
    def PriorityLevel(self):
        """Priority Level 1=highest 15=lowest

        Returns:
            number
        """
        return self._get_attribute('priorityLevel')
    @PriorityLevel.setter
    def PriorityLevel(self, value):
        self._set_attribute('priorityLevel', value)

    @property
    def Qci(self):
        """QoS Class Identifier

        Returns:
            number
        """
        return self._get_attribute('qci')
    @Qci.setter
    def Qci(self, value):
        self._set_attribute('qci', value)

    @property
    def QosLabel(self):
        """Quality of Service characteristics requested by the SGSN for the primary PDP contexts.

        Returns:
            str
        """
        return self._get_attribute('qosLabel')
    @QosLabel.setter
    def QosLabel(self, value):
        self._set_attribute('qosLabel', value)

    @property
    def QosUpdateValue(self):
        """QoS update value (in %).

        Returns:
            number
        """
        return self._get_attribute('qosUpdateValue')
    @QosUpdateValue.setter
    def QosUpdateValue(self, value):
        self._set_attribute('qosUpdateValue', value)

    @property
    def Tft(self):
        """Traffic Flow Template

        Returns:
            str
        """
        return self._get_attribute('tft')
    @Tft.setter
    def Tft(self, value):
        self._set_attribute('tft', value)

    @property
    def TimeoutAction(self):
        """Action to be execute when a bearer lifetime expires

        Returns:
            str
        """
        return self._get_attribute('timeoutAction')
    @TimeoutAction.setter
    def TimeoutAction(self, value):
        self._set_attribute('timeoutAction', value)

    def update(self, ApnAmbrUpdateValue=None, Arp=None, Custom_tft=None, EnableLifetime=None, Enabled=None, Gbrd=None, Gbru=None, Lifetime=None, Mbrd=None, Mbru=None, Mode=None, Name=None, PreemptionCapability=None, PreemptionVulnerability=None, PriorityLevel=None, Qci=None, QosLabel=None, QosUpdateValue=None, Tft=None, TimeoutAction=None):
        """Updates a child instance of dedicatedBearersS5S8Pgw on the server.

        Args:
            ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
            Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
            Custom_tft (str): 
            EnableLifetime (bool): Enable bearer lifetime control
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Lifetime (number): Bearer lifetime (seconds)
            Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
            Name (str): Name of range
            PreemptionCapability (bool): If true preemption capability is enabled
            PreemptionVulnerability (bool): If true preemption vulnerability is enabled
            PriorityLevel (number): Priority Level 1=highest 15=lowest
            Qci (number): QoS Class Identifier
            QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
            QosUpdateValue (number): QoS update value (in %).
            Tft (str): Traffic Flow Template
            TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ApnAmbrUpdateValue=None, Arp=None, Custom_tft=None, EnableLifetime=None, Enabled=None, Gbrd=None, Gbru=None, Lifetime=None, Mbrd=None, Mbru=None, Mode=None, Name=None, PreemptionCapability=None, PreemptionVulnerability=None, PriorityLevel=None, Qci=None, QosLabel=None, QosUpdateValue=None, Tft=None, TimeoutAction=None):
        """Adds a new dedicatedBearersS5S8Pgw node on the server and retrieves it in this instance.

        Args:
            ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
            Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
            Custom_tft (str): 
            EnableLifetime (bool): Enable bearer lifetime control
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Lifetime (number): Bearer lifetime (seconds)
            Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
            Name (str): Name of range
            PreemptionCapability (bool): If true preemption capability is enabled
            PreemptionVulnerability (bool): If true preemption vulnerability is enabled
            PriorityLevel (number): Priority Level 1=highest 15=lowest
            Qci (number): QoS Class Identifier
            QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
            QosUpdateValue (number): QoS update value (in %).
            Tft (str): Traffic Flow Template
            TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Returns:
            self: This instance with all currently retrieved dedicatedBearersS5S8Pgw data using find and the newly added dedicatedBearersS5S8Pgw data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dedicatedBearersS5S8Pgw data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ApnAmbrUpdateValue=None, Arp=None, Custom_tft=None, EnableLifetime=None, Enabled=None, Gbrd=None, Gbru=None, Lifetime=None, Mbrd=None, Mbru=None, Mode=None, Name=None, ObjectId=None, PreemptionCapability=None, PreemptionVulnerability=None, PriorityLevel=None, Qci=None, QosLabel=None, QosUpdateValue=None, Tft=None, TimeoutAction=None):
        """Finds and retrieves dedicatedBearersS5S8Pgw data from the server.

        All named parameters support regex and can be used to selectively retrieve dedicatedBearersS5S8Pgw data from the server.
        By default the find method takes no parameters and will retrieve all dedicatedBearersS5S8Pgw data from the server.

        Args:
            ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
            Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
            Custom_tft (str): 
            EnableLifetime (bool): Enable bearer lifetime control
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Lifetime (number): Bearer lifetime (seconds)
            Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            PreemptionCapability (bool): If true preemption capability is enabled
            PreemptionVulnerability (bool): If true preemption vulnerability is enabled
            PriorityLevel (number): Priority Level 1=highest 15=lowest
            Qci (number): QoS Class Identifier
            QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
            QosUpdateValue (number): QoS update value (in %).
            Tft (str): Traffic Flow Template
            TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Returns:
            self: This instance with matching dedicatedBearersS5S8Pgw data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dedicatedBearersS5S8Pgw data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dedicatedBearersS5S8Pgw data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
