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


class SpbNetworkRange(Base):
    """The SPB Network Range.
    The SpbNetworkRange class encapsulates a list of spbNetworkRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbNetworkRange.find() method.
    The list can be managed by using the SpbNetworkRange.add() and SpbNetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'spbNetworkRange'
    _SDM_ATT_MAP = {
        'EnableAdvertiseNetworkRange': 'enableAdvertiseNetworkRange',
        'EnableHostName': 'enableHostName',
        'EntryColumn': 'entryColumn',
        'EntryRow': 'entryRow',
        'HostNamePrefix': 'hostNamePrefix',
        'InterfaceMetric': 'interfaceMetric',
        'NoOfColumns': 'noOfColumns',
        'NoOfRows': 'noOfRows',
        'StartSystemId': 'startSystemId',
        'SystemIdIncrementBy': 'systemIdIncrementBy',
    }

    def __init__(self, parent):
        super(SpbNetworkRange, self).__init__(parent)

    @property
    def SpbOutsideLinks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spboutsidelinks_dfb7b1e816409cddb14e138ebc2096dc.SpbOutsideLinks): An instance of the SpbOutsideLinks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spboutsidelinks_dfb7b1e816409cddb14e138ebc2096dc import SpbOutsideLinks
        return SpbOutsideLinks(self)

    @property
    def SpbmNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodetopologyrange_199093afa11cd9f4488faaa1ad3ec3a7.SpbmNodeTopologyRange): An instance of the SpbmNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodetopologyrange_199093afa11cd9f4488faaa1ad3ec3a7 import SpbmNodeTopologyRange
        return SpbmNodeTopologyRange(self)

    @property
    def EnableAdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: If true, this SPB ISIS Network Range is advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvertiseNetworkRange'])
    @EnableAdvertiseNetworkRange.setter
    def EnableAdvertiseNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvertiseNetworkRange'], value)

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - bool: If true, the host name of the router is activated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostName'])
    @EnableHostName.setter
    def EnableHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostName'], value)

    @property
    def EntryColumn(self):
        """
        Returns
        -------
        - number: The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryColumn'])
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryColumn'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def HostNamePrefix(self):
        """
        Returns
        -------
        - str: The host name prefix information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostNamePrefix'])
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostNamePrefix'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: The metric cost associated with this emulated SPB ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def NoOfColumns(self):
        """
        Returns
        -------
        - number: The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfColumns'])
    @NoOfColumns.setter
    def NoOfColumns(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfColumns'], value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def StartSystemId(self):
        """
        Returns
        -------
        - str: The System ID assigned to the starting SPB ISIS router in this network range. The default is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSystemId'])
    @StartSystemId.setter
    def StartSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSystemId'], value)

    @property
    def SystemIdIncrementBy(self):
        """
        Returns
        -------
        - str: This is used when more than one router is to be emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemIdIncrementBy'])
    @SystemIdIncrementBy.setter
    def SystemIdIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SystemIdIncrementBy'], value)

    def update(self, EnableAdvertiseNetworkRange=None, EnableHostName=None, EntryColumn=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, NoOfColumns=None, NoOfRows=None, StartSystemId=None, SystemIdIncrementBy=None):
        """Updates spbNetworkRange resource on the server.

        Args
        ----
        - EnableAdvertiseNetworkRange (bool): If true, this SPB ISIS Network Range is advertised.
        - EnableHostName (bool): If true, the host name of the router is activated.
        - EntryColumn (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): The host name prefix information.
        - InterfaceMetric (number): The metric cost associated with this emulated SPB ISIS router.
        - NoOfColumns (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - NoOfRows (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - StartSystemId (str): The System ID assigned to the starting SPB ISIS router in this network range. The default is 00 00 00 00 00 00.
        - SystemIdIncrementBy (str): This is used when more than one router is to be emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableAdvertiseNetworkRange=None, EnableHostName=None, EntryColumn=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, NoOfColumns=None, NoOfRows=None, StartSystemId=None, SystemIdIncrementBy=None):
        """Adds a new spbNetworkRange resource on the server and adds it to the container.

        Args
        ----
        - EnableAdvertiseNetworkRange (bool): If true, this SPB ISIS Network Range is advertised.
        - EnableHostName (bool): If true, the host name of the router is activated.
        - EntryColumn (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): The host name prefix information.
        - InterfaceMetric (number): The metric cost associated with this emulated SPB ISIS router.
        - NoOfColumns (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - NoOfRows (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - StartSystemId (str): The System ID assigned to the starting SPB ISIS router in this network range. The default is 00 00 00 00 00 00.
        - SystemIdIncrementBy (str): This is used when more than one router is to be emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Returns
        -------
        - self: This instance with all currently retrieved spbNetworkRange resources using find and the newly added spbNetworkRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbNetworkRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableAdvertiseNetworkRange=None, EnableHostName=None, EntryColumn=None, EntryRow=None, HostNamePrefix=None, InterfaceMetric=None, NoOfColumns=None, NoOfRows=None, StartSystemId=None, SystemIdIncrementBy=None):
        """Finds and retrieves spbNetworkRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbNetworkRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbNetworkRange resources from the server.

        Args
        ----
        - EnableAdvertiseNetworkRange (bool): If true, this SPB ISIS Network Range is advertised.
        - EnableHostName (bool): If true, the host name of the router is activated.
        - EntryColumn (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - EntryRow (number): The value is used in combination to specify which virtual router in the Network Range is connected to the current ISIS L2/L3 Router.
        - HostNamePrefix (str): The host name prefix information.
        - InterfaceMetric (number): The metric cost associated with this emulated SPB ISIS router.
        - NoOfColumns (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - NoOfRows (number): The value is used in combination to create a matrix (grid) for an emulated network range of the following size: The # Rows multiplied the # Cols = Number of routers in this Network Range. (For example, 3 Rows x 3 Columns = 9 Routers).
        - StartSystemId (str): The System ID assigned to the starting SPB ISIS router in this network range. The default is 00 00 00 00 00 00.
        - SystemIdIncrementBy (str): This is used when more than one router is to be emulated. The increment value is added to the previous System ID for each additional emulated router in this network range.

        Returns
        -------
        - self: This instance with matching spbNetworkRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbNetworkRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbNetworkRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
