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


class TestConfig(Base):
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AddrRateNumFrames(self):
        """
        Returns
        -------
        - number: Indicates the address rate in number of frames.
        """
        return self._get_attribute('addrRateNumFrames')
    @AddrRateNumFrames.setter
    def AddrRateNumFrames(self, value):
        self._set_attribute('addrRateNumFrames', value)

    @property
    def AddrRateValidationFpsRate(self):
        """
        Returns
        -------
        - str: Indicates that the step rate of the load unit is fpsRate.
        """
        return self._get_attribute('addrRateValidationFpsRate')
    @AddrRateValidationFpsRate.setter
    def AddrRateValidationFpsRate(self, value):
        self._set_attribute('addrRateValidationFpsRate', value)

    @property
    def AddrRateValidationRate(self):
        """
        Returns
        -------
        - number: Indicates the address rate validation rate.
        """
        return self._get_attribute('addrRateValidationRate')
    @AddrRateValidationRate.setter
    def AddrRateValidationRate(self, value):
        self._set_attribute('addrRateValidationRate', value)

    @property
    def AddrRateValidationRateUnit(self):
        """
        Returns
        -------
        - str(fps | percentMaxRate): Indicates the address rate validation rate unit.
        """
        return self._get_attribute('addrRateValidationRateUnit')
    @AddrRateValidationRateUnit.setter
    def AddrRateValidationRateUnit(self, value):
        self._set_attribute('addrRateValidationRateUnit', value)

    @property
    def AddressRatePassCriteriaMode(self):
        """
        Returns
        -------
        - str: Indicates the address rate pass criteria mode.
        """
        return self._get_attribute('addressRatePassCriteriaMode')
    @AddressRatePassCriteriaMode.setter
    def AddressRatePassCriteriaMode(self, value):
        self._set_attribute('addressRatePassCriteriaMode', value)

    @property
    def AddressRatePassFailValue(self):
        """
        Returns
        -------
        - number: Indicates the Address Rate value.
        """
        return self._get_attribute('addressRatePassFailValue')
    @AddressRatePassFailValue.setter
    def AddressRatePassFailValue(self, value):
        self._set_attribute('addressRatePassFailValue', value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The binary search interval through which the next iteration's rate is obtained.
        """
        return self._get_attribute('binaryBackoff')
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute('binaryBackoff', value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(fpsRate): Indicates the binary load unit.
        """
        return self._get_attribute('binaryLoadUnit')
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute('binaryLoadUnit', value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: Indicates the resolution during the binary search.
        """
        return self._get_attribute('binaryResolution')
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute('binaryResolution', value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear): Indicates the search type for a Binary search.
        """
        return self._get_attribute('binarySearchType')
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute('binarySearchType', value)

    @property
    def CacheTimeout(self):
        """
        Returns
        -------
        - number: Indicates cache time out.
        """
        return self._get_attribute('cacheTimeout')
    @CacheTimeout.setter
    def CacheTimeout(self, value):
        self._set_attribute('cacheTimeout', value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute('delayAfterTransmit')
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute('delayAfterTransmit', value)

    @property
    def EnableAddressRatePassFail(self):
        """
        Returns
        -------
        - bool: If true, allows Address Rate to be used as a Pass/Fail criteria.
        """
        return self._get_attribute('enableAddressRatePassFail')
    @EnableAddressRatePassFail.setter
    def EnableAddressRatePassFail(self, value):
        self._set_attribute('enableAddressRatePassFail', value)

    @property
    def EnableCacheTimeout(self):
        """
        Returns
        -------
        - bool: If true, enables cache time out.
        """
        return self._get_attribute('enableCacheTimeout')
    @EnableCacheTimeout.setter
    def EnableCacheTimeout(self, value):
        self._set_attribute('enableCacheTimeout', value)

    @property
    def EnableDaD(self):
        """
        Returns
        -------
        - bool: If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
        """
        return self._get_attribute('enableDaD')
    @EnableDaD.setter
    def EnableDaD(self, value):
        self._set_attribute('enableDaD', value)

    @property
    def EnableDropLink(self):
        """
        Returns
        -------
        - bool: If true, allows Route Range to be dropped.
        """
        return self._get_attribute('enableDropLink')
    @EnableDropLink.setter
    def EnableDropLink(self, value):
        self._set_attribute('enableDropLink', value)

    @property
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: If true, enables extra iterations. Sets extra iteration offset values.
        """
        return self._get_attribute('enableExtraIterations')
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute('enableExtraIterations', value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, allows to set minimum frame size.
        """
        return self._get_attribute('enableMinFrameSize')
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute('enableMinFrameSize', value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: Sets extra iteration offset values.
        """
        return self._get_attribute('extraIterationOffsets')
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute('extraIterationOffsets', value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(fixed): Indicates the frame size mode.
        """
        return self._get_attribute('frameSizeMode')
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute('frameSizeMode', value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - str: The frame size used by the service.
        """
        return self._get_attribute('framesize')
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute('framesize', value)

    @property
    def FramesizeFixedValue(self):
        """
        Returns
        -------
        - number: It signifies the frame size fixed value.
        """
        return self._get_attribute('framesizeFixedValue')
    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        self._set_attribute('framesizeFixedValue', value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): The list of the available frame size.
        """
        return self._get_attribute('framesizeList')
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute('framesizeList', value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Indicates the initial binary load rate.
        """
        return self._get_attribute('initialBinaryLoadRate')
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute('initialBinaryLoadRate', value)

    @property
    def Layer3AddressCount(self):
        """
        Returns
        -------
        - number: Indicates the Layer 3 address count.
        """
        return self._get_attribute('layer3AddressCount')
    @Layer3AddressCount.setter
    def Layer3AddressCount(self, value):
        self._set_attribute('layer3AddressCount', value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: Enter the Load Rate List.
        """
        return self._get_attribute('loadRateList')
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute('loadRateList', value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary): Indicates the load type.
        """
        return self._get_attribute('loadType')
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute('loadType', value)

    @property
    def LoadUnit(self):
        """
        Returns
        -------
        - str(fpsRate): Indicates the load unit.
        """
        return self._get_attribute('loadUnit')
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute('loadUnit', value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: Indicates the traffic map type.
        """
        return self._get_attribute('mapType')
    @MapType.setter
    def MapType(self, value):
        self._set_attribute('mapType', value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Indicates the maximum binary load rate.
        """
        return self._get_attribute('maxBinaryLoadRate')
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute('maxBinaryLoadRate', value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: Indicates maximum outstanding request.
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: Indicates the minimum binary load rate.
        """
        return self._get_attribute('minBinaryLoadRate')
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute('minBinaryLoadRate', value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Number of trials that can be run.
        """
        return self._get_attribute('numtrials')
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute('numtrials', value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('portDelayEnabled')
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute('portDelayEnabled', value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute('portDelayUnit')
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute('portDelayUnit', value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute('portDelayValue')
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute('portDelayValue', value)

    @property
    def PortDownTime(self):
        """
        Returns
        -------
        - number: During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
        """
        return self._get_attribute('portDownTime')
    @PortDownTime.setter
    def PortDownTime(self, value):
        self._set_attribute('portDownTime', value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute('protocolItem')
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute('protocolItem', value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Enables a staggered start to traffic transmit.
        """
        return self._get_attribute('staggeredStart')
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute('staggeredStart', value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The traffic types supported.
        """
        return self._get_attribute('supportedTrafficTypes')
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute('supportedTrafficTypes', value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    def update(self, AddrRateNumFrames=None, AddrRateValidationFpsRate=None, AddrRateValidationRate=None, AddrRateValidationRateUnit=None, AddressRatePassCriteriaMode=None, AddressRatePassFailValue=None, BinaryBackoff=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, CacheTimeout=None, DelayAfterTransmit=None, EnableAddressRatePassFail=None, EnableCacheTimeout=None, EnableDaD=None, EnableDropLink=None, EnableExtraIterations=None, EnableMinFrameSize=None, ExtraIterationOffsets=None, FrameSizeMode=None, Framesize=None, FramesizeFixedValue=None, FramesizeList=None, InitialBinaryLoadRate=None, Layer3AddressCount=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxBinaryLoadRate=None, MaxOutstandingRequests=None, MinBinaryLoadRate=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortDownTime=None, ProtocolItem=None, StaggeredStart=None, SupportedTrafficTypes=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AddrRateNumFrames (number): Indicates the address rate in number of frames.
        - AddrRateValidationFpsRate (str): Indicates that the step rate of the load unit is fpsRate.
        - AddrRateValidationRate (number): Indicates the address rate validation rate.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): Indicates the address rate validation rate unit.
        - AddressRatePassCriteriaMode (str): Indicates the address rate pass criteria mode.
        - AddressRatePassFailValue (number): Indicates the Address Rate value.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryLoadUnit (str(fpsRate)): Indicates the binary load unit.
        - BinaryResolution (number): Indicates the resolution during the binary search.
        - BinarySearchType (str(linear)): Indicates the search type for a Binary search.
        - CacheTimeout (number): Indicates cache time out.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - EnableAddressRatePassFail (bool): If true, allows Address Rate to be used as a Pass/Fail criteria.
        - EnableCacheTimeout (bool): If true, enables cache time out.
        - EnableDaD (bool): If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
        - EnableDropLink (bool): If true, allows Route Range to be dropped.
        - EnableExtraIterations (bool): If true, enables extra iterations. Sets extra iteration offset values.
        - EnableMinFrameSize (bool): If true, allows to set minimum frame size.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FrameSizeMode (str(fixed)): Indicates the frame size mode.
        - Framesize (str): The frame size used by the service.
        - FramesizeFixedValue (number): It signifies the frame size fixed value.
        - FramesizeList (list(str)): The list of the available frame size.
        - InitialBinaryLoadRate (number): Indicates the initial binary load rate.
        - Layer3AddressCount (number): Indicates the Layer 3 address count.
        - LoadRateList (str): Enter the Load Rate List.
        - LoadType (str(binary)): Indicates the load type.
        - LoadUnit (str(fpsRate)): Indicates the load unit.
        - MapType (str): Indicates the traffic map type.
        - MaxBinaryLoadRate (number): Indicates the maximum binary load rate.
        - MaxOutstandingRequests (number): Indicates maximum outstanding request.
        - MinBinaryLoadRate (number): Indicates the minimum binary load rate.
        - Numtrials (number): Number of trials that can be run.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - StaggeredStart (bool): Enables a staggered start to traffic transmit.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TxDelay (number): Specifies the amount of delay after every transmit.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
