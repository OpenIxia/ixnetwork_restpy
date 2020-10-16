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


class IsisPseudoSRv6LocatorEntryList(Base):
    """ISIS SRv6 Locator Entry
    The IsisPseudoSRv6LocatorEntryList class encapsulates a required isisPseudoSRv6LocatorEntryList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoSRv6LocatorEntryList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseLocatorAsPrefix': 'advertiseLocatorAsPrefix',
        'Algorithm': 'algorithm',
        'Count': 'count',
        'DBit': 'dBit',
        'DescriptiveName': 'descriptiveName',
        'Locator': 'locator',
        'LocatorName': 'locatorName',
        'LocatorSize': 'locatorSize',
        'Metric': 'metric',
        'MtApplicabilityForIPv6Locator': 'mtApplicabilityForIPv6Locator',
        'MtId': 'mtId',
        'Name': 'name',
        'PrefixLength': 'prefixLength',
        'Redistribution': 'redistribution',
        'ReservedFlags': 'reservedFlags',
        'RouteMetric': 'routeMetric',
        'RouteOrigin': 'routeOrigin',
        'SidCount': 'sidCount',
    }

    def __init__(self, parent):
        super(IsisPseudoSRv6LocatorEntryList, self).__init__(parent)

    @property
    def IsisPseudoSRv6EndSIDList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6endsidlist_541f5f93c3d1828a205bdca154abe5ac.IsisPseudoSRv6EndSIDList): An instance of the IsisPseudoSRv6EndSIDList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6endsidlist_541f5f93c3d1828a205bdca154abe5ac import IsisPseudoSRv6EndSIDList
        return IsisPseudoSRv6EndSIDList(self)._select()

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
    def AdvertiseLocatorAsPrefix(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Locator as Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseLocatorAsPrefix']))

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
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DBit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): D Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBit']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Locator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Locator']))

    @property
    def LocatorName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorName']))

    @property
    def LocatorSize(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Size
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorSize']))

    @property
    def Metric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric']))

    @property
    def MtApplicabilityForIPv6Locator(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Multi-Topology Applicability for IPv6
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MtApplicabilityForIPv6Locator']))

    @property
    def MtId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MTID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MtId']))

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
    def PrefixLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prefix Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def Redistribution(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Redistribution
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Redistribution']))

    @property
    def ReservedFlags(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved (Flags)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedFlags']))

    @property
    def RouteMetric(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteMetric']))

    @property
    def RouteOrigin(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteOrigin']))

    @property
    def SidCount(self):
        """
        Returns
        -------
        - number: SID Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SidCount'])
    @SidCount.setter
    def SidCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SidCount'], value)

    def update(self, Name=None, SidCount=None):
        """Updates isisPseudoSRv6LocatorEntryList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SidCount (number): SID Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseLocatorAsPrefix=None, Algorithm=None, DBit=None, Locator=None, LocatorName=None, LocatorSize=None, Metric=None, MtApplicabilityForIPv6Locator=None, MtId=None, PrefixLength=None, Redistribution=None, ReservedFlags=None, RouteMetric=None, RouteOrigin=None):
        """Base class infrastructure that gets a list of isisPseudoSRv6LocatorEntryList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseLocatorAsPrefix (str): optional regex of advertiseLocatorAsPrefix
        - Algorithm (str): optional regex of algorithm
        - DBit (str): optional regex of dBit
        - Locator (str): optional regex of locator
        - LocatorName (str): optional regex of locatorName
        - LocatorSize (str): optional regex of locatorSize
        - Metric (str): optional regex of metric
        - MtApplicabilityForIPv6Locator (str): optional regex of mtApplicabilityForIPv6Locator
        - MtId (str): optional regex of mtId
        - PrefixLength (str): optional regex of prefixLength
        - Redistribution (str): optional regex of redistribution
        - ReservedFlags (str): optional regex of reservedFlags
        - RouteMetric (str): optional regex of routeMetric
        - RouteOrigin (str): optional regex of routeOrigin

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
