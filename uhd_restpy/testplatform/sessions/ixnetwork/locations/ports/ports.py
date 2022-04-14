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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Ports(Base):
    """
    The Ports class encapsulates a list of ports resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ports.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ports'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'IsAvailable': 'isAvailable',
        'IsBusy': 'isBusy',
        'IsLinkUp': 'isLinkUp',
        'Location': 'location',
        'Owner': 'owner',
        'ResourceMode': 'resourceMode',
    }
    _SDM_ENUM_MAP = {
        'resourceMode': ['normal', 'tenGig', 'fortyGig', 'singleMode', 'dualMode', 'hundredGigNonFanOut', 'fortyGigFanOut', 'threeByTenGigFanOut', 'eightByTenGigFanOut', 'fourByTwentyFiveGigNonFanOut', 'twoByTwentyFiveGigNonFanOut', 'oneByFiftyGigNonFanOut', 'fortyGigNonFanOut', 'oneByTenGigFanOut', 'fourByTenGigFanOut', 'incompatibleMode', 'hundredGigCapturePlayback', 'fortyGigCapturePlayback', 'novusHundredGigNonFanOut', 'novusFourByTwentyFiveGigNonFanOut', 'novusTwoByFiftyGigNonFanOut', 'novusOneByFortyGigNonFanOut', 'novusFourByTenGigNonFanOut', 'krakenOneByFourHundredGigNonFanOut', 'krakenOneByTwoHundredGigNonFanOut', 'krakenTwoByOneHundredGigFanOut', 'krakenFourByFiftyGigFanOut', 'aresOneOneByFourHundredGigNonFanOut', 'aresOneTwoByTwoHundredGigFanOut', 'aresOneFourByOneHundredGigFanOut', 'aresOneFourByOneHundredGigMacSecFanOut', 'aresOneEightByFiftyGigFanOut', 'uhdOneHundredEightByHundredGigNonFanOut', 'uhdOneHundredEightByFortyGigNonFanOut', 'uhdOneHundredSixteenByFiftyGigFanOut', 'uhdOneHundredThirtyTwoByTwentyFiveGigFanOut', 'uhdOneHundredThirtyTwoByTenGigFanOut', 'notApplicable'],
    }

    def __init__(self, parent, list_op=False):
        super(Ports, self).__init__(parent, list_op)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def IsAvailable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAvailable'])

    @property
    def IsBusy(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsBusy'])

    @property
    def IsLinkUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLinkUp'])

    @property
    def Location(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Location'])

    @property
    def Owner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Owner'])

    @property
    def ResourceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | notApplicable): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResourceMode'])

    def add(self):
        """Adds a new ports resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ports resources using find and the newly added ports resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Description=None, IsAvailable=None, IsBusy=None, IsLinkUp=None, Location=None, Owner=None, ResourceMode=None):
        # type: (str, bool, bool, bool, str, str, str) -> Ports
        """Finds and retrieves ports resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ports resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ports resources from the server.

        Args
        ----
        - Description (str): 
        - IsAvailable (bool): 
        - IsBusy (bool): 
        - IsLinkUp (bool): 
        - Location (str): 
        - Owner (str): 
        - ResourceMode (str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | notApplicable)): 

        Returns
        -------
        - self: This instance with matching ports resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ports data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ports resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearOwnership(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearOwnership operation on the server.

        Clears ownership on a list of location ports.

        clearOwnership(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearOwnership', payload=payload, response_object=None)
