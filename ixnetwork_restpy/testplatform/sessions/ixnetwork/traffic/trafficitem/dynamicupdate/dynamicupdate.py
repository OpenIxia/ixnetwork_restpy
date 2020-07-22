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


class DynamicUpdate(Base):
    """Contains attributes that help IxNetwork update the corresponding traffic packet labels on the fly based on the information from the configured protocol.
    The DynamicUpdate class encapsulates a list of dynamicUpdate resources that are managed by the system.
    A list of resources can be retrieved from the server using the DynamicUpdate.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'dynamicUpdate'
    _SDM_ATT_MAP = {
        'AvailableDynamicUpdateFields': 'availableDynamicUpdateFields',
        'AvailableSessionAwareTrafficFields': 'availableSessionAwareTrafficFields',
        'EnabledDynamicUpdateFields': 'enabledDynamicUpdateFields',
        'EnabledDynamicUpdateFieldsDisplayNames': 'enabledDynamicUpdateFieldsDisplayNames',
        'EnabledSessionAwareTrafficFields': 'enabledSessionAwareTrafficFields',
    }

    def __init__(self, parent):
        super(DynamicUpdate, self).__init__(parent)

    @property
    def AvailableDynamicUpdateFields(self):
        """
        Returns
        -------
        - list(str): (Read only) Specifies the available Dynamic Updates support.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableDynamicUpdateFields'])

    @property
    def AvailableSessionAwareTrafficFields(self):
        """
        Returns
        -------
        - list(str): (Read only) Specifies the available Kill Bit support.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSessionAwareTrafficFields'])

    @property
    def EnabledDynamicUpdateFields(self):
        """
        Returns
        -------
        - list(str): If true, enables the Dynamic Updates support.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledDynamicUpdateFields'])
    @EnabledDynamicUpdateFields.setter
    def EnabledDynamicUpdateFields(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledDynamicUpdateFields'], value)

    @property
    def EnabledDynamicUpdateFieldsDisplayNames(self):
        """
        Returns
        -------
        - list(str): Returns user friendly list of dynamic update fields
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledDynamicUpdateFieldsDisplayNames'])

    @property
    def EnabledSessionAwareTrafficFields(self):
        """
        Returns
        -------
        - list(str): If true, enables the Kill Bit support.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledSessionAwareTrafficFields'])
    @EnabledSessionAwareTrafficFields.setter
    def EnabledSessionAwareTrafficFields(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledSessionAwareTrafficFields'], value)

    def update(self, EnabledDynamicUpdateFields=None, EnabledSessionAwareTrafficFields=None):
        """Updates dynamicUpdate resource on the server.

        Args
        ----
        - EnabledDynamicUpdateFields (list(str)): If true, enables the Dynamic Updates support.
        - EnabledSessionAwareTrafficFields (list(str)): If true, enables the Kill Bit support.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableDynamicUpdateFields=None, AvailableSessionAwareTrafficFields=None, EnabledDynamicUpdateFields=None, EnabledDynamicUpdateFieldsDisplayNames=None, EnabledSessionAwareTrafficFields=None):
        """Finds and retrieves dynamicUpdate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dynamicUpdate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dynamicUpdate resources from the server.

        Args
        ----
        - AvailableDynamicUpdateFields (list(str)): (Read only) Specifies the available Dynamic Updates support.
        - AvailableSessionAwareTrafficFields (list(str)): (Read only) Specifies the available Kill Bit support.
        - EnabledDynamicUpdateFields (list(str)): If true, enables the Dynamic Updates support.
        - EnabledDynamicUpdateFieldsDisplayNames (list(str)): Returns user friendly list of dynamic update fields
        - EnabledSessionAwareTrafficFields (list(str)): If true, enables the Kill Bit support.

        Returns
        -------
        - self: This instance with matching dynamicUpdate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dynamicUpdate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dynamicUpdate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
