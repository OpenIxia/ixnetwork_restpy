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
from typing import List, Any, Union


class LdpLeafRangeV4(Base):
    """LDP Basic LeafRange V4 Configuration
    The LdpLeafRangeV4 class encapsulates a required ldpLeafRangeV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ldpLeafRangeV4'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ContinuousIncrementOVAcrossRoot': 'continuousIncrementOVAcrossRoot',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'GroupAddressV4': 'groupAddressV4',
        'GroupAddressV6': 'groupAddressV6',
        'GroupCountPerLsp': 'groupCountPerLsp',
        'LSPType': 'lSPType',
        'LabelValueStart': 'labelValueStart',
        'LabelValueStep': 'labelValueStep',
        'LspCountPerRoot': 'lspCountPerRoot',
        'Name': 'name',
        'NumberOfTLVs': 'numberOfTLVs',
        'RootAddress': 'rootAddress',
        'RootAddressCount': 'rootAddressCount',
        'RootAddressStep': 'rootAddressStep',
    }
    _SDM_ENUM_MAP = {
        'lSPType': ['p2MP'],
    }

    def __init__(self, parent, list_op=False):
        super(LdpLeafRangeV4, self).__init__(parent, list_op)

    @property
    def LdpTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2.LdpTLVList): An instance of the LdpTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2 import LdpTLVList
        if self._properties.get('LdpTLVList', None) is not None:
            return self._properties.get('LdpTLVList')
        else:
            return LdpTLVList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        if self._properties.get('Tag', None) is not None:
            return self._properties.get('Tag')
        else:
            return Tag(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ContinuousIncrementOVAcrossRoot(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Continuous Increment Opaque Value Across Root
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ContinuousIncrementOVAcrossRoot']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def GroupAddressV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressV4']))

    @property
    def GroupAddressV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressV6']))

    @property
    def GroupCountPerLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Count per LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupCountPerLsp']))

    @property
    def LSPType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(p2MP): LSP Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['LSPType'])
    @LSPType.setter
    def LSPType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LSPType'], value)

    @property
    def LabelValueStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Value Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelValueStart']))

    @property
    def LabelValueStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Value Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelValueStep']))

    @property
    def LspCountPerRoot(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Count Per Root
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspCountPerRoot']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NumberOfTLVs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of TLVs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfTLVs'])
    @NumberOfTLVs.setter
    def NumberOfTLVs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfTLVs'], value)

    @property
    def RootAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddress']))

    @property
    def RootAddressCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddressCount']))

    @property
    def RootAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddressStep']))

    def update(self, LSPType=None, Name=None, NumberOfTLVs=None):
        # type: (str, str, int) -> LdpLeafRangeV4
        """Updates ldpLeafRangeV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - LSPType (str(p2MP)): LSP Type
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfTLVs (number): Number Of TLVs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def ActivateLeafRange(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the activateLeafRange operation on the server.

        Activate Multicast Leaf Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        activateLeafRange(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        activateLeafRange(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        activateLeafRange(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        activateLeafRange(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('activateLeafRange', payload=payload, response_object=None)

    def DeactivateLeafRange(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the deactivateLeafRange operation on the server.

        Deactivate Multicast Leaf Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        deactivateLeafRange(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        deactivateLeafRange(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        deactivateLeafRange(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        deactivateLeafRange(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('deactivateLeafRange', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, ContinuousIncrementOVAcrossRoot=None, GroupAddressV4=None, GroupAddressV6=None, GroupCountPerLsp=None, LabelValueStart=None, LabelValueStep=None, LspCountPerRoot=None, RootAddress=None, RootAddressCount=None, RootAddressStep=None):
        """Base class infrastructure that gets a list of ldpLeafRangeV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ContinuousIncrementOVAcrossRoot (str): optional regex of continuousIncrementOVAcrossRoot
        - GroupAddressV4 (str): optional regex of groupAddressV4
        - GroupAddressV6 (str): optional regex of groupAddressV6
        - GroupCountPerLsp (str): optional regex of groupCountPerLsp
        - LabelValueStart (str): optional regex of labelValueStart
        - LabelValueStep (str): optional regex of labelValueStep
        - LspCountPerRoot (str): optional regex of lspCountPerRoot
        - RootAddress (str): optional regex of rootAddress
        - RootAddressCount (str): optional regex of rootAddressCount
        - RootAddressStep (str): optional regex of rootAddressStep

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
