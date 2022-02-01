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


class DrillDown(Base):
    """Executes drill down operation on the drill down object set through steps 1-4.
    The DrillDown class encapsulates a list of drillDown resources that are managed by the user.
    A list of resources can be retrieved from the server using the DrillDown.find() method.
    The list can be managed by using the DrillDown.add() and DrillDown.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'drillDown'
    _SDM_ATT_MAP = {
        'AvailableDrillDownOptions': 'availableDrillDownOptions',
        'TargetDrillDownOption': 'targetDrillDownOption',
        'TargetRow': 'targetRow',
        'TargetRowFilter': 'targetRowFilter',
        'TargetRowIndex': 'targetRowIndex',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(DrillDown, self).__init__(parent, list_op)

    @property
    def AvailableTargetRowFilters(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.availabletargetrowfilters.availabletargetrowfilters.AvailableTargetRowFilters): An instance of the AvailableTargetRowFilters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.availabletargetrowfilters.availabletargetrowfilters import AvailableTargetRowFilters
        if len(self._object_properties) > 0:
            if self._properties.get('AvailableTargetRowFilters', None) is not None:
                return self._properties.get('AvailableTargetRowFilters')
        return AvailableTargetRowFilters(self)

    @property
    def AvailableDrillDownOptions(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Gets the available drill down options for the selected row.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableDrillDownOptions'])

    @property
    def TargetDrillDownOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the drill down option attribute to the drilldown object. It is one of the items in the list returned at 2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetDrillDownOption'])
    @TargetDrillDownOption.setter
    def TargetDrillDownOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TargetDrillDownOption'], value)

    @property
    def TargetRow(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Gets the target row, set previously, at step 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetRow'])

    @property
    def TargetRowFilter(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTargetRowFilters): Sets the row (from the view) that will be used to perform the drill-down. This is done by using one of the filters provided by availableTargetRowFilters
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetRowFilter'])
    @TargetRowFilter.setter
    def TargetRowFilter(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TargetRowFilter'], value)

    @property
    def TargetRowIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the attribute targetRowIndex to the drill down object. This is the row (from the view) that will be used to perform the drill-down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetRowIndex'])
    @TargetRowIndex.setter
    def TargetRowIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TargetRowIndex'], value)

    def update(self, TargetDrillDownOption=None, TargetRowFilter=None, TargetRowIndex=None):
        # type: (str, str, int) -> DrillDown
        """Updates drillDown resource on the server.

        Args
        ----
        - TargetDrillDownOption (str): Sets the drill down option attribute to the drilldown object. It is one of the items in the list returned at 2.
        - TargetRowFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTargetRowFilters)): Sets the row (from the view) that will be used to perform the drill-down. This is done by using one of the filters provided by availableTargetRowFilters
        - TargetRowIndex (number): Sets the attribute targetRowIndex to the drill down object. This is the row (from the view) that will be used to perform the drill-down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, TargetDrillDownOption=None, TargetRowFilter=None, TargetRowIndex=None):
        # type: (str, str, int) -> DrillDown
        """Adds a new drillDown resource on the server and adds it to the container.

        Args
        ----
        - TargetDrillDownOption (str): Sets the drill down option attribute to the drilldown object. It is one of the items in the list returned at 2.
        - TargetRowFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTargetRowFilters)): Sets the row (from the view) that will be used to perform the drill-down. This is done by using one of the filters provided by availableTargetRowFilters
        - TargetRowIndex (number): Sets the attribute targetRowIndex to the drill down object. This is the row (from the view) that will be used to perform the drill-down.

        Returns
        -------
        - self: This instance with all currently retrieved drillDown resources using find and the newly added drillDown resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained drillDown resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AvailableDrillDownOptions=None, TargetDrillDownOption=None, TargetRow=None, TargetRowFilter=None, TargetRowIndex=None):
        # type: (List[str], str, List[str], str, int) -> DrillDown
        """Finds and retrieves drillDown resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve drillDown resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all drillDown resources from the server.

        Args
        ----
        - AvailableDrillDownOptions (list(str)): Gets the available drill down options for the selected row.
        - TargetDrillDownOption (str): Sets the drill down option attribute to the drilldown object. It is one of the items in the list returned at 2.
        - TargetRow (list(str)): Gets the target row, set previously, at step 1.
        - TargetRowFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTargetRowFilters)): Sets the row (from the view) that will be used to perform the drill-down. This is done by using one of the filters provided by availableTargetRowFilters
        - TargetRowIndex (number): Sets the attribute targetRowIndex to the drill down object. This is the row (from the view) that will be used to perform the drill-down.

        Returns
        -------
        - self: This instance with matching drillDown resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of drillDown data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the drillDown resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DoDrillDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the doDrillDown operation on the server.

        Perform a drill down.

        doDrillDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('doDrillDown', payload=payload, response_object=None)
