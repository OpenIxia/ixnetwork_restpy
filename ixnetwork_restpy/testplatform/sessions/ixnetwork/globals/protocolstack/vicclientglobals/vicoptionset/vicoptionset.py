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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class VicOptionSet(Base):
    """Defines a group of TLV options.
    The VicOptionSet class encapsulates a list of vicOptionSet resources that are managed by the user.
    A list of resources can be retrieved from the server using the VicOptionSet.find() method.
    The list can be managed by using the VicOptionSet.add() and VicOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "vicOptionSet"
    _SDM_ATT_MAP = {
        "Defaultp": "defaultp",
        "FeatureType": "featureType",
        "Name": "name",
        "ObjectId": "objectId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(VicOptionSet, self).__init__(parent, list_op)

    @property
    def VicOptionTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptiontlv.vicoptiontlv.VicOptionTlv): An instance of the VicOptionTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptiontlv.vicoptiontlv import (
            VicOptionTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VicOptionTlv", None) is not None:
                return self._properties.get("VicOptionTlv")
        return VicOptionTlv(self)

    @property
    def Defaultp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: True to assign this option set to new ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Defaultp"])

    @Defaultp.setter
    def Defaultp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Defaultp"], value)

    @property
    def FeatureType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The usage purpose of this TLV set.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureType"])

    @FeatureType.setter
    def FeatureType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureType"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Option set name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    def update(self, Defaultp=None, FeatureType=None, Name=None):
        # type: (bool, int, str) -> VicOptionSet
        """Updates vicOptionSet resource on the server.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - FeatureType (number): The usage purpose of this TLV set.
        - Name (str): Option set name.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Defaultp=None, FeatureType=None, Name=None):
        # type: (bool, int, str) -> VicOptionSet
        """Adds a new vicOptionSet resource on the server and adds it to the container.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - FeatureType (number): The usage purpose of this TLV set.
        - Name (str): Option set name.

        Returns
        -------
        - self: This instance with all currently retrieved vicOptionSet resources using find and the newly added vicOptionSet resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vicOptionSet resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, FeatureType=None, Name=None, ObjectId=None):
        # type: (bool, int, str, str) -> VicOptionSet
        """Finds and retrieves vicOptionSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vicOptionSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vicOptionSet resources from the server.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - FeatureType (number): The usage purpose of this TLV set.
        - Name (str): Option set name.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching vicOptionSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vicOptionSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vicOptionSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
