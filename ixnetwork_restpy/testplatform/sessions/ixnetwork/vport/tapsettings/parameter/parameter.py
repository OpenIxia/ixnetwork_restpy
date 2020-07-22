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
    """
    The Parameter class encapsulates a list of parameter resources that are managed by the system.
    A list of resources can be retrieved from the server using the Parameter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'parameter'
    _SDM_ATT_MAP = {
        'AvailableChoices': 'availableChoices',
        'CurrentValue': 'currentValue',
        'CustomDefaultValue': 'customDefaultValue',
        'DefaultValue': 'defaultValue',
        'IsReadOnly': 'isReadOnly',
        'MaxValue': 'maxValue',
        'MinValue': 'minValue',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(Parameter, self).__init__(parent)

    @property
    def AvailableChoices(self):
        """
        Returns
        -------
        - list(str): Available Choices
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableChoices'])

    @property
    def CurrentValue(self):
        """
        Returns
        -------
        - str: Parameter UI Display Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentValue'])
    @CurrentValue.setter
    def CurrentValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CurrentValue'], value)

    @property
    def CustomDefaultValue(self):
        """
        Returns
        -------
        - str: Parameter Custom Default Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomDefaultValue'])

    @property
    def DefaultValue(self):
        """
        Returns
        -------
        - str: Parameter Default Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultValue'])

    @property
    def IsReadOnly(self):
        """
        Returns
        -------
        - bool: Parameter value type
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsReadOnly'])

    @property
    def MaxValue(self):
        """
        Returns
        -------
        - str: Parameter Maximum Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])

    @property
    def MinValue(self):
        """
        Returns
        -------
        - str: Parameter Minimum Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Parameter Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    def update(self, CurrentValue=None):
        """Updates parameter resource on the server.

        Args
        ----
        - CurrentValue (str): Parameter UI Display Value

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableChoices=None, CurrentValue=None, CustomDefaultValue=None, DefaultValue=None, IsReadOnly=None, MaxValue=None, MinValue=None, Name=None):
        """Finds and retrieves parameter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve parameter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all parameter resources from the server.

        Args
        ----
        - AvailableChoices (list(str)): Available Choices
        - CurrentValue (str): Parameter UI Display Value
        - CustomDefaultValue (str): Parameter Custom Default Value
        - DefaultValue (str): Parameter Default Value
        - IsReadOnly (bool): Parameter value type
        - MaxValue (str): Parameter Maximum Value
        - MinValue (str): Parameter Minimum Value
        - Name (str): Parameter Name.

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
