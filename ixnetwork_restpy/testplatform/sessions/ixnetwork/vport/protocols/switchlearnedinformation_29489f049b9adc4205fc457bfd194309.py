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


class SwitchLearnedInformation(Base):
    """This object allows to configure the switch learned information parameters.
    The SwitchLearnedInformation class encapsulates a required switchLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'switchLearnedInformation'
    _SDM_ATT_MAP = {
        'EnableVendorExperimenterMessage': 'enableVendorExperimenterMessage',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpProtocol': 'ipProtocol',
        'Ipv4Source': 'ipv4Source',
        'Ipv4destination': 'ipv4destination',
        'IsOfChannelLearnedInformationRefreshed': 'isOfChannelLearnedInformationRefreshed',
        'IsOfFlowsLearnedInformationRefreshed': 'isOfFlowsLearnedInformationRefreshed',
        'OutPort': 'outPort',
        'OutPortInputMode': 'outPortInputMode',
        'TableId': 'tableId',
        'TableIdInputMode': 'tableIdInputMode',
        'TansportSource': 'tansportSource',
        'TransportDestination': 'transportDestination',
        'VendorExperimenterId': 'vendorExperimenterId',
        'VendorExperimenterType': 'vendorExperimenterType',
        'VendorMessage': 'vendorMessage',
        'VendorMessageLength': 'vendorMessageLength',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(SwitchLearnedInformation, self).__init__(parent)

    @property
    def OfChannelSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_8014ef79f44d2c63a73d35dd12599267.OfChannelSwitchLearnedInfo): An instance of the OfChannelSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_8014ef79f44d2c63a73d35dd12599267 import OfChannelSwitchLearnedInfo
        return OfChannelSwitchLearnedInfo(self)

    @property
    def SwitchFlow131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_f684d69a421575142ffb1973005001bd.SwitchFlow131TriggerAttributes): An instance of the SwitchFlow131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_f684d69a421575142ffb1973005001bd import SwitchFlow131TriggerAttributes
        return SwitchFlow131TriggerAttributes(self)._select()

    @property
    def SwitchFlowLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_ca1989680f648fe88b21f62ddc39567b.SwitchFlowLearnedInfo): An instance of the SwitchFlowLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_ca1989680f648fe88b21f62ddc39567b import SwitchFlowLearnedInfo
        return SwitchFlowLearnedInfo(self)

    @property
    def SwitchFlowMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_3aa835176420a29823aa2b0d3e4805b2.SwitchFlowMatchCriteria131TriggerAttributes): An instance of the SwitchFlowMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_3aa835176420a29823aa2b0d3e4805b2 import SwitchFlowMatchCriteria131TriggerAttributes
        return SwitchFlowMatchCriteria131TriggerAttributes(self)._select()

    @property
    def SwitchGroupLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_aafd044030635b13c0db790095a88328.SwitchGroupLearnedInfo): An instance of the SwitchGroupLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_aafd044030635b13c0db790095a88328 import SwitchGroupLearnedInfo
        return SwitchGroupLearnedInfo(self)

    @property
    def SwitchMeterLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_99f3b816edb76e0b23f8211b94b0b8c7.SwitchMeterLearnedInfo): An instance of the SwitchMeterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_99f3b816edb76e0b23f8211b94b0b8c7 import SwitchMeterLearnedInfo
        return SwitchMeterLearnedInfo(self)

    @property
    def SwitchTableFeaturesStatLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_bb49dadbbed3b7e099461fbcb8d8e518.SwitchTableFeaturesStatLearnedInfo): An instance of the SwitchTableFeaturesStatLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_bb49dadbbed3b7e099461fbcb8d8e518 import SwitchTableFeaturesStatLearnedInfo
        return SwitchTableFeaturesStatLearnedInfo(self)

    @property
    def EnableVendorExperimenterMessage(self):
        """
        Returns
        -------
        - bool: If true, the vendor message trigger configuration parameters are available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVendorExperimenterMessage'])
    @EnableVendorExperimenterMessage.setter
    def EnableVendorExperimenterMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVendorExperimenterMessage'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for ethernet destination address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: This describes the flow match value for ethernet source address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: This describes the Ethernet type of the flow match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetType'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: This describes the flow match value for input port field
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IP ToS field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IP Protocol field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 source address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Ipv4destination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 destination address field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4destination'])
    @Ipv4destination.setter
    def Ipv4destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4destination'], value)

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the OF Channels is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfChannelLearnedInformationRefreshed'])

    @property
    def IsOfFlowsLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Flow Learned Info for the OF Channels is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfFlowsLearnedInformationRefreshed'])

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: This describes the flow match value for output port field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPort'])
    @OutPort.setter
    def OutPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPort'], value)

    @property
    def OutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom): This describes the output port type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortInputMode'])
    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPortInputMode'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])
    @TableId.setter
    def TableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableId'], value)

    @property
    def TableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | tableIdCustom): This describes the type of table from which flow statistics will be sought.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableIdInputMode'])
    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableIdInputMode'], value)

    @property
    def TansportSource(self):
        """
        Returns
        -------
        - str: This describes the flow match value for transport source field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TansportSource'])
    @TansportSource.setter
    def TansportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TansportSource'], value)

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for transport destination field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestination'])
    @TransportDestination.setter
    def TransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportDestination'], value)

    @property
    def VendorExperimenterId(self):
        """
        Returns
        -------
        - number: This describes the ID of the vendor for which vendor message is triggered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorExperimenterId'])
    @VendorExperimenterId.setter
    def VendorExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorExperimenterId'], value)

    @property
    def VendorExperimenterType(self):
        """
        Returns
        -------
        - number: This describes the Type of experimenter only for v 1.3.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorExperimenterType'])
    @VendorExperimenterType.setter
    def VendorExperimenterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorExperimenterType'], value)

    @property
    def VendorMessage(self):
        """
        Returns
        -------
        - str: This describes the vendor data of the vendor message trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessage'])
    @VendorMessage.setter
    def VendorMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorMessage'], value)

    @property
    def VendorMessageLength(self):
        """
        Returns
        -------
        - number: This describes the length of vendor data of the vendor message trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessageLength'])
    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorMessageLength'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: This describes the flow match value for VLAN ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: This describes the flow match value for VLAN Priority field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, EnableVendorExperimenterMessage=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Source=None, Ipv4destination=None, OutPort=None, OutPortInputMode=None, TableId=None, TableIdInputMode=None, TansportSource=None, TransportDestination=None, VendorExperimenterId=None, VendorExperimenterType=None, VendorMessage=None, VendorMessageLength=None, VlanId=None, VlanPriority=None):
        """Updates switchLearnedInformation resource on the server.

        Args
        ----
        - EnableVendorExperimenterMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - EthernetDestination (str): This describes the flow match value for ethernet destination address field.
        - EthernetSource (str): This describes the flow match value for ethernet source address field.
        - EthernetType (str): This describes the Ethernet type of the flow match.
        - InPort (str): This describes the flow match value for input port field
        - IpDscp (str): This describes the flow match value for IP ToS field.
        - IpProtocol (str): This describes the flow match value for IP Protocol field.
        - Ipv4Source (str): This describes the flow match value for IPv4 source address field.
        - Ipv4destination (str): This describes the flow match value for IPv4 destination address field.
        - OutPort (number): This describes the flow match value for output port field.
        - OutPortInputMode (str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom)): This describes the output port type.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | tableIdCustom)): This describes the type of table from which flow statistics will be sought.
        - TansportSource (str): This describes the flow match value for transport source field.
        - TransportDestination (str): This describes the flow match value for transport destination field.
        - VendorExperimenterId (number): This describes the ID of the vendor for which vendor message is triggered.
        - VendorExperimenterType (number): This describes the Type of experimenter only for v 1.3.
        - VendorMessage (str): This describes the vendor data of the vendor message trigger.
        - VendorMessageLength (number): This describes the length of vendor data of the vendor message trigger.
        - VlanId (str): This describes the flow match value for VLAN ID field.
        - VlanPriority (str): This describes the flow match value for VLAN Priority field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def ClearRecordsForTrigger(self):
        """Executes the clearRecordsForTrigger operation on the server.

        API to clear records for any trigger.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('clearRecordsForTrigger', payload=payload, response_object=None)

    def RefreshFlows(self):
        """Executes the refreshFlows operation on the server.

        This describes that the flows learned information is refreshed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshFlows', payload=payload, response_object=None)

    def RefreshGroupLearnedInformation(self):
        """Executes the refreshGroupLearnedInformation operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshGroupLearnedInformation', payload=payload, response_object=None)

    def RefreshMeterLearnedInformation(self):
        """Executes the refreshMeterLearnedInformation operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshMeterLearnedInformation', payload=payload, response_object=None)

    def RefreshOfChannelLearnedInformation(self):
        """Executes the refreshOfChannelLearnedInformation operation on the server.

        This describes that the ofChannellearned information is refreshed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshOfChannelLearnedInformation', payload=payload, response_object=None)

    def RefreshTableFeature(self):
        """Executes the refreshTableFeature operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshTableFeature', payload=payload, response_object=None)

    def Trigger(self):
        """Executes the trigger operation on the server.

        API to send Trigger.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('trigger', payload=payload, response_object=None)
