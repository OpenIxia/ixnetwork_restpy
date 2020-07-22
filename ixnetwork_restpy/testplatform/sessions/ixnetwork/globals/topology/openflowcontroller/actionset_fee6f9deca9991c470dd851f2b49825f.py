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


class ActionSet(Base):
    """Action prototype.
    The ActionSet class encapsulates a list of actionSet resources that are managed by the user.
    A list of resources can be retrieved from the server using the ActionSet.find() method.
    The list can be managed by using the ActionSet.add() and ActionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'actionSet'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Description': 'description',
        'IsEditable': 'isEditable',
        'IsRepeatable': 'isRepeatable',
        'IsRequired': 'isRequired',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(ActionSet, self).__init__(parent)

    @property
    def Action(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.action_fca3673b74732220701dbad581b63119.Action): An instance of the Action class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.action_fca3673b74732220701dbad581b63119 import Action
        return Action(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of the TLV prototype.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def IsEditable(self):
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEditable'])
    @IsEditable.setter
    def IsEditable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEditable'], value)

    @property
    def IsRepeatable(self):
        """
        Returns
        -------
        - bool: Information if the field can be multiplied in the tlv definition.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRepeatable'])
    @IsRepeatable.setter
    def IsRepeatable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRepeatable'], value)

    @property
    def IsRequired(self):
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRequired'])
    @IsRequired.setter
    def IsRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRequired'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the TLV field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Updates actionSet resource on the server.

        Args
        ----
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Adds a new actionSet resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Returns
        -------
        - self: This instance with all currently retrieved actionSet resources using find and the newly added actionSet resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained actionSet resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Finds and retrieves actionSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve actionSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all actionSet resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Returns
        -------
        - self: This instance with matching actionSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of actionSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the actionSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
