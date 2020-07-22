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


class NetworkRange(Base):
    """A list of network ranges for the ISIS router.
    The NetworkRange class encapsulates a list of networkRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkRange.find() method.
    The list can be managed by using the NetworkRange.add() and NetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkRange'
    _SDM_ATT_MAP = {
        'EnableHostName': 'enableHostName',
        'Enabled': 'enabled',
        'EntryCol': 'entryCol',
        'EntryRow': 'entryRow',
        'GridNodeRoutes': 'gridNodeRoutes',
        'GridOutsideExLinks': 'gridOutsideExLinks',
        'GridOutsideLinks': 'gridOutsideLinks',
        'HostNamePrefix': 'hostNamePrefix',
        'InterfaceIps': 'interfaceIps',
        'InterfaceMetric': 'interfaceMetric',
        'Ipv6MtMetric': 'ipv6MtMetric',
        'LinkType': 'linkType',
        'NoOfCols': 'noOfCols',
        'NoOfRows': 'noOfRows',
        'RouterId': 'routerId',
        'RouterIdIncrement': 'routerIdIncrement',
        'TePaths': 'tePaths',
        'UseWideMetric': 'useWideMetric',
    }

    def __init__(self, parent):
        super(NetworkRange, self).__init__(parent)

    @property
    def EntryTe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.entryte_9cd30e209352f3748008e607434e92a4.EntryTe): An instance of the EntryTe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.entryte_9cd30e209352f3748008e607434e92a4 import EntryTe
        return EntryTe(self)._select()

    @property
    def RangeTe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rangete_9c7f010a9212f361a3dacba9c17f9cf0.RangeTe): An instance of the RangeTe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rangete_9c7f010a9212f361a3dacba9c17f9cf0 import RangeTe
        return RangeTe(self)._select()

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - bool: If true, the given dynamic host name is transmitted in all the packets sent from this router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHostName'])
    @EnableHostName.setter
    def EnableHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHostName'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If enabled, this route range will be advertised by the nodes in the network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EntryCol(self):
        """
        Returns
        -------
        - number: The simulated router is connected to a router in the grid at a particular row and column location. This option is the column number. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryCol'])
    @EntryCol.setter
    def EntryCol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryCol'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The simulated router is connected to a router in the grid at a particular row and column location. This option is the row number. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def GridNodeRoutes(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number)): The set of advertised networks within the grid to be included in isisGrid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridNodeRoutes'])
    @GridNodeRoutes.setter
    def GridNodeRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridNodeRoutes'], value)

    @property
    def GridOutsideExLinks(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str)): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridOutsideExLinks'])
    @GridOutsideExLinks.setter
    def GridOutsideExLinks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridOutsideExLinks'], value)

    @property
    def GridOutsideLinks(self):
        """DEPRECATED 
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:str,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str)): Sets up the outside links between an ISIS grid and another ISIS grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GridOutsideLinks'])
    @GridOutsideLinks.setter
    def GridOutsideLinks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GridOutsideLinks'], value)

    @property
    def HostNamePrefix(self):
        """
        Returns
        -------
        - str: Allows to add a host name to this network range. The name prefix is appended by row ID and column ID in .<rowid>.<colid> combination as per the router placed in the emulated network grid behind the Ixia port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostNamePrefix'])
    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HostNamePrefix'], value)

    @property
    def InterfaceIps(self):
        """
        Returns
        -------
        - list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)): The interface IP information for the simulated network.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIps'])
    @InterfaceIps.setter
    def InterfaceIps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIps'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: The metric cost associated with this emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def Ipv6MtMetric(self):
        """
        Returns
        -------
        - number: This metric is same as the Interface Metric. If enabled, it allows you to enter data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'])
    @Ipv6MtMetric.setter
    def Ipv6MtMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast): The type of network link for this emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def NoOfCols(self):
        """
        Returns
        -------
        - number: The number of columns in the simulated grid. (default = 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCols'])
    @NoOfCols.setter
    def NoOfCols(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCols'], value)

    @property
    def NoOfRows(self):
        """
        Returns
        -------
        - number: The number of rows in the simulated grid. (default = 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRows'])
    @NoOfRows.setter
    def NoOfRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRows'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: The router ID for the first emulated ISIS router in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def RouterIdIncrement(self):
        """
        Returns
        -------
        - str: The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterIdIncrement'])
    @RouterIdIncrement.setter
    def RouterIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterIdIncrement'], value)

    @property
    def TePaths(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str,arg17:str,arg18:str,arg19:str)): Adds a Traffic Engineering (TE) Path to the list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TePaths'])
    @TePaths.setter
    def TePaths(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TePaths'], value)

    @property
    def UseWideMetric(self):
        """
        Returns
        -------
        - bool: Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (IP routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, Wide Metrics will be enabled automatically. The Wide Metrics may be used without enabling TE, however.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseWideMetric'])
    @UseWideMetric.setter
    def UseWideMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseWideMetric'], value)

    def update(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Updates networkRange resource on the server.

        Args
        ----
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - Enabled (bool): If enabled, this route range will be advertised by the nodes in the network range.
        - EntryCol (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the column number. (default = 1)
        - EntryRow (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the row number. (default = 1)
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): The set of advertised networks within the grid to be included in isisGrid.
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str))): NOT DEFINED
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:str,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str))): Sets up the outside links between an ISIS grid and another ISIS grid.
        - HostNamePrefix (str): Allows to add a host name to this network range. The name prefix is appended by row ID and column ID in .<rowid>.<colid> combination as per the router placed in the emulated network grid behind the Ixia port.
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): The interface IP information for the simulated network.
        - InterfaceMetric (number): The metric cost associated with this emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If enabled, it allows you to enter data.
        - LinkType (str(pointToPoint | broadcast)): The type of network link for this emulated ISIS router.
        - NoOfCols (number): The number of columns in the simulated grid. (default = 3)
        - NoOfRows (number): The number of rows in the simulated grid. (default = 3)
        - RouterId (str): The router ID for the first emulated ISIS router in this network range.
        - RouterIdIncrement (str): The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str,arg17:str,arg18:str,arg19:str))): Adds a Traffic Engineering (TE) Path to the list.
        - UseWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (IP routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, Wide Metrics will be enabled automatically. The Wide Metrics may be used without enabling TE, however.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Adds a new networkRange resource on the server and adds it to the container.

        Args
        ----
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - Enabled (bool): If enabled, this route range will be advertised by the nodes in the network range.
        - EntryCol (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the column number. (default = 1)
        - EntryRow (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the row number. (default = 1)
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): The set of advertised networks within the grid to be included in isisGrid.
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str))): NOT DEFINED
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:str,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str))): Sets up the outside links between an ISIS grid and another ISIS grid.
        - HostNamePrefix (str): Allows to add a host name to this network range. The name prefix is appended by row ID and column ID in .<rowid>.<colid> combination as per the router placed in the emulated network grid behind the Ixia port.
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): The interface IP information for the simulated network.
        - InterfaceMetric (number): The metric cost associated with this emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If enabled, it allows you to enter data.
        - LinkType (str(pointToPoint | broadcast)): The type of network link for this emulated ISIS router.
        - NoOfCols (number): The number of columns in the simulated grid. (default = 3)
        - NoOfRows (number): The number of rows in the simulated grid. (default = 3)
        - RouterId (str): The router ID for the first emulated ISIS router in this network range.
        - RouterIdIncrement (str): The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str,arg17:str,arg18:str,arg19:str))): Adds a Traffic Engineering (TE) Path to the list.
        - UseWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (IP routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, Wide Metrics will be enabled automatically. The Wide Metrics may be used without enabling TE, however.

        Returns
        -------
        - self: This instance with all currently retrieved networkRange resources using find and the newly added networkRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableHostName=None, Enabled=None, EntryCol=None, EntryRow=None, GridNodeRoutes=None, GridOutsideExLinks=None, GridOutsideLinks=None, HostNamePrefix=None, InterfaceIps=None, InterfaceMetric=None, Ipv6MtMetric=None, LinkType=None, NoOfCols=None, NoOfRows=None, RouterId=None, RouterIdIncrement=None, TePaths=None, UseWideMetric=None):
        """Finds and retrieves networkRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkRange resources from the server.

        Args
        ----
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - Enabled (bool): If enabled, this route range will be advertised by the nodes in the network range.
        - EntryCol (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the column number. (default = 1)
        - EntryRow (number): The simulated router is connected to a router in the grid at a particular row and column location. This option is the row number. (default = 1)
        - GridNodeRoutes (list(dict(arg1:bool,arg2:str[ipAny | ipv4 | ipv6],arg3:str,arg4:number,arg5:number,arg6:number,arg7:number,arg8:bool,arg9:bool,arg10:number))): The set of advertised networks within the grid to be included in isisGrid.
        - GridOutsideExLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:list[dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number)],arg5:str,arg6:number,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str))): NOT DEFINED
        - GridOutsideLinks (list(dict(arg1:number,arg2:number,arg3:str,arg4:str,arg5:number,arg6:str,arg7:str,arg8:str,arg9:str,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str))): Sets up the outside links between an ISIS grid and another ISIS grid.
        - HostNamePrefix (str): Allows to add a host name to this network range. The name prefix is appended by row ID and column ID in .<rowid>.<colid> combination as per the router placed in the emulated network grid behind the Ixia port.
        - InterfaceIps (list(dict(arg1:str[ipAny | ipv4 | ipv6],arg2:str,arg3:number))): The interface IP information for the simulated network.
        - InterfaceMetric (number): The metric cost associated with this emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If enabled, it allows you to enter data.
        - LinkType (str(pointToPoint | broadcast)): The type of network link for this emulated ISIS router.
        - NoOfCols (number): The number of columns in the simulated grid. (default = 3)
        - NoOfRows (number): The number of rows in the simulated grid. (default = 3)
        - RouterId (str): The router ID for the first emulated ISIS router in this network range.
        - RouterIdIncrement (str): The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        - TePaths (list(dict(arg1:number,arg2:number,arg3:number,arg4:number,arg5:number,arg6:number,arg7:bool,arg8:str,arg9:number,arg10:str,arg11:str,arg12:str,arg13:str,arg14:str,arg15:str,arg16:str,arg17:str,arg18:str,arg19:str))): Adds a Traffic Engineering (TE) Path to the list.
        - UseWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (IP routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, Wide Metrics will be enabled automatically. The Wide Metrics may be used without enabling TE, however.

        Returns
        -------
        - self: This instance with matching networkRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
