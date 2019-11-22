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

    def __init__(self, parent):
        super(EgtpUeRange, self).__init__(parent)

    @property
    def MobilePathEntries(self):
        """An instance of the MobilePathEntries class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentries_6a07e110e42ebf0f9f068d52f1415211.MobilePathEntries)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentries_6a07e110e42ebf0f9f068d52f1415211 import MobilePathEntries
        return MobilePathEntries(self)

    @property
    def TrafficProfileProxies(self):
        """An instance of the TrafficProfileProxies class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxies_9aa63bb5951228c5db8de11f3c117b5a.TrafficProfileProxies)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxies_9aa63bb5951228c5db8de11f3c117b5a import TrafficProfileProxies
        return TrafficProfileProxies(self)

    @property
    def AmbrDl(self):
        """Obsolete. Use values from APN list

        Returns:
            number
        """
        return self._get_attribute('ambrDl')
    @AmbrDl.setter
    def AmbrDl(self, value):
        self._set_attribute('ambrDl', value)

    @property
    def AmbrUl(self):
        """Obsolete. Use values from APN list

        Returns:
            number
        """
        return self._get_attribute('ambrUl')
    @AmbrUl.setter
    def AmbrUl(self, value):
        self._set_attribute('ambrUl', value)

    @property
    def ApnIncrement(self):
        """Use the first APN from the list bellow. Increment it for each UE

        Returns:
            bool
        """
        return self._get_attribute('apnIncrement')
    @ApnIncrement.setter
    def ApnIncrement(self, value):
        self._set_attribute('apnIncrement', value)

    @property
    def ApnRestriction(self):
        """Authorization to access another APN

        Returns:
            number
        """
        return self._get_attribute('apnRestriction')
    @ApnRestriction.setter
    def ApnRestriction(self, value):
        self._set_attribute('apnRestriction', value)

    @property
    def Count(self):
        """The total number of UEs to be created for this range.

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def EnableMobility(self):
        """Perform a mobility test

        Returns:
            bool
        """
        return self._get_attribute('enableMobility')
    @EnableMobility.setter
    def EnableMobility(self, value):
        self._set_attribute('enableMobility', value)

    @property
    def EnableSv(self):
        """Use Software Version to generate IMEISV

        Returns:
            bool
        """
        return self._get_attribute('enableSv')
    @EnableSv.setter
    def EnableSv(self, value):
        self._set_attribute('enableSv', value)

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
    def Hni(self):
        """Home Network Identifier: MNC+MCC (doesn't need to mach eNodeB Location Information)

        Returns:
            str
        """
        return self._get_attribute('hni')
    @Hni.setter
    def Hni(self, value):
        self._set_attribute('hni', value)

    @property
    def Imsi(self):
        """International Mobile Subscriber Identity

        Returns:
            str
        """
        return self._get_attribute('imsi')
    @Imsi.setter
    def Imsi(self, value):
        self._set_attribute('imsi', value)

    @property
    def IncrementBy(self):
        """Increment by this amount

        Returns:
            number
        """
        return self._get_attribute('incrementBy')
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute('incrementBy', value)

    @property
    def MaxDelayVariation(self):
        """Randomize Start delay by max +/- X%

        Returns:
            number
        """
        return self._get_attribute('maxDelayVariation')
    @MaxDelayVariation.setter
    def MaxDelayVariation(self, value):
        self._set_attribute('maxDelayVariation', value)

    @property
    def MaxIntervalVariation(self):
        """Randomize Mobility interval by max +/- X%

        Returns:
            number
        """
        return self._get_attribute('maxIntervalVariation')
    @MaxIntervalVariation.setter
    def MaxIntervalVariation(self, value):
        self._set_attribute('maxIntervalVariation', value)

    @property
    def Mei(self):
        """International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.

        Returns:
            str
        """
        return self._get_attribute('mei')
    @Mei.setter
    def Mei(self, value):
        self._set_attribute('mei', value)

    @property
    def MobilityInterval(self):
        """The total time (seconds) it will take the mobile to return to the starting node

        Returns:
            number
        """
        return self._get_attribute('mobilityInterval')
    @MobilityInterval.setter
    def MobilityInterval(self, value):
        self._set_attribute('mobilityInterval', value)

    @property
    def Msisdn(self):
        """Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number

        Returns:
            str
        """
        return self._get_attribute('msisdn')
    @Msisdn.setter
    def Msisdn(self, value):
        self._set_attribute('msisdn', value)

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
    def ParentENodeB(self):
        """Do not use this. Use parentRange instead

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)
        """
        return self._get_attribute('parentENodeB')
    @ParentENodeB.setter
    def ParentENodeB(self, value):
        self._set_attribute('parentENodeB', value)

    @property
    def ParentRange(self):
        """Parent range

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)
        """
        return self._get_attribute('parentRange')
    @ParentRange.setter
    def ParentRange(self, value):
        self._set_attribute('parentRange', value)

    @property
    def RelocateSgwOnLastEnodeB(self):
        """Relocate SGW on Last eNB

        Returns:
            bool
        """
        return self._get_attribute('relocateSgwOnLastEnodeB')
    @RelocateSgwOnLastEnodeB.setter
    def RelocateSgwOnLastEnodeB(self, value):
        self._set_attribute('relocateSgwOnLastEnodeB', value)

    @property
    def StartDelay(self):
        """How many seconds to wait before starting to move the UEs

        Returns:
            number
        """
        return self._get_attribute('startDelay')
    @StartDelay.setter
    def StartDelay(self, value):
        self._set_attribute('startDelay', value)

    @property
    def Sv(self):
        """The software version number to be appended to the IMEI in order to generate IMEISV

        Returns:
            str
        """
        return self._get_attribute('sv')
    @Sv.setter
    def Sv(self, value):
        self._set_attribute('sv', value)

    def update(self, AmbrDl=None, AmbrUl=None, ApnIncrement=None, ApnRestriction=None, Count=None, EnableMobility=None, EnableSv=None, Enabled=None, Hni=None, Imsi=None, IncrementBy=None, MaxDelayVariation=None, MaxIntervalVariation=None, Mei=None, MobilityInterval=None, Msisdn=None, Name=None, ParentENodeB=None, ParentRange=None, RelocateSgwOnLastEnodeB=None, StartDelay=None, Sv=None):
        """Updates a child instance of egtpUeRange on the server.

        Args:
            AmbrDl (number): Obsolete. Use values from APN list
            AmbrUl (number): Obsolete. Use values from APN list
            ApnIncrement (bool): Use the first APN from the list bellow. Increment it for each UE
            ApnRestriction (number): Authorization to access another APN
            Count (number): The total number of UEs to be created for this range.
            EnableMobility (bool): Perform a mobility test
            EnableSv (bool): Use Software Version to generate IMEISV
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Hni (str): Home Network Identifier: MNC+MCC (doesn't need to mach eNodeB Location Information)
            Imsi (str): International Mobile Subscriber Identity
            IncrementBy (number): Increment by this amount
            MaxDelayVariation (number): Randomize Start delay by max +/- X%
            MaxIntervalVariation (number): Randomize Mobility interval by max +/- X%
            Mei (str): International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
            MobilityInterval (number): The total time (seconds) it will take the mobile to return to the starting node
            Msisdn (str): Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
            Name (str): Name of range
            ParentENodeB (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): Do not use this. Use parentRange instead
            ParentRange (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): Parent range
            RelocateSgwOnLastEnodeB (bool): Relocate SGW on Last eNB
            StartDelay (number): How many seconds to wait before starting to move the UEs
            Sv (str): The software version number to be appended to the IMEI in order to generate IMEISV

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

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
