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


class Bands(Base):
    """Openflow Controller Bands Configuration
    The Bands class encapsulates a list of bands resources that are managed by the system.
    A list of resources can be retrieved from the server using the Bands.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'bands'
    _SDM_ATT_MAP = {
        'BandDescription': 'bandDescription',
        'BandType': 'bandType',
        'BurstSize': 'burstSize',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Experimenter': 'experimenter',
        'MeterIndex': 'meterIndex',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'PrecedenceLevel': 'precedenceLevel',
        'Rate': 'rate',
    }

    def __init__(self, parent):
        super(Bands, self).__init__(parent)

    @property
    def BandDescription(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the Meter. It is a read-only field.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandDescription']))

    @property
    def BandType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the band type from the list. Options are as follows: 1) Drop 2) DSCP Remark 3) Experimenter
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandType']))

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BurstSize']))

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
    def Experimenter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicats the experimenter ID. The default value is 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Experimenter']))

    @property
    def MeterIndex(self):
        """
        Returns
        -------
        - list(str): Indicats the Parent Meter Index
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterIndex'])

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def PrecedenceLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrecedenceLevel']))

    @property
    def Rate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This indicates the rate value above which the corresponding band may apply to packets. The default value is 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Rate']))

    def update(self, Multiplier=None, Name=None):
        """Updates bands resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, MeterIndex=None, Multiplier=None, Name=None):
        """Finds and retrieves bands resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bands resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bands resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - MeterIndex (list(str)): Indicats the Parent Meter Index
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching bands resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bands data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bands resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BandDescription=None, BandType=None, BurstSize=None, Experimenter=None, PrecedenceLevel=None, Rate=None):
        """Base class infrastructure that gets a list of bands device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BandDescription (str): optional regex of bandDescription
        - BandType (str): optional regex of bandType
        - BurstSize (str): optional regex of burstSize
        - Experimenter (str): optional regex of experimenter
        - PrecedenceLevel (str): optional regex of precedenceLevel
        - Rate (str): optional regex of rate

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
