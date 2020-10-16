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


class IsisPseudoSRv6EndSIDList(Base):
    """ISIS SRv6 End SID
    The IsisPseudoSRv6EndSIDList class encapsulates a required isisPseudoSRv6EndSIDList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoSRv6EndSIDList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseCustomSubTLV': 'advertiseCustomSubTLV',
        'ArgumentLength': 'argumentLength',
        'Count': 'count',
        'CustomEndPointFunction': 'customEndPointFunction',
        'CustomSubTlv': 'customSubTlv',
        'DescriptiveName': 'descriptiveName',
        'EndPointFunction': 'endPointFunction',
        'Flags': 'flags',
        'FunctionLength': 'functionLength',
        'IncludeSRv6SIDStructureSubSubTlv': 'includeSRv6SIDStructureSubSubTlv',
        'LocatorBlockLength': 'locatorBlockLength',
        'LocatorName': 'locatorName',
        'LocatorNodeLength': 'locatorNodeLength',
        'Name': 'name',
        'Sid': 'sid',
        'SidName': 'sidName',
    }

    def __init__(self, parent):
        super(IsisPseudoSRv6EndSIDList, self).__init__(parent)

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
    def AdvertiseCustomSubTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseCustomSubTLV']))

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
    def CustomSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomSubTlv']))

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
    def Flags(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Flags
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

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
    def IncludeSRv6SIDStructureSubSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubSubTlv']))

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
    def LocatorName(self):
        """
        Returns
        -------
        - list(str): Locator Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocatorName'])

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
    def Sid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sid']))

    @property
    def SidName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SID Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidName']))

    def update(self, Name=None):
        """Updates isisPseudoSRv6EndSIDList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseCustomSubTLV=None, ArgumentLength=None, CustomEndPointFunction=None, CustomSubTlv=None, EndPointFunction=None, Flags=None, FunctionLength=None, IncludeSRv6SIDStructureSubSubTlv=None, LocatorBlockLength=None, LocatorNodeLength=None, Sid=None, SidName=None):
        """Base class infrastructure that gets a list of isisPseudoSRv6EndSIDList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseCustomSubTLV (str): optional regex of advertiseCustomSubTLV
        - ArgumentLength (str): optional regex of argumentLength
        - CustomEndPointFunction (str): optional regex of customEndPointFunction
        - CustomSubTlv (str): optional regex of customSubTlv
        - EndPointFunction (str): optional regex of endPointFunction
        - Flags (str): optional regex of flags
        - FunctionLength (str): optional regex of functionLength
        - IncludeSRv6SIDStructureSubSubTlv (str): optional regex of includeSRv6SIDStructureSubSubTlv
        - LocatorBlockLength (str): optional regex of locatorBlockLength
        - LocatorNodeLength (str): optional regex of locatorNodeLength
        - Sid (str): optional regex of sid
        - SidName (str): optional regex of sidName

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
