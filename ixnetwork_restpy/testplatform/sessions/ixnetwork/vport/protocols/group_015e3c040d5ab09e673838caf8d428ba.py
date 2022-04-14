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


class Group(Base):
    """A group is a list of action buckets and some means of choosing one or more of those buckets to apply on a per-packet basis. A group table consists of group entries. The ability for a flow entry to point to a group enables OpenFlow to represent additional methods of forwarding
    The Group class encapsulates a list of group resources that are managed by the user.
    A list of resources can be retrieved from the server using the Group.find() method.
    The list can be managed by using the Group.add() and Group.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "group"
    _SDM_ATT_MAP = {
        "Id__": "__id__",
        "Description": "description",
        "Enabled": "enabled",
        "GroupAdvertise": "groupAdvertise",
        "Type": "type",
        "UpdateGroupModStatus": "updateGroupModStatus",
    }
    _SDM_ENUM_MAP = {
        "type": ["all", "select", "indirect", "fastFailover"],
    }

    def __init__(self, parent, list_op=False):
        super(Group, self).__init__(parent, list_op)

    @property
    def Bucket(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucket_70fad76e12d52147154e1637a004a478.Bucket): An instance of the Bucket class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucket_70fad76e12d52147154e1637a004a478 import (
            Bucket,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bucket", None) is not None:
                return self._properties.get("Bucket")
        return Bucket(self)

    @property
    def Id__(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
        """
        return self._get_attribute(self._SDM_ATT_MAP["Id__"])

    @Id__.setter
    def Id__(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Id__"], value)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A description of the group is shown
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Description"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, this group is used in this controller configuration. The default value is False.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GroupAdvertise(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAdvertise"])

    @GroupAdvertise.setter
    def GroupAdvertise(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupAdvertise"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(all | select | indirect | fastFailover): Select the type to determine the group semantics.The default Value is all.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    @property
    def UpdateGroupModStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is a read-only field which indicates if any group is changed in the GUI. If any group is changed then this status indicates to the user to send a Group MOD request to the switch so that the changed value is updated in switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdateGroupModStatus"])

    def update(
        self, Id__=None, Description=None, Enabled=None, GroupAdvertise=None, Type=None
    ):
        # type: (int, str, bool, bool, str) -> Group
        """Updates group resource on the server.

        Args
        ----
        - Id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
        - Description (str): A description of the group is shown
        - Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
        - GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
        - Type (str(all | select | indirect | fastFailover)): Select the type to determine the group semantics.The default Value is all.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self, Id__=None, Description=None, Enabled=None, GroupAdvertise=None, Type=None
    ):
        # type: (int, str, bool, bool, str) -> Group
        """Adds a new group resource on the server and adds it to the container.

        Args
        ----
        - Id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
        - Description (str): A description of the group is shown
        - Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
        - GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
        - Type (str(all | select | indirect | fastFailover)): Select the type to determine the group semantics.The default Value is all.

        Returns
        -------
        - self: This instance with all currently retrieved group resources using find and the newly added group resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained group resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Id__=None,
        Description=None,
        Enabled=None,
        GroupAdvertise=None,
        Type=None,
        UpdateGroupModStatus=None,
    ):
        # type: (int, str, bool, bool, str, str) -> Group
        """Finds and retrieves group resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve group resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all group resources from the server.

        Args
        ----
        - Id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
        - Description (str): A description of the group is shown
        - Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
        - GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
        - Type (str(all | select | indirect | fastFailover)): Select the type to determine the group semantics.The default Value is all.
        - UpdateGroupModStatus (str): It is a read-only field which indicates if any group is changed in the GUI. If any group is changed then this status indicates to the user to send a Group MOD request to the switch so that the changed value is updated in switch.

        Returns
        -------
        - self: This instance with matching group resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of group data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the group resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateGroupMod(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the updateGroupMod operation on the server.

        NOT DEFINED

        updateGroupMod(Arg2=enum, async_operation=bool)bool
        ---------------------------------------------------
        - Arg2 (str(sendGroupAdd | sendGroupModify | sendGroupRemove)): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("updateGroupMod", payload=payload, response_object=None)
