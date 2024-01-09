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


class CuspCPAccessInterfaceConfigList(Base):
    """Access Interface Config parameters..
    The CuspCPAccessInterfaceConfigList class encapsulates a required cuspCPAccessInterfaceConfigList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cuspCPAccessInterfaceConfigList"
    _SDM_ATT_MAP = {
        "AccessMode": "accessMode",
        "Active": "active",
        "ArpProxy": "arpProxy",
        "ArpTrigger": "arpTrigger",
        "AuthMethod": "authMethod",
        "AuthMethodv6": "authMethodv6",
        "BasAccessType": "basAccessType",
        "ChassisNumber": "chassisNumber",
        "ConfigureAccessType": "configureAccessType",
        "ConfigureBrasSubInterface": "configureBrasSubInterface",
        "ConfigureInterfacesVia": "configureInterfacesVia",
        "ConfigureVlan": "configureVlan",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EgressL1HqosInstanceName": "egressL1HqosInstanceName",
        "EgressL1HqosProfileName": "egressL1HqosProfileName",
        "EndCvlanId": "endCvlanId",
        "EndSvlanId": "endSvlanId",
        "IncludeL1HqosProfile": "includeL1HqosProfile",
        "IngressL1HqosInstanceName": "ingressL1HqosInstanceName",
        "IngressL1HqosProfileName": "ingressL1HqosProfileName",
        "InterfaceType": "interfaceType",
        "IpoeFlowCheck": "ipoeFlowCheck",
        "Ipv4Trigger": "ipv4Trigger",
        "Ipv6Trigger": "ipv6Trigger",
        "L1HqosActionDesc": "l1HqosActionDesc",
        "L1HqosActionName": "l1HqosActionName",
        "L1HqosProfileName": "l1HqosProfileName",
        "L1HqosRuleActionPairName": "l1HqosRuleActionPairName",
        "L1HqosRuleName": "l1HqosRuleName",
        "LogicID": "logicID",
        "Name": "name",
        "NdProxy": "ndProxy",
        "NdTrigger": "ndTrigger",
        "PortNumber": "portNumber",
        "PortType": "portType",
        "PppOnly": "pppOnly",
        "PppoeFlowCheck": "pppoeFlowCheck",
        "SlotNumber": "slotNumber",
        "StartCvlanId": "startCvlanId",
        "StartSvlanId": "startSvlanId",
        "SubPortNumber": "subPortNumber",
        "SubslotNumber": "subslotNumber",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CuspCPAccessInterfaceConfigList, self).__init__(parent, list_op)

    @property
    def AccessMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mode of access.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AccessMode"]))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def ArpProxy(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable/disable ARP proxy, allowing processing of ARP requests across different Port and Vlans .
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ArpProxy"]))

    @property
    def ArpTrigger(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether ARP packets can trigger a subscriber to go online.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ArpTrigger"]))

    @property
    def AuthMethod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auth Method on this interface for IPv4 scenario.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AuthMethod"]))

    @property
    def AuthMethodv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auth Method on this interface for IPv6 scenario.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AuthMethodv6"]))

    @property
    def BasAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BAS Access Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BasAccessType"]))

    @property
    def ChassisNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Frame number (set to 0 if there is no frame number).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChassisNumber"]))

    @property
    def ConfigureAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Sub-Interface BRAS function as per CMCC vBRAS Yang model.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureAccessType"])
        )

    @property
    def ConfigureBrasSubInterface(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure BRAS Sub-Interface as per CMCC vBRAS Yang model.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureBrasSubInterface"])
        )

    @property
    def ConfigureInterfacesVia(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines how should the BRAS Access Interface configuration be done, by CUSP or by NETCONF.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureInterfacesVia"])
        )

    @property
    def ConfigureVlan(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure VLAN under Sub-Interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ConfigureVlan"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EgressL1HqosInstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress L1 HQoS Instance Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressL1HqosInstanceName"])
        )

    @property
    def EgressL1HqosProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress L1 HQoS Profile Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressL1HqosProfileName"])
        )

    @property
    def EndCvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): End C-VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndCvlanId"]))

    @property
    def EndSvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): End S-VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndSvlanId"]))

    @property
    def IncludeL1HqosProfile(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include L1 HQoS Profile
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeL1HqosProfile"])
        )

    @property
    def IngressL1HqosInstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress L1 HQoS Instance Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressL1HqosInstanceName"])
        )

    @property
    def IngressL1HqosProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress L1 HQoS Profile Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressL1HqosProfileName"])
        )

    @property
    def InterfaceType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of the interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InterfaceType"]))

    @property
    def IpoeFlowCheck(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Used for UP detection.Enable/Disbale traffic detection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IpoeFlowCheck"]))

    @property
    def Ipv4Trigger(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether IPv4 packets can trigger a subscriber to go online.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4Trigger"]))

    @property
    def Ipv6Trigger(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether IPv4 packets can trigger a subscriber to go online.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6Trigger"]))

    @property
    def L1HqosActionDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: pir <pir-value> [ pbs <pbs-value> | weight <weight-value> ] * Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L1HqosActionDesc"])
        )

    @property
    def L1HqosActionName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L1 HQoS Action Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L1HqosActionName"])
        )

    @property
    def L1HqosProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L1 HQoS Profile Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L1HqosProfileName"])
        )

    @property
    def L1HqosRuleActionPairName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L1 HQoS Rule Action Pair Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L1HqosRuleActionPairName"])
        )

    @property
    def L1HqosRuleName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L1 HQoS Rule Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L1HqosRuleName"])
        )

    @property
    def LogicID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Virtual port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LogicID"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NdProxy(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable/disable ND proxy, allowing processing of ND NS requests across different Port and Vlans .
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NdProxy"]))

    @property
    def NdTrigger(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether ND packets can trigger a subscriber to go online.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NdTrigger"]))

    @property
    def PortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Physical port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortNumber"]))

    @property
    def PortType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of the Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortType"]))

    @property
    def PppOnly(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access to PPP users is only allowed if this is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PppOnly"]))

    @property
    def PppoeFlowCheck(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Used for UP detection.Enable/Disbale traffic detection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PppoeFlowCheck"])
        )

    @property
    def SlotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlotNumber"]))

    @property
    def StartCvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start C-VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartCvlanId"]))

    @property
    def StartSvlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start S-VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartSvlanId"]))

    @property
    def SubPortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub-Port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubPortNumber"]))

    @property
    def SubslotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubslotNumber"]))

    def update(self, Name=None):
        # type: (str) -> CuspCPAccessInterfaceConfigList
        """Updates cuspCPAccessInterfaceConfigList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> CuspCPAccessInterfaceConfigList
        """Finds and retrieves cuspCPAccessInterfaceConfigList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cuspCPAccessInterfaceConfigList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cuspCPAccessInterfaceConfigList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching cuspCPAccessInterfaceConfigList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cuspCPAccessInterfaceConfigList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cuspCPAccessInterfaceConfigList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        AccessMode=None,
        Active=None,
        ArpProxy=None,
        ArpTrigger=None,
        AuthMethod=None,
        AuthMethodv6=None,
        BasAccessType=None,
        ChassisNumber=None,
        ConfigureAccessType=None,
        ConfigureBrasSubInterface=None,
        ConfigureInterfacesVia=None,
        ConfigureVlan=None,
        EgressL1HqosInstanceName=None,
        EgressL1HqosProfileName=None,
        EndCvlanId=None,
        EndSvlanId=None,
        IncludeL1HqosProfile=None,
        IngressL1HqosInstanceName=None,
        IngressL1HqosProfileName=None,
        InterfaceType=None,
        IpoeFlowCheck=None,
        Ipv4Trigger=None,
        Ipv6Trigger=None,
        L1HqosActionDesc=None,
        L1HqosActionName=None,
        L1HqosProfileName=None,
        L1HqosRuleActionPairName=None,
        L1HqosRuleName=None,
        LogicID=None,
        NdProxy=None,
        NdTrigger=None,
        PortNumber=None,
        PortType=None,
        PppOnly=None,
        PppoeFlowCheck=None,
        SlotNumber=None,
        StartCvlanId=None,
        StartSvlanId=None,
        SubPortNumber=None,
        SubslotNumber=None,
    ):
        """Base class infrastructure that gets a list of cuspCPAccessInterfaceConfigList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AccessMode (str): optional regex of accessMode
        - Active (str): optional regex of active
        - ArpProxy (str): optional regex of arpProxy
        - ArpTrigger (str): optional regex of arpTrigger
        - AuthMethod (str): optional regex of authMethod
        - AuthMethodv6 (str): optional regex of authMethodv6
        - BasAccessType (str): optional regex of basAccessType
        - ChassisNumber (str): optional regex of chassisNumber
        - ConfigureAccessType (str): optional regex of configureAccessType
        - ConfigureBrasSubInterface (str): optional regex of configureBrasSubInterface
        - ConfigureInterfacesVia (str): optional regex of configureInterfacesVia
        - ConfigureVlan (str): optional regex of configureVlan
        - EgressL1HqosInstanceName (str): optional regex of egressL1HqosInstanceName
        - EgressL1HqosProfileName (str): optional regex of egressL1HqosProfileName
        - EndCvlanId (str): optional regex of endCvlanId
        - EndSvlanId (str): optional regex of endSvlanId
        - IncludeL1HqosProfile (str): optional regex of includeL1HqosProfile
        - IngressL1HqosInstanceName (str): optional regex of ingressL1HqosInstanceName
        - IngressL1HqosProfileName (str): optional regex of ingressL1HqosProfileName
        - InterfaceType (str): optional regex of interfaceType
        - IpoeFlowCheck (str): optional regex of ipoeFlowCheck
        - Ipv4Trigger (str): optional regex of ipv4Trigger
        - Ipv6Trigger (str): optional regex of ipv6Trigger
        - L1HqosActionDesc (str): optional regex of l1HqosActionDesc
        - L1HqosActionName (str): optional regex of l1HqosActionName
        - L1HqosProfileName (str): optional regex of l1HqosProfileName
        - L1HqosRuleActionPairName (str): optional regex of l1HqosRuleActionPairName
        - L1HqosRuleName (str): optional regex of l1HqosRuleName
        - LogicID (str): optional regex of logicID
        - NdProxy (str): optional regex of ndProxy
        - NdTrigger (str): optional regex of ndTrigger
        - PortNumber (str): optional regex of portNumber
        - PortType (str): optional regex of portType
        - PppOnly (str): optional regex of pppOnly
        - PppoeFlowCheck (str): optional regex of pppoeFlowCheck
        - SlotNumber (str): optional regex of slotNumber
        - StartCvlanId (str): optional regex of startCvlanId
        - StartSvlanId (str): optional regex of startSvlanId
        - SubPortNumber (str): optional regex of subPortNumber
        - SubslotNumber (str): optional regex of subslotNumber

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
