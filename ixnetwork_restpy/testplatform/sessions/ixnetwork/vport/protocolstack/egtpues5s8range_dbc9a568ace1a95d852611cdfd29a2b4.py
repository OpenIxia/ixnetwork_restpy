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


class EgtpUeS5S8Range(Base):
    """UE range
    The EgtpUeS5S8Range class encapsulates a required egtpUeS5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpUeS5S8Range'

    def __init__(self, parent):
        super(EgtpUeS5S8Range, self).__init__(parent)

    @property
    def MobilePathEntriesS5S8Sgw(self):
        """An instance of the MobilePathEntriesS5S8Sgw class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentriess5s8sgw_0a1e5cd43467a489ba9164ed4763547d.MobilePathEntriesS5S8Sgw)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentriess5s8sgw_0a1e5cd43467a489ba9164ed4763547d import MobilePathEntriesS5S8Sgw
        return MobilePathEntriesS5S8Sgw(self)

    @property
    def TrafficProfileProxiesS5S8Sgw(self):
        """An instance of the TrafficProfileProxiesS5S8Sgw class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8sgw_269fe2af145fddcbfddef88a056cc4ab.TrafficProfileProxiesS5S8Sgw)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8sgw_269fe2af145fddcbfddef88a056cc4ab import TrafficProfileProxiesS5S8Sgw
        return TrafficProfileProxiesS5S8Sgw(self)

    @property
    def APNRestriction(self):
        """Authorization to access another APN

        Returns:
            number
        """
        return self._get_attribute('aPNRestriction')
    @APNRestriction.setter
    def APNRestriction(self, value):
        self._set_attribute('aPNRestriction', value)

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
    def EnableLifetime(self):
        """Enable UE lifetime control. The UE will disconnect after the specified time.

        Returns:
            bool
        """
        return self._get_attribute('enableLifetime')
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute('enableLifetime', value)

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
    def EnableSV(self):
        """Use Software Version to generate IMEISV

        Returns:
            bool
        """
        return self._get_attribute('enableSV')
    @EnableSV.setter
    def EnableSV(self, value):
        self._set_attribute('enableSV', value)

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
    def IMSI(self):
        """International Mobile Subscriber Identity

        Returns:
            str
        """
        return self._get_attribute('iMSI')
    @IMSI.setter
    def IMSI(self, value):
        self._set_attribute('iMSI', value)

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
    def Lifetime(self):
        """Amount of time (in seconds) to wait after attach procedure completes before scheduling forced detach.

        Returns:
            number
        """
        return self._get_attribute('lifetime')
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute('lifetime', value)

    @property
    def MEI(self):
        """International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.

        Returns:
            str
        """
        return self._get_attribute('mEI')
    @MEI.setter
    def MEI(self, value):
        self._set_attribute('mEI', value)

    @property
    def MSISDN(self):
        """Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number

        Returns:
            str
        """
        return self._get_attribute('mSISDN')
    @MSISDN.setter
    def MSISDN(self, value):
        self._set_attribute('mSISDN', value)

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
    def ParentRange(self):
        """Parent range

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=enbS5S8SecondaryRange)
        """
        return self._get_attribute('parentRange')
    @ParentRange.setter
    def ParentRange(self, value):
        self._set_attribute('parentRange', value)

    @property
    def SV(self):
        """The software version number to be appended to the IMEI in order to generate IMEISV

        Returns:
            str
        """
        return self._get_attribute('sV')
    @SV.setter
    def SV(self, value):
        self._set_attribute('sV', value)

    @property
    def SelectionMode(self):
        """Indicates the origin of the APN in the message

        Returns:
            number
        """
        return self._get_attribute('selectionMode')
    @SelectionMode.setter
    def SelectionMode(self, value):
        self._set_attribute('selectionMode', value)

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
    def UpdateAmbrEnable(self):
        """Update APN-AMBR for this UE

        Returns:
            bool
        """
        return self._get_attribute('updateAmbrEnable')
    @UpdateAmbrEnable.setter
    def UpdateAmbrEnable(self, value):
        self._set_attribute('updateAmbrEnable', value)

    @property
    def UpdateAmbrIncrement(self):
        """Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.

        Returns:
            number
        """
        return self._get_attribute('updateAmbrIncrement')
    @UpdateAmbrIncrement.setter
    def UpdateAmbrIncrement(self, value):
        self._set_attribute('updateAmbrIncrement', value)

    @property
    def UpdateAmbrIterations(self):
        """How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates

        Returns:
            number
        """
        return self._get_attribute('updateAmbrIterations')
    @UpdateAmbrIterations.setter
    def UpdateAmbrIterations(self, value):
        self._set_attribute('updateAmbrIterations', value)

    @property
    def UpdateAmbrTimeout(self):
        """Time to wait (in seconds) since the session was created until sending the update

        Returns:
            number
        """
        return self._get_attribute('updateAmbrTimeout')
    @UpdateAmbrTimeout.setter
    def UpdateAmbrTimeout(self, value):
        self._set_attribute('updateAmbrTimeout', value)

    def update(self, APNRestriction=None, Count=None, EnableLifetime=None, EnableMobility=None, EnableSV=None, Enabled=None, IMSI=None, IncrementBy=None, Lifetime=None, MEI=None, MSISDN=None, MaxDelayVariation=None, MaxIntervalVariation=None, MobilityInterval=None, Name=None, ParentRange=None, SV=None, SelectionMode=None, StartDelay=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None):
        """Updates a child instance of egtpUeS5S8Range on the server.

        Args:
            APNRestriction (number): Authorization to access another APN
            Count (number): The total number of UEs to be created for this range.
            EnableLifetime (bool): Enable UE lifetime control. The UE will disconnect after the specified time.
            EnableMobility (bool): Perform a mobility test
            EnableSV (bool): Use Software Version to generate IMEISV
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IMSI (str): International Mobile Subscriber Identity
            IncrementBy (number): Increment by this amount
            Lifetime (number): Amount of time (in seconds) to wait after attach procedure completes before scheduling forced detach.
            MEI (str): International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
            MSISDN (str): Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
            MaxDelayVariation (number): Randomize Start delay by max +/- X%
            MaxIntervalVariation (number): Randomize Mobility interval by max +/- X%
            MobilityInterval (number): The total time (seconds) it will take the mobile to return to the starting node
            Name (str): Name of range
            ParentRange (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=enbS5S8SecondaryRange)): Parent range
            SV (str): The software version number to be appended to the IMEI in order to generate IMEISV
            SelectionMode (number): Indicates the origin of the APN in the message
            StartDelay (number): How many seconds to wait before starting to move the UEs
            UpdateAmbrEnable (bool): Update APN-AMBR for this UE
            UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
            UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
            UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update

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
