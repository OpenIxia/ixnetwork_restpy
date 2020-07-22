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


class TestConfig(Base):
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'AddrRateNumFrames': 'addrRateNumFrames',
        'AddrRateValidationFpsRate': 'addrRateValidationFpsRate',
        'AddrRateValidationRate': 'addrRateValidationRate',
        'AddrRateValidationRateUnit': 'addrRateValidationRateUnit',
        'AddressRatePassCriteriaMode': 'addressRatePassCriteriaMode',
        'AddressRatePassFailValue': 'addressRatePassFailValue',
        'Age': 'age',
        'BidirectionalOptionEnabled': 'bidirectionalOptionEnabled',
        'BinaryBackoff': 'binaryBackoff',
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'BinarySearchType': 'binarySearchType',
        'BinaryTolerance': 'binaryTolerance',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'EnableAddressRatePassFail': 'enableAddressRatePassFail',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableDropLink': 'enableDropLink',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnforceBidirectional': 'enforceBidirectional',
        'FrameSizeMode': 'frameSizeMode',
        'FramesizeList': 'framesizeList',
        'InitialBinaryLoadRate': 'initialBinaryLoadRate',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'LoadUnit': 'loadUnit',
        'MapType': 'mapType',
        'MaxBinaryLoadRate': 'maxBinaryLoadRate',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MinBinaryLoadRate': 'minBinaryLoadRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'PortDownTime': 'portDownTime',
        'ProtocolItem': 'protocolItem',
        'Rfc2889ordering': 'rfc2889ordering',
        'ShowDetailedBinaryResults': 'showDetailedBinaryResults',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'Tablesize': 'tablesize',
        'TxDelay': 'txDelay',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AddrRateNumFrames(self):
        """
        Returns
        -------
        - number: The number of addresses that are to be used for each port in the current configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateNumFrames'])
    @AddrRateNumFrames.setter
    def AddrRateNumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateNumFrames'], value)

    @property
    def AddrRateValidationFpsRate(self):
        """
        Returns
        -------
        - str: The rate at which validation frames are sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationFpsRate'])
    @AddrRateValidationFpsRate.setter
    def AddrRateValidationFpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationFpsRate'], value)

    @property
    def AddrRateValidationRate(self):
        """
        Returns
        -------
        - number: The number of validation frames that IxNetwork sends for each address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationRate'])
    @AddrRateValidationRate.setter
    def AddrRateValidationRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationRate'], value)

    @property
    def AddrRateValidationRateUnit(self):
        """
        Returns
        -------
        - str(fps | percentMaxRate): Rate at which validation frames are transmitted for each address. Can be expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrRateValidationRateUnit'])
    @AddrRateValidationRateUnit.setter
    def AddrRateValidationRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrRateValidationRateUnit'], value)

    @property
    def AddressRatePassCriteriaMode(self):
        """
        Returns
        -------
        - str: Mode used to determine pass criteria. Can be Average Port or Minimum Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressRatePassCriteriaMode'])
    @AddressRatePassCriteriaMode.setter
    def AddressRatePassCriteriaMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressRatePassCriteriaMode'], value)

    @property
    def AddressRatePassFailValue(self):
        """
        Returns
        -------
        - number: Determines whether the trial in the test passed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressRatePassFailValue'])
    @AddressRatePassFailValue.setter
    def AddressRatePassFailValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressRatePassFailValue'], value)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: This indicates the age in time, in seconds, since it was last refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])
    @Age.setter
    def Age(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Age'], value)

    @property
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: If true, allows bidirectional traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'])
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BidirectionalOptionEnabled'], value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The percentage to be applied to the search interval through which the next iteration rate is obtained.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryBackoff'])
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryBackoff'], value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(fpsRate): The binary load unit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'])
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'], value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: The resolution of the iteration during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear): It signifies the binary search type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinarySearchType'])
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinarySearchType'], value)

    @property
    def BinaryTolerance(self):
        """
        Returns
        -------
        - number: The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryTolerance'])
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryTolerance'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: If true, randomly counts the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def EnableAddressRatePassFail(self):
        """
        Returns
        -------
        - bool: If true, IxNetwork applies the pass or fail criteria to each trial in the test and determines whether the trial passed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAddressRatePassFail'])
    @EnableAddressRatePassFail.setter
    def EnableAddressRatePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAddressRatePassFail'], value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

    @property
    def EnableDropLink(self):
        """
        Returns
        -------
        - bool: If true, allows to drop link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDropLink'])
    @EnableDropLink.setter
    def EnableDropLink(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDropLink'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnforceBidirectional(self):
        """
        Returns
        -------
        - bool: If true, uses bidirectional traffic mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforceBidirectional'])
    @EnforceBidirectional.setter
    def EnforceBidirectional(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnforceBidirectional'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): List containing the frame sizes used in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeList'])
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeList'], value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The load rate used in the first iteration for each frame size during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'])
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadRate'], value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: It signifies the list of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateList'])
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateList'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary): Specifies the load type of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def LoadUnit(self):
        """
        Returns
        -------
        - str(fpsRate): The load unit value of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadUnit'])
    @LoadUnit.setter
    def LoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadUnit'], value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The mapping type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The upper bound of the iteration rates for each frame size during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'])
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadRate'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The lower bound of the iteration rates for each frame size during a binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'])
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadRate'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Defines how many times each frame size will be tested.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

    @property
    def PortDownTime(self):
        """
        Returns
        -------
        - number: The time interval during the port is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDownTime'])
    @PortDownTime.setter
    def PortDownTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDownTime'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def Rfc2889ordering(self):
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): Enables ordering.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rfc2889ordering'])
    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rfc2889ordering'], value)

    @property
    def ShowDetailedBinaryResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'])
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowDetailedBinaryResults'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The incremental step value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The supported traffic types. Possible values of traffic types are ipmix, IPv4, IPv6 and MAC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def Tablesize(self):
        """
        Returns
        -------
        - number: New table size for each retry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tablesize'])
    @Tablesize.setter
    def Tablesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tablesize'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: Signifies the transmission delay time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    def update(self, AddrRateNumFrames=None, AddrRateValidationFpsRate=None, AddrRateValidationRate=None, AddrRateValidationRateUnit=None, AddressRatePassCriteriaMode=None, AddressRatePassFailValue=None, Age=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, CountRandomFrameSize=None, DelayAfterTransmit=None, EnableAddressRatePassFail=None, EnableDataIntegrity=None, EnableDropLink=None, EnableMinFrameSize=None, EnforceBidirectional=None, FrameSizeMode=None, FramesizeList=None, InitialBinaryLoadRate=None, LoadRateList=None, LoadType=None, LoadUnit=None, MapType=None, MaxBinaryLoadRate=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinBinaryLoadRate=None, MinIncrementFrameSize=None, MinRandomFrameSize=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, PortDownTime=None, ProtocolItem=None, Rfc2889ordering=None, ShowDetailedBinaryResults=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, Tablesize=None, TxDelay=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AddrRateNumFrames (number): The number of addresses that are to be used for each port in the current configuration.
        - AddrRateValidationFpsRate (str): The rate at which validation frames are sent.
        - AddrRateValidationRate (number): The number of validation frames that IxNetwork sends for each address.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): Rate at which validation frames are transmitted for each address. Can be expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        - AddressRatePassCriteriaMode (str): Mode used to determine pass criteria. Can be Average Port or Minimum Port.
        - AddressRatePassFailValue (number): Determines whether the trial in the test passed or failed.
        - Age (number): This indicates the age in time, in seconds, since it was last refreshed.
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinaryBackoff (number): The percentage to be applied to the search interval through which the next iteration rate is obtained.
        - BinaryLoadUnit (str(fpsRate)): The binary load unit value.
        - BinaryResolution (number): The resolution of the iteration during a binary search.
        - BinarySearchType (str(linear)): It signifies the binary search type value.
        - BinaryTolerance (number): The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - EnableAddressRatePassFail (bool): If true, IxNetwork applies the pass or fail criteria to each trial in the test and determines whether the trial passed or failed.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableDropLink (bool): If true, allows to drop link.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - InitialBinaryLoadRate (number): The load rate used in the first iteration for each frame size during a binary search.
        - LoadRateList (str): It signifies the list of load rate.
        - LoadType (str(binary)): Specifies the load type of the test configuration.
        - LoadUnit (str(fpsRate)): The load unit value of the test configuration.
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinBinaryLoadRate (number): The lower bound of the iteration rates for each frame size during a binary search.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): The time interval during the port is down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): Enables ordering.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The supported traffic types. Possible values of traffic types are ipmix, IPv4, IPv6 and MAC.
        - Tablesize (number): New table size for each retry.
        - TxDelay (number): Signifies the transmission delay time.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
