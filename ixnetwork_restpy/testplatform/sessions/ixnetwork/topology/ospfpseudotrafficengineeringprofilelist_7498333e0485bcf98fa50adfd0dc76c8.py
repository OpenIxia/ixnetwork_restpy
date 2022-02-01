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


class OspfPseudoTrafficEngineeringProfileList(Base):
    """OSPF Traffic Engineering Profiles
    The OspfPseudoTrafficEngineeringProfileList class encapsulates a required ospfPseudoTrafficEngineeringProfileList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfPseudoTrafficEngineeringProfileList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActiveTo': 'activeTo',
        'AdministratorGroup': 'administratorGroup',
        'AdministratorGroupTo': 'administratorGroupTo',
        'AdvertiseExtAdminGroup': 'advertiseExtAdminGroup',
        'BandwidthPriority0': 'bandwidthPriority0',
        'BandwidthPriority0To': 'bandwidthPriority0To',
        'BandwidthPriority1': 'bandwidthPriority1',
        'BandwidthPriority1To': 'bandwidthPriority1To',
        'BandwidthPriority2': 'bandwidthPriority2',
        'BandwidthPriority2To': 'bandwidthPriority2To',
        'BandwidthPriority3': 'bandwidthPriority3',
        'BandwidthPriority3To': 'bandwidthPriority3To',
        'BandwidthPriority4': 'bandwidthPriority4',
        'BandwidthPriority4To': 'bandwidthPriority4To',
        'BandwidthPriority5': 'bandwidthPriority5',
        'BandwidthPriority5To': 'bandwidthPriority5To',
        'BandwidthPriority6': 'bandwidthPriority6',
        'BandwidthPriority6To': 'bandwidthPriority6To',
        'BandwidthPriority7': 'bandwidthPriority7',
        'BandwidthPriority7To': 'bandwidthPriority7To',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'ExtAdminGroup': 'extAdminGroup',
        'ExtAdminGroupLength': 'extAdminGroupLength',
        'MaxBandwidth': 'maxBandwidth',
        'MaxBandwidthTo': 'maxBandwidthTo',
        'MaxReservableBandwidth': 'maxReservableBandwidth',
        'MaxReservableBandwidthTo': 'maxReservableBandwidthTo',
        'MetricLevel': 'metricLevel',
        'MetricLevelTo': 'metricLevelTo',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OspfPseudoTrafficEngineeringProfileList, self).__init__(parent, list_op)

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE To-Node Enable/Disable.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveTo']))

    @property
    def AdministratorGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Administrator Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroup']))

    @property
    def AdministratorGroupTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Administrator Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroupTo']))

    @property
    def AdvertiseExtAdminGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Advertise Ext Admin Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseExtAdminGroup']))

    @property
    def BandwidthPriority0(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 0 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0']))

    @property
    def BandwidthPriority0To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 0 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0To']))

    @property
    def BandwidthPriority1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 1 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1']))

    @property
    def BandwidthPriority1To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 1 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1To']))

    @property
    def BandwidthPriority2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 2 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2']))

    @property
    def BandwidthPriority2To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 2 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2To']))

    @property
    def BandwidthPriority3(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 3 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3']))

    @property
    def BandwidthPriority3To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 3 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3To']))

    @property
    def BandwidthPriority4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 4 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4']))

    @property
    def BandwidthPriority4To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 4 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4To']))

    @property
    def BandwidthPriority5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 5 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5']))

    @property
    def BandwidthPriority5To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 5 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5To']))

    @property
    def BandwidthPriority6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 6 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6']))

    @property
    def BandwidthPriority6To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 6 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6To']))

    @property
    def BandwidthPriority7(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 7 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7']))

    @property
    def BandwidthPriority7To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 7 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7To']))

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
    def ExtAdminGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Ext Admin Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroup']))

    @property
    def ExtAdminGroupLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Ext Admin Group Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroupLength']))

    @property
    def MaxBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Maximum Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth']))

    @property
    def MaxBandwidthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidthTo']))

    @property
    def MaxReservableBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Maximum Reservable Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidth']))

    @property
    def MaxReservableBandwidthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Reservable Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidthTo']))

    @property
    def MetricLevel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, TE Metric Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevel']))

    @property
    def MetricLevelTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, TE Metric Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevelTo']))

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

    def update(self, Name=None):
        # type: (str) -> OspfPseudoTrafficEngineeringProfileList
        """Updates ospfPseudoTrafficEngineeringProfileList resource on the server.

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
        # type: (int, str, str) -> OspfPseudoTrafficEngineeringProfileList
        """Finds and retrieves ospfPseudoTrafficEngineeringProfileList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoTrafficEngineeringProfileList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoTrafficEngineeringProfileList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching ospfPseudoTrafficEngineeringProfileList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfPseudoTrafficEngineeringProfileList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfPseudoTrafficEngineeringProfileList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def get_device_ids(self, PortNames=None, Active=None, ActiveTo=None, AdministratorGroup=None, AdministratorGroupTo=None, AdvertiseExtAdminGroup=None, BandwidthPriority0=None, BandwidthPriority0To=None, BandwidthPriority1=None, BandwidthPriority1To=None, BandwidthPriority2=None, BandwidthPriority2To=None, BandwidthPriority3=None, BandwidthPriority3To=None, BandwidthPriority4=None, BandwidthPriority4To=None, BandwidthPriority5=None, BandwidthPriority5To=None, BandwidthPriority6=None, BandwidthPriority6To=None, BandwidthPriority7=None, BandwidthPriority7To=None, ExtAdminGroup=None, ExtAdminGroupLength=None, MaxBandwidth=None, MaxBandwidthTo=None, MaxReservableBandwidth=None, MaxReservableBandwidthTo=None, MetricLevel=None, MetricLevelTo=None):
        """Base class infrastructure that gets a list of ospfPseudoTrafficEngineeringProfileList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTo (str): optional regex of activeTo
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdministratorGroupTo (str): optional regex of administratorGroupTo
        - AdvertiseExtAdminGroup (str): optional regex of advertiseExtAdminGroup
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority0To (str): optional regex of bandwidthPriority0To
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority1To (str): optional regex of bandwidthPriority1To
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority2To (str): optional regex of bandwidthPriority2To
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority3To (str): optional regex of bandwidthPriority3To
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority4To (str): optional regex of bandwidthPriority4To
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority5To (str): optional regex of bandwidthPriority5To
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority6To (str): optional regex of bandwidthPriority6To
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - BandwidthPriority7To (str): optional regex of bandwidthPriority7To
        - ExtAdminGroup (str): optional regex of extAdminGroup
        - ExtAdminGroupLength (str): optional regex of extAdminGroupLength
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxBandwidthTo (str): optional regex of maxBandwidthTo
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MaxReservableBandwidthTo (str): optional regex of maxReservableBandwidthTo
        - MetricLevel (str): optional regex of metricLevel
        - MetricLevelTo (str): optional regex of metricLevelTo

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
