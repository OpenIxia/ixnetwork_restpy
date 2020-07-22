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


class Link(Base):
    """
    The Link class encapsulates a list of link resources that are managed by the user.
    A list of resources can be retrieved from the server using the Link.find() method.
    The list can be managed by using the Link.add() and Link.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'link'
    _SDM_ATT_MAP = {
        'DisableInformationPduTx': 'disableInformationPduTx',
        'DisableNonInformationPduTx': 'disableNonInformationPduTx',
        'EnableCriticalEvent': 'enableCriticalEvent',
        'EnableDyingGasp': 'enableDyingGasp',
        'EnableLinkFault': 'enableLinkFault',
        'EnableLoopbackResponse': 'enableLoopbackResponse',
        'EnableVariableResponse': 'enableVariableResponse',
        'Enabled': 'enabled',
        'EthernetTypeUsedForDataTraffic': 'ethernetTypeUsedForDataTraffic',
        'EventInterval': 'eventInterval',
        'InformationPduCountPerSecond': 'informationPduCountPerSecond',
        'IsDiscLearnedInfoRefreshed': 'isDiscLearnedInfoRefreshed',
        'IsEventNotificationLearnedInfoRefreshed': 'isEventNotificationLearnedInfoRefreshed',
        'IsLoopbackLearnedInfoRefreshed': 'isLoopbackLearnedInfoRefreshed',
        'IsVariableRequestLearnedInfoRefreshed': 'isVariableRequestLearnedInfoRefreshed',
        'LinkEventTxMode': 'linkEventTxMode',
        'LocalLostLinkTimer': 'localLostLinkTimer',
        'LoopbackCmd': 'loopbackCmd',
        'LoopbackTimeout': 'loopbackTimeout',
        'MacAddress': 'macAddress',
        'MaxOamPduSize': 'maxOamPduSize',
        'OperationMode': 'operationMode',
        'Oui': 'oui',
        'OverrideLocalEvaluating': 'overrideLocalEvaluating',
        'OverrideLocalSatisfied': 'overrideLocalSatisfied',
        'OverrideLocalStable': 'overrideLocalStable',
        'OverrideRemoteEvaluating': 'overrideRemoteEvaluating',
        'OverrideRemoteStable': 'overrideRemoteStable',
        'OverrideRevision': 'overrideRevision',
        'OverrideSequenceNumber': 'overrideSequenceNumber',
        'Revision': 'revision',
        'SequenceNumber': 'sequenceNumber',
        'SupportsInterpretingLinkEvents': 'supportsInterpretingLinkEvents',
        'SupportsRemoteLoopback': 'supportsRemoteLoopback',
        'SupportsUnidirectionalMode': 'supportsUnidirectionalMode',
        'SupportsVariableRetrieval': 'supportsVariableRetrieval',
        'UpdateRequired': 'updateRequired',
        'VariableResponseTimeout': 'variableResponseTimeout',
        'VendorSpecificInformation': 'vendorSpecificInformation',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Link, self).__init__(parent)

    @property
    def DiscoveredLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.discoveredlearnedinfo_188b8a898cd970d269c9b640e26bb1ee.DiscoveredLearnedInfo): An instance of the DiscoveredLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.discoveredlearnedinfo_188b8a898cd970d269c9b640e26bb1ee import DiscoveredLearnedInfo
        return DiscoveredLearnedInfo(self)

    @property
    def ErroredFramePeriodTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframeperiodtlv_7cc91abe9c8b1fd8a9f51f296f6067cf.ErroredFramePeriodTlv): An instance of the ErroredFramePeriodTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframeperiodtlv_7cc91abe9c8b1fd8a9f51f296f6067cf import ErroredFramePeriodTlv
        return ErroredFramePeriodTlv(self)._select()

    @property
    def ErroredFrameSecondsSummaryTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframesecondssummarytlv_2fc89811037ac2e7d1d2e1288ecab4b0.ErroredFrameSecondsSummaryTlv): An instance of the ErroredFrameSecondsSummaryTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframesecondssummarytlv_2fc89811037ac2e7d1d2e1288ecab4b0 import ErroredFrameSecondsSummaryTlv
        return ErroredFrameSecondsSummaryTlv(self)._select()

    @property
    def ErroredFrameTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframetlv_4d3383ca7f2cec201c28a9edbdc121a3.ErroredFrameTlv): An instance of the ErroredFrameTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredframetlv_4d3383ca7f2cec201c28a9edbdc121a3 import ErroredFrameTlv
        return ErroredFrameTlv(self)._select()

    @property
    def ErroredSymbolPeriodTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredsymbolperiodtlv_feb3ee080ce21514d62d548c686666e3.ErroredSymbolPeriodTlv): An instance of the ErroredSymbolPeriodTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.erroredsymbolperiodtlv_feb3ee080ce21514d62d548c686666e3 import ErroredSymbolPeriodTlv
        return ErroredSymbolPeriodTlv(self)._select()

    @property
    def EventNotificationLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eventnotificationlearnedinfo_8e9f812623dab234dee810e2be72f464.EventNotificationLearnedInfo): An instance of the EventNotificationLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eventnotificationlearnedinfo_8e9f812623dab234dee810e2be72f464 import EventNotificationLearnedInfo
        return EventNotificationLearnedInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_628fdf0890417e234e9b9a33933fd6bf.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_628fdf0890417e234e9b9a33933fd6bf import Interface
        return Interface(self)

    @property
    def OrganizationSpecificEventTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificeventtlv_6bcef15ff151fc7a01812fd203f92bec.OrganizationSpecificEventTlv): An instance of the OrganizationSpecificEventTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificeventtlv_6bcef15ff151fc7a01812fd203f92bec import OrganizationSpecificEventTlv
        return OrganizationSpecificEventTlv(self)._select()

    @property
    def OrganizationSpecificInfoTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificinfotlv_bceedaa80532e61885f020d2120259b3.OrganizationSpecificInfoTlv): An instance of the OrganizationSpecificInfoTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificinfotlv_bceedaa80532e61885f020d2120259b3 import OrganizationSpecificInfoTlv
        return OrganizationSpecificInfoTlv(self)

    @property
    def OrganizationSpecificOamPduData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificoampdudata_4962ac6d533f0d0f2ad3d9f0a6d09d2e.OrganizationSpecificOamPduData): An instance of the OrganizationSpecificOamPduData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.organizationspecificoampdudata_4962ac6d533f0d0f2ad3d9f0a6d09d2e import OrganizationSpecificOamPduData
        return OrganizationSpecificOamPduData(self)

    @property
    def VarDescriptor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vardescriptor_1bd65d7811e52b7fb52ca36b198f3522.VarDescriptor): An instance of the VarDescriptor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vardescriptor_1bd65d7811e52b7fb52ca36b198f3522 import VarDescriptor
        return VarDescriptor(self)

    @property
    def VariableRequestLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variablerequestlearnedinfo_12a8a1ec9b0f5c97bcaf9f19d8f2ea9b.VariableRequestLearnedInfo): An instance of the VariableRequestLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variablerequestlearnedinfo_12a8a1ec9b0f5c97bcaf9f19d8f2ea9b import VariableRequestLearnedInfo
        return VariableRequestLearnedInfo(self)

    @property
    def VariableResponseDatabase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variableresponsedatabase_e5817ec548a5137b5dd919236225f7d2.VariableResponseDatabase): An instance of the VariableResponseDatabase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.variableresponsedatabase_e5817ec548a5137b5dd919236225f7d2 import VariableResponseDatabase
        return VariableResponseDatabase(self)

    @property
    def DisableInformationPduTx(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableInformationPduTx'])
    @DisableInformationPduTx.setter
    def DisableInformationPduTx(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableInformationPduTx'], value)

    @property
    def DisableNonInformationPduTx(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableNonInformationPduTx'])
    @DisableNonInformationPduTx.setter
    def DisableNonInformationPduTx(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableNonInformationPduTx'], value)

    @property
    def EnableCriticalEvent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCriticalEvent'])
    @EnableCriticalEvent.setter
    def EnableCriticalEvent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCriticalEvent'], value)

    @property
    def EnableDyingGasp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDyingGasp'])
    @EnableDyingGasp.setter
    def EnableDyingGasp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDyingGasp'], value)

    @property
    def EnableLinkFault(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkFault'])
    @EnableLinkFault.setter
    def EnableLinkFault(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkFault'], value)

    @property
    def EnableLoopbackResponse(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLoopbackResponse'])
    @EnableLoopbackResponse.setter
    def EnableLoopbackResponse(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLoopbackResponse'], value)

    @property
    def EnableVariableResponse(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVariableResponse'])
    @EnableVariableResponse.setter
    def EnableVariableResponse(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVariableResponse'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EthernetTypeUsedForDataTraffic(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetTypeUsedForDataTraffic'])
    @EthernetTypeUsedForDataTraffic.setter
    def EthernetTypeUsedForDataTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetTypeUsedForDataTraffic'], value)

    @property
    def EventInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EventInterval'])
    @EventInterval.setter
    def EventInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EventInterval'], value)

    @property
    def InformationPduCountPerSecond(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InformationPduCountPerSecond'])
    @InformationPduCountPerSecond.setter
    def InformationPduCountPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InformationPduCountPerSecond'], value)

    @property
    def IsDiscLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDiscLearnedInfoRefreshed'])

    @property
    def IsEventNotificationLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEventNotificationLearnedInfoRefreshed'])

    @property
    def IsLoopbackLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLoopbackLearnedInfoRefreshed'])

    @property
    def IsVariableRequestLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsVariableRequestLearnedInfoRefreshed'])

    @property
    def LinkEventTxMode(self):
        """
        Returns
        -------
        - str(single | periodic): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkEventTxMode'])
    @LinkEventTxMode.setter
    def LinkEventTxMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkEventTxMode'], value)

    @property
    def LocalLostLinkTimer(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalLostLinkTimer'])
    @LocalLostLinkTimer.setter
    def LocalLostLinkTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalLostLinkTimer'], value)

    @property
    def LoopbackCmd(self):
        """
        Returns
        -------
        - str(disableLoopback | enableLoopback): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopbackCmd'])
    @LoopbackCmd.setter
    def LoopbackCmd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoopbackCmd'], value)

    @property
    def LoopbackTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopbackTimeout'])
    @LoopbackTimeout.setter
    def LoopbackTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoopbackTimeout'], value)

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def MaxOamPduSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOamPduSize'])
    @MaxOamPduSize.setter
    def MaxOamPduSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOamPduSize'], value)

    @property
    def OperationMode(self):
        """
        Returns
        -------
        - str(active | passive): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OperationMode'])
    @OperationMode.setter
    def OperationMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OperationMode'], value)

    @property
    def Oui(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Oui'])
    @Oui.setter
    def Oui(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Oui'], value)

    @property
    def OverrideLocalEvaluating(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideLocalEvaluating'])
    @OverrideLocalEvaluating.setter
    def OverrideLocalEvaluating(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideLocalEvaluating'], value)

    @property
    def OverrideLocalSatisfied(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideLocalSatisfied'])
    @OverrideLocalSatisfied.setter
    def OverrideLocalSatisfied(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideLocalSatisfied'], value)

    @property
    def OverrideLocalStable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideLocalStable'])
    @OverrideLocalStable.setter
    def OverrideLocalStable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideLocalStable'], value)

    @property
    def OverrideRemoteEvaluating(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideRemoteEvaluating'])
    @OverrideRemoteEvaluating.setter
    def OverrideRemoteEvaluating(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideRemoteEvaluating'], value)

    @property
    def OverrideRemoteStable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideRemoteStable'])
    @OverrideRemoteStable.setter
    def OverrideRemoteStable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideRemoteStable'], value)

    @property
    def OverrideRevision(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideRevision'])
    @OverrideRevision.setter
    def OverrideRevision(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideRevision'], value)

    @property
    def OverrideSequenceNumber(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideSequenceNumber'])
    @OverrideSequenceNumber.setter
    def OverrideSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideSequenceNumber'], value)

    @property
    def Revision(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Revision'])
    @Revision.setter
    def Revision(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Revision'], value)

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])
    @SequenceNumber.setter
    def SequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SequenceNumber'], value)

    @property
    def SupportsInterpretingLinkEvents(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsInterpretingLinkEvents'])
    @SupportsInterpretingLinkEvents.setter
    def SupportsInterpretingLinkEvents(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportsInterpretingLinkEvents'], value)

    @property
    def SupportsRemoteLoopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsRemoteLoopback'])
    @SupportsRemoteLoopback.setter
    def SupportsRemoteLoopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportsRemoteLoopback'], value)

    @property
    def SupportsUnidirectionalMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsUnidirectionalMode'])
    @SupportsUnidirectionalMode.setter
    def SupportsUnidirectionalMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportsUnidirectionalMode'], value)

    @property
    def SupportsVariableRetrieval(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsVariableRetrieval'])
    @SupportsVariableRetrieval.setter
    def SupportsVariableRetrieval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportsVariableRetrieval'], value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])

    @property
    def VariableResponseTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VariableResponseTimeout'])
    @VariableResponseTimeout.setter
    def VariableResponseTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VariableResponseTimeout'], value)

    @property
    def VendorSpecificInformation(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorSpecificInformation'])
    @VendorSpecificInformation.setter
    def VendorSpecificInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorSpecificInformation'], value)

    @property
    def Version(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])
    @Version.setter
    def Version(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Version'], value)

    def update(self, DisableInformationPduTx=None, DisableNonInformationPduTx=None, EnableCriticalEvent=None, EnableDyingGasp=None, EnableLinkFault=None, EnableLoopbackResponse=None, EnableVariableResponse=None, Enabled=None, EthernetTypeUsedForDataTraffic=None, EventInterval=None, InformationPduCountPerSecond=None, LinkEventTxMode=None, LocalLostLinkTimer=None, LoopbackCmd=None, LoopbackTimeout=None, MacAddress=None, MaxOamPduSize=None, OperationMode=None, Oui=None, OverrideLocalEvaluating=None, OverrideLocalSatisfied=None, OverrideLocalStable=None, OverrideRemoteEvaluating=None, OverrideRemoteStable=None, OverrideRevision=None, OverrideSequenceNumber=None, Revision=None, SequenceNumber=None, SupportsInterpretingLinkEvents=None, SupportsRemoteLoopback=None, SupportsUnidirectionalMode=None, SupportsVariableRetrieval=None, VariableResponseTimeout=None, VendorSpecificInformation=None, Version=None):
        """Updates link resource on the server.

        Args
        ----
        - DisableInformationPduTx (bool): 
        - DisableNonInformationPduTx (bool): 
        - EnableCriticalEvent (bool): 
        - EnableDyingGasp (bool): 
        - EnableLinkFault (bool): 
        - EnableLoopbackResponse (bool): 
        - EnableVariableResponse (bool): 
        - Enabled (bool): 
        - EthernetTypeUsedForDataTraffic (number): 
        - EventInterval (number): 
        - InformationPduCountPerSecond (number): 
        - LinkEventTxMode (str(single | periodic)): 
        - LocalLostLinkTimer (number): 
        - LoopbackCmd (str(disableLoopback | enableLoopback)): 
        - LoopbackTimeout (number): 
        - MacAddress (str): 
        - MaxOamPduSize (number): 
        - OperationMode (str(active | passive)): 
        - Oui (str): 
        - OverrideLocalEvaluating (bool): 
        - OverrideLocalSatisfied (bool): 
        - OverrideLocalStable (bool): 
        - OverrideRemoteEvaluating (bool): 
        - OverrideRemoteStable (bool): 
        - OverrideRevision (bool): 
        - OverrideSequenceNumber (bool): 
        - Revision (number): 
        - SequenceNumber (number): 
        - SupportsInterpretingLinkEvents (bool): 
        - SupportsRemoteLoopback (bool): 
        - SupportsUnidirectionalMode (bool): 
        - SupportsVariableRetrieval (bool): 
        - VariableResponseTimeout (number): 
        - VendorSpecificInformation (str): 
        - Version (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DisableInformationPduTx=None, DisableNonInformationPduTx=None, EnableCriticalEvent=None, EnableDyingGasp=None, EnableLinkFault=None, EnableLoopbackResponse=None, EnableVariableResponse=None, Enabled=None, EthernetTypeUsedForDataTraffic=None, EventInterval=None, InformationPduCountPerSecond=None, LinkEventTxMode=None, LocalLostLinkTimer=None, LoopbackCmd=None, LoopbackTimeout=None, MacAddress=None, MaxOamPduSize=None, OperationMode=None, Oui=None, OverrideLocalEvaluating=None, OverrideLocalSatisfied=None, OverrideLocalStable=None, OverrideRemoteEvaluating=None, OverrideRemoteStable=None, OverrideRevision=None, OverrideSequenceNumber=None, Revision=None, SequenceNumber=None, SupportsInterpretingLinkEvents=None, SupportsRemoteLoopback=None, SupportsUnidirectionalMode=None, SupportsVariableRetrieval=None, VariableResponseTimeout=None, VendorSpecificInformation=None, Version=None):
        """Adds a new link resource on the server and adds it to the container.

        Args
        ----
        - DisableInformationPduTx (bool): 
        - DisableNonInformationPduTx (bool): 
        - EnableCriticalEvent (bool): 
        - EnableDyingGasp (bool): 
        - EnableLinkFault (bool): 
        - EnableLoopbackResponse (bool): 
        - EnableVariableResponse (bool): 
        - Enabled (bool): 
        - EthernetTypeUsedForDataTraffic (number): 
        - EventInterval (number): 
        - InformationPduCountPerSecond (number): 
        - LinkEventTxMode (str(single | periodic)): 
        - LocalLostLinkTimer (number): 
        - LoopbackCmd (str(disableLoopback | enableLoopback)): 
        - LoopbackTimeout (number): 
        - MacAddress (str): 
        - MaxOamPduSize (number): 
        - OperationMode (str(active | passive)): 
        - Oui (str): 
        - OverrideLocalEvaluating (bool): 
        - OverrideLocalSatisfied (bool): 
        - OverrideLocalStable (bool): 
        - OverrideRemoteEvaluating (bool): 
        - OverrideRemoteStable (bool): 
        - OverrideRevision (bool): 
        - OverrideSequenceNumber (bool): 
        - Revision (number): 
        - SequenceNumber (number): 
        - SupportsInterpretingLinkEvents (bool): 
        - SupportsRemoteLoopback (bool): 
        - SupportsUnidirectionalMode (bool): 
        - SupportsVariableRetrieval (bool): 
        - VariableResponseTimeout (number): 
        - VendorSpecificInformation (str): 
        - Version (number): 

        Returns
        -------
        - self: This instance with all currently retrieved link resources using find and the newly added link resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained link resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DisableInformationPduTx=None, DisableNonInformationPduTx=None, EnableCriticalEvent=None, EnableDyingGasp=None, EnableLinkFault=None, EnableLoopbackResponse=None, EnableVariableResponse=None, Enabled=None, EthernetTypeUsedForDataTraffic=None, EventInterval=None, InformationPduCountPerSecond=None, IsDiscLearnedInfoRefreshed=None, IsEventNotificationLearnedInfoRefreshed=None, IsLoopbackLearnedInfoRefreshed=None, IsVariableRequestLearnedInfoRefreshed=None, LinkEventTxMode=None, LocalLostLinkTimer=None, LoopbackCmd=None, LoopbackTimeout=None, MacAddress=None, MaxOamPduSize=None, OperationMode=None, Oui=None, OverrideLocalEvaluating=None, OverrideLocalSatisfied=None, OverrideLocalStable=None, OverrideRemoteEvaluating=None, OverrideRemoteStable=None, OverrideRevision=None, OverrideSequenceNumber=None, Revision=None, SequenceNumber=None, SupportsInterpretingLinkEvents=None, SupportsRemoteLoopback=None, SupportsUnidirectionalMode=None, SupportsVariableRetrieval=None, UpdateRequired=None, VariableResponseTimeout=None, VendorSpecificInformation=None, Version=None):
        """Finds and retrieves link resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve link resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all link resources from the server.

        Args
        ----
        - DisableInformationPduTx (bool): 
        - DisableNonInformationPduTx (bool): 
        - EnableCriticalEvent (bool): 
        - EnableDyingGasp (bool): 
        - EnableLinkFault (bool): 
        - EnableLoopbackResponse (bool): 
        - EnableVariableResponse (bool): 
        - Enabled (bool): 
        - EthernetTypeUsedForDataTraffic (number): 
        - EventInterval (number): 
        - InformationPduCountPerSecond (number): 
        - IsDiscLearnedInfoRefreshed (bool): 
        - IsEventNotificationLearnedInfoRefreshed (bool): 
        - IsLoopbackLearnedInfoRefreshed (bool): 
        - IsVariableRequestLearnedInfoRefreshed (bool): 
        - LinkEventTxMode (str(single | periodic)): 
        - LocalLostLinkTimer (number): 
        - LoopbackCmd (str(disableLoopback | enableLoopback)): 
        - LoopbackTimeout (number): 
        - MacAddress (str): 
        - MaxOamPduSize (number): 
        - OperationMode (str(active | passive)): 
        - Oui (str): 
        - OverrideLocalEvaluating (bool): 
        - OverrideLocalSatisfied (bool): 
        - OverrideLocalStable (bool): 
        - OverrideRemoteEvaluating (bool): 
        - OverrideRemoteStable (bool): 
        - OverrideRevision (bool): 
        - OverrideSequenceNumber (bool): 
        - Revision (number): 
        - SequenceNumber (number): 
        - SupportsInterpretingLinkEvents (bool): 
        - SupportsRemoteLoopback (bool): 
        - SupportsUnidirectionalMode (bool): 
        - SupportsVariableRetrieval (bool): 
        - UpdateRequired (bool): 
        - VariableResponseTimeout (number): 
        - VendorSpecificInformation (str): 
        - Version (number): 

        Returns
        -------
        - self: This instance with matching link resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of link data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the link resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshDiscLearnedInfo(self):
        """Executes the refreshDiscLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshDiscLearnedInfo', payload=payload, response_object=None)

    def RefreshEventNotificationLearnedInfo(self):
        """Executes the refreshEventNotificationLearnedInfo operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshEventNotificationLearnedInfo', payload=payload, response_object=None)

    def RestartDiscovery(self):
        """Executes the restartDiscovery operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('restartDiscovery', payload=payload, response_object=None)

    def SendLoopback(self):
        """Executes the sendLoopback operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendLoopback', payload=payload, response_object=None)

    def SendOrgSpecificPdu(self):
        """Executes the sendOrgSpecificPdu operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendOrgSpecificPdu', payload=payload, response_object=None)

    def SendUpdatedParameters(self):
        """Executes the sendUpdatedParameters operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendUpdatedParameters', payload=payload, response_object=None)

    def SendVariableRequest(self):
        """Executes the sendVariableRequest operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendVariableRequest', payload=payload, response_object=None)

    def StartEventPduTransmission(self):
        """Executes the startEventPduTransmission operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startEventPduTransmission', payload=payload, response_object=None)

    def StopEventPduTransmission(self):
        """Executes the stopEventPduTransmission operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stopEventPduTransmission', payload=payload, response_object=None)
