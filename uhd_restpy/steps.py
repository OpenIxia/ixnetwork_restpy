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
from uhd_restpy.base import Base


class Steps(Base):
    """List of all possible steps for this multivalue
    """
    _SDM_NAME = 'nest'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'Step': 'step',
        'Owner': 'owner',
        'Description': 'description'
    }

    def __init__(self, parent):
        super(Steps, self).__init__(parent)

    @property
    def Description(self):
        """The description of this step

        Returns
        -------
        - str: The description of the step
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def Owner(self):
        """The owner of this step

        Returns
        -------
        - str: The href of the owner
        """
        return self._get_attribute(self._SDM_ATT_MAP['Owner'])

    @property
    def Enabled(self):
        """Enable/disable the step

        Returns
        -------
        - bool: Enable the step or disable the step
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, enabled):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], enabled)

    @property
    def Step(self):
        """The value of the step. This value must be in the same format as the parent multivalue

        Returns
        -------
        - str: The value of the step
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    def update(self, Enabled=None, Step=None):
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Description=None):
        """Finds and retrieves multivalue step resources from the server.

        All named parameters support regex and can be used to selectively retrieve step data from the server.
        By default the find method takes no parameters and will retrieve all step data from the server.

        Args
        ----
        - Description (str): The description of the Step

        Returns
        -------
        - self: This instance with matching step data retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._custom_select(Description)

    def _custom_select(self, Description=None):
        filters = []
        if Description is not None:
            filters.append({'property': 'description', 'regex': Description})
        payload = {
            'selects': [
                {
                    'from': self._parent.href,
                    'properties': [],
                    'children': [
                        {
                            'child': Steps._SDM_NAME,
                            'properties': ['*'],
                            'filters': filters
                        }
                    ],
                    'inlines': []
                }
            ]
        }
        end = self._parent.href.index('ixnetwork') + len('ixnetwork')
        url = '%s/operations/select' % self._parent.href[0:end]
        self._set_properties(None, clear=True)
        for properties in self._connection._execute(url, payload)[0][Steps._SDM_NAME]:
            self._set_properties(properties)
        return self
