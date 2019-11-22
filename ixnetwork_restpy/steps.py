from ixnetwork_restpy.base import Base


class Steps(Base):
    """List of all possible steps for this multivalue
    """
    _SDM_NAME = 'nest'

    def __init__(self, parent):
        super(Steps, self).__init__(parent)

    @property
    def Description(self):
        """The description of this step

        Returns:
            str: The description of the step
        """
        return self._get_attribute('description')

    @property
    def Owner(self):
        """The owner of this step

        Returns:
            str: The href of the owner
        """
        return self._get_attribute('owner')

    @property
    def Enabled(self):
        """Enable/disable the step

        Returns:
            bool
        """
        return self._get_attribute('enabled')

    @Enabled.setter
    def Enabled(self, enabled):
        self._set_attribute('enabled', enabled)

    @property
    def Step(self):
        """The value of the step. This value must be in the same format as the parent multivalue

        Returns:
            str
        """
        return self._get_attribute('step')

    @Step.setter
    def Step(self, value):
        self._set_attribute('step', value)

    def find(self, Description=None):
        """Finds and retrieves multivalue step data from the server.

        All named parameters support regex and can be used to selectively retrieve step data from the server.
        By default the find method takes no parameters and will retrieve all step data from the server.

        Args:
            Description (str): The description of the Step

         Returns:
            self: This instance with matching step data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._custom_select(Description)

    def _custom_select(self, Description=None):
        filters = []
        if Description is not None:
            filters.append({'name': 'Description', 'regex': Description})
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
        for properties in self._connection._execute(url, payload)[0][Steps._SDM_NAME]:
            self._set_properties(properties)
        return self
