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


class CakCache(Base):
    """CAK Cache configuration.
    The CakCache class encapsulates a required cakCache resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cakCache"
    _SDM_ATT_MAP = {
        "CakName": "cakName",
        "CakValue128": "cakValue128",
        "CakValue256": "cakValue256",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "KeyDuration": "keyDuration",
        "KeyStartTime": "keyStartTime",
        "LifetimeValidity": "lifetimeValidity",
        "MemberIdentifier": "memberIdentifier",
        "Name": "name",
        "OverlappingKeys": "overlappingKeys",
        "ParticipantState": "participantState",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CakCache, self).__init__(parent, list_op)

    @property
    def CakName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes CAK Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CakName"]))

    @property
    def CakValue128(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the 128 bit CAK value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CakValue128"]))

    @property
    def CakValue256(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines the 256 bit CAK value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CakValue256"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def KeyDuration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the user to configure the duration of this key. The timer values are relative to the Test Start Time configured in MKA port properties.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyDuration"]))

    @property
    def KeyStartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the user to configure the Start Time of this key. The timer values are relative to the Test Start Time configured in MKA port properties.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyStartTime"]))

    @property
    def LifetimeValidity(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Determines whether the CAK, CKN tuple expires or not. If enabled, the key will never expire.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LifetimeValidity"])
        )

    @property
    def MemberIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - list(obj(ixnetwork_restpy.multivalue.Multivalue)): Displays the Member Identifier calculated by the state machine for this MKA participant.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MemberIdentifier"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def OverlappingKeys(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this box is un-checked, then the current key will expire on the activation of the next key.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverlappingKeys"])

    @OverlappingKeys.setter
    def OverlappingKeys(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverlappingKeys"], value)

    @property
    def ParticipantState(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[active | activePrincipalActor | activeSuccessfulActor | expired | inactive | none]): Displays the state of this participant for this device (KaY).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ParticipantState"])

    def update(self, Name=None, OverlappingKeys=None):
        # type: (str, bool) -> CakCache
        """Updates cakCache resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OverlappingKeys (bool): If this box is un-checked, then the current key will expire on the activation of the next key.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        OverlappingKeys=None,
        ParticipantState=None,
    ):
        # type: (int, str, str, bool, List[str]) -> CakCache
        """Finds and retrieves cakCache resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cakCache resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cakCache resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OverlappingKeys (bool): If this box is un-checked, then the current key will expire on the activation of the next key.
        - ParticipantState (list(str[active | activePrincipalActor | activeSuccessfulActor | expired | inactive | none])): Displays the state of this participant for this device (KaY).

        Returns
        -------
        - self: This instance with matching cakCache resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cakCache data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cakCache resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        CakName=None,
        CakValue128=None,
        CakValue256=None,
        KeyDuration=None,
        KeyStartTime=None,
        LifetimeValidity=None,
        MemberIdentifier=None,
    ):
        """Base class infrastructure that gets a list of cakCache device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - CakName (str): optional regex of cakName
        - CakValue128 (str): optional regex of cakValue128
        - CakValue256 (str): optional regex of cakValue256
        - KeyDuration (str): optional regex of keyDuration
        - KeyStartTime (str): optional regex of keyStartTime
        - LifetimeValidity (str): optional regex of lifetimeValidity
        - MemberIdentifier (str): optional regex of memberIdentifier

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
