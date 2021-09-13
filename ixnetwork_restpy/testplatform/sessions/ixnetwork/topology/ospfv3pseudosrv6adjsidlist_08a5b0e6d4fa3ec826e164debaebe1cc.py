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


class Ospfv3PseudoSRv6AdjSIDList(Base):
    """OSPFv3 SRv6 Adj SID
    The Ospfv3PseudoSRv6AdjSIDList class encapsulates a required ospfv3PseudoSRv6AdjSIDList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv3PseudoSRv6AdjSIDList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActiveTo': 'activeTo',
        'Algorithm': 'algorithm',
        'AlgorithmTo': 'algorithmTo',
        'ArgumentLength': 'argumentLength',
        'ArgumentLengthTo': 'argumentLengthTo',
        'BFlag': 'bFlag',
        'BFlagTo': 'bFlagTo',
        'Count': 'count',
        'CustomEndPointFunction': 'customEndPointFunction',
        'CustomEndPointFunctionTo': 'customEndPointFunctionTo',
        'DescriptiveName': 'descriptiveName',
        'EndPointFunction': 'endPointFunction',
        'EndPointFunctionTo': 'endPointFunctionTo',
        'FunctionLength': 'functionLength',
        'FunctionLengthTo': 'functionLengthTo',
        'IncludeSRv6SIDStructureSubTlv': 'includeSRv6SIDStructureSubTlv',
        'IncludeSRv6SIDStructureSubTlvTo': 'includeSRv6SIDStructureSubTlvTo',
        'Ipv6AdjSid': 'ipv6AdjSid',
        'Ipv6AdjSidTo': 'ipv6AdjSidTo',
        'LocatorBlockLength': 'locatorBlockLength',
        'LocatorBlockLengthTo': 'locatorBlockLengthTo',
        'LocatorNodeLength': 'locatorNodeLength',
        'LocatorNodeLengthTo': 'locatorNodeLengthTo',
        'Name': 'name',
        'PFlag': 'pFlag',
        'PFlagTo': 'pFlagTo',
        'Reserved1': 'reserved1',
        'Reserved1To': 'reserved1To',
        'Reserved2': 'reserved2',
        'Reserved2To': 'reserved2To',
        'ReservedFlag': 'reservedFlag',
        'ReservedFlagTo': 'reservedFlagTo',
        'SFlag': 'sFlag',
        'SFlagTo': 'sFlagTo',
        'Weight': 'weight',
        'WeightTo': 'weightTo',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3PseudoSRv6AdjSIDList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ActiveTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveTo']))

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm associated with Segment Identifier(SID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def AlgorithmTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm associated with Segment Identifier(SID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AlgorithmTo']))

    @property
    def ArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Argument Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLength']))

    @property
    def ArgumentLengthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Argument Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLengthTo']))

    @property
    def BFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B Flag: Backup Flag: If set, the Adjacency Segment Identifier(SID) refers to an adjacency that is eligible for protection.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def BFlagTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B Flag: Backup Flag: If set, the Adjacency Segment Identifier(SID) refers to an adjacency that is eligible for protection.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlagTo']))

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
    def CustomEndPointFunction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Function.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomEndPointFunction']))

    @property
    def CustomEndPointFunctionTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Function.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomEndPointFunctionTo']))

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
    def EndPointFunction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The End Point Function associated with SRv6 adjacency Segment Identifier(SID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointFunction']))

    @property
    def EndPointFunctionTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The End Point Function associated with SRv6 adjacency Segment Identifier(SID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointFunctionTo']))

    @property
    def FunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Function Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLength']))

    @property
    def FunctionLengthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Function Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLengthTo']))

    @property
    def IncludeSRv6SIDStructureSubTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Includes SRv6 SID Structure Sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubTlv']))

    @property
    def IncludeSRv6SIDStructureSubTlvTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Includes SRv6 SID Structure Sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubTlvTo']))

    @property
    def Ipv6AdjSid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AdjSid']))

    @property
    def Ipv6AdjSidTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AdjSidTo']))

    @property
    def LocatorBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Block Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorBlockLength']))

    @property
    def LocatorBlockLengthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Block Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorBlockLengthTo']))

    @property
    def LocatorNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Node Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorNodeLength']))

    @property
    def LocatorNodeLengthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Node Length in Bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorNodeLengthTo']))

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
    def PFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P-Flag:Persistent Flag: If set, the Segement Identifier(SID) is persistently allocated. The Segment Identifier(SID) value remains consistent across router restart and session/interface flap.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def PFlagTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P-Flag:Persistent Flag: If set, the Segment Identifier(SID) is persistently allocated. The Segment Identifier(SID) value remains consistent across router restart and session/interface flap.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagTo']))

    @property
    def Reserved1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved1 Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1']))

    @property
    def Reserved1To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved1 Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1To']))

    @property
    def Reserved2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved2 Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    @property
    def Reserved2To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved2 Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2To']))

    @property
    def ReservedFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved bits value in Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedFlag']))

    @property
    def ReservedFlagTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved bits value in Flag Field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedFlagTo']))

    @property
    def SFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S Flag: Set Flag. If Set, the Segment Identifier(SID) refers to a set of adjacencies.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def SFlagTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S Flag: Set Flag. If Set, the Segement Identifier(SID) refers to a set of adjacencies.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlagTo']))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the weight of the adjacency Segment Identifier(SID) for the purpose of load balancing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    @property
    def WeightTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the weight of the adjacency Segment Identifier(SID) for the purpose of load balancing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WeightTo']))

    def update(self, Name=None):
        # type: (str) -> Ospfv3PseudoSRv6AdjSIDList
        """Updates ospfv3PseudoSRv6AdjSIDList resource on the server.

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

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, ActiveTo=None, Algorithm=None, AlgorithmTo=None, ArgumentLength=None, ArgumentLengthTo=None, BFlag=None, BFlagTo=None, CustomEndPointFunction=None, CustomEndPointFunctionTo=None, EndPointFunction=None, EndPointFunctionTo=None, FunctionLength=None, FunctionLengthTo=None, IncludeSRv6SIDStructureSubTlv=None, IncludeSRv6SIDStructureSubTlvTo=None, Ipv6AdjSid=None, Ipv6AdjSidTo=None, LocatorBlockLength=None, LocatorBlockLengthTo=None, LocatorNodeLength=None, LocatorNodeLengthTo=None, PFlag=None, PFlagTo=None, Reserved1=None, Reserved1To=None, Reserved2=None, Reserved2To=None, ReservedFlag=None, ReservedFlagTo=None, SFlag=None, SFlagTo=None, Weight=None, WeightTo=None):
        """Base class infrastructure that gets a list of ospfv3PseudoSRv6AdjSIDList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTo (str): optional regex of activeTo
        - Algorithm (str): optional regex of algorithm
        - AlgorithmTo (str): optional regex of algorithmTo
        - ArgumentLength (str): optional regex of argumentLength
        - ArgumentLengthTo (str): optional regex of argumentLengthTo
        - BFlag (str): optional regex of bFlag
        - BFlagTo (str): optional regex of bFlagTo
        - CustomEndPointFunction (str): optional regex of customEndPointFunction
        - CustomEndPointFunctionTo (str): optional regex of customEndPointFunctionTo
        - EndPointFunction (str): optional regex of endPointFunction
        - EndPointFunctionTo (str): optional regex of endPointFunctionTo
        - FunctionLength (str): optional regex of functionLength
        - FunctionLengthTo (str): optional regex of functionLengthTo
        - IncludeSRv6SIDStructureSubTlv (str): optional regex of includeSRv6SIDStructureSubTlv
        - IncludeSRv6SIDStructureSubTlvTo (str): optional regex of includeSRv6SIDStructureSubTlvTo
        - Ipv6AdjSid (str): optional regex of ipv6AdjSid
        - Ipv6AdjSidTo (str): optional regex of ipv6AdjSidTo
        - LocatorBlockLength (str): optional regex of locatorBlockLength
        - LocatorBlockLengthTo (str): optional regex of locatorBlockLengthTo
        - LocatorNodeLength (str): optional regex of locatorNodeLength
        - LocatorNodeLengthTo (str): optional regex of locatorNodeLengthTo
        - PFlag (str): optional regex of pFlag
        - PFlagTo (str): optional regex of pFlagTo
        - Reserved1 (str): optional regex of reserved1
        - Reserved1To (str): optional regex of reserved1To
        - Reserved2 (str): optional regex of reserved2
        - Reserved2To (str): optional regex of reserved2To
        - ReservedFlag (str): optional regex of reservedFlag
        - ReservedFlagTo (str): optional regex of reservedFlagTo
        - SFlag (str): optional regex of sFlag
        - SFlagTo (str): optional regex of sFlagTo
        - Weight (str): optional regex of weight
        - WeightTo (str): optional regex of weightTo

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
