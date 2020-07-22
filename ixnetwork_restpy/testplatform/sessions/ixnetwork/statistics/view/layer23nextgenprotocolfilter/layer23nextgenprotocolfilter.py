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


class Layer23NextGenProtocolFilter(Base):
    """Describes the filter of next gen protocols for layer 2 and layer 3
    The Layer23NextGenProtocolFilter class encapsulates a list of layer23NextGenProtocolFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23NextGenProtocolFilter.find() method.
    The list can be managed by using the Layer23NextGenProtocolFilter.add() and Layer23NextGenProtocolFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23NextGenProtocolFilter'
    _SDM_ATT_MAP = {
        'AdvancedCVFilter': 'advancedCVFilter',
        'AdvancedFilterName': 'advancedFilterName',
        'AggregationType': 'aggregationType',
        'AllAdvancedFilters': 'allAdvancedFilters',
        'MatchingAdvancedFilters': 'matchingAdvancedFilters',
        'PortFilterIds': 'portFilterIds',
        'ProtocolFilterIds': 'protocolFilterIds',
    }

    def __init__(self, parent):
        super(Layer23NextGenProtocolFilter, self).__init__(parent)

    @property
    def AdvancedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.advancedfilter.advancedfilter.AdvancedFilter): An instance of the AdvancedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.advancedfilter.advancedfilter import AdvancedFilter
        return AdvancedFilter(self)

    @property
    def AvailableAdvancedFilterOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.availableadvancedfilteroptions.availableadvancedfilteroptions.AvailableAdvancedFilterOptions): An instance of the AvailableAdvancedFilterOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.availableadvancedfilteroptions.availableadvancedfilteroptions import AvailableAdvancedFilterOptions
        return AvailableAdvancedFilterOptions(self)

    @property
    def AdvancedCVFilter(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../advancedCVFilters): Sets the advanced filter for a custom view. Note: To change the filter on an existing view, you must first disable it.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvancedCVFilter'])
    @AdvancedCVFilter.setter
    def AdvancedCVFilter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvancedCVFilter'], value)

    @property
    def AdvancedFilterName(self):
        """
        Returns
        -------
        - str: Selects an advanced filter from the ones available in the selected drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvancedFilterName'])
    @AdvancedFilterName.setter
    def AdvancedFilterName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvancedFilterName'], value)

    @property
    def AggregationType(self):
        """
        Returns
        -------
        - str(perPort | perSession): Signifies the type of aggregation of next gen protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregationType'])
    @AggregationType.setter
    def AggregationType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregationType'], value)

    @property
    def AllAdvancedFilters(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters): Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllAdvancedFilters'])

    @property
    def MatchingAdvancedFilters(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters): Returns a list that contains only the filters that can be applied on the current drill down view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchingAdvancedFilters'])

    @property
    def PortFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter]): Filters the port IDs
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortFilterIds'])
    @PortFilterIds.setter
    def PortFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortFilterIds'], value)

    @property
    def ProtocolFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter]): Filters the protocol IDs
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolFilterIds'])
    @ProtocolFilterIds.setter
    def ProtocolFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolFilterIds'], value)

    def update(self, AdvancedCVFilter=None, AdvancedFilterName=None, AggregationType=None, PortFilterIds=None, ProtocolFilterIds=None):
        """Updates layer23NextGenProtocolFilter resource on the server.

        Args
        ----
        - AdvancedCVFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../advancedCVFilters)): Sets the advanced filter for a custom view. Note: To change the filter on an existing view, you must first disable it.
        - AdvancedFilterName (str): Selects an advanced filter from the ones available in the selected drill down view.
        - AggregationType (str(perPort | perSession)): Signifies the type of aggregation of next gen protocols
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Filters the port IDs
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Filters the protocol IDs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvancedCVFilter=None, AdvancedFilterName=None, AggregationType=None, PortFilterIds=None, ProtocolFilterIds=None):
        """Adds a new layer23NextGenProtocolFilter resource on the server and adds it to the container.

        Args
        ----
        - AdvancedCVFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../advancedCVFilters)): Sets the advanced filter for a custom view. Note: To change the filter on an existing view, you must first disable it.
        - AdvancedFilterName (str): Selects an advanced filter from the ones available in the selected drill down view.
        - AggregationType (str(perPort | perSession)): Signifies the type of aggregation of next gen protocols
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Filters the port IDs
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Filters the protocol IDs

        Returns
        -------
        - self: This instance with all currently retrieved layer23NextGenProtocolFilter resources using find and the newly added layer23NextGenProtocolFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23NextGenProtocolFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvancedCVFilter=None, AdvancedFilterName=None, AggregationType=None, AllAdvancedFilters=None, MatchingAdvancedFilters=None, PortFilterIds=None, ProtocolFilterIds=None):
        """Finds and retrieves layer23NextGenProtocolFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23NextGenProtocolFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23NextGenProtocolFilter resources from the server.

        Args
        ----
        - AdvancedCVFilter (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../advancedCVFilters)): Sets the advanced filter for a custom view. Note: To change the filter on an existing view, you must first disable it.
        - AdvancedFilterName (str): Selects an advanced filter from the ones available in the selected drill down view.
        - AggregationType (str(perPort | perSession)): Signifies the type of aggregation of next gen protocols
        - AllAdvancedFilters (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.
        - MatchingAdvancedFilters (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): Returns a list that contains only the filters that can be applied on the current drill down view.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Filters the port IDs
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Filters the protocol IDs

        Returns
        -------
        - self: This instance with matching layer23NextGenProtocolFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23NextGenProtocolFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23NextGenProtocolFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddAdvancedFilter(self, *args, **kwargs):
        """Executes the addAdvancedFilter operation on the server.

        NOT DEFINED

        addAdvancedFilter(Arg2=href)
        ----------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableAdvancedFilters)): NOT DEFINED

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
        """Executes the removeAdvancedFilter operation on the server.

        NOT DEFINED

        removeAdvancedFilter(Arg2=string)
        ---------------------------------
        - Arg2 (str): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeAdvancedFilter', payload=payload, response_object=None)

    def RemoveAllAdvancedFilters(self):
        """Executes the removeAllAdvancedFilters operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('removeAllAdvancedFilters', payload=payload, response_object=None)
