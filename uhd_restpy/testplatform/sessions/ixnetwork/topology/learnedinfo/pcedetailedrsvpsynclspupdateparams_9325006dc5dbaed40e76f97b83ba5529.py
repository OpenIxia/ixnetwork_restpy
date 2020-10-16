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


class PceDetailedRsvpSyncLspUpdateParams(Base):
    """PCE Learned LSPs Information Database
    The PceDetailedRsvpSyncLspUpdateParams class encapsulates a list of pceDetailedRsvpSyncLspUpdateParams resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceDetailedRsvpSyncLspUpdateParams.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceDetailedRsvpSyncLspUpdateParams'
    _SDM_ATT_MAP = {
        'Bandwidth': 'bandwidth',
        'BindingType': 'bindingType',
        'Bos': 'bos',
        'ConfigureBandwidth': 'configureBandwidth',
        'ConfigureEro': 'configureEro',
        'ConfigureLsp': 'configureLsp',
        'ConfigureLspa': 'configureLspa',
        'ConfigureMetric': 'configureMetric',
        'ExcludeAny': 'excludeAny',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IncludeConfiguredERO': 'includeConfiguredERO',
        'IncludeSrp': 'includeSrp',
        'IncludeSymbolicPathName': 'includeSymbolicPathName',
        'IncludeTEPathBindingTLV': 'includeTEPathBindingTLV',
        'IncludeXro': 'includeXro',
        'LocalProtection': 'localProtection',
        'MplsLabel': 'mplsLabel',
        'NumberOfEroSubObjects': 'numberOfEroSubObjects',
        'NumberOfMetricSubObjects': 'numberOfMetricSubObjects',
        'NumberOfXroSubObjects': 'numberOfXroSubObjects',
        'OverridePLSPID': 'overridePLSPID',
        'OverrideSrpId': 'overrideSrpId',
        'PceTriggersChoiceList': 'pceTriggersChoiceList',
        'PlspIdTriggerParam': 'plspIdTriggerParam',
        'SendEmptyTLV': 'sendEmptyTLV',
        'SetupPriority': 'setupPriority',
        'SrpId': 'srpId',
        'Srv6SID': 'srv6SID',
        'Tc': 'tc',
        'Ttl': 'ttl',
        'XroFailBit': 'xroFailBit',
    }

    def __init__(self, parent):
        super(PceDetailedRsvpSyncLspUpdateParams, self).__init__(parent)

    @property
    def PceUpdateRsvpEroSubObjectList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist_f72a62fe60fa1ddf919cc7fba7858d6e.PceUpdateRsvpEroSubObjectList): An instance of the PceUpdateRsvpEroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist_f72a62fe60fa1ddf919cc7fba7858d6e import PceUpdateRsvpEroSubObjectList
        return PceUpdateRsvpEroSubObjectList(self)

    @property
    def PceUpdateRsvpMetricSubObjectList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist_fd8fa1e77098fa6f4bc87b12a1ed3fcb.PceUpdateRsvpMetricSubObjectList): An instance of the PceUpdateRsvpMetricSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist_fd8fa1e77098fa6f4bc87b12a1ed3fcb import PceUpdateRsvpMetricSubObjectList
        return PceUpdateRsvpMetricSubObjectList(self)

    @property
    def PceUpdateXroSubObjectList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist_3cb16b2513bf72ff7ee4a5e0387625cf.PceUpdateXroSubObjectList): An instance of the PceUpdateXroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist_3cb16b2513bf72ff7ee4a5e0387625cf import PceUpdateXroSubObjectList
        return PceUpdateXroSubObjectList(self)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth (bps)
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
    def ConfigureBandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure Bandwidth
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureBandwidth']))

    @property
    def ConfigureEro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure ERO
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureEro']))

    @property
    def ConfigureLsp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureLsp']))

    @property
    def ConfigureLspa(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure LSPA
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureLspa']))

    @property
    def ConfigureMetric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureMetric']))

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
    def IncludeConfiguredERO(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If this is enabled, entire ERO will be go out in packet even if there is Binding SID, meaning no SR-ERO/SRv6-ERO validation will be done.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeConfiguredERO']))

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
    def IncludeSymbolicPathName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSymbolicPathName']))

    @property
    def IncludeTEPathBindingTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCUpate trigger message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTEPathBindingTLV']))

    @property
    def IncludeXro(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether XRO object will be included in a PcUpdate message. All other attributes in sub-tab Update XRO would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeXro']))

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
    def NumberOfMetricSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfMetricSubObjects'])
    @NumberOfMetricSubObjects.setter
    def NumberOfMetricSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfMetricSubObjects'], value)

    @property
    def NumberOfXroSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of XRO Sub Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfXroSubObjects'])
    @NumberOfXroSubObjects.setter
    def NumberOfXroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfXroSubObjects'], value)

    @property
    def OverridePLSPID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Allows the user to Send PcUpdate with an unknown PLSP-ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverridePLSPID']))

    @property
    def OverrideSrpId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideSrpId']))

    @property
    def PceTriggersChoiceList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PceTriggersChoiceList']))

    @property
    def PlspIdTriggerParam(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The value of PLSP-ID that should be put in the PcUpdate Message
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PlspIdTriggerParam']))

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
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Setup Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetupPriority']))

    @property
    def SrpId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrpId']))

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

    @property
    def XroFailBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): XRO Fail bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['XroFailBit']))

    def update(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, NumberOfXroSubObjects=None):
        """Updates pceDetailedRsvpSyncLspUpdateParams resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, NumberOfXroSubObjects=None):
        """Finds and retrieves pceDetailedRsvpSyncLspUpdateParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceDetailedRsvpSyncLspUpdateParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceDetailedRsvpSyncLspUpdateParams resources from the server.

        Args
        ----
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with matching pceDetailedRsvpSyncLspUpdateParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceDetailedRsvpSyncLspUpdateParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceDetailedRsvpSyncLspUpdateParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Bandwidth=None, BindingType=None, Bos=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeConfiguredERO=None, IncludeSrp=None, IncludeSymbolicPathName=None, IncludeTEPathBindingTLV=None, IncludeXro=None, LocalProtection=None, MplsLabel=None, OverridePLSPID=None, OverrideSrpId=None, PceTriggersChoiceList=None, PlspIdTriggerParam=None, SendEmptyTLV=None, SetupPriority=None, SrpId=None, Srv6SID=None, Tc=None, Ttl=None, XroFailBit=None):
        """Base class infrastructure that gets a list of pceDetailedRsvpSyncLspUpdateParams device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - ConfigureBandwidth (str): optional regex of configureBandwidth
        - ConfigureEro (str): optional regex of configureEro
        - ConfigureLsp (str): optional regex of configureLsp
        - ConfigureLspa (str): optional regex of configureLspa
        - ConfigureMetric (str): optional regex of configureMetric
        - ExcludeAny (str): optional regex of excludeAny
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathName (str): optional regex of includeSymbolicPathName
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - IncludeXro (str): optional regex of includeXro
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - OverridePLSPID (str): optional regex of overridePLSPID
        - OverrideSrpId (str): optional regex of overrideSrpId
        - PceTriggersChoiceList (str): optional regex of pceTriggersChoiceList
        - PlspIdTriggerParam (str): optional regex of plspIdTriggerParam
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - SrpId (str): optional regex of srpId
        - Srv6SID (str): optional regex of srv6SID
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl
        - XroFailBit (str): optional regex of xroFailBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def SendPcUpdate(self, *args, **kwargs):
        """Executes the sendPcUpdate operation on the server.

        Counts property changes created by the user.

        sendPcUpdate(Arg2=list)list
        ---------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPcUpdate', payload=payload, response_object=None)

    def SendReturnDelegation(self, *args, **kwargs):
        """Executes the sendReturnDelegation operation on the server.

        Counts property changes created by the user.

        sendReturnDelegation(Arg2=list)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendReturnDelegation', payload=payload, response_object=None)
