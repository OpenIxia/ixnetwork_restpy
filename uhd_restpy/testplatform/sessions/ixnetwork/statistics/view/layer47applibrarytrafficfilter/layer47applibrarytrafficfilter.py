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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class Layer47AppLibraryTrafficFilter(Base):
    """Describes the filter for a layer 4-7 AppLibrary Traffic view.
    The Layer47AppLibraryTrafficFilter class encapsulates a list of layer47AppLibraryTrafficFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer47AppLibraryTrafficFilter.find() method.
    The list can be managed by using the Layer47AppLibraryTrafficFilter.add() and Layer47AppLibraryTrafficFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer47AppLibraryTrafficFilter'
    _SDM_ATT_MAP = {
        'AdvancedFilterName': 'advancedFilterName',
        'AllAdvancedFilters': 'allAdvancedFilters',
        'MatchingAdvancedFilters': 'matchingAdvancedFilters',
        'TopxEnabled': 'topxEnabled',
        'TopxValue': 'topxValue',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Layer47AppLibraryTrafficFilter, self).__init__(parent, list_op)

    @property
    def AdvancedFilter(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter.AdvancedFilter): An instance of the AdvancedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter import AdvancedFilter
        if self._properties.get('AdvancedFilter', None) is not None:
            return self._properties.get('AdvancedFilter')
        else:
            return AdvancedFilter(self)

    @property
    def AdvancedFilterName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies an advanced filter from the ones available in the selected drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvancedFilterName'])
    @AdvancedFilterName.setter
    def AdvancedFilterName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdvancedFilterName'], value)

    @property
    def AllAdvancedFilters(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters): Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllAdvancedFilters'])

    @property
    def MatchingAdvancedFilters(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters): Specifies a list that contains only the filters which can be applied on the current drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchingAdvancedFilters'])

    @property
    def TopxEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TopxEnabled'])
    @TopxEnabled.setter
    def TopxEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['TopxEnabled'], value)

    @property
    def TopxValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of rows to be shown when TopXEnabled is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TopxValue'])
    @TopxValue.setter
    def TopxValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TopxValue'], value)

    def update(self, AdvancedFilterName=None, TopxEnabled=None, TopxValue=None):
        # type: (str, bool, int) -> Layer47AppLibraryTrafficFilter
        """Updates layer47AppLibraryTrafficFilter resource on the server.

        Args
        ----
        - AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
        - TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
        - TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvancedFilterName=None, TopxEnabled=None, TopxValue=None):
        # type: (str, bool, int) -> Layer47AppLibraryTrafficFilter
        """Adds a new layer47AppLibraryTrafficFilter resource on the server and adds it to the container.

        Args
        ----
        - AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
        - TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
        - TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

        Returns
        -------
        - self: This instance with all currently retrieved layer47AppLibraryTrafficFilter resources using find and the newly added layer47AppLibraryTrafficFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer47AppLibraryTrafficFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvancedFilterName=None, AllAdvancedFilters=None, MatchingAdvancedFilters=None, TopxEnabled=None, TopxValue=None):
        # type: (str, str, str, bool, int) -> Layer47AppLibraryTrafficFilter
        """Finds and retrieves layer47AppLibraryTrafficFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer47AppLibraryTrafficFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer47AppLibraryTrafficFilter resources from the server.

        Args
        ----
        - AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
        - AllAdvancedFilters (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.
        - MatchingAdvancedFilters (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Specifies a list that contains only the filters which can be applied on the current drill down view.
        - TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
        - TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

        Returns
        -------
        - self: This instance with matching layer47AppLibraryTrafficFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer47AppLibraryTrafficFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer47AppLibraryTrafficFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddAdvancedFilter(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addAdvancedFilter operation on the server.

        NOT DEFINED

        addAdvancedFilter(Arg2=href, async_operation=bool)
        --------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addAdvancedFilter', payload=payload, response_object=None)

    def RemoveAdvancedFilter(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the removeAdvancedFilter operation on the server.

        NOT DEFINED

        removeAdvancedFilter(Arg2=string, async_operation=bool)
        -------------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeAdvancedFilter', payload=payload, response_object=None)

    def RemoveAllAdvancedFilters(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the removeAllAdvancedFilters operation on the server.

        NOT DEFINED

        removeAllAdvancedFilters(async_operation=bool)
        ----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeAllAdvancedFilters', payload=payload, response_object=None)
