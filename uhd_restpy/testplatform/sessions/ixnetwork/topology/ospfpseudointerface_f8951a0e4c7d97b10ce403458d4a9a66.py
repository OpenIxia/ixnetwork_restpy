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


class OspfPseudoInterface(Base):
    """Information for Simulated Router Interfaces
    The OspfPseudoInterface class encapsulates a list of ospfPseudoInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the OspfPseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfPseudoInterface'
    _SDM_ATT_MAP = {
        'AdjSID': 'adjSID',
        'AdministratorGroup': 'administratorGroup',
        'BFlag': 'bFlag',
        'BandwidthPriority0': 'bandwidthPriority0',
        'BandwidthPriority1': 'bandwidthPriority1',
        'BandwidthPriority2': 'bandwidthPriority2',
        'BandwidthPriority3': 'bandwidthPriority3',
        'BandwidthPriority4': 'bandwidthPriority4',
        'BandwidthPriority5': 'bandwidthPriority5',
        'BandwidthPriority6': 'bandwidthPriority6',
        'BandwidthPriority7': 'bandwidthPriority7',
        'Count': 'count',
        'Dedicated1Plus1': 'dedicated1Plus1',
        'Dedicated1To1': 'dedicated1To1',
        'DescriptiveName': 'descriptiveName',
        'EnLinkProtection': 'enLinkProtection',
        'Enable': 'enable',
        'EnableAdjSID': 'enableAdjSID',
        'EnableSRLG': 'enableSRLG',
        'Enhanced': 'enhanced',
        'ExtraTraffic': 'extraTraffic',
        'LFlag': 'lFlag',
        'MaxBandwidth': 'maxBandwidth',
        'MaxReservableBandwidth': 'maxReservableBandwidth',
        'Metric': 'metric',
        'MetricLevel': 'metricLevel',
        'Name': 'name',
        'PFlag': 'pFlag',
        'Reserved40': 'reserved40',
        'Reserved80': 'reserved80',
        'SFlag': 'sFlag',
        'Shared': 'shared',
        'SrlgCount': 'srlgCount',
        'Unprotected': 'unprotected',
        'VFlag': 'vFlag',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(OspfPseudoInterface, self).__init__(parent)

    @property
    def SrlgValueList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist_355b617a5f46ce90d800290d21158418.SrlgValueList): An instance of the SrlgValueList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist_355b617a5f46ce90d800290d21158418 import SrlgValueList
        return SrlgValueList(self)

    @property
    def AdjSID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Adjacency SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdjSID']))

    @property
    def AdministratorGroup(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Administrator Group
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroup']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Backup Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def BandwidthPriority0(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0']))

    @property
    def BandwidthPriority1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1']))

    @property
    def BandwidthPriority2(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2']))

    @property
    def BandwidthPriority3(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3']))

    @property
    def BandwidthPriority4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4']))

    @property
    def BandwidthPriority5(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5']))

    @property
    def BandwidthPriority6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6']))

    @property
    def BandwidthPriority7(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def Dedicated1Plus1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dedicated1Plus1']))

    @property
    def Dedicated1To1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dedicated1To1']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnLinkProtection(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This enables the link protection on the OSPF link between two mentioned interfaces.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnLinkProtection']))

    @property
    def Enable(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TE Enabled
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enable']))

    @property
    def EnableAdjSID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Adj SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAdjSID']))

    @property
    def EnableSRLG(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This enables the SRLG on the OSPF link between two mentioned interfaces.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSRLG']))

    @property
    def Enhanced(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enhanced']))

    @property
    def ExtraTraffic(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtraTraffic']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local/Global Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def MaxBandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth']))

    @property
    def MaxReservableBandwidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidth']))

    @property
    def Metric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Link Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric']))

    @property
    def MetricLevel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TE Metric Level
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevel']))

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
        - obj(uhd_restpy.multivalue.Multivalue): Persistent Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def Reserved40(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x40.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved40']))

    @property
    def Reserved80(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x80.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved80']))

    @property
    def SFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Set/Group Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def Shared(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Shared']))

    @property
    def SrlgCount(self):
        """
        Returns
        -------
        - number: This field value shows how many SRLG Value columns would be there in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlgCount'])
    @SrlgCount.setter
    def SrlgCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrlgCount'], value)

    @property
    def Unprotected(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unprotected']))

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value/Index Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None, SrlgCount=None):
        """Updates ospfPseudoInterface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, SrlgCount=None):
        """Finds and retrieves ospfPseudoInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoInterface resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns
        -------
        - self: This instance with matching ospfPseudoInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfPseudoInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfPseudoInterface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AdjSID=None, AdministratorGroup=None, BFlag=None, BandwidthPriority0=None, BandwidthPriority1=None, BandwidthPriority2=None, BandwidthPriority3=None, BandwidthPriority4=None, BandwidthPriority5=None, BandwidthPriority6=None, BandwidthPriority7=None, Dedicated1Plus1=None, Dedicated1To1=None, EnLinkProtection=None, Enable=None, EnableAdjSID=None, EnableSRLG=None, Enhanced=None, ExtraTraffic=None, LFlag=None, MaxBandwidth=None, MaxReservableBandwidth=None, Metric=None, MetricLevel=None, PFlag=None, Reserved40=None, Reserved80=None, SFlag=None, Shared=None, Unprotected=None, VFlag=None, Weight=None):
        """Base class infrastructure that gets a list of ospfPseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdjSID (str): optional regex of adjSID
        - AdministratorGroup (str): optional regex of administratorGroup
        - BFlag (str): optional regex of bFlag
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - Dedicated1Plus1 (str): optional regex of dedicated1Plus1
        - Dedicated1To1 (str): optional regex of dedicated1To1
        - EnLinkProtection (str): optional regex of enLinkProtection
        - Enable (str): optional regex of enable
        - EnableAdjSID (str): optional regex of enableAdjSID
        - EnableSRLG (str): optional regex of enableSRLG
        - Enhanced (str): optional regex of enhanced
        - ExtraTraffic (str): optional regex of extraTraffic
        - LFlag (str): optional regex of lFlag
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - Metric (str): optional regex of metric
        - MetricLevel (str): optional regex of metricLevel
        - PFlag (str): optional regex of pFlag
        - Reserved40 (str): optional regex of reserved40
        - Reserved80 (str): optional regex of reserved80
        - SFlag (str): optional regex of sFlag
        - Shared (str): optional regex of shared
        - Unprotected (str): optional regex of unprotected
        - VFlag (str): optional regex of vFlag
        - Weight (str): optional regex of weight

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

    def Disconnect(self, *args, **kwargs):
        """Executes the disconnect operation on the server.

        Disconnect Simulated Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        disconnect(SessionIndices=list)
        -------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        disconnect(SessionIndices=string)
        ---------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disconnect', payload=payload, response_object=None)

    def Reconnect(self, *args, **kwargs):
        """Executes the reconnect operation on the server.

        Reconnect Simulated Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        reconnect(SessionIndices=list)
        ------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        reconnect(SessionIndices=string)
        --------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('reconnect', payload=payload, response_object=None)

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
