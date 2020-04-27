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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Group(Base):
    """This object configures a set of multicast addresses that a host wishes to receive traffic from.
    The Group class encapsulates a list of group resources that are managed by the user.
    A list of resources can be retrieved from the server using the Group.find() method.
    The list can be managed by using the Group.add() and Group.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'group'

    def __init__(self, parent):
        super(Group, self).__init__(parent)

    @property
    def Source(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_2be2bb8ab889272532a2af12b8769de4.Source): An instance of the Source class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_2be2bb8ab889272532a2af12b8769de4 import Source
        return Source(self)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: If enabled, this option controls how many multicast records and sources will be included in each listener report for this group range.
        """
        return self._get_attribute('enablePacking')
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute('enablePacking', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the group range in the IGMP simulation.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - number: Specifies the set of IPv4 multicast addresses in the group range.
        """
        return self._get_attribute('groupCount')
    @GroupCount.setter
    def GroupCount(self, value):
        self._set_attribute('groupCount', value)

    @property
    def GroupFrom(self):
        """
        Returns
        -------
        - str: The IP address of the first member of the group (multicast address).
        """
        return self._get_attribute('groupFrom')
    @GroupFrom.setter
    def GroupFrom(self, value):
        self._set_attribute('groupFrom', value)

    @property
    def IncrementStep(self):
        """
        Returns
        -------
        - number: The value used to increment the IP address for each additional member of the group.
        """
        return self._get_attribute('incrementStep')
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute('incrementStep', value)

    @property
    def RecordsPerFrame(self):
        """
        Returns
        -------
        - number: If the user wants a specified number of records to be sent in each frame, packing should be enabled (enablePacking is true), and the number of records indicated with the recordsPerFrame option.
        """
        return self._get_attribute('recordsPerFrame')
    @RecordsPerFrame.setter
    def RecordsPerFrame(self, value):
        self._set_attribute('recordsPerFrame', value)

    @property
    def SourceMode(self):
        """
        Returns
        -------
        - str(include | exclude): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        """
        return self._get_attribute('sourceMode')
    @SourceMode.setter
    def SourceMode(self, value):
        self._set_attribute('sourceMode', value)

    @property
    def SourcesPerRecord(self):
        """
        Returns
        -------
        - number: The number of multicast sources that will be included in each listener report for this group range.
        """
        return self._get_attribute('sourcesPerRecord')
    @SourcesPerRecord.setter
    def SourcesPerRecord(self, value):
        self._set_attribute('sourcesPerRecord', value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - bool: Notifies the user that the changes made to the IGMP configuration of the source IP addresses for this group range need to be reflected.
        """
        return self._get_attribute('updateRequired')
    @UpdateRequired.setter
    def UpdateRequired(self, value):
        self._set_attribute('updateRequired', value)

    def update(self, EnablePacking=None, Enabled=None, GroupCount=None, GroupFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None, UpdateRequired=None):
        """Updates group resource on the server.

        Args
        ----
        - EnablePacking (bool): If enabled, this option controls how many multicast records and sources will be included in each listener report for this group range.
        - Enabled (bool): Enables the use of the group range in the IGMP simulation.
        - GroupCount (number): Specifies the set of IPv4 multicast addresses in the group range.
        - GroupFrom (str): The IP address of the first member of the group (multicast address).
        - IncrementStep (number): The value used to increment the IP address for each additional member of the group.
        - RecordsPerFrame (number): If the user wants a specified number of records to be sent in each frame, packing should be enabled (enablePacking is true), and the number of records indicated with the recordsPerFrame option.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The number of multicast sources that will be included in each listener report for this group range.
        - UpdateRequired (bool): Notifies the user that the changes made to the IGMP configuration of the source IP addresses for this group range need to be reflected.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, EnablePacking=None, Enabled=None, GroupCount=None, GroupFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None, UpdateRequired=None):
        """Adds a new group resource on the server and adds it to the container.

        Args
        ----
        - EnablePacking (bool): If enabled, this option controls how many multicast records and sources will be included in each listener report for this group range.
        - Enabled (bool): Enables the use of the group range in the IGMP simulation.
        - GroupCount (number): Specifies the set of IPv4 multicast addresses in the group range.
        - GroupFrom (str): The IP address of the first member of the group (multicast address).
        - IncrementStep (number): The value used to increment the IP address for each additional member of the group.
        - RecordsPerFrame (number): If the user wants a specified number of records to be sent in each frame, packing should be enabled (enablePacking is true), and the number of records indicated with the recordsPerFrame option.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The number of multicast sources that will be included in each listener report for this group range.
        - UpdateRequired (bool): Notifies the user that the changes made to the IGMP configuration of the source IP addresses for this group range need to be reflected.

        Returns
        -------
        - self: This instance with all currently retrieved group resources using find and the newly added group resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained group resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnablePacking=None, Enabled=None, GroupCount=None, GroupFrom=None, IncrementStep=None, RecordsPerFrame=None, SourceMode=None, SourcesPerRecord=None, UpdateRequired=None):
        """Finds and retrieves group resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve group resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all group resources from the server.

        Args
        ----
        - EnablePacking (bool): If enabled, this option controls how many multicast records and sources will be included in each listener report for this group range.
        - Enabled (bool): Enables the use of the group range in the IGMP simulation.
        - GroupCount (number): Specifies the set of IPv4 multicast addresses in the group range.
        - GroupFrom (str): The IP address of the first member of the group (multicast address).
        - IncrementStep (number): The value used to increment the IP address for each additional member of the group.
        - RecordsPerFrame (number): If the user wants a specified number of records to be sent in each frame, packing should be enabled (enablePacking is true), and the number of records indicated with the recordsPerFrame option.
        - SourceMode (str(include | exclude)): Indicates whether the associated source range is a set of IP addresses to be included or excluded.
        - SourcesPerRecord (number): The number of multicast sources that will be included in each listener report for this group range.
        - UpdateRequired (bool): Notifies the user that the changes made to the IGMP configuration of the source IP addresses for this group range need to be reflected.

        Returns
        -------
        - self: This instance with matching group resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of group data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the group resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateSources(self):
        """Executes the updateSources operation on the server.

        This command is used to update the host group source information for IGMP.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateSources', payload=payload, response_object=None)
