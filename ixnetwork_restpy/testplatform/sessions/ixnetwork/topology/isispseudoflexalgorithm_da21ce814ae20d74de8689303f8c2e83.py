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


class IsisPseudoFlexAlgorithm(Base):
    """ISIS Pseudo Flex Algorithm
    The IsisPseudoFlexAlgorithm class encapsulates a required isisPseudoFlexAlgorithm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoFlexAlgorithm'
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

    def __init__(self, parent):
        super(IsisPseudoFlexAlgorithm, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvTwiceExcludeAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Exclude AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceExcludeAg']))

    @property
    def AdvTwiceIncludeAllAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Include-All AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceIncludeAllAg']))

    @property
    def AdvTwiceIncludeAnyAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Include-Any AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvTwiceIncludeAnyAg']))

    @property
    def CalcType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calc Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CalcType']))

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
    def DontAdvInSrAlgo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Don't Adv. in SR Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DontAdvInSrAlgo']))

    @property
    def EnableExcludeAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Exclude Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExcludeAg']))

    @property
    def EnableFadfTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled then following attributes will get enabled and ISIS Flexible Algorithm Definition Flags Sub-TLV or FADF sub-sub-TLV will be advertised with FAD Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFadfTlv']))

    @property
    def EnableIncludeAllAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-All Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAllAg']))

    @property
    def EnableIncludeAnyAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-Any Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAnyAg']))

    @property
    def ExcludeAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAg']))

    @property
    def ExcludeAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAgLen']))

    @property
    def FadfLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FADF AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadfLen']))

    @property
    def FlexAlgo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flex Algo
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlexAlgo']))

    @property
    def IncludeAllAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-All AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAg']))

    @property
    def IncludeAllAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAgLen']))

    @property
    def IncludeAnyAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-Any AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAg']))

    @property
    def IncludeAnyAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAgLen']))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): M-Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def MetricType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricType']))

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
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def ReservedBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedBits']))

    def update(self, Name=None):
        """Updates isisPseudoFlexAlgorithm resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AdvTwiceExcludeAg=None, AdvTwiceIncludeAllAg=None, AdvTwiceIncludeAnyAg=None, CalcType=None, DontAdvInSrAlgo=None, EnableExcludeAg=None, EnableFadfTlv=None, EnableIncludeAllAg=None, EnableIncludeAnyAg=None, ExcludeAgExtAg=None, ExcludeAgExtAgLen=None, FadfLen=None, FlexAlgo=None, IncludeAllAgExtAg=None, IncludeAllAgExtAgLen=None, IncludeAnyAgExtAg=None, IncludeAnyAgExtAgLen=None, MFlag=None, MetricType=None, Priority=None, ReservedBits=None):
        """Base class infrastructure that gets a list of isisPseudoFlexAlgorithm device ids encapsulated by this object.

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
