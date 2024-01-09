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


class L4HqosConfigList(Base):
    """L4 HQoS Config parameters
    The L4HqosConfigList class encapsulates a required l4HqosConfigList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "l4HqosConfigList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Ipv4RuleDesc": "ipv4RuleDesc",
        "Ipv4RuleName": "ipv4RuleName",
        "Ipv6RuleDesc": "ipv6RuleDesc",
        "Ipv6RuleName": "ipv6RuleName",
        "L4HqosActionDesc": "l4HqosActionDesc",
        "L4HqosActionName": "l4HqosActionName",
        "L4HqosProfileName": "l4HqosProfileName",
        "L4HqosRuleActionPairName": "l4HqosRuleActionPairName",
        "L4HqosRuleName": "l4HqosRuleName",
        "Name": "name",
        "QosActionDesc": "qosActionDesc",
        "QosActionDescCar": "qosActionDescCar",
        "QosActionDescType": "qosActionDescType",
        "QosActionName": "qosActionName",
        "QosPolicyName": "qosPolicyName",
        "ServiceActionDesc": "serviceActionDesc",
        "ServiceActionDescType": "serviceActionDescType",
        "ServiceActionName": "serviceActionName",
        "ServicePolicyName": "servicePolicyName",
        "UserAclPolicyName": "userAclPolicyName",
        "UserPolicyGroupName": "userPolicyGroupName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(L4HqosConfigList, self).__init__(parent, list_op)

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
    def Ipv4RuleDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: action dir proto from src to dst example: permit in ip from assigned to any Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4RuleDesc"]))

    @property
    def Ipv4RuleName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Rule Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4RuleName"]))

    @property
    def Ipv6RuleDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: action dir proto from src to dst example: permit in ip from assigned to any Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6RuleDesc"]))

    @property
    def Ipv6RuleName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Rule Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6RuleName"]))

    @property
    def L4HqosActionDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: queue <queue-id> { pir <pir-value> | pbs <pbs-value> | { pq | lpq | wfq weight <weight-value> } } * Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L4HqosActionDesc"])
        )

    @property
    def L4HqosActionName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L4 HQoS Action Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L4HqosActionName"])
        )

    @property
    def L4HqosProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L4 HQoS Profile Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L4HqosProfileName"])
        )

    @property
    def L4HqosRuleActionPairName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L4 HQoS Rule Action Pair Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L4HqosRuleActionPairName"])
        )

    @property
    def L4HqosRuleName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L4 HQoS Rule Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L4HqosRuleName"])
        )

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
    def QosActionDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): QoS Action Desc (1 octet)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QosActionDesc"]))

    @property
    def QosActionDescCar(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: cir <cir-val> cbs <cbs-val> pir <pir-val> <pbs-val> Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QosActionDescCar"])
        )

    @property
    def QosActionDescType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): QoS Action Description Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QosActionDescType"])
        )

    @property
    def QosActionName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): QoS Action Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QosActionName"]))

    @property
    def QosPolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): QoS Policy Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QosPolicyName"]))

    @property
    def ServiceActionDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): format: redirect-ip: dst-ip X.X.X.X VPN-Name dst-ipv6 X:X:X:X VPN-Name redirect-nat: nat-instance-name UPF predefine action: 255 UP predefine action, specifying the name of the action that performs the predefined action on the UPF Keep Empty If Not Requried
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceActionDesc"])
        )

    @property
    def ServiceActionDescType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Service Action Description Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceActionDescType"])
        )

    @property
    def ServiceActionName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Service Action Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceActionName"])
        )

    @property
    def ServicePolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Service Policy Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServicePolicyName"])
        )

    @property
    def UserAclPolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User ACL Policy Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserAclPolicyName"])
        )

    @property
    def UserPolicyGroupName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Policy Group Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserPolicyGroupName"])
        )

    def update(self, Name=None):
        # type: (str) -> L4HqosConfigList
        """Updates l4HqosConfigList resource on the server.

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
        # type: (int, str, str) -> L4HqosConfigList
        """Finds and retrieves l4HqosConfigList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l4HqosConfigList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l4HqosConfigList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching l4HqosConfigList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l4HqosConfigList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l4HqosConfigList resources from the server available through an iterator or index

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
        Active=None,
        Ipv4RuleDesc=None,
        Ipv4RuleName=None,
        Ipv6RuleDesc=None,
        Ipv6RuleName=None,
        L4HqosActionDesc=None,
        L4HqosActionName=None,
        L4HqosProfileName=None,
        L4HqosRuleActionPairName=None,
        L4HqosRuleName=None,
        QosActionDesc=None,
        QosActionDescCar=None,
        QosActionDescType=None,
        QosActionName=None,
        QosPolicyName=None,
        ServiceActionDesc=None,
        ServiceActionDescType=None,
        ServiceActionName=None,
        ServicePolicyName=None,
        UserAclPolicyName=None,
        UserPolicyGroupName=None,
    ):
        """Base class infrastructure that gets a list of l4HqosConfigList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Ipv4RuleDesc (str): optional regex of ipv4RuleDesc
        - Ipv4RuleName (str): optional regex of ipv4RuleName
        - Ipv6RuleDesc (str): optional regex of ipv6RuleDesc
        - Ipv6RuleName (str): optional regex of ipv6RuleName
        - L4HqosActionDesc (str): optional regex of l4HqosActionDesc
        - L4HqosActionName (str): optional regex of l4HqosActionName
        - L4HqosProfileName (str): optional regex of l4HqosProfileName
        - L4HqosRuleActionPairName (str): optional regex of l4HqosRuleActionPairName
        - L4HqosRuleName (str): optional regex of l4HqosRuleName
        - QosActionDesc (str): optional regex of qosActionDesc
        - QosActionDescCar (str): optional regex of qosActionDescCar
        - QosActionDescType (str): optional regex of qosActionDescType
        - QosActionName (str): optional regex of qosActionName
        - QosPolicyName (str): optional regex of qosPolicyName
        - ServiceActionDesc (str): optional regex of serviceActionDesc
        - ServiceActionDescType (str): optional regex of serviceActionDescType
        - ServiceActionName (str): optional regex of serviceActionName
        - ServicePolicyName (str): optional regex of servicePolicyName
        - UserAclPolicyName (str): optional regex of userAclPolicyName
        - UserPolicyGroupName (str): optional regex of userPolicyGroupName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
