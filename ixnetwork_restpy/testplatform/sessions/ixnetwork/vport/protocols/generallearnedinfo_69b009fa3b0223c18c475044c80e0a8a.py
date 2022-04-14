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


class GeneralLearnedInfo(Base):
    """This object holds lists of the general learned route information.
    The GeneralLearnedInfo class encapsulates a list of generalLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the GeneralLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "generalLearnedInfo"
    _SDM_ATT_MAP = {
        "AisRx": "aisRx",
        "AisState": "aisState",
        "AisTx": "aisTx",
        "AlarmTypeAis": "alarmTypeAis",
        "AlarmTypeLck": "alarmTypeLck",
        "ApsLocalDataPath": "apsLocalDataPath",
        "ApsLocalFaultPath": "apsLocalFaultPath",
        "ApsLocalState": "apsLocalState",
        "ApsRemoteDataPath": "apsRemoteDataPath",
        "ApsRemoteFaultPath": "apsRemoteFaultPath",
        "ApsRemoteRequestState": "apsRemoteRequestState",
        "ContinuityCheckLocalState": "continuityCheckLocalState",
        "ContinuityCheckRemoteState": "continuityCheckRemoteState",
        "ContinuityCheckRxInterval": "continuityCheckRxInterval",
        "ContinuityCheckTxInterval": "continuityCheckTxInterval",
        "IncomingLabelOuterInner": "incomingLabelOuterInner",
        "LastAlarmDuration": "lastAlarmDuration",
        "LckRx": "lckRx",
        "LckState": "lckState",
        "LckTx": "lckTx",
        "Ldi": "ldi",
        "LocalPwStatus": "localPwStatus",
        "OutgoingLabelOuterInner": "outgoingLabelOuterInner",
        "RemoteDefectIndication": "remoteDefectIndication",
        "RemotePwStatus": "remotePwStatus",
        "Role": "role",
        "TimeSinceLastAlarm": "timeSinceLastAlarm",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {
        "apsLocalDataPath": ["working", "protect", "na"],
        "apsLocalFaultPath": ["working", "protect", "both", "none", "na"],
        "apsLocalState": [
            "na",
            "apsNoRequest",
            "apsLockoutOfProtection",
            "apsSignalFailOnWorking",
            "apsManualSwitch",
            "apsWaitToRestore",
            "apsDoNotRevert",
            "apsExercise",
            "apsReverseRequest",
            "pscNormal",
            "pscUnavailable",
            "pscProtectingAdmin",
            "pscProtectingFailure",
            "pscWaitToRevert",
            "pscDoNotRevert",
            "apsSignalFailOnProtection",
            "apsForceSwitch",
        ],
        "apsRemoteDataPath": ["protect", "na", "working"],
        "apsRemoteFaultPath": ["na", "working", "protect", "both", "none"],
        "apsRemoteRequestState": [
            "na",
            "apsNoRequest",
            "apsLockoutOfProtection",
            "apsSignalFailOnWorking",
            "apsManualSwitch",
            "apsWaitToRestore",
            "apsDoNotRevert",
            "apsExercise",
            "apsReverseRequest",
            "pscNormal",
            "pscUnavailable",
            "pscProtectingAdmin",
            "pscProtectingFailure",
            "pscWaitToRevert",
            "pscDoNotRevert",
            "apsSignalFailOnProtection",
            "apsForceSwitch",
        ],
        "continuityCheckLocalState": [
            "na",
            "bfdDown",
            "bfdInit",
            "bfdUp",
            "y1731Down",
            "y1731Init",
            "y1731Up",
        ],
        "continuityCheckRemoteState": [
            "na",
            "bfdDown",
            "bfdInit",
            "bfdUp",
            "y1731Down",
            "y1731Init",
            "y1731Up",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(GeneralLearnedInfo, self).__init__(parent, list_op)

    @property
    def AisRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of AIS frames received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisRx"])

    @property
    def AisState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the state of AIS, either Clear or Fault.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisState"])

    @property
    def AisTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of AIS frames transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisTx"])

    @property
    def AlarmTypeAis(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the type of the AIS alarm, either ietf or y1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmTypeAis"])

    @property
    def AlarmTypeLck(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the type of the LCK alarm, either ietf or y1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlarmTypeLck"])

    @property
    def ApsLocalDataPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str(working | protect | na): This signifies the path of the APS local data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsLocalDataPath"])

    @property
    def ApsLocalFaultPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str(working | protect | both | none | na): This signifies the path of the APS local fault.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsLocalFaultPath"])

    @property
    def ApsLocalState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(na | apsNoRequest | apsLockoutOfProtection | apsSignalFailOnWorking | apsManualSwitch | apsWaitToRestore | apsDoNotRevert | apsExercise | apsReverseRequest | pscNormal | pscUnavailable | pscProtectingAdmin | pscProtectingFailure | pscWaitToRevert | pscDoNotRevert | apsSignalFailOnProtection | apsForceSwitch): This signifies the APS local state information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsLocalState"])

    @property
    def ApsRemoteDataPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str(protect | na | working): This signifies the path of the APS remote data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsRemoteDataPath"])

    @property
    def ApsRemoteFaultPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str(na | working | protect | both | none): This signifies the path of the APS remote fault.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsRemoteFaultPath"])

    @property
    def ApsRemoteRequestState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(na | apsNoRequest | apsLockoutOfProtection | apsSignalFailOnWorking | apsManualSwitch | apsWaitToRestore | apsDoNotRevert | apsExercise | apsReverseRequest | pscNormal | pscUnavailable | pscProtectingAdmin | pscProtectingFailure | pscWaitToRevert | pscDoNotRevert | apsSignalFailOnProtection | apsForceSwitch): This signifies the APS remote request state information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApsRemoteRequestState"])

    @property
    def ContinuityCheckLocalState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(na | bfdDown | bfdInit | bfdUp | y1731Down | y1731Init | y1731Up): This signifies the status of the Continuity Check Local State.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContinuityCheckLocalState"])

    @property
    def ContinuityCheckRemoteState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(na | bfdDown | bfdInit | bfdUp | y1731Down | y1731Init | y1731Up): This signifies the status of the Continuity Check Remote State.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContinuityCheckRemoteState"])

    @property
    def ContinuityCheckRxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This Signifies the CC Rx Interval configured on the source side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContinuityCheckRxInterval"])

    @property
    def ContinuityCheckTxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This Signifies the Negotiated CC Tx Interval on the source side.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContinuityCheckTxInterval"])

    @property
    def IncomingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the incoming label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncomingLabelOuterInner"])

    @property
    def LastAlarmDuration(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the duration for how long the LSP/PW was in fault state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastAlarmDuration"])

    @property
    def LckRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of LCK frames received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckRx"])

    @property
    def LckState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the state of LCK, either Clear or Fault.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckState"])

    @property
    def LckTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of LCK frames transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckTx"])

    @property
    def Ldi(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the state of the LDI bit, either NA or Set.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ldi"])

    @property
    def LocalPwStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the local PW status.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPwStatus"])

    @property
    def OutgoingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Outgoing Label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutgoingLabelOuterInner"])

    @property
    def RemoteDefectIndication(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This Signifies the Defect Indication received in the cc message from remote port if any.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteDefectIndication"])

    @property
    def RemotePwStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the remote PW status.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemotePwStatus"])

    @property
    def Role(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the selection of this option to filter according to the following roles None,Protect and Working.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Role"])

    @property
    def TimeSinceLastAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the time elapsed since the LSP/PW has recovered from the last fault state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimeSinceLastAlarm"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the selection of this option to filter according to the following types LSP and PW.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    def add(self):
        """Adds a new generalLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved generalLearnedInfo resources using find and the newly added generalLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AisRx=None,
        AisState=None,
        AisTx=None,
        AlarmTypeAis=None,
        AlarmTypeLck=None,
        ApsLocalDataPath=None,
        ApsLocalFaultPath=None,
        ApsLocalState=None,
        ApsRemoteDataPath=None,
        ApsRemoteFaultPath=None,
        ApsRemoteRequestState=None,
        ContinuityCheckLocalState=None,
        ContinuityCheckRemoteState=None,
        ContinuityCheckRxInterval=None,
        ContinuityCheckTxInterval=None,
        IncomingLabelOuterInner=None,
        LastAlarmDuration=None,
        LckRx=None,
        LckState=None,
        LckTx=None,
        Ldi=None,
        LocalPwStatus=None,
        OutgoingLabelOuterInner=None,
        RemoteDefectIndication=None,
        RemotePwStatus=None,
        Role=None,
        TimeSinceLastAlarm=None,
        Type=None,
    ):
        # type: (int, str, int, str, str, str, str, str, str, str, str, str, str, int, int, str, str, int, str, int, str, str, str, str, str, str, str, str) -> GeneralLearnedInfo
        """Finds and retrieves generalLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve generalLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all generalLearnedInfo resources from the server.

        Args
        ----
        - AisRx (number): This signifies the number of AIS frames received.
        - AisState (str): This signifies the state of AIS, either Clear or Fault.
        - AisTx (number): This signifies the number of AIS frames transmitted.
        - AlarmTypeAis (str): This signifies the type of the AIS alarm, either ietf or y1731.
        - AlarmTypeLck (str): This signifies the type of the LCK alarm, either ietf or y1731.
        - ApsLocalDataPath (str(working | protect | na)): This signifies the path of the APS local data.
        - ApsLocalFaultPath (str(working | protect | both | none | na)): This signifies the path of the APS local fault.
        - ApsLocalState (str(na | apsNoRequest | apsLockoutOfProtection | apsSignalFailOnWorking | apsManualSwitch | apsWaitToRestore | apsDoNotRevert | apsExercise | apsReverseRequest | pscNormal | pscUnavailable | pscProtectingAdmin | pscProtectingFailure | pscWaitToRevert | pscDoNotRevert | apsSignalFailOnProtection | apsForceSwitch)): This signifies the APS local state information.
        - ApsRemoteDataPath (str(protect | na | working)): This signifies the path of the APS remote data.
        - ApsRemoteFaultPath (str(na | working | protect | both | none)): This signifies the path of the APS remote fault.
        - ApsRemoteRequestState (str(na | apsNoRequest | apsLockoutOfProtection | apsSignalFailOnWorking | apsManualSwitch | apsWaitToRestore | apsDoNotRevert | apsExercise | apsReverseRequest | pscNormal | pscUnavailable | pscProtectingAdmin | pscProtectingFailure | pscWaitToRevert | pscDoNotRevert | apsSignalFailOnProtection | apsForceSwitch)): This signifies the APS remote request state information.
        - ContinuityCheckLocalState (str(na | bfdDown | bfdInit | bfdUp | y1731Down | y1731Init | y1731Up)): This signifies the status of the Continuity Check Local State.
        - ContinuityCheckRemoteState (str(na | bfdDown | bfdInit | bfdUp | y1731Down | y1731Init | y1731Up)): This signifies the status of the Continuity Check Remote State.
        - ContinuityCheckRxInterval (number): This Signifies the CC Rx Interval configured on the source side.
        - ContinuityCheckTxInterval (number): This Signifies the Negotiated CC Tx Interval on the source side.
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - LastAlarmDuration (str): This signifies the duration for how long the LSP/PW was in fault state.
        - LckRx (number): This signifies the number of LCK frames received.
        - LckState (str): This signifies the state of LCK, either Clear or Fault.
        - LckTx (number): This signifies the number of LCK frames transmitted.
        - Ldi (str): This signifies the state of the LDI bit, either NA or Set.
        - LocalPwStatus (str): This signifies the local PW status.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - RemoteDefectIndication (str): This Signifies the Defect Indication received in the cc message from remote port if any.
        - RemotePwStatus (str): This signifies the remote PW status.
        - Role (str): This signifies the selection of this option to filter according to the following roles None,Protect and Working.
        - TimeSinceLastAlarm (str): This signifies the time elapsed since the LSP/PW has recovered from the last fault state.
        - Type (str): This signifies the selection of this option to filter according to the following types LSP and PW.

        Returns
        -------
        - self: This instance with matching generalLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of generalLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the generalLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the addRecordForTrigger operation on the server.

        This signifies the record added for trigger settings.

        addRecordForTrigger(async_operation=bool)bool
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "addRecordForTrigger", payload=payload, response_object=None
        )
