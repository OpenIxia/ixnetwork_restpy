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


class L1Config(Base):
    """Layer 1 (physical) configuration.
    The L1Config class encapsulates a required l1Config resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'l1Config'
    _SDM_ATT_MAP = {
        'CurrentType': 'currentType',
    }
    _SDM_ENUM_MAP = {
        'currentType': ['uhdOneHundredGigLan'],
    }

    def __init__(self, parent, list_op=False):
        super(L1Config, self).__init__(parent, list_op)

    @property
    def OAM(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.oam.oam.OAM): An instance of the OAM class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.oam.oam import OAM
        if len(self._object_properties) > 0:
            if self._properties.get('OAM', None) is not None:
                return self._properties.get('OAM')
        return OAM(self)._select()

    @property
    def FramePreemption(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.framepreemption.framepreemption.FramePreemption): An instance of the FramePreemption class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.framepreemption.framepreemption import FramePreemption
        if len(self._object_properties) > 0:
            if self._properties.get('FramePreemption', None) is not None:
                return self._properties.get('FramePreemption')
        return FramePreemption(self)._select()

    @property
    def RxFilters(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.rxfilters.rxfilters.RxFilters): An instance of the RxFilters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.rxfilters.rxfilters import RxFilters
        if len(self._object_properties) > 0:
            if self._properties.get('RxFilters', None) is not None:
                return self._properties.get('RxFilters')
        return RxFilters(self)._select()

    @property
    def UhdOneHundredGigLan(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.uhdonehundredgiglan.uhdonehundredgiglan.UhdOneHundredGigLan): An instance of the UhdOneHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.l1config.uhdonehundredgiglan.uhdonehundredgiglan import UhdOneHundredGigLan
        if len(self._object_properties) > 0:
            if self._properties.get('UhdOneHundredGigLan', None) is not None:
                return self._properties.get('UhdOneHundredGigLan')
        return UhdOneHundredGigLan(self)._select()

    @property
    def CurrentType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(uhdOneHundredGigLan): Indicates the five types of ports for configuration to choose from.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentType'])
    @CurrentType.setter
    def CurrentType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CurrentType'], value)

    def update(self, CurrentType=None):
        # type: (str) -> L1Config
        """Updates l1Config resource on the server.

        Args
        ----
        - CurrentType (str(uhdOneHundredGigLan)): Indicates the five types of ports for configuration to choose from.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CurrentType=None):
        # type: (str) -> L1Config
        """Finds and retrieves l1Config resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l1Config resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l1Config resources from the server.

        Args
        ----
        - CurrentType (str(uhdOneHundredGigLan)): Indicates the five types of ports for configuration to choose from.

        Returns
        -------
        - self: This instance with matching l1Config resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l1Config data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l1Config resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
