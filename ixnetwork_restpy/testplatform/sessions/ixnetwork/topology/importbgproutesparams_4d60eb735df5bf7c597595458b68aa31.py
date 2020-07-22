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


class ImportBgpRoutesParams(Base):
    """Import IPv4 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.
    The ImportBgpRoutesParams class encapsulates a required importBgpRoutesParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'importBgpRoutesParams'
    _SDM_ATT_MAP = {
        'BestRoutes': 'bestRoutes',
        'DataFile': 'dataFile',
        'FileType': 'fileType',
        'NextHop': 'nextHop',
        'RouteDistributionType': 'routeDistributionType',
        'RouteLimit': 'routeLimit',
    }

    def __init__(self, parent):
        super(ImportBgpRoutesParams, self).__init__(parent)

    @property
    def BestRoutes(self):
        """
        Returns
        -------
        - bool: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['BestRoutes'])
    @BestRoutes.setter
    def BestRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BestRoutes'], value)

    @property
    def DataFile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.files.Files): Select source file having route information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataFile'])
    @DataFile.setter
    def DataFile(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataFile'], value)

    @property
    def FileType(self):
        """
        Returns
        -------
        - str(csv | juniper | cisco): Import routes file type. Route import may fail in file type is not matching with the file being imported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FileType'])
    @FileType.setter
    def FileType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FileType'], value)

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str(overwriteTestersAddress | preserveFromFile): Option for setting Next Hop modification type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def RouteDistributionType(self):
        """
        Returns
        -------
        - str(roundRobin | replicate): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistributionType'])
    @RouteDistributionType.setter
    def RouteDistributionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteDistributionType'], value)

    @property
    def RouteLimit(self):
        """
        Returns
        -------
        - number: Specify maximum routes(per port) that you want to import. Based on Card Memory, the Max Route Limit Per Port are: - 4GB or more => 2.0 million 2GB => 1.6 million 1GB => 0.8 million Less than 1GB => 0.5 million
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteLimit'])
    @RouteLimit.setter
    def RouteLimit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteLimit'], value)

    def update(self, BestRoutes=None, DataFile=None, FileType=None, NextHop=None, RouteDistributionType=None, RouteLimit=None):
        """Updates importBgpRoutesParams resource on the server.

        Args
        ----
        - BestRoutes (bool): Import only the best routes (provided route file has this information).
        - DataFile (obj(ixnetwork_restpy.files.Files)): Select source file having route information.
        - FileType (str(csv | juniper | cisco)): Import routes file type. Route import may fail in file type is not matching with the file being imported.
        - NextHop (str(overwriteTestersAddress | preserveFromFile)): Option for setting Next Hop modification type.
        - RouteDistributionType (str(roundRobin | replicate)): Option to specify distribution type, for distributing imported routes across all BGP Peer. Options: Round-Robin, for allocating routes sequentially, and Replicate, for allocating all routes to each Peer.
        - RouteLimit (number): Specify maximum routes(per port) that you want to import. Based on Card Memory, the Max Route Limit Per Port are: - 4GB or more => 2.0 million 2GB => 1.6 million 1GB => 0.8 million Less than 1GB => 0.5 million

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def ImportBgpRoutes(self):
        """Executes the importBgpRoutes operation on the server.

        Import IPv4 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('importBgpRoutes', payload=payload, response_object=None)
