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


class Parameter(Base):
    """This specifies the parameter related properties.
    The Parameter class encapsulates a list of parameter resources that are managed by the system.
    A list of resources can be retrieved from the server using the Parameter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'parameter'
    _SDM_ATT_MAP = {
        'DisplayValue': 'displayValue',
        'Option': 'option',
        'SupportedOptions': 'supportedOptions',
    }

    def __init__(self, parent):
        super(Parameter, self).__init__(parent)

    @property
    def Bool(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.bool.bool.Bool): An instance of the Bool class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.bool.bool import Bool
        return Bool(self)

    @property
    def Choice(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.choice.choice.Choice): An instance of the Choice class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.choice.choice import Choice
        return Choice(self)

    @property
    def Hex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.hex.hex.Hex): An instance of the Hex class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.hex.hex import Hex
        return Hex(self)

    @property
    def Number(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.number.number.Number): An instance of the Number class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.number.number import Number
        return Number(self)

    @property
    def Range(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.range.range.Range): An instance of the Range class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.range.range import Range
        return Range(self)

    @property
    def String(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.string.string.String): An instance of the String class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.string.string import String
        return String(self)

    @property
    def DisplayValue(self):
        """
        Returns
        -------
        - str: Current parameter UI Display Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayValue'])

    @property
    def Option(self):
        """
        Returns
        -------
        - str(choice | range | value): Each parameter has one or multiple options. Runtime supported options for specific parameter can be retrieved from supportedOptions attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP['Option'])
    @Option.setter
    def Option(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Option'], value)

    @property
    def SupportedOptions(self):
        """
        Returns
        -------
        - list(str[choice | range | value]): Runtime supported options for a specific parameter
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedOptions'])

    def update(self, Option=None):
        """Updates parameter resource on the server.

        Args
        ----
        - Option (str(choice | range | value)): Each parameter has one or multiple options. Runtime supported options for specific parameter can be retrieved from supportedOptions attribute

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, DisplayValue=None, Option=None, SupportedOptions=None):
        """Finds and retrieves parameter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve parameter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all parameter resources from the server.

        Args
        ----
        - DisplayValue (str): Current parameter UI Display Value
        - Option (str(choice | range | value)): Each parameter has one or multiple options. Runtime supported options for specific parameter can be retrieved from supportedOptions attribute
        - SupportedOptions (list(str[choice | range | value])): Runtime supported options for a specific parameter

        Returns
        -------
        - self: This instance with matching parameter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of parameter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the parameter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
