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


class PceInitiateLSPParameters(Base):
    """This tab configures the Initiated LSP Parameters.
    The PceInitiateLSPParameters class encapsulates a required pceInitiateLSPParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pceInitiateLSPParameters'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AssociationId': 'associationId',
        'Bandwidth': 'bandwidth',
        'BindingType': 'bindingType',
        'Bos': 'bos',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestEndPointIpv4': 'destEndPointIpv4',
        'DestEndPointIpv6': 'destEndPointIpv6',
        'EnableXro': 'enableXro',
        'ExcludeAny': 'excludeAny',
        'FailBit': 'failBit',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IncludeAssociation': 'includeAssociation',
        'IncludeBandwidth': 'includeBandwidth',
        'IncludeConfiguredERO': 'includeConfiguredERO',
        'IncludeEndPoints': 'includeEndPoints',
        'IncludeEro': 'includeEro',
        'IncludeLsp': 'includeLsp',
        'IncludeLspa': 'includeLspa',
        'IncludeMetric': 'includeMetric',
        'IncludeSrp': 'includeSrp',
        'IncludeSymbolicPathNameTlv': 'includeSymbolicPathNameTlv',
        'IncludeTEPathBindingTLV': 'includeTEPathBindingTLV',
        'IpVersion': 'ipVersion',
        'LocalProtection': 'localProtection',
        'MplsLabel': 'mplsLabel',
        'Name': 'name',
        'NumberOfEroSubObjects': 'numberOfEroSubObjects',
        'NumberOfMetricSubObject': 'numberOfMetricSubObject',
        'NumberOfXroSubObjects': 'numberOfXroSubObjects',
        'OverridePlspId': 'overridePlspId',
        'OverrideSrpIdNumber': 'overrideSrpIdNumber',
        'PathSetupType': 'pathSetupType',
        'PlspId': 'plspId',
        'ProtectionLsp': 'protectionLsp',
        'SendEmptyTLV': 'sendEmptyTLV',
        'SessionInfo': 'sessionInfo',
        'SetupPriority': 'setupPriority',
        'SrcEndPointIpv4': 'srcEndPointIpv4',
        'SrcEndPointIpv6': 'srcEndPointIpv6',
        'SrpIdNumber': 'srpIdNumber',
        'Srv6SID': 'srv6SID',
        'StandbyMode': 'standbyMode',
        'SymbolicPathName': 'symbolicPathName',
        'Tc': 'tc',
        'Ttl': 'ttl',
    }

    def __init__(self, parent):
        super(PceInitiateLSPParameters, self).__init__(parent)

    @property
    def PceInitiateXROobject(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject_4394b1635bed370ec02e722a5dab40b6.PceInitiateXROobject): An instance of the PceInitiateXROobject class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject_4394b1635bed370ec02e722a5dab40b6 import PceInitiateXROobject
        return PceInitiateXROobject(self)

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
    def AssociationId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The Association ID of this LSP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssociationId']))

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
    def BindingType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label SRv6 SID Default value is 20bit MPLS Label.
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
    def DestEndPointIpv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Dest IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv6.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestEndPointIpv4']))

    @property
    def DestEndPointIpv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Dest IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv4.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestEndPointIpv6']))

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
        - obj(uhd_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link only if the link carries all of the attributes in the set.
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
        - obj(uhd_restpy.multivalue.Multivalue): The priority of the LSP with respect to holding resources. The value 0 is the highest priority. Holding Priority is used in deciding whether this session can be preempted by another session.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HoldingPriority']))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control excludes a link from consideration if the link carries any of the attributes in the set.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAll']))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link if the link carries any of the attributes in the set.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAny']))

    @property
    def IncludeAssociation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether PPAG will be included in a PCInitiate message. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAssociation']))

    @property
    def IncludeBandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether Bandwidth will be included in a PCInitiate message. All other attributes in sub-tab-Bandwidth would be editable only if this checkbox is enabled.
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
    def IncludeEndPoints(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether END-POINTS object will be included in a PCInitiate message. All other attributes in sub-tab-End Points would be editable only if this checkbox is enabled
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeEndPoints']))

    @property
    def IncludeEro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies whether ERO is active or inactive. All subsequent attributes of the sub-tab-ERO would be editable only if this is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeEro']))

    @property
    def IncludeLsp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether LSP will be included in a PCInitiate message. All other attributes in sub-tab-LSP would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLsp']))

    @property
    def IncludeLspa(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether LSPA will be included in a PCInitiate message. All other attributes in sub-tab-LSPA would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeLspa']))

    @property
    def IncludeMetric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether the PCInitiate message will have the metric list that is configured. All subsequent attributes of the sub-tab-Metric would be editable only if this is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMetric']))

    @property
    def IncludeSrp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSrp']))

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
    def IpVersion(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Drop down to select the IP Version with 2 choices : IPv4 / IPv6
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpVersion']))

    @property
    def LocalProtection(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): When set, this means that the path must include links protected with Fast Reroute
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
    def NumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of ERO Sub Objects to be configured.
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
        - number: Value that indicates the number of Metric Objects to be configured.
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
    def OverridePlspId(self):
        """
        Returns
        -------
        - bool: Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverridePlspId'])
    @OverridePlspId.setter
    def OverridePlspId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverridePlspId'], value)

    @property
    def OverrideSrpIdNumber(self):
        """
        Returns
        -------
        - bool: Indicates whether SRP ID Number is overridable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideSrpIdNumber'])
    @OverrideSrpIdNumber.setter
    def OverrideSrpIdNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideSrpIdNumber'], value)

    @property
    def PathSetupType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates which type of LSP will be requested in the PCInitiated Request.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PathSetupType']))

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
    def ProtectionLsp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether Protection LSP Bit is On.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProtectionLsp']))

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
        - list(str[advertised | delegatedActive | delegatedDown | delegatedGoingUp | delegatedUp | init | none | notDelegatedActive | notDelegatedDown | notDelegatedGoingUp | notDelegatedUp | pcErrorReceived | removedByPCC | removedByPCE | returnDelegation]): Logs additional information about the LSP state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The priority of the LSP with respect to taking resources.The value 0 is the highest priority.The Setup Priority is used in deciding whether this session can preempt another session.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetupPriority']))

    @property
    def SrcEndPointIpv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is set to IPv6.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcEndPointIpv4']))

    @property
    def SrcEndPointIpv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP version is set to IPv4.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcEndPointIpv6']))

    @property
    def SrpIdNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrpIdNumber']))

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
    def StandbyMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether Standby LSP Bit is On.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StandbyMode']))

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

    def update(self, Name=None, NumberOfEroSubObjects=None, NumberOfMetricSubObject=None, NumberOfXroSubObjects=None, OverridePlspId=None, OverrideSrpIdNumber=None):
        """Updates pceInitiateLSPParameters resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObject (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfXroSubObjects (number): Number of XRO Sub Objects
        - OverridePlspId (bool): Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        - OverrideSrpIdNumber (bool): Indicates whether SRP ID Number is overridable.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AssociationId=None, Bandwidth=None, BindingType=None, Bos=None, DestEndPointIpv4=None, DestEndPointIpv6=None, EnableXro=None, ExcludeAny=None, FailBit=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeAssociation=None, IncludeBandwidth=None, IncludeConfiguredERO=None, IncludeEndPoints=None, IncludeEro=None, IncludeLsp=None, IncludeLspa=None, IncludeMetric=None, IncludeSrp=None, IncludeSymbolicPathNameTlv=None, IncludeTEPathBindingTLV=None, IpVersion=None, LocalProtection=None, MplsLabel=None, PathSetupType=None, PlspId=None, ProtectionLsp=None, SendEmptyTLV=None, SetupPriority=None, SrcEndPointIpv4=None, SrcEndPointIpv6=None, SrpIdNumber=None, Srv6SID=None, StandbyMode=None, SymbolicPathName=None, Tc=None, Ttl=None):
        """Base class infrastructure that gets a list of pceInitiateLSPParameters device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AssociationId (str): optional regex of associationId
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - DestEndPointIpv4 (str): optional regex of destEndPointIpv4
        - DestEndPointIpv6 (str): optional regex of destEndPointIpv6
        - EnableXro (str): optional regex of enableXro
        - ExcludeAny (str): optional regex of excludeAny
        - FailBit (str): optional regex of failBit
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeAssociation (str): optional regex of includeAssociation
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeEndPoints (str): optional regex of includeEndPoints
        - IncludeEro (str): optional regex of includeEro
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - IpVersion (str): optional regex of ipVersion
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - PathSetupType (str): optional regex of pathSetupType
        - PlspId (str): optional regex of plspId
        - ProtectionLsp (str): optional regex of protectionLsp
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - SrcEndPointIpv4 (str): optional regex of srcEndPointIpv4
        - SrcEndPointIpv6 (str): optional regex of srcEndPointIpv6
        - SrpIdNumber (str): optional regex of srpIdNumber
        - Srv6SID (str): optional regex of srv6SID
        - StandbyMode (str): optional regex of standbyMode
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

        Return Delegation of PCE-Initiated LSPs

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

    def TakeControl(self, *args, **kwargs):
        """Executes the takeControl operation on the server.

        Take Control of PCE-Initiated LSPs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        takeControl(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        takeControl(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        takeControl(Arg2=list)list
        --------------------------
        - Arg2 (list(number)): Take Control.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('takeControl', payload=payload, response_object=None)
