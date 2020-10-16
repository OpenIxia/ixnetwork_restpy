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


class PcReplyLspParameters(Base):
    """PCReply LSP Parameters
    The PcReplyLspParameters class encapsulates a required pcReplyLspParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pcReplyLspParameters'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Bandwidth': 'bandwidth',
        'BiDirectional': 'biDirectional',
        'BindingType': 'bindingType',
        'Bos': 'bos',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableCFlag': 'enableCFlag',
        'EnableEro': 'enableEro',
        'EnableLoose': 'enableLoose',
        'EnableXro': 'enableXro',
        'ExcludeAny': 'excludeAny',
        'FailBit': 'failBit',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IncludeBandwidth': 'includeBandwidth',
        'IncludeConfiguredERO': 'includeConfiguredERO',
        'IncludeLsp': 'includeLsp',
        'IncludeLspa': 'includeLspa',
        'IncludeMetric': 'includeMetric',
        'IncludeRp': 'includeRp',
        'IncludeSymbolicPathNameTlv': 'includeSymbolicPathNameTlv',
        'IncludeTEPathBindingTLV': 'includeTEPathBindingTLV',
        'LocalProtection': 'localProtection',
        'MplsLabel': 'mplsLabel',
        'Name': 'name',
        'NatureOfIssue': 'natureOfIssue',
        'NumberOfEroSubObjects': 'numberOfEroSubObjects',
        'NumberOfMetricSubObject': 'numberOfMetricSubObject',
        'NumberOfXroSubObjects': 'numberOfXroSubObjects',
        'PlspId': 'plspId',
        'PriorityValue': 'priorityValue',
        'ProcessType': 'processType',
        'ReceivedPLSPID': 'receivedPLSPID',
        'ReceivedSymbolicPath': 'receivedSymbolicPath',
        'ReflectLSP': 'reflectLSP',
        'ReflectRP': 'reflectRP',
        'ReflectedObjectNoPath': 'reflectedObjectNoPath',
        'RequestId': 'requestId',
        'ResponseOptions': 'responseOptions',
        'ResponsePathType': 'responsePathType',
        'SendEmptyTLV': 'sendEmptyTLV',
        'SessionInfo': 'sessionInfo',
        'SetupPriority': 'setupPriority',
        'Srv6SID': 'srv6SID',
        'SymbolicPathName': 'symbolicPathName',
        'Tc': 'tc',
        'Ttl': 'ttl',
    }

    def __init__(self, parent):
        super(PcReplyLspParameters, self).__init__(parent)

    @property
    def PceXroSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist_497bc286ebfb51b8813947a23cd5817a.PceXroSubObjectsList): An instance of the PceXroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist_497bc286ebfb51b8813947a23cd5817a import PceXroSubObjectsList
        return PceXroSubObjectsList(self)

    @property
    def PcepEroSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist_7ea27079d1a1d53cebc6e1e83b2ca0b4.PcepEroSubObjectsList): An instance of the PcepEroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist_7ea27079d1a1d53cebc6e1e83b2ca0b4 import PcepEroSubObjectsList
        return PcepEroSubObjectsList(self)

    @property
    def PcepMetricSubObjectsList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist_b1398d82dd25e8e98d50662ebf5ba3d1.PcepMetricSubObjectsList): An instance of the PcepMetricSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist_b1398d82dd25e8e98d50662ebf5ba3d1 import PcepMetricSubObjectsList
        return PcepMetricSubObjectsList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth (bits/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bandwidth']))

    @property
    def BiDirectional(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bi-directional
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BiDirectional']))

    @property
    def BindingType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. SRv6 SID Default value is 20bit MPLS Label.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BindingType']))

    @property
    def Bos(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bos']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableCFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): C Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCFlag']))

    @property
    def EnableEro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include ERO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEro']))

    @property
    def EnableLoose(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Loose
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLoose']))

    @property
    def EnableXro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include XRO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableXro']))

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Exclude Any
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAny']))

    @property
    def FailBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Fail Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FailBit']))

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Holding Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HoldingPriority']))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include All
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAll']))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Any
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAny']))

    @property
    def IncludeBandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Bandwidth
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeBandwidth']))

    @property
    def IncludeConfiguredERO(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If this is enabled, entire ERO will go out in packet even if there is Binding SID, which means no SR-ERO/SRv6-ERO validation will be done.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeConfiguredERO']))

    @property
    def IncludeLsp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLsp']))

    @property
    def IncludeLspa(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include LSPA
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLspa']))

    @property
    def IncludeMetric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMetric']))

    @property
    def IncludeRp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include RP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRp']))

    @property
    def IncludeSymbolicPathNameTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSymbolicPathNameTlv']))

    @property
    def IncludeTEPathBindingTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTEPathBindingTLV']))

    @property
    def LocalProtection(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Protection
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalProtection']))

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MplsLabel']))

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
    def NatureOfIssue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Nature Of Issue
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NatureOfIssue']))

    @property
    def NumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Number of ERO Sub Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfEroSubObjects'])
    @NumberOfEroSubObjects.setter
    def NumberOfEroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfEroSubObjects'], value)

    @property
    def NumberOfMetricSubObject(self):
        """
        Returns
        -------
        - number: Number of Metric
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfMetricSubObject'])
    @NumberOfMetricSubObject.setter
    def NumberOfMetricSubObject(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfMetricSubObject'], value)

    @property
    def NumberOfXroSubObjects(self):
        """
        Returns
        -------
        - number: Number of XRO Sub Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfXroSubObjects'])
    @NumberOfXroSubObjects.setter
    def NumberOfXroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfXroSubObjects'], value)

    @property
    def PlspId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PlspId']))

    @property
    def PriorityValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PriorityValue']))

    @property
    def ProcessType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates how the XRO is responded in the Path Request Response.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProcessType']))

    @property
    def ReceivedPLSPID(self):
        """
        Returns
        -------
        - list(number): Received PLSP-ID in PcRequest
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPLSPID'])

    @property
    def ReceivedSymbolicPath(self):
        """
        Returns
        -------
        - list(str): Received Symbolic Path Name in PcRequest
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedSymbolicPath'])

    @property
    def ReflectLSP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reflect LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReflectLSP']))

    @property
    def ReflectRP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reflect RP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReflectRP']))

    @property
    def ReflectedObjectNoPath(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reflected Object
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReflectedObjectNoPath']))

    @property
    def RequestId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Request ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestId']))

    @property
    def ResponseOptions(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reply Options
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResponseOptions']))

    @property
    def ResponsePathType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates which type of LSP will be responsed in the Path Request Response.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResponsePathType']))

    @property
    def SendEmptyTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled all fields after Binding Type will be grayed out.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendEmptyTLV']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[delegatedActive | delegatedDown | delegatedGoingUp | delegatedUp | noLSPObjectInPCRequest | none | notDelegatedActive | notDelegatedDown | notDelegatedGoingUp | notDelegatedUp | pcErrorReceived | removedByPCC | replySent | replySentReportNotReceived]): Logs additional information about the LSP state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Setup Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetupPriority']))

    @property
    def Srv6SID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID with a format of a 16 byte IPv6 address.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SID']))

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Each LSP (path) must have a symbolic name that is unique in the PCC. It must remain constant throughout a path's lifetime, which may span across multiple consecutive PCEP sessions and/or PCC restarts.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SymbolicPathName']))

    @property
    def Tc(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Tc']))

    @property
    def Ttl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ttl']))

    def update(self, Name=None, NumberOfEroSubObjects=None, NumberOfMetricSubObject=None, NumberOfXroSubObjects=None):
        """Updates pcReplyLspParameters resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfEroSubObjects (number): Number of ERO Sub Objects
        - NumberOfMetricSubObject (number): Number of Metric
        - NumberOfXroSubObjects (number): Number of XRO Sub Objects

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, Bandwidth=None, BiDirectional=None, BindingType=None, Bos=None, EnableCFlag=None, EnableEro=None, EnableLoose=None, EnableXro=None, ExcludeAny=None, FailBit=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeBandwidth=None, IncludeConfiguredERO=None, IncludeLsp=None, IncludeLspa=None, IncludeMetric=None, IncludeRp=None, IncludeSymbolicPathNameTlv=None, IncludeTEPathBindingTLV=None, LocalProtection=None, MplsLabel=None, NatureOfIssue=None, PlspId=None, PriorityValue=None, ProcessType=None, ReflectLSP=None, ReflectRP=None, ReflectedObjectNoPath=None, RequestId=None, ResponseOptions=None, ResponsePathType=None, SendEmptyTLV=None, SetupPriority=None, Srv6SID=None, SymbolicPathName=None, Tc=None, Ttl=None):
        """Base class infrastructure that gets a list of pcReplyLspParameters device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Bandwidth (str): optional regex of bandwidth
        - BiDirectional (str): optional regex of biDirectional
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - EnableCFlag (str): optional regex of enableCFlag
        - EnableEro (str): optional regex of enableEro
        - EnableLoose (str): optional regex of enableLoose
        - EnableXro (str): optional regex of enableXro
        - ExcludeAny (str): optional regex of excludeAny
        - FailBit (str): optional regex of failBit
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludeRp (str): optional regex of includeRp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - NatureOfIssue (str): optional regex of natureOfIssue
        - PlspId (str): optional regex of plspId
        - PriorityValue (str): optional regex of priorityValue
        - ProcessType (str): optional regex of processType
        - ReflectLSP (str): optional regex of reflectLSP
        - ReflectRP (str): optional regex of reflectRP
        - ReflectedObjectNoPath (str): optional regex of reflectedObjectNoPath
        - RequestId (str): optional regex of requestId
        - ResponseOptions (str): optional regex of responseOptions
        - ResponsePathType (str): optional regex of responsePathType
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - Srv6SID (str): optional regex of srv6SID
        - SymbolicPathName (str): optional regex of symbolicPathName
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ReturnDelegation(self, *args, **kwargs):
        """Executes the returnDelegation operation on the server.

        Return Delegation of PCE-Replied LSPs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        returnDelegation(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        returnDelegation(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        returnDelegation(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): Return Delegation.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('returnDelegation', payload=payload, response_object=None)
