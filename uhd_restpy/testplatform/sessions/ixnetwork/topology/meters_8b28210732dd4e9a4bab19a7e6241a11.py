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


class Meters(Base):
    """Openflow Meter Configuration
    The Meters class encapsulates a list of meters resources that are managed by the system.
    A list of resources can be retrieved from the server using the Meters.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'meters'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Advertise': 'advertise',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Flags': 'flags',
        'MeterDesc': 'meterDesc',
        'MeterId': 'meterId',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfBands': 'numberOfBands',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Meters, self).__init__(parent, list_op)

    @property
    def Bands(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bands_392f44cb40ca53ad5e0fc665cc14dea3.Bands): An instance of the Bands class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bands_392f44cb40ca53ad5e0fc665cc14dea3 import Bands
        if len(self._object_properties) > 0:
            if self._properties.get('Bands', None) is not None:
                return self._properties.get('Bands')
        return Bands(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Advertise(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): When this check box is cleared, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is selected or cleared.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Advertise']))

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
    def Flags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Select the meter configuration flags from the list.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def MeterDesc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A description of the meter
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MeterDesc']))

    @property
    def MeterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The value by which a meter is uniquely identified .
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MeterId']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def NumberOfBands(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the number of Bands.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBands'])
    @NumberOfBands.setter
    def NumberOfBands(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBands'], value)

    def update(self, Multiplier=None, Name=None, NumberOfBands=None):
        # type: (int, str, int) -> Meters
        """Updates meters resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBands (number): Specify the number of Bands.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Multiplier=None, Name=None, NumberOfBands=None):
        # type: (int, str, int) -> Meters
        """Adds a new meters resource on the json, only valid with batch add utility

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBands (number): Specify the number of Bands.

        Returns
        -------
        - self: This instance with all currently retrieved meters resources using find and the newly added meters resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Multiplier=None, Name=None, NumberOfBands=None):
        # type: (int, str, int, str, int) -> Meters
        """Finds and retrieves meters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve meters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all meters resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBands (number): Specify the number of Bands.

        Returns
        -------
        - self: This instance with matching meters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of meters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the meters resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SendAllMeterAdd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendAllMeterAdd operation on the server.

        Sends a Meter Add on all meters.

        sendAllMeterAdd(async_operation=bool)list
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendAllMeterAdd', payload=payload, response_object=None)

    def SendAllMeterRemove(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendAllMeterRemove operation on the server.

        Sends a Meter Remove on all meters.

        sendAllMeterRemove(async_operation=bool)list
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendAllMeterRemove', payload=payload, response_object=None)

    def SendMeterAdd(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendMeterAdd operation on the server.

        Sends a Meter Add on selected Meter.

        sendMeterAdd(Arg2=list, async_operation=bool)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the meter range grid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendMeterAdd', payload=payload, response_object=None)

    def SendMeterRemove(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendMeterRemove operation on the server.

        Sends a Meter Remove on selected Meter.

        sendMeterRemove(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the meter range grid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendMeterRemove', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, Advertise=None, Flags=None, MeterDesc=None, MeterId=None):
        """Base class infrastructure that gets a list of meters device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Advertise (str): optional regex of advertise
        - Flags (str): optional regex of flags
        - MeterDesc (str): optional regex of meterDesc
        - MeterId (str): optional regex of meterId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
