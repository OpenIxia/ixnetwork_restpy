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


class TlvSettings(Base):
    """DCBX TLV settings
    The TlvSettings class encapsulates a required tlvSettings resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "tlvSettings"
    _SDM_ATT_MAP = {
        "ObjectId": "objectId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TlvSettings, self).__init__(parent, list_op)

    @property
    def DcbxTlvAppQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_02a35dfd3b5f648c7f668c46bd448d56.DcbxTlvAppQaz): An instance of the DcbxTlvAppQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_02a35dfd3b5f648c7f668c46bd448d56 import (
            DcbxTlvAppQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvAppQaz", None) is not None:
                return self._properties.get("DcbxTlvAppQaz")
        return DcbxTlvAppQaz(self)._select()

    @property
    def DcbxTlvBcn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_a1a91400db1d9914d85f42e65e5fca2b.DcbxTlvBcn): An instance of the DcbxTlvBcn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_a1a91400db1d9914d85f42e65e5fca2b import (
            DcbxTlvBcn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvBcn", None) is not None:
                return self._properties.get("DcbxTlvBcn")
        return DcbxTlvBcn(self)._select()

    @property
    def DcbxTlvCustom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_b8d4729d6e36738e0b8dea24089fa803.DcbxTlvCustom): An instance of the DcbxTlvCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_b8d4729d6e36738e0b8dea24089fa803 import (
            DcbxTlvCustom,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvCustom", None) is not None:
                return self._properties.get("DcbxTlvCustom")
        return DcbxTlvCustom(self)._select()

    @property
    def DcbxTlvEtsQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_721d7b3f4bd0a8d3b1cf166224740621.DcbxTlvEtsQaz): An instance of the DcbxTlvEtsQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_721d7b3f4bd0a8d3b1cf166224740621 import (
            DcbxTlvEtsQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvEtsQaz", None) is not None:
                return self._properties.get("DcbxTlvEtsQaz")
        return DcbxTlvEtsQaz(self)._select()

    @property
    def DcbxTlvFcoeIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_221a9d9374d868c351a083f39264f5c2.DcbxTlvFcoeIeee): An instance of the DcbxTlvFcoeIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_221a9d9374d868c351a083f39264f5c2 import (
            DcbxTlvFcoeIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvFcoeIeee", None) is not None:
                return self._properties.get("DcbxTlvFcoeIeee")
        return DcbxTlvFcoeIeee(self)._select()

    @property
    def DcbxTlvFcoeIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_49a1ef98a6702422b88b29433daab98c.DcbxTlvFcoeIntel): An instance of the DcbxTlvFcoeIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_49a1ef98a6702422b88b29433daab98c import (
            DcbxTlvFcoeIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvFcoeIntel", None) is not None:
                return self._properties.get("DcbxTlvFcoeIntel")
        return DcbxTlvFcoeIntel(self)._select()

    @property
    def DcbxTlvLogicalLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_4c1f796d4253ef800f469182f860034e.DcbxTlvLogicalLink): An instance of the DcbxTlvLogicalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_4c1f796d4253ef800f469182f860034e import (
            DcbxTlvLogicalLink,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvLogicalLink", None) is not None:
                return self._properties.get("DcbxTlvLogicalLink")
        return DcbxTlvLogicalLink(self)._select()

    @property
    def DcbxTlvNivIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_bfda4ebaca3805fd204108031bec7a2c.DcbxTlvNivIeee): An instance of the DcbxTlvNivIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_bfda4ebaca3805fd204108031bec7a2c import (
            DcbxTlvNivIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvNivIeee", None) is not None:
                return self._properties.get("DcbxTlvNivIeee")
        return DcbxTlvNivIeee(self)._select()

    @property
    def DcbxTlvNivIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_9bc6d9fd29e6e3c4fb53c1924f821086.DcbxTlvNivIntel): An instance of the DcbxTlvNivIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_9bc6d9fd29e6e3c4fb53c1924f821086 import (
            DcbxTlvNivIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvNivIntel", None) is not None:
                return self._properties.get("DcbxTlvNivIntel")
        return DcbxTlvNivIntel(self)._select()

    @property
    def DcbxTlvPfcIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_5859cbed593a119684ed73bad3546ba3.DcbxTlvPfcIeee): An instance of the DcbxTlvPfcIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_5859cbed593a119684ed73bad3546ba3 import (
            DcbxTlvPfcIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcIeee", None) is not None:
                return self._properties.get("DcbxTlvPfcIeee")
        return DcbxTlvPfcIeee(self)._select()

    @property
    def DcbxTlvPfcIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_aafbda8e30a51d7a9024ecc7f6790159.DcbxTlvPfcIntel): An instance of the DcbxTlvPfcIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_aafbda8e30a51d7a9024ecc7f6790159 import (
            DcbxTlvPfcIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcIntel", None) is not None:
                return self._properties.get("DcbxTlvPfcIntel")
        return DcbxTlvPfcIntel(self)._select()

    @property
    def DcbxTlvPfcQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_ee356b2f3ec6d2356abbb8171f736027.DcbxTlvPfcQaz): An instance of the DcbxTlvPfcQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_ee356b2f3ec6d2356abbb8171f736027 import (
            DcbxTlvPfcQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcQaz", None) is not None:
                return self._properties.get("DcbxTlvPfcQaz")
        return DcbxTlvPfcQaz(self)._select()

    @property
    def DcbxTlvPgIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_fe6ebf156acf4a283f3e8df9f75b9783.DcbxTlvPgIeee): An instance of the DcbxTlvPgIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_fe6ebf156acf4a283f3e8df9f75b9783 import (
            DcbxTlvPgIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPgIeee", None) is not None:
                return self._properties.get("DcbxTlvPgIeee")
        return DcbxTlvPgIeee(self)._select()

    @property
    def DcbxTlvPgIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_c3943ff77b2764ca73fd9869d6fcd7c8.DcbxTlvPgIntel): An instance of the DcbxTlvPgIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_c3943ff77b2764ca73fd9869d6fcd7c8 import (
            DcbxTlvPgIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPgIntel", None) is not None:
                return self._properties.get("DcbxTlvPgIntel")
        return DcbxTlvPgIntel(self)._select()

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    def find(self, ObjectId=None):
        # type: (str) -> TlvSettings
        """Finds and retrieves tlvSettings resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tlvSettings resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tlvSettings resources from the server.

        Args
        ----
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching tlvSettings resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tlvSettings data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tlvSettings resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
