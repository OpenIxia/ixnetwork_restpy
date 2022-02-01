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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class IsisFlexAlgorithmList(Base):
    """ISIS Flex Algorithm
    The IsisFlexAlgorithmList class encapsulates a required isisFlexAlgorithmList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisFlexAlgorithmList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvTwiceExcludeAg': 'advTwiceExcludeAg',
        'AdvTwiceIncludeAllAg': 'advTwiceIncludeAllAg',
        'AdvTwiceIncludeAnyAg': 'advTwiceIncludeAnyAg',
        'CalcType': 'calcType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DontAdvInSrAlgo': 'dontAdvInSrAlgo',
        'EnableExcludeAg': 'enableExcludeAg',
        'EnableFadfTlv': 'enableFadfTlv',
        'EnableIncludeAllAg': 'enableIncludeAllAg',
        'EnableIncludeAnyAg': 'enableIncludeAnyAg',
        'ExcludeAgExtAg': 'excludeAgExtAg',
        'ExcludeAgExtAgLen': 'excludeAgExtAgLen',
        'FadfLen': 'fadfLen',
        'FlexAlgo': 'flexAlgo',
        'IncludeAllAgExtAg': 'includeAllAgExtAg',
        'IncludeAllAgExtAgLen': 'includeAllAgExtAgLen',
        'IncludeAnyAgExtAg': 'includeAnyAgExtAg',
        'IncludeAnyAgExtAgLen': 'includeAnyAgExtAgLen',
        'MFlag': 'mFlag',
        'MetricType': 'metricType',
        'Name': 'name',
        'Priority': 'priority',
        'ReservedBits': 'reservedBits',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(IsisFlexAlgorithmList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvTwiceExcludeAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Twice Exclude AG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceExcludeAg']))

    @property
    def AdvTwiceIncludeAllAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Twice Include-All AG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceIncludeAllAg']))

    @property
    def AdvTwiceIncludeAnyAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Twice Include-Any AG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceIncludeAnyAg']))

    @property
    def CalcType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Calc Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CalcType']))

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
    def DontAdvInSrAlgo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Don't Adv. in SR Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DontAdvInSrAlgo']))

    @property
    def EnableExcludeAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Exclude Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExcludeAg']))

    @property
    def EnableFadfTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled then following attributes will get enabled and ISIS Flexible Algorithm Definition Flags Sub-TLV or FADF sub-sub-TLV will be advertised with FAD Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFadfTlv']))

    @property
    def EnableIncludeAllAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-All Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAllAg']))

    @property
    def EnableIncludeAnyAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-Any Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAnyAg']))

    @property
    def ExcludeAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAg']))

    @property
    def ExcludeAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext AG Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAgLen']))

    @property
    def FadfLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FADF AG Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadfLen']))

    @property
    def FlexAlgo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flex Algo
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlexAlgo']))

    @property
    def IncludeAllAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext Include-All AG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAg']))

    @property
    def IncludeAllAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext AG Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAgLen']))

    @property
    def IncludeAnyAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext Include-Any AG
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAg']))

    @property
    def IncludeAnyAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Ext AG Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAgLen']))

    @property
    def MFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): M-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def MetricType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Metric Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricType']))

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
    def Priority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def ReservedBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedBits']))

    def update(self, Name=None):
        # type: (str) -> IsisFlexAlgorithmList
        """Updates isisFlexAlgorithmList resource on the server.

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
        # type: (int, str, str) -> IsisFlexAlgorithmList
        """Finds and retrieves isisFlexAlgorithmList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisFlexAlgorithmList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisFlexAlgorithmList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisFlexAlgorithmList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisFlexAlgorithmList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisFlexAlgorithmList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdvTwiceExcludeAg=None, AdvTwiceIncludeAllAg=None, AdvTwiceIncludeAnyAg=None, CalcType=None, DontAdvInSrAlgo=None, EnableExcludeAg=None, EnableFadfTlv=None, EnableIncludeAllAg=None, EnableIncludeAnyAg=None, ExcludeAgExtAg=None, ExcludeAgExtAgLen=None, FadfLen=None, FlexAlgo=None, IncludeAllAgExtAg=None, IncludeAllAgExtAgLen=None, IncludeAnyAgExtAg=None, IncludeAnyAgExtAgLen=None, MFlag=None, MetricType=None, Priority=None, ReservedBits=None):
        """Base class infrastructure that gets a list of isisFlexAlgorithmList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvTwiceExcludeAg (str): optional regex of advTwiceExcludeAg
        - AdvTwiceIncludeAllAg (str): optional regex of advTwiceIncludeAllAg
        - AdvTwiceIncludeAnyAg (str): optional regex of advTwiceIncludeAnyAg
        - CalcType (str): optional regex of calcType
        - DontAdvInSrAlgo (str): optional regex of dontAdvInSrAlgo
        - EnableExcludeAg (str): optional regex of enableExcludeAg
        - EnableFadfTlv (str): optional regex of enableFadfTlv
        - EnableIncludeAllAg (str): optional regex of enableIncludeAllAg
        - EnableIncludeAnyAg (str): optional regex of enableIncludeAnyAg
        - ExcludeAgExtAg (str): optional regex of excludeAgExtAg
        - ExcludeAgExtAgLen (str): optional regex of excludeAgExtAgLen
        - FadfLen (str): optional regex of fadfLen
        - FlexAlgo (str): optional regex of flexAlgo
        - IncludeAllAgExtAg (str): optional regex of includeAllAgExtAg
        - IncludeAllAgExtAgLen (str): optional regex of includeAllAgExtAgLen
        - IncludeAnyAgExtAg (str): optional regex of includeAnyAgExtAg
        - IncludeAnyAgExtAgLen (str): optional regex of includeAnyAgExtAgLen
        - MFlag (str): optional regex of mFlag
        - MetricType (str): optional regex of metricType
        - Priority (str): optional regex of priority
        - ReservedBits (str): optional regex of reservedBits

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
