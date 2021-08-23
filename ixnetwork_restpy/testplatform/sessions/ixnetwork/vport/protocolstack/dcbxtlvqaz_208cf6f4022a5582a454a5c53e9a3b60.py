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
from typing import List, Any, Union


class DcbxTlvQaz(Base):
    """DCBX TLV 802.1Qaz (Type-Length-Value)
    The DcbxTlvQaz class encapsulates a list of dcbxTlvQaz resources that are managed by the user.
    A list of resources can be retrieved from the server using the DcbxTlvQaz.find() method.
    The list can be managed by using the DcbxTlvQaz.add() and DcbxTlvQaz.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlvQaz'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'FeatureType': 'featureType',
        'Name': 'name',
        'ObjectId': 'objectId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(DcbxTlvQaz, self).__init__(parent, list_op)

    @property
    def TlvSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_ad441434443552a20b710e8a8150e89e.TlvSettings): An instance of the TlvSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_ad441434443552a20b710e8a8150e89e import TlvSettings
        if self._properties.get('TlvSettings', None) is not None:
            return self._properties.get('TlvSettings')
        else:
            return TlvSettings(self)._select()

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Specifies if this TLV is used in the configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FeatureType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FeatureType'])
    @FeatureType.setter
    def FeatureType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FeatureType'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of TLV
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

    def update(self, Enabled=None, FeatureType=None, Name=None):
        # type: (bool, int, str) -> DcbxTlvQaz
        """Updates dcbxTlvQaz resource on the server.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - Name (str): Name of TLV

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, FeatureType=None, Name=None):
        # type: (bool, int, str) -> DcbxTlvQaz
        """Adds a new dcbxTlvQaz resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - Name (str): Name of TLV

        Returns
        -------
        - self: This instance with all currently retrieved dcbxTlvQaz resources using find and the newly added dcbxTlvQaz resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dcbxTlvQaz resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FeatureType=None, Name=None, ObjectId=None):
        # type: (bool, int, str, str) -> DcbxTlvQaz
        """Finds and retrieves dcbxTlvQaz resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlvQaz resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlvQaz resources from the server.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - Name (str): Name of TLV
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching dcbxTlvQaz resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlvQaz data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlvQaz resources from the server available through an iterator or index

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
