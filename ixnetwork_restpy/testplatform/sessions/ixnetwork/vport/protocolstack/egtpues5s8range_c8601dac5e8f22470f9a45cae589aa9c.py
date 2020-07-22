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


class EgtpUeS5S8Range(Base):
    """UE range
    The EgtpUeS5S8Range class encapsulates a required egtpUeS5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpUeS5S8Range'
    _SDM_ATT_MAP = {
        'APNRestriction': 'aPNRestriction',
        'Count': 'count',
        'EnableLifetime': 'enableLifetime',
        'EnableMobility': 'enableMobility',
        'EnableSV': 'enableSV',
        'Enabled': 'enabled',
        'IMSI': 'iMSI',
        'IncrementBy': 'incrementBy',
        'Lifetime': 'lifetime',
        'MEI': 'mEI',
        'MSISDN': 'mSISDN',
        'MaxDelayVariation': 'maxDelayVariation',
        'MaxIntervalVariation': 'maxIntervalVariation',
        'MobilityInterval': 'mobilityInterval',
        'Name': 'name',
        'ObjectId': 'objectId',
        'ParentRange': 'parentRange',
        'SV': 'sV',
        'SelectionMode': 'selectionMode',
        'StartDelay': 'startDelay',
        'UpdateAmbrEnable': 'updateAmbrEnable',
        'UpdateAmbrIncrement': 'updateAmbrIncrement',
        'UpdateAmbrIterations': 'updateAmbrIterations',
        'UpdateAmbrTimeout': 'updateAmbrTimeout',
    }

    def __init__(self, parent):
        super(EgtpUeS5S8Range, self).__init__(parent)

    @property
    def MobilePathEntriesS5S8Sgw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentriess5s8sgw_16d6056dfc577e5a954fb832f3a3de97.MobilePathEntriesS5S8Sgw): An instance of the MobilePathEntriesS5S8Sgw class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.mobilepathentriess5s8sgw_16d6056dfc577e5a954fb832f3a3de97 import MobilePathEntriesS5S8Sgw
        return MobilePathEntriesS5S8Sgw(self)

    @property
    def TrafficProfileProxiesS5S8Sgw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8sgw_226b78057d8646de70af27de844cb6a6.TrafficProfileProxiesS5S8Sgw): An instance of the TrafficProfileProxiesS5S8Sgw class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8sgw_226b78057d8646de70af27de844cb6a6 import TrafficProfileProxiesS5S8Sgw
        return TrafficProfileProxiesS5S8Sgw(self)

    @property
    def APNRestriction(self):
        """
        Returns
        -------
        - number: Authorization to access another APN
        """
        return self._get_attribute(self._SDM_ATT_MAP['APNRestriction'])
    @APNRestriction.setter
    def APNRestriction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['APNRestriction'], value)

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
    def EnableLifetime(self):
        """
        Returns
        -------
        - bool: Enable UE lifetime control. The UE will disconnect after the specified time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLifetime'])
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLifetime'], value)

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
    def EnableSV(self):
        """
        Returns
        -------
        - bool: Use Software Version to generate IMEISV
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSV'])
    @EnableSV.setter
    def EnableSV(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSV'], value)

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
    def IMSI(self):
        """
        Returns
        -------
        - str: International Mobile Subscriber Identity
        """
        return self._get_attribute(self._SDM_ATT_MAP['IMSI'])
    @IMSI.setter
    def IMSI(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IMSI'], value)

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
    def Lifetime(self):
        """
        Returns
        -------
        - number: Amount of time (in seconds) to wait after attach procedure completes before scheduling forced detach.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Lifetime'])
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Lifetime'], value)

    @property
    def MEI(self):
        """
        Returns
        -------
        - str: International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MEI'])
    @MEI.setter
    def MEI(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MEI'], value)

    @property
    def MSISDN(self):
        """
        Returns
        -------
        - str: Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
        """
        return self._get_attribute(self._SDM_ATT_MAP['MSISDN'])
    @MSISDN.setter
    def MSISDN(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MSISDN'], value)

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
    def ParentRange(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../enbS5S8SecondaryRange): Parent range
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentRange'])
    @ParentRange.setter
    def ParentRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ParentRange'], value)

    @property
    def SV(self):
        """
        Returns
        -------
        - str: The software version number to be appended to the IMEI in order to generate IMEISV
        """
        return self._get_attribute(self._SDM_ATT_MAP['SV'])
    @SV.setter
    def SV(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SV'], value)

    @property
    def SelectionMode(self):
        """
        Returns
        -------
        - number: Indicates the origin of the APN in the message
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectionMode'])
    @SelectionMode.setter
    def SelectionMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectionMode'], value)

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
    def UpdateAmbrEnable(self):
        """
        Returns
        -------
        - bool: Update APN-AMBR for this UE
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrEnable'])
    @UpdateAmbrEnable.setter
    def UpdateAmbrEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrEnable'], value)

    @property
    def UpdateAmbrIncrement(self):
        """
        Returns
        -------
        - number: Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrIncrement'])
    @UpdateAmbrIncrement.setter
    def UpdateAmbrIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrIncrement'], value)

    @property
    def UpdateAmbrIterations(self):
        """
        Returns
        -------
        - number: How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrIterations'])
    @UpdateAmbrIterations.setter
    def UpdateAmbrIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrIterations'], value)

    @property
    def UpdateAmbrTimeout(self):
        """
        Returns
        -------
        - number: Time to wait (in seconds) since the session was created until sending the update
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrTimeout'])
    @UpdateAmbrTimeout.setter
    def UpdateAmbrTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrTimeout'], value)

    def update(self, APNRestriction=None, Count=None, EnableLifetime=None, EnableMobility=None, EnableSV=None, Enabled=None, IMSI=None, IncrementBy=None, Lifetime=None, MEI=None, MSISDN=None, MaxDelayVariation=None, MaxIntervalVariation=None, MobilityInterval=None, Name=None, ParentRange=None, SV=None, SelectionMode=None, StartDelay=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None):
        """Updates egtpUeS5S8Range resource on the server.

        Args
        ----
        - APNRestriction (number): Authorization to access another APN
        - Count (number): The total number of UEs to be created for this range.
        - EnableLifetime (bool): Enable UE lifetime control. The UE will disconnect after the specified time.
        - EnableMobility (bool): Perform a mobility test
        - EnableSV (bool): Use Software Version to generate IMEISV
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IMSI (str): International Mobile Subscriber Identity
        - IncrementBy (number): Increment by this amount
        - Lifetime (number): Amount of time (in seconds) to wait after attach procedure completes before scheduling forced detach.
        - MEI (str): International Mobile Equipment Identity IMEI MUST be 15 char length. You must enter only the first 14! The last number(15th) of the IMEI is a check digit calculated using the Luhn algorithm.
        - MSISDN (str): Start value for Mobile Subscriber ISDN(Integrated Services Digital Network) Number
        - MaxDelayVariation (number): Randomize Start delay by max +/- X%
        - MaxIntervalVariation (number): Randomize Mobility interval by max +/- X%
        - MobilityInterval (number): The total time (seconds) it will take the mobile to return to the starting node
        - Name (str): Name of range
        - ParentRange (str(None | /api/v1/sessions/1/ixnetwork/vport/.../enbS5S8SecondaryRange)): Parent range
        - SV (str): The software version number to be appended to the IMEI in order to generate IMEISV
        - SelectionMode (number): Indicates the origin of the APN in the message
        - StartDelay (number): How many seconds to wait before starting to move the UEs
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update

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
