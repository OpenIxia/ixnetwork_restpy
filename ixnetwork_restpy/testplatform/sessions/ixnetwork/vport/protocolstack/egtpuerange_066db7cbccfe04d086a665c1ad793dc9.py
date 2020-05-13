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


class EgtpUeRange(Base):
    """UE range
    The EgtpUeRange class encapsulates a required egtpUeRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpUeRange'
    _SDM_ATT_MAP = {
        'AmbrDl': 'ambrDl',
        'AmbrUl': 'ambrUl',
        'ApnIncrement': 'apnIncrement',
        'ApnRestriction': 'apnRestriction',
        'Count': 'count',
        'EnableMobility': 'enableMobility',
        'EnableSv': 'enableSv',
        'Enabled': 'enabled',
        'Hni': 'hni',
        'Imsi': 'imsi',
        'IncrementBy': 'incrementBy',
        'MaxDelayVariation': 'maxDelayVariation',
        'MaxIntervalVariation': 'maxIntervalVariation',
        'Mei': 'mei',
        'MobilityInterval': 'mobilityInterval',
        'Msisdn': 'msisdn',
        'Name': 'name',
        'ObjectId': 'objectId',
        'ParentENodeB': 'parentENodeB',
        'ParentRange': 'parentRange',
        'RelocateSgwOnLastEnodeB': 'relocateSgwOnLastEnodeB',
        'StartDelay': 'startDelay',
        'Sv': 'sv',
    }

    def __init__(self, parent):
        super(EgtpUeRange, self).__init__(parent)

    @property
    def MobilePathEntries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentries_d3f666fdb70fab40ed74c1a23e95847f.MobilePathEntries): An instance of the MobilePathEntries class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentries_d3f666fdb70fab40ed74c1a23e95847f import MobilePathEntries
        return MobilePathEntries(self)

    @property
    def TrafficProfileProxies(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxies_0757c19409c7d00cd732fd579f5b18a0.TrafficProfileProxies): An instance of the TrafficProfileProxies class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxies_0757c19409c7d00cd732fd579f5b18a0 import TrafficProfileProxies
        return TrafficProfileProxies(self)

    @property
    def AmbrDl(self):
        """
        Returns
        -------
        - number: Obsolete. Use values from APN list
        """
        return self._get_attribute(self._SDM_ATT_MAP['AmbrDl'])
    @AmbrDl.setter
    def AmbrDl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AmbrDl'], value)

    @property
    def AmbrUl(self):
        """
        Returns
        -------
        - number: Obsolete. Use values from APN list
        """
        return self._get_attribute(self._SDM_ATT_MAP['AmbrUl'])
    @AmbrUl.setter
    def AmbrUl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AmbrUl'], value)

    @property
    def ApnIncrement(self):
        """
        Returns
        -------
        - bool: Use the first APN from the list bellow. Increment it for each UE
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApnIncrement'])
    @ApnIncrement.setter
    def ApnIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApnIncrement'], value)

    @property
    def ApnRestriction(self):
        """
        Returns
        -------
        - number: Authorization to access another APN
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApnRestriction'])
    @ApnRestriction.setter
    def ApnRestriction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApnRestriction'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The total number of UEs to be created for this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def EnableMobility(self):
        """
        Returns
        -------
        - bool: Perform a mobility test
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMobility'])
    @EnableMobility.setter
    def EnableMobility(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMobility'], value)

    @property
    def EnableSv(self):
        """
        Returns
        -------
        - bool: Use Software Version to generate IMEISV
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSv'])
    @EnableSv.setter
    def EnableSv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSv'], value)

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
    def Hni(self):
        """
        Returns
        -------
        - str: Home Network Identifier: MNC+MCC (doesn't need to mach eNodeB Location Information)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Hni'])
    @Hni.setter
    def Hni(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Hni'], value)

    @property
    def Imsi(self):
        """
        Returns
        -------
        - str: International Mobile Subscriber Identity
        """
        return self._get_attribute(self._SDM_ATT_MAP['Imsi'])
    @Imsi.setter
    def Imsi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Imsi'], value)

    @property
    def IncrementBy(self):
        """
        Returns
        -------
        - number: Increment by this amount
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementBy'])
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementBy'], value)

    @property
    def MaxDelayVariation(self):
        """
        Returns
        -------
        - number: Randomize Start delay by max +/- X%
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxDelayVariation'])
    @MaxDelayVariation.setter
    def MaxDelayVariation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxDelayVariation'], value)

    @property
    def MaxIntervalVariation(self):
        """
        Returns
        -------
        - number: Randomize Mobility interval by max +/- X%
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIntervalVariation'])
    @MaxIntervalVariation.setter
    def MaxIntervalVariation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIntervalVariation'], value)

    @property
    def Mei(self):
        """
        Returns
        -------
        - str: International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mei'])
    @Mei.setter
    def Mei(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mei'], value)

    @property
    def MobilityInterval(self):
        """
        Returns
        -------
        - number: The total time (seconds) it will take the mobile to return to the starting node
        """
        return self._get_attribute(self._SDM_ATT_MAP['MobilityInterval'])
    @MobilityInterval.setter
    def MobilityInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MobilityInterval'], value)

    @property
    def Msisdn(self):
        """
        Returns
        -------
        - str: Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
        """
        return self._get_attribute(self._SDM_ATT_MAP['Msisdn'])
    @Msisdn.setter
    def Msisdn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Msisdn'], value)

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
    def ParentENodeB(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../range): Do not use this. Use parentRange instead
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentENodeB'])
    @ParentENodeB.setter
    def ParentENodeB(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ParentENodeB'], value)

    @property
    def ParentRange(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../range): Parent range
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentRange'])
    @ParentRange.setter
    def ParentRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ParentRange'], value)

    @property
    def RelocateSgwOnLastEnodeB(self):
        """
        Returns
        -------
        - bool: Relocate SGW on Last eNB
        """
        return self._get_attribute(self._SDM_ATT_MAP['RelocateSgwOnLastEnodeB'])
    @RelocateSgwOnLastEnodeB.setter
    def RelocateSgwOnLastEnodeB(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RelocateSgwOnLastEnodeB'], value)

    @property
    def StartDelay(self):
        """
        Returns
        -------
        - number: How many seconds to wait before starting to move the UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartDelay'])
    @StartDelay.setter
    def StartDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartDelay'], value)

    @property
    def Sv(self):
        """
        Returns
        -------
        - str: The software version number to be appended to the IMEI in order to generate IMEISV
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sv'])
    @Sv.setter
    def Sv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Sv'], value)

    def update(self, AmbrDl=None, AmbrUl=None, ApnIncrement=None, ApnRestriction=None, Count=None, EnableMobility=None, EnableSv=None, Enabled=None, Hni=None, Imsi=None, IncrementBy=None, MaxDelayVariation=None, MaxIntervalVariation=None, Mei=None, MobilityInterval=None, Msisdn=None, Name=None, ParentENodeB=None, ParentRange=None, RelocateSgwOnLastEnodeB=None, StartDelay=None, Sv=None):
        """Updates egtpUeRange resource on the server.

        Args
        ----
        - AmbrDl (number): Obsolete. Use values from APN list
        - AmbrUl (number): Obsolete. Use values from APN list
        - ApnIncrement (bool): Use the first APN from the list bellow. Increment it for each UE
        - ApnRestriction (number): Authorization to access another APN
        - Count (number): The total number of UEs to be created for this range.
        - EnableMobility (bool): Perform a mobility test
        - EnableSv (bool): Use Software Version to generate IMEISV
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Hni (str): Home Network Identifier: MNC+MCC (doesn't need to mach eNodeB Location Information)
        - Imsi (str): International Mobile Subscriber Identity
        - IncrementBy (number): Increment by this amount
        - MaxDelayVariation (number): Randomize Start delay by max +/- X%
        - MaxIntervalVariation (number): Randomize Mobility interval by max +/- X%
        - Mei (str): International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
        - MobilityInterval (number): The total time (seconds) it will take the mobile to return to the starting node
        - Msisdn (str): Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
        - Name (str): Name of range
        - ParentENodeB (str(None | /api/v1/sessions/1/ixnetwork/vport/.../range)): Do not use this. Use parentRange instead
        - ParentRange (str(None | /api/v1/sessions/1/ixnetwork/vport/.../range)): Parent range
        - RelocateSgwOnLastEnodeB (bool): Relocate SGW on Last eNB
        - StartDelay (number): How many seconds to wait before starting to move the UEs
        - Sv (str): The software version number to be appended to the IMEI in order to generate IMEISV

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
