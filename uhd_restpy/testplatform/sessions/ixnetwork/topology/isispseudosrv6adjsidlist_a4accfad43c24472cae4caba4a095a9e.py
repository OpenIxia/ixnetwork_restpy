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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class IsisPseudoSRv6AdjSIDList(Base):
    """ISIS SRv6 Adj SID
    The IsisPseudoSRv6AdjSIDList class encapsulates a required isisPseudoSRv6AdjSIDList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoSRv6AdjSIDList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActiveTo': 'activeTo',
        'AdvertiseCustomSubTLV': 'advertiseCustomSubTLV',
        'AdvertiseCustomSubTLVTo': 'advertiseCustomSubTLVTo',
        'Algorithm': 'algorithm',
        'AlgorithmTo': 'algorithmTo',
        'ArgumentLength': 'argumentLength',
        'ArgumentLengthTo': 'argumentLengthTo',
        'BFlag': 'bFlag',
        'BFlagTo': 'bFlagTo',
        'Count': 'count',
        'CustomEndPointFunction': 'customEndPointFunction',
        'CustomEndPointFunctionTo': 'customEndPointFunctionTo',
        'CustomSubTlv': 'customSubTlv',
        'CustomSubTlvTo': 'customSubTlvTo',
        'DescriptiveName': 'descriptiveName',
        'EndPointFunction': 'endPointFunction',
        'EndPointFunctionTo': 'endPointFunctionTo',
        'FunctionLength': 'functionLength',
        'FunctionLengthTo': 'functionLengthTo',
        'IncludeSRv6SIDStructureSubSubTlv': 'includeSRv6SIDStructureSubSubTlv',
        'IncludeSRv6SIDStructureSubSubTlvTo': 'includeSRv6SIDStructureSubSubTlvTo',
        'Ipv6AdjSid': 'ipv6AdjSid',
        'Ipv6AdjSidTo': 'ipv6AdjSidTo',
        'LocatorBlockLength': 'locatorBlockLength',
        'LocatorBlockLengthTo': 'locatorBlockLengthTo',
        'LocatorNodeLength': 'locatorNodeLength',
        'LocatorNodeLengthTo': 'locatorNodeLengthTo',
        'Name': 'name',
        'PFlag': 'pFlag',
        'PFlagTo': 'pFlagTo',
        'Reserved': 'reserved',
        'ReservedTo': 'reservedTo',
        'SFlag': 'sFlag',
        'SFlagTo': 'sFlagTo',
        'Weight': 'weight',
        'WeightTo': 'weightTo',
    }

    def __init__(self, parent):
        super(IsisPseudoSRv6AdjSIDList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ActiveTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flag.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveTo']))

    @property
    def AdvertiseCustomSubTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseCustomSubTLV']))

    @property
    def AdvertiseCustomSubTLVTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseCustomSubTLVTo']))

    @property
    def Algorithm(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def AlgorithmTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AlgorithmTo']))

    @property
    def ArgumentLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Argument Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLength']))

    @property
    def ArgumentLengthTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Argument Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLengthTo']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def BFlagTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlagTo']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CustomEndPointFunction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom End-Point Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomEndPointFunction']))

    @property
    def CustomEndPointFunctionTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom End-Point Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomEndPointFunctionTo']))

    @property
    def CustomSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomSubTlv']))

    @property
    def CustomSubTlvTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomSubTlvTo']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EndPointFunction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): End-Point Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointFunction']))

    @property
    def EndPointFunctionTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): End-Point Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointFunctionTo']))

    @property
    def FunctionLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Function Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLength']))

    @property
    def FunctionLengthTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Function Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLengthTo']))

    @property
    def IncludeSRv6SIDStructureSubSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubSubTlv']))

    @property
    def IncludeSRv6SIDStructureSubSubTlvTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubSubTlvTo']))

    @property
    def Ipv6AdjSid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AdjSid']))

    @property
    def Ipv6AdjSidTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AdjSidTo']))

    @property
    def LocatorBlockLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Block Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorBlockLength']))

    @property
    def LocatorBlockLengthTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Block Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorBlockLengthTo']))

    @property
    def LocatorNodeLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Node Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorNodeLength']))

    @property
    def LocatorNodeLengthTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Node Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorNodeLengthTo']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): P-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def PFlagTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): P-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlagTo']))

    @property
    def Reserved(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def ReservedTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedTo']))

    @property
    def SFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def SFlagTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlagTo']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    @property
    def WeightTo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WeightTo']))

    def update(self, Name=None):
        """Updates isisPseudoSRv6AdjSIDList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, ActiveTo=None, AdvertiseCustomSubTLV=None, AdvertiseCustomSubTLVTo=None, Algorithm=None, AlgorithmTo=None, ArgumentLength=None, ArgumentLengthTo=None, BFlag=None, BFlagTo=None, CustomEndPointFunction=None, CustomEndPointFunctionTo=None, CustomSubTlv=None, CustomSubTlvTo=None, EndPointFunction=None, EndPointFunctionTo=None, FunctionLength=None, FunctionLengthTo=None, IncludeSRv6SIDStructureSubSubTlv=None, IncludeSRv6SIDStructureSubSubTlvTo=None, Ipv6AdjSid=None, Ipv6AdjSidTo=None, LocatorBlockLength=None, LocatorBlockLengthTo=None, LocatorNodeLength=None, LocatorNodeLengthTo=None, PFlag=None, PFlagTo=None, Reserved=None, ReservedTo=None, SFlag=None, SFlagTo=None, Weight=None, WeightTo=None):
        """Base class infrastructure that gets a list of isisPseudoSRv6AdjSIDList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTo (str): optional regex of activeTo
        - AdvertiseCustomSubTLV (str): optional regex of advertiseCustomSubTLV
        - AdvertiseCustomSubTLVTo (str): optional regex of advertiseCustomSubTLVTo
        - Algorithm (str): optional regex of algorithm
        - AlgorithmTo (str): optional regex of algorithmTo
        - ArgumentLength (str): optional regex of argumentLength
        - ArgumentLengthTo (str): optional regex of argumentLengthTo
        - BFlag (str): optional regex of bFlag
        - BFlagTo (str): optional regex of bFlagTo
        - CustomEndPointFunction (str): optional regex of customEndPointFunction
        - CustomEndPointFunctionTo (str): optional regex of customEndPointFunctionTo
        - CustomSubTlv (str): optional regex of customSubTlv
        - CustomSubTlvTo (str): optional regex of customSubTlvTo
        - EndPointFunction (str): optional regex of endPointFunction
        - EndPointFunctionTo (str): optional regex of endPointFunctionTo
        - FunctionLength (str): optional regex of functionLength
        - FunctionLengthTo (str): optional regex of functionLengthTo
        - IncludeSRv6SIDStructureSubSubTlv (str): optional regex of includeSRv6SIDStructureSubSubTlv
        - IncludeSRv6SIDStructureSubSubTlvTo (str): optional regex of includeSRv6SIDStructureSubSubTlvTo
        - Ipv6AdjSid (str): optional regex of ipv6AdjSid
        - Ipv6AdjSidTo (str): optional regex of ipv6AdjSidTo
        - LocatorBlockLength (str): optional regex of locatorBlockLength
        - LocatorBlockLengthTo (str): optional regex of locatorBlockLengthTo
        - LocatorNodeLength (str): optional regex of locatorNodeLength
        - LocatorNodeLengthTo (str): optional regex of locatorNodeLengthTo
        - PFlag (str): optional regex of pFlag
        - PFlagTo (str): optional regex of pFlagTo
        - Reserved (str): optional regex of reserved
        - ReservedTo (str): optional regex of reservedTo
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

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
