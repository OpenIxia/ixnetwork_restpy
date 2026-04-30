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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class PtpSlaveWizardPage(Base):
    """Slave port settings page
    The PtpSlaveWizardPage class encapsulates a list of ptpSlaveWizardPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the PtpSlaveWizardPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ptpSlaveWizardPage"
    _SDM_ATT_MAP = {
        "ClockAccuracy": "clockAccuracy",
        "ClockClass": "clockClass",
        "ClockIncrement": "clockIncrement",
        "ClockRangeIncrement": "clockRangeIncrement",
        "DelayRespDropRate": "delayRespDropRate",
        "DelayResponseDelay": "delayResponseDelay",
        "DelayResponseDelayInsertionRate": "delayResponseDelayInsertionRate",
        "FirstClock": "firstClock",
        "FollowUpBadCrcRate": "followUpBadCrcRate",
        "FollowUpDelay": "followUpDelay",
        "FollowUpDelayInsertionRate": "followUpDelayInsertionRate",
        "FollowUpDropRate": "followUpDropRate",
        "IsExtensionOnMac": "isExtensionOnMac",
        "IsMaster": "isMaster",
        "MasterIpAddress": "masterIpAddress",
        "MasterIpIncrementBy": "masterIpIncrementBy",
        "MasterIpRangeIncrementBy": "masterIpRangeIncrementBy",
        "MasterMacAddress": "masterMacAddress",
        "MasterMacIncrementBy": "masterMacIncrementBy",
        "MasterMacRangeIncrementBy": "masterMacRangeIncrementBy",
        "Priority1": "priority1",
        "Priority2": "priority2",
        "UseClockIdentity": "useClockIdentity",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PtpSlaveWizardPage, self).__init__(parent, list_op)

    @property
    def ClockAccuracy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The expected accuracy of a clock when it is the Grandmaster, or in the event it becomes the Grandmaster
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClockAccuracy"])

    @ClockAccuracy.setter
    def ClockAccuracy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClockAccuracy"], value)

    @property
    def ClockClass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The traceability of the time or frequency distributed by the Grandmaster Clock
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClockClass"])

    @ClockClass.setter
    def ClockClass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClockClass"], value)

    @property
    def ClockIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The clock Identity increment to be used in this range
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClockIncrement"])

    @ClockIncrement.setter
    def ClockIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClockIncrement"], value)

    @property
    def ClockRangeIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The clock identity increment value used when the wizard creates multiple ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClockRangeIncrement"])

    @ClockRangeIncrement.setter
    def ClockRangeIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClockRangeIncrement"], value)

    @property
    def DelayRespDropRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Delay Response Drop rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayRespDropRate"])

    @DelayRespDropRate.setter
    def DelayRespDropRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayRespDropRate"], value)

    @property
    def DelayResponseDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Delay Response Delay
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayResponseDelay"])

    @DelayResponseDelay.setter
    def DelayResponseDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayResponseDelay"], value)

    @property
    def DelayResponseDelayInsertionRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Delay Response Delay Insertion rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayResponseDelayInsertionRate"])

    @DelayResponseDelayInsertionRate.setter
    def DelayResponseDelayInsertionRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayResponseDelayInsertionRate"], value)

    @property
    def FirstClock(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first Clock Identity to be used in this range
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstClock"])

    @FirstClock.setter
    def FirstClock(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstClock"], value)

    @property
    def FollowUpBadCrcRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Follow-up Bad CRC rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FollowUpBadCrcRate"])

    @FollowUpBadCrcRate.setter
    def FollowUpBadCrcRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FollowUpBadCrcRate"], value)

    @property
    def FollowUpDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Follow-up Delay
        """
        return self._get_attribute(self._SDM_ATT_MAP["FollowUpDelay"])

    @FollowUpDelay.setter
    def FollowUpDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FollowUpDelay"], value)

    @property
    def FollowUpDelayInsertionRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Follow-up Delay Insertion rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FollowUpDelayInsertionRate"])

    @FollowUpDelayInsertionRate.setter
    def FollowUpDelayInsertionRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FollowUpDelayInsertionRate"], value)

    @property
    def FollowUpDropRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Follow-up Drop rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FollowUpDropRate"])

    @FollowUpDropRate.setter
    def FollowUpDropRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FollowUpDropRate"], value)

    @property
    def IsExtensionOnMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PTP Extension is added to MAC stack
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsExtensionOnMac"])

    @IsExtensionOnMac.setter
    def IsExtensionOnMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsExtensionOnMac"], value)

    @property
    def IsMaster(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets clock as Master
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMaster"])

    @IsMaster.setter
    def IsMaster(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsMaster"], value)

    @property
    def MasterIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IP address in the range
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterIpAddress"])

    @MasterIpAddress.setter
    def MasterIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterIpAddress"], value)

    @property
    def MasterIpIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value used to enumerate all the addresses in the range
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterIpIncrementBy"])

    @MasterIpIncrementBy.setter
    def MasterIpIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterIpIncrementBy"], value)

    @property
    def MasterIpRangeIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: How the starting IP addresses are incremented when the wizard creates multiple ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterIpRangeIncrementBy"])

    @MasterIpRangeIncrementBy.setter
    def MasterIpRangeIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterIpRangeIncrementBy"], value)

    @property
    def MasterMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base value used when the network stack element creates MAC addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterMacAddress"])

    @MasterMacAddress.setter
    def MasterMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterMacAddress"], value)

    @property
    def MasterMacIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value that is used (in conjunction with the Master MAC address) to create a range of multiple MAC addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterMacIncrementBy"])

    @MasterMacIncrementBy.setter
    def MasterMacIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterMacIncrementBy"], value)

    @property
    def MasterMacRangeIncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC address incrementor used when the wizard creates multiple ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterMacRangeIncrementBy"])

    @MasterMacRangeIncrementBy.setter
    def MasterMacRangeIncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterMacRangeIncrementBy"], value)

    @property
    def Priority1(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The priority1 attribute of the Grandmaster Clock
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority1"])

    @Priority1.setter
    def Priority1(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority1"], value)

    @property
    def Priority2(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The priority2 attribute of the Grandmaster Clock
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority2"])

    @Priority2.setter
    def Priority2(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority2"], value)

    @property
    def UseClockIdentity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IxNetwork configures the clock identity using the Clock Identity values specified here
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseClockIdentity"])

    @UseClockIdentity.setter
    def UseClockIdentity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseClockIdentity"], value)

    def update(
        self,
        ClockAccuracy=None,
        ClockClass=None,
        ClockIncrement=None,
        ClockRangeIncrement=None,
        DelayRespDropRate=None,
        DelayResponseDelay=None,
        DelayResponseDelayInsertionRate=None,
        FirstClock=None,
        FollowUpBadCrcRate=None,
        FollowUpDelay=None,
        FollowUpDelayInsertionRate=None,
        FollowUpDropRate=None,
        IsExtensionOnMac=None,
        IsMaster=None,
        MasterIpAddress=None,
        MasterIpIncrementBy=None,
        MasterIpRangeIncrementBy=None,
        MasterMacAddress=None,
        MasterMacIncrementBy=None,
        MasterMacRangeIncrementBy=None,
        Priority1=None,
        Priority2=None,
        UseClockIdentity=None,
    ):
        # type: (str, int, str, str, int, int, int, str, int, int, int, int, bool, bool, str, str, str, str, str, str, int, int, bool) -> PtpSlaveWizardPage
        """Updates ptpSlaveWizardPage resource on the server.

        Args
        ----
        - ClockAccuracy (str): The expected accuracy of a clock when it is the Grandmaster, or in the event it becomes the Grandmaster
        - ClockClass (number): The traceability of the time or frequency distributed by the Grandmaster Clock
        - ClockIncrement (str): The clock Identity increment to be used in this range
        - ClockRangeIncrement (str): The clock identity increment value used when the wizard creates multiple ranges
        - DelayRespDropRate (number): The Delay Response Drop rate
        - DelayResponseDelay (number): The Delay Response Delay
        - DelayResponseDelayInsertionRate (number): The Delay Response Delay Insertion rate
        - FirstClock (str): The first Clock Identity to be used in this range
        - FollowUpBadCrcRate (number): The Follow-up Bad CRC rate
        - FollowUpDelay (number): The Follow-up Delay
        - FollowUpDelayInsertionRate (number): The Follow-up Delay Insertion rate
        - FollowUpDropRate (number): The Follow-up Drop rate
        - IsExtensionOnMac (bool): PTP Extension is added to MAC stack
        - IsMaster (bool): Sets clock as Master
        - MasterIpAddress (str): The first IP address in the range
        - MasterIpIncrementBy (str): The value used to enumerate all the addresses in the range
        - MasterIpRangeIncrementBy (str): How the starting IP addresses are incremented when the wizard creates multiple ranges
        - MasterMacAddress (str): The base value used when the network stack element creates MAC addresses
        - MasterMacIncrementBy (str): The value that is used (in conjunction with the Master MAC address) to create a range of multiple MAC addresses
        - MasterMacRangeIncrementBy (str): The MAC address incrementor used when the wizard creates multiple ranges
        - Priority1 (number): The priority1 attribute of the Grandmaster Clock
        - Priority2 (number): The priority2 attribute of the Grandmaster Clock
        - UseClockIdentity (bool): IxNetwork configures the clock identity using the Clock Identity values specified here

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ClockAccuracy=None,
        ClockClass=None,
        ClockIncrement=None,
        ClockRangeIncrement=None,
        DelayRespDropRate=None,
        DelayResponseDelay=None,
        DelayResponseDelayInsertionRate=None,
        FirstClock=None,
        FollowUpBadCrcRate=None,
        FollowUpDelay=None,
        FollowUpDelayInsertionRate=None,
        FollowUpDropRate=None,
        IsExtensionOnMac=None,
        IsMaster=None,
        MasterIpAddress=None,
        MasterIpIncrementBy=None,
        MasterIpRangeIncrementBy=None,
        MasterMacAddress=None,
        MasterMacIncrementBy=None,
        MasterMacRangeIncrementBy=None,
        Priority1=None,
        Priority2=None,
        UseClockIdentity=None,
    ):
        # type: (str, int, str, str, int, int, int, str, int, int, int, int, bool, bool, str, str, str, str, str, str, int, int, bool) -> PtpSlaveWizardPage
        """Adds a new ptpSlaveWizardPage resource on the json, only valid with batch add utility

        Args
        ----
        - ClockAccuracy (str): The expected accuracy of a clock when it is the Grandmaster, or in the event it becomes the Grandmaster
        - ClockClass (number): The traceability of the time or frequency distributed by the Grandmaster Clock
        - ClockIncrement (str): The clock Identity increment to be used in this range
        - ClockRangeIncrement (str): The clock identity increment value used when the wizard creates multiple ranges
        - DelayRespDropRate (number): The Delay Response Drop rate
        - DelayResponseDelay (number): The Delay Response Delay
        - DelayResponseDelayInsertionRate (number): The Delay Response Delay Insertion rate
        - FirstClock (str): The first Clock Identity to be used in this range
        - FollowUpBadCrcRate (number): The Follow-up Bad CRC rate
        - FollowUpDelay (number): The Follow-up Delay
        - FollowUpDelayInsertionRate (number): The Follow-up Delay Insertion rate
        - FollowUpDropRate (number): The Follow-up Drop rate
        - IsExtensionOnMac (bool): PTP Extension is added to MAC stack
        - IsMaster (bool): Sets clock as Master
        - MasterIpAddress (str): The first IP address in the range
        - MasterIpIncrementBy (str): The value used to enumerate all the addresses in the range
        - MasterIpRangeIncrementBy (str): How the starting IP addresses are incremented when the wizard creates multiple ranges
        - MasterMacAddress (str): The base value used when the network stack element creates MAC addresses
        - MasterMacIncrementBy (str): The value that is used (in conjunction with the Master MAC address) to create a range of multiple MAC addresses
        - MasterMacRangeIncrementBy (str): The MAC address incrementor used when the wizard creates multiple ranges
        - Priority1 (number): The priority1 attribute of the Grandmaster Clock
        - Priority2 (number): The priority2 attribute of the Grandmaster Clock
        - UseClockIdentity (bool): IxNetwork configures the clock identity using the Clock Identity values specified here

        Returns
        -------
        - self: This instance with all currently retrieved ptpSlaveWizardPage resources using find and the newly added ptpSlaveWizardPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ClockAccuracy=None,
        ClockClass=None,
        ClockIncrement=None,
        ClockRangeIncrement=None,
        DelayRespDropRate=None,
        DelayResponseDelay=None,
        DelayResponseDelayInsertionRate=None,
        FirstClock=None,
        FollowUpBadCrcRate=None,
        FollowUpDelay=None,
        FollowUpDelayInsertionRate=None,
        FollowUpDropRate=None,
        IsExtensionOnMac=None,
        IsMaster=None,
        MasterIpAddress=None,
        MasterIpIncrementBy=None,
        MasterIpRangeIncrementBy=None,
        MasterMacAddress=None,
        MasterMacIncrementBy=None,
        MasterMacRangeIncrementBy=None,
        Priority1=None,
        Priority2=None,
        UseClockIdentity=None,
    ):
        # type: (str, int, str, str, int, int, int, str, int, int, int, int, bool, bool, str, str, str, str, str, str, int, int, bool) -> PtpSlaveWizardPage
        """Finds and retrieves ptpSlaveWizardPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ptpSlaveWizardPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ptpSlaveWizardPage resources from the server.

        Args
        ----
        - ClockAccuracy (str): The expected accuracy of a clock when it is the Grandmaster, or in the event it becomes the Grandmaster
        - ClockClass (number): The traceability of the time or frequency distributed by the Grandmaster Clock
        - ClockIncrement (str): The clock Identity increment to be used in this range
        - ClockRangeIncrement (str): The clock identity increment value used when the wizard creates multiple ranges
        - DelayRespDropRate (number): The Delay Response Drop rate
        - DelayResponseDelay (number): The Delay Response Delay
        - DelayResponseDelayInsertionRate (number): The Delay Response Delay Insertion rate
        - FirstClock (str): The first Clock Identity to be used in this range
        - FollowUpBadCrcRate (number): The Follow-up Bad CRC rate
        - FollowUpDelay (number): The Follow-up Delay
        - FollowUpDelayInsertionRate (number): The Follow-up Delay Insertion rate
        - FollowUpDropRate (number): The Follow-up Drop rate
        - IsExtensionOnMac (bool): PTP Extension is added to MAC stack
        - IsMaster (bool): Sets clock as Master
        - MasterIpAddress (str): The first IP address in the range
        - MasterIpIncrementBy (str): The value used to enumerate all the addresses in the range
        - MasterIpRangeIncrementBy (str): How the starting IP addresses are incremented when the wizard creates multiple ranges
        - MasterMacAddress (str): The base value used when the network stack element creates MAC addresses
        - MasterMacIncrementBy (str): The value that is used (in conjunction with the Master MAC address) to create a range of multiple MAC addresses
        - MasterMacRangeIncrementBy (str): The MAC address incrementor used when the wizard creates multiple ranges
        - Priority1 (number): The priority1 attribute of the Grandmaster Clock
        - Priority2 (number): The priority2 attribute of the Grandmaster Clock
        - UseClockIdentity (bool): IxNetwork configures the clock identity using the Clock Identity values specified here

        Returns
        -------
        - self: This instance with matching ptpSlaveWizardPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ptpSlaveWizardPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ptpSlaveWizardPage resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
