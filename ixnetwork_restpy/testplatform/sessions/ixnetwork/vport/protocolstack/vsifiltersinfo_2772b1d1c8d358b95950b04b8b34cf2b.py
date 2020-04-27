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


class VsiFiltersInfo(Base):
    """
    The VsiFiltersInfo class encapsulates a list of vsiFiltersInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the VsiFiltersInfo.find() method.
    The list can be managed by using the VsiFiltersInfo.add() and VsiFiltersInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vsiFiltersInfo'

    def __init__(self, parent):
        super(VsiFiltersInfo, self).__init__(parent)

    @property
    def CvlanFirstId(self):
        """
        Returns
        -------
        - number: The first ID to be used for the C-VLAN tag.
        """
        return self._get_attribute('cvlanFirstId')
    @CvlanFirstId.setter
    def CvlanFirstId(self, value):
        self._set_attribute('cvlanFirstId', value)

    @property
    def CvlanIncrement(self):
        """
        Returns
        -------
        - number: Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        """
        return self._get_attribute('cvlanIncrement')
    @CvlanIncrement.setter
    def CvlanIncrement(self, value):
        self._set_attribute('cvlanIncrement', value)

    @property
    def CvlanIncrementStep(self):
        """
        Returns
        -------
        - number: Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        """
        return self._get_attribute('cvlanIncrementStep')
    @CvlanIncrementStep.setter
    def CvlanIncrementStep(self, value):
        self._set_attribute('cvlanIncrementStep', value)

    @property
    def CvlanUniqueCount(self):
        """
        Returns
        -------
        - number: Number of unique C-VLAN IDs to use.
        """
        return self._get_attribute('cvlanUniqueCount')
    @CvlanUniqueCount.setter
    def CvlanUniqueCount(self, value):
        self._set_attribute('cvlanUniqueCount', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def GroupFirstId(self):
        """
        Returns
        -------
        - number: The first Group ID to be used.
        """
        return self._get_attribute('groupFirstId')
    @GroupFirstId.setter
    def GroupFirstId(self, value):
        self._set_attribute('groupFirstId', value)

    @property
    def GroupIncrement(self):
        """
        Returns
        -------
        - number: Amount of increment per increment step for Group ID.
        """
        return self._get_attribute('groupIncrement')
    @GroupIncrement.setter
    def GroupIncrement(self, value):
        self._set_attribute('groupIncrement', value)

    @property
    def GroupIncrementStep(self):
        """
        Returns
        -------
        - number: Frequency of Group ID increment.
        """
        return self._get_attribute('groupIncrementStep')
    @GroupIncrementStep.setter
    def GroupIncrementStep(self, value):
        self._set_attribute('groupIncrementStep', value)

    @property
    def GroupUniqueCount(self):
        """
        Returns
        -------
        - number: Number of unique Group IDs to use.
        """
        return self._get_attribute('groupUniqueCount')
    @GroupUniqueCount.setter
    def GroupUniqueCount(self, value):
        self._set_attribute('groupUniqueCount', value)

    @property
    def Mac(self):
        """
        Returns
        -------
        - str: The start MAC address for the interface. It is always available.
        """
        return self._get_attribute('mac')
    @Mac.setter
    def Mac(self, value):
        self._set_attribute('mac', value)

    @property
    def MacIncrementBy(self):
        """
        Returns
        -------
        - str: The increment MAC address.
        """
        return self._get_attribute('macIncrementBy')
    @MacIncrementBy.setter
    def MacIncrementBy(self, value):
        self._set_attribute('macIncrementBy', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def PcpFirstId(self):
        """
        Returns
        -------
        - number: The first ID to be used for the PCP tag.
        """
        return self._get_attribute('pcpFirstId')
    @PcpFirstId.setter
    def PcpFirstId(self, value):
        self._set_attribute('pcpFirstId', value)

    @property
    def PcpIncrement(self):
        """
        Returns
        -------
        - number: Amount of increment per increment step for PCP.
        """
        return self._get_attribute('pcpIncrement')
    @PcpIncrement.setter
    def PcpIncrement(self, value):
        self._set_attribute('pcpIncrement', value)

    @property
    def PcpIncrementStep(self):
        """
        Returns
        -------
        - number: Frequency of PCP ID increment.
        """
        return self._get_attribute('pcpIncrementStep')
    @PcpIncrementStep.setter
    def PcpIncrementStep(self, value):
        self._set_attribute('pcpIncrementStep', value)

    @property
    def PcpUniqueCount(self):
        """
        Returns
        -------
        - number: Number of unique PCP IDs to use.
        """
        return self._get_attribute('pcpUniqueCount')
    @PcpUniqueCount.setter
    def PcpUniqueCount(self, value):
        self._set_attribute('pcpUniqueCount', value)

    @property
    def Ps(self):
        """
        Returns
        -------
        - bool: Enable/disable priority.
        """
        return self._get_attribute('ps')
    @Ps.setter
    def Ps(self, value):
        self._set_attribute('ps', value)

    def update(self, CvlanFirstId=None, CvlanIncrement=None, CvlanIncrementStep=None, CvlanUniqueCount=None, Enabled=None, GroupFirstId=None, GroupIncrement=None, GroupIncrementStep=None, GroupUniqueCount=None, Mac=None, MacIncrementBy=None, PcpFirstId=None, PcpIncrement=None, PcpIncrementStep=None, PcpUniqueCount=None, Ps=None):
        """Updates vsiFiltersInfo resource on the server.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool): 
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CvlanFirstId=None, CvlanIncrement=None, CvlanIncrementStep=None, CvlanUniqueCount=None, Enabled=None, GroupFirstId=None, GroupIncrement=None, GroupIncrementStep=None, GroupUniqueCount=None, Mac=None, MacIncrementBy=None, PcpFirstId=None, PcpIncrement=None, PcpIncrementStep=None, PcpUniqueCount=None, Ps=None):
        """Adds a new vsiFiltersInfo resource on the server and adds it to the container.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool): 
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Returns
        -------
        - self: This instance with all currently retrieved vsiFiltersInfo resources using find and the newly added vsiFiltersInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained vsiFiltersInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CvlanFirstId=None, CvlanIncrement=None, CvlanIncrementStep=None, CvlanUniqueCount=None, Enabled=None, GroupFirstId=None, GroupIncrement=None, GroupIncrementStep=None, GroupUniqueCount=None, Mac=None, MacIncrementBy=None, ObjectId=None, PcpFirstId=None, PcpIncrement=None, PcpIncrementStep=None, PcpUniqueCount=None, Ps=None):
        """Finds and retrieves vsiFiltersInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vsiFiltersInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vsiFiltersInfo resources from the server.

        Args
        ----
        - CvlanFirstId (number): The first ID to be used for the C-VLAN tag.
        - CvlanIncrement (number): Amount of increment per increment step for C-VLAN. E.g. increment step = 10 and increment = 2 means increment C-VLAN ID by 2 for every 10 IPs.
        - CvlanIncrementStep (number): Frequency of C-VLAN ID increment. E.g., value of 10 means increment C-VLAN ID once for every 10 IP addresses.
        - CvlanUniqueCount (number): Number of unique C-VLAN IDs to use.
        - Enabled (bool): 
        - GroupFirstId (number): The first Group ID to be used.
        - GroupIncrement (number): Amount of increment per increment step for Group ID.
        - GroupIncrementStep (number): Frequency of Group ID increment.
        - GroupUniqueCount (number): Number of unique Group IDs to use.
        - Mac (str): The start MAC address for the interface. It is always available.
        - MacIncrementBy (str): The increment MAC address.
        - ObjectId (str): Unique identifier for this object
        - PcpFirstId (number): The first ID to be used for the PCP tag.
        - PcpIncrement (number): Amount of increment per increment step for PCP.
        - PcpIncrementStep (number): Frequency of PCP ID increment.
        - PcpUniqueCount (number): Number of unique PCP IDs to use.
        - Ps (bool): Enable/disable priority.

        Returns
        -------
        - self: This instance with matching vsiFiltersInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vsiFiltersInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vsiFiltersInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
