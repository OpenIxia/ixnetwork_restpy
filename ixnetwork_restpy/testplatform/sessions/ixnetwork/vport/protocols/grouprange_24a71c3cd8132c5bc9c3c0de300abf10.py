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


class GroupRange(Base):
    """This object holds a list of multicast addresses that a particular host is interested in.
    The GroupRange class encapsulates a list of groupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the GroupRange.find() method.
    The list can be managed by using the GroupRange.add() and GroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'groupRange'
    _SDM_ATT_MAP = {
        'EnablePacking': 'enablePacking',
        'EnableUpdateRequired': 'enableUpdateRequired',
        'Enabled': 'enabled',
        'GroupCount': 'groupCount',
        'GroupIpFrom': 'groupIpFrom',
        'IncrementStep': 'incrementStep',
        'RecordsPerFrame': 'recordsPerFrame',
        'SourceMode': 'sourceMode',
        'SourcesPerRecord': 'sourcesPerRecord',
    }

    def __init__(self, parent):
        super(GroupRange, self).__init__(parent)

    @property
    def SourceRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.sourcerange_d0238c26b928f418670a6e52d73bbb97.SourceRange): An instance of the SourceRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.sourcerange_d0238c26b928f418670a6e52d73bbb97 import SourceRange
        return SourceRange(self)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: If enabled, the user can specify the number of records per frame and sources per record.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePacking'])
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePacking'], value)

    @property
    def EnableUpdateRequired(self):
        """
        Returns
        -------
        - bool: If true, updates the the changes to the Source IP addresses to take effect and to be displayed in the table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUpdateRequired'])
    @EnableUpdateRequired.setter
    def EnableUpdateRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableUpdateRequired'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the group range in the MLD simulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - number: The total number of IPv6 groups (Multicast Addresses) in this group range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupCount'])
    @GroupCount.setter
    def GroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupCount'], value)

    @property
    def GroupIpFrom(self):
        """
        Returns
        -------
        - str: The IPv6 address of the first member of the Group (Multicast Address).
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupIpFrom'])
    @GroupIpFrom.setter
    def GroupIpFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupIpFrom'], value)

    @property
    def IncrementStep(self):
        """
        Returns
        -------
        - number: The value used to increment the IPv6 address for each additional member of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementStep'])
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementStep'], value)

    @property
    def RecordsPerFrame(self):
        """
        Returns
        -------
        - number: The total number of group records to be added to each frame/message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecordsPerFrame'])
    @RecordsPerFrame.setter
    def RecordsPerFrame(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RecordsPerFrame'], value)

    @property
    def SourceMode(self):
        """
        Returns
        -------
        - str(include | exclude): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceMode'])
    @SourceMode.setter
    def SourceMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceMode'], value)

    @property
    def SourcesPerRecord(self):
        """
        Returns
        -------
        - number: The total number of sources to be added to each record.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourcesPerRecord'])
    @SourcesPerRecord.setter
    def SourcesPerRecord(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourcesPerRecord'], value)

    def update(self, EnablePacking=None, EnableUpdateRequired=None, Enabled=None, GroupCount=None, GroupIpFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None):
        """Updates groupRange resource on the server.

        Args
        ----
        - EnablePacking (bool): If enabled, the user can specify the number of records per frame and sources per record.
        - EnableUpdateRequired (bool): If true, updates the the changes to the Source IP addresses to take effect and to be displayed in the table.
        - Enabled (bool): Enables the use of the group range in the MLD simulation.
        - GroupCount (number): The total number of IPv6 groups (Multicast Addresses) in this group range.
        - GroupIpFrom (str): The IPv6 address of the first member of the Group (Multicast Address).
        - IncrementStep (number): The value used to increment the IPv6 address for each additional member of the group.
        - RecordsPerFrame (number): The total number of group records to be added to each frame/message.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The total number of sources to be added to each record.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnablePacking=None, EnableUpdateRequired=None, Enabled=None, GroupCount=None, GroupIpFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None):
        """Adds a new groupRange resource on the server and adds it to the container.

        Args
        ----
        - EnablePacking (bool): If enabled, the user can specify the number of records per frame and sources per record.
        - EnableUpdateRequired (bool): If true, updates the the changes to the Source IP addresses to take effect and to be displayed in the table.
        - Enabled (bool): Enables the use of the group range in the MLD simulation.
        - GroupCount (number): The total number of IPv6 groups (Multicast Addresses) in this group range.
        - GroupIpFrom (str): The IPv6 address of the first member of the Group (Multicast Address).
        - IncrementStep (number): The value used to increment the IPv6 address for each additional member of the group.
        - RecordsPerFrame (number): The total number of group records to be added to each frame/message.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The total number of sources to be added to each record.

        Returns
        -------
        - self: This instance with all currently retrieved groupRange resources using find and the newly added groupRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained groupRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnablePacking=None, EnableUpdateRequired=None, Enabled=None, GroupCount=None, GroupIpFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None):
        """Finds and retrieves groupRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupRange resources from the server.

        Args
        ----
        - EnablePacking (bool): If enabled, the user can specify the number of records per frame and sources per record.
        - EnableUpdateRequired (bool): If true, updates the the changes to the Source IP addresses to take effect and to be displayed in the table.
        - Enabled (bool): Enables the use of the group range in the MLD simulation.
        - GroupCount (number): The total number of IPv6 groups (Multicast Addresses) in this group range.
        - GroupIpFrom (str): The IPv6 address of the first member of the Group (Multicast Address).
        - IncrementStep (number): The value used to increment the IPv6 address for each additional member of the group.
        - RecordsPerFrame (number): The total number of group records to be added to each frame/message.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The total number of sources to be added to each record.

        Returns
        -------
        - self: This instance with matching groupRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateSource(self):
        """Executes the updateSource operation on the server.

        Updates the source information for the group host for MLD.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateSource', payload=payload, response_object=None)
