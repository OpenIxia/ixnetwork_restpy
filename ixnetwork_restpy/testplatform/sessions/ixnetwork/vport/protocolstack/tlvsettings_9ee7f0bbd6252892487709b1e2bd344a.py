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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_587acb2c8baf495ea66170032055878b.DcbxTlvAppQaz): An instance of the DcbxTlvAppQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_587acb2c8baf495ea66170032055878b import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_3b81386afeb068318a1e62f02a9da5dd.DcbxTlvBcn): An instance of the DcbxTlvBcn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_3b81386afeb068318a1e62f02a9da5dd import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_03275859075c4e6ed702cf66d51cacbc.DcbxTlvCustom): An instance of the DcbxTlvCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_03275859075c4e6ed702cf66d51cacbc import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_04e4d4f9220135fb169caf1f82c3c682.DcbxTlvEtsQaz): An instance of the DcbxTlvEtsQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_04e4d4f9220135fb169caf1f82c3c682 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_96a877200349714c34d4895d720d0bc7.DcbxTlvFcoeIeee): An instance of the DcbxTlvFcoeIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_96a877200349714c34d4895d720d0bc7 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_fcf0f6f5e7ff409ce4a32c93cedee9fd.DcbxTlvFcoeIntel): An instance of the DcbxTlvFcoeIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_fcf0f6f5e7ff409ce4a32c93cedee9fd import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_d04b8ac5be821679d2c562369f7becc9.DcbxTlvLogicalLink): An instance of the DcbxTlvLogicalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_d04b8ac5be821679d2c562369f7becc9 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_f8a4eea5f43c15671e2ae0b7270b8d8c.DcbxTlvNivIeee): An instance of the DcbxTlvNivIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_f8a4eea5f43c15671e2ae0b7270b8d8c import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_e737a38b76044a795c7ed858b1a2213d.DcbxTlvNivIntel): An instance of the DcbxTlvNivIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_e737a38b76044a795c7ed858b1a2213d import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_bd7d08517c4bada6e40073649c4b169b.DcbxTlvPfcIeee): An instance of the DcbxTlvPfcIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_bd7d08517c4bada6e40073649c4b169b import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_54c442933f28122b24622c86a570f5d1.DcbxTlvPfcIntel): An instance of the DcbxTlvPfcIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_54c442933f28122b24622c86a570f5d1 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_0e854f66d9d6ebece1b3ef2e12724a53.DcbxTlvPfcQaz): An instance of the DcbxTlvPfcQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_0e854f66d9d6ebece1b3ef2e12724a53 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_06160cc09161a4199f2eb699e1d29b17.DcbxTlvPgIeee): An instance of the DcbxTlvPgIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_06160cc09161a4199f2eb699e1d29b17 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_dee71f02fca764a8d3616fac2380ec93.DcbxTlvPgIntel): An instance of the DcbxTlvPgIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_dee71f02fca764a8d3616fac2380ec93 import (
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
