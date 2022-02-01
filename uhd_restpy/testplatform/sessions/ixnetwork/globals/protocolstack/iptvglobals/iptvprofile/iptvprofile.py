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


class IptvProfile(Base):
    """
    The IptvProfile class encapsulates a list of iptvProfile resources that are managed by the user.
    A list of resources can be retrieved from the server using the IptvProfile.find() method.
    The list can be managed by using the IptvProfile.add() and IptvProfile.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'iptvProfile'
    _SDM_ATT_MAP = {
        'ChangesBeforeView': 'changesBeforeView',
        'Name': 'name',
        'ObjectId': 'objectId',
        'ViewDuration': 'viewDuration',
        'ZapBehavior': 'zapBehavior',
        'ZapDirection': 'zapDirection',
        'ZapInterval': 'zapInterval',
        'ZapIntervalType': 'zapIntervalType',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(IptvProfile, self).__init__(parent, list_op)

    @property
    def ChangesBeforeView(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of channels to change before stopping on a channel and watching it for View Duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChangesBeforeView'])
    @ChangesBeforeView.setter
    def ChangesBeforeView(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['ChangesBeforeView'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the viewing profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def ViewDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the time in milliseconds to view the last channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ViewDuration'])
    @ViewDuration.setter
    def ViewDuration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['ViewDuration'], value)

    @property
    def ZapBehavior(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ZapBehavior'])
    @ZapBehavior.setter
    def ZapBehavior(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ZapBehavior'], value)

    @property
    def ZapDirection(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the direction of changing channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ZapDirection'])
    @ZapDirection.setter
    def ZapDirection(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ZapDirection'], value)

    @property
    def ZapInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Interval in milliseconds between channel changes based on the selected type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ZapInterval'])
    @ZapInterval.setter
    def ZapInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['ZapInterval'], value)

    @property
    def ZapIntervalType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the wait interval type before changing the channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ZapIntervalType'])
    @ZapIntervalType.setter
    def ZapIntervalType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ZapIntervalType'], value)

    def update(self, ChangesBeforeView=None, Name=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
        # type: (int, str, int, str, str, int, str) -> IptvProfile
        """Updates iptvProfile resource on the server.

        Args
        ----
        - ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
        - Name (str): The name of the viewing profile.
        - ViewDuration (number): Specifies the time in milliseconds to view the last channel.
        - ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
        - ZapDirection (str): Specifies the direction of changing channels.
        - ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
        - ZapIntervalType (str): Specifies the wait interval type before changing the channels.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ChangesBeforeView=None, Name=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
        # type: (int, str, int, str, str, int, str) -> IptvProfile
        """Adds a new iptvProfile resource on the server and adds it to the container.

        Args
        ----
        - ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
        - Name (str): The name of the viewing profile.
        - ViewDuration (number): Specifies the time in milliseconds to view the last channel.
        - ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
        - ZapDirection (str): Specifies the direction of changing channels.
        - ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
        - ZapIntervalType (str): Specifies the wait interval type before changing the channels.

        Returns
        -------
        - self: This instance with all currently retrieved iptvProfile resources using find and the newly added iptvProfile resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained iptvProfile resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ChangesBeforeView=None, Name=None, ObjectId=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
        # type: (int, str, str, int, str, str, int, str) -> IptvProfile
        """Finds and retrieves iptvProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve iptvProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all iptvProfile resources from the server.

        Args
        ----
        - ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
        - Name (str): The name of the viewing profile.
        - ObjectId (str): Unique identifier for this object
        - ViewDuration (number): Specifies the time in milliseconds to view the last channel.
        - ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
        - ZapDirection (str): Specifies the direction of changing channels.
        - ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
        - ZapIntervalType (str): Specifies the wait interval type before changing the channels.

        Returns
        -------
        - self: This instance with matching iptvProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of iptvProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the iptvProfile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
