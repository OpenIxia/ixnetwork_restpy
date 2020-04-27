# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class IsisFlexAlgorithmList(Base):
    """ISIS Flex Algorithm
    The IsisFlexAlgorithmList class encapsulates a required isisFlexAlgorithmList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisFlexAlgorithmList'

    def __init__(self, parent):
        super(IsisFlexAlgorithmList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def AdvTwiceExcludeAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Exclude AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advTwiceExcludeAg'))

    @property
    def AdvTwiceIncludeAllAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Include-All AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advTwiceIncludeAllAg'))

    @property
    def AdvTwiceIncludeAnyAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Twice Include-Any AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advTwiceIncludeAnyAg'))

    @property
    def CalcType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calc Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('calcType'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def DontAdvInSrAlgo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Don't Adv. in SR Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dontAdvInSrAlgo'))

    @property
    def EnableExcludeAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Exclude Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableExcludeAg'))

    @property
    def EnableFadfTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled then following attributes will get enabled and ISIS Flexible Algorithm Definition Flags Sub-TLV or FADF sub-sub-TLV will be advertised with FAD Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableFadfTlv'))

    @property
    def EnableIncludeAllAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-All Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableIncludeAllAg'))

    @property
    def EnableIncludeAnyAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Flexible Algorithm Include-Any Admin Group Sub-Sub TLV will be advertised with FAD sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableIncludeAnyAg'))

    @property
    def ExcludeAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('excludeAgExtAg'))

    @property
    def ExcludeAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('excludeAgExtAgLen'))

    @property
    def FadfLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FADF AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fadfLen'))

    @property
    def FlexAlgo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flex Algo
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('flexAlgo'))

    @property
    def IncludeAllAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-All AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAllAgExtAg'))

    @property
    def IncludeAllAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAllAgExtAgLen'))

    @property
    def IncludeAnyAgExtAg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-Any AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAnyAgExtAg'))

    @property
    def IncludeAnyAgExtAgLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAnyAgExtAgLen'))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): M-Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mFlag'))

    @property
    def MetricType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('metricType'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('priority'))

    @property
    def ReservedBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('reservedBits'))

    def update(self, Name=None):
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
        return self._update(locals())

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
