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


class CfmCustomTLVList(Base):
    """
    The CfmCustomTLVList class encapsulates a list of cfmCustomTLVList resources that are managed by the system.
    A list of resources can be retrieved from the server using the CfmCustomTLVList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'cfmCustomTLVList'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'IncludeTLVinCCM': 'includeTLVinCCM',
        'IncludeTLVinLBM': 'includeTLVinLBM',
        'IncludeTLVinLBR': 'includeTLVinLBR',
        'IncludeTLVinLMM': 'includeTLVinLMM',
        'IncludeTLVinLMR': 'includeTLVinLMR',
        'IncludeTLVinLTM': 'includeTLVinLTM',
        'IncludeTLVinLTR': 'includeTLVinLTR',
        'Length': 'length',
        'Name': 'name',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(CfmCustomTLVList, self).__init__(parent)

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
    def IncludeTLVinCCM(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in CCM
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinCCM']))

    @property
    def IncludeTLVinLBM(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LBM
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLBM']))

    @property
    def IncludeTLVinLBR(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LBR
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLBR']))

    @property
    def IncludeTLVinLMM(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LMM
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLMM']))

    @property
    def IncludeTLVinLMR(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LMR
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLMR']))

    @property
    def IncludeTLVinLTM(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LTM
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLTM']))

    @property
    def IncludeTLVinLTR(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Custom TLV in LTR
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLTR']))

    @property
    def Length(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TLV Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

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
    def Type(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Value(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TLV Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Value']))

    def update(self, Name=None):
        """Updates cfmCustomTLVList resource on the server.

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
        """Finds and retrieves cfmCustomTLVList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cfmCustomTLVList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cfmCustomTLVList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching cfmCustomTLVList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cfmCustomTLVList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cfmCustomTLVList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, IncludeTLVinCCM=None, IncludeTLVinLBM=None, IncludeTLVinLBR=None, IncludeTLVinLMM=None, IncludeTLVinLMR=None, IncludeTLVinLTM=None, IncludeTLVinLTR=None, Length=None, Type=None, Value=None):
        """Base class infrastructure that gets a list of cfmCustomTLVList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - IncludeTLVinCCM (str): optional regex of includeTLVinCCM
        - IncludeTLVinLBM (str): optional regex of includeTLVinLBM
        - IncludeTLVinLBR (str): optional regex of includeTLVinLBR
        - IncludeTLVinLMM (str): optional regex of includeTLVinLMM
        - IncludeTLVinLMR (str): optional regex of includeTLVinLMR
        - IncludeTLVinLTM (str): optional regex of includeTLVinLTM
        - IncludeTLVinLTR (str): optional regex of includeTLVinLTR
        - Length (str): optional regex of length
        - Type (str): optional regex of type
        - Value (str): optional regex of value

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
