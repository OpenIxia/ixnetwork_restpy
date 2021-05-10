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


class DcbxTlv(Base):
    """DCBX TLV (Type-Length-Value)
    The DcbxTlv class encapsulates a list of dcbxTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the DcbxTlv.find() method.
    The list can be managed by using the DcbxTlv.add() and DcbxTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dcbxTlv'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'Error': 'error',
        'ErrorOverride': 'errorOverride',
        'FeatureEnable': 'featureEnable',
        'FeatureType': 'featureType',
        'MaxVersion': 'maxVersion',
        'Name': 'name',
        'ObjectId': 'objectId',
        'SubType': 'subType',
        'Willing': 'willing',
    }

    def __init__(self, parent):
        super(DcbxTlv, self).__init__(parent)

    @property
    def TlvSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_9ee7f0bbd6252892487709b1e2bd344a.TlvSettings): An instance of the TlvSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_9ee7f0bbd6252892487709b1e2bd344a import TlvSettings
        return TlvSettings(self)._select()

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Specifies if this TLV is used in the configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Error(self):
        """
        Returns
        -------
        - bool: Indicates that an error has occurred during the configuration exchange with the peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Error'])
    @Error.setter
    def Error(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Error'], value)

    @property
    def ErrorOverride(self):
        """
        Returns
        -------
        - bool: True to override the error bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorOverride'])
    @ErrorOverride.setter
    def ErrorOverride(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ErrorOverride'], value)

    @property
    def FeatureEnable(self):
        """
        Returns
        -------
        - bool: Indicates whether the DCB feature is enabled or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FeatureEnable'])
    @FeatureEnable.setter
    def FeatureEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FeatureEnable'], value)

    @property
    def FeatureType(self):
        """
        Returns
        -------
        - number: Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FeatureType'])
    @FeatureType.setter
    def FeatureType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FeatureType'], value)

    @property
    def MaxVersion(self):
        """
        Returns
        -------
        - number: Highest feature version supported by the system.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxVersion'])
    @MaxVersion.setter
    def MaxVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxVersion'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of TLV
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SubType(self):
        """
        Returns
        -------
        - number: Indicates specific types of network traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubType'])
    @SubType.setter
    def SubType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubType'], value)

    @property
    def Willing(self):
        """
        Returns
        -------
        - bool: Indicates whether this feature accepts its configuration from the peer or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Willing'])
    @Willing.setter
    def Willing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Willing'], value)

    def update(self, Enabled=None, Error=None, ErrorOverride=None, FeatureEnable=None, FeatureType=None, MaxVersion=None, Name=None, SubType=None, Willing=None):
        """Updates dcbxTlv resource on the server.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): True to override the error bit.
        - FeatureEnable (bool): Indicates whether the DCB feature is enabled or not.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - MaxVersion (number): Highest feature version supported by the system.
        - Name (str): Name of TLV
        - SubType (number): Indicates specific types of network traffic.
        - Willing (bool): Indicates whether this feature accepts its configuration from the peer or not.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, Error=None, ErrorOverride=None, FeatureEnable=None, FeatureType=None, MaxVersion=None, Name=None, SubType=None, Willing=None):
        """Adds a new dcbxTlv resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): True to override the error bit.
        - FeatureEnable (bool): Indicates whether the DCB feature is enabled or not.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - MaxVersion (number): Highest feature version supported by the system.
        - Name (str): Name of TLV
        - SubType (number): Indicates specific types of network traffic.
        - Willing (bool): Indicates whether this feature accepts its configuration from the peer or not.

        Returns
        -------
        - self: This instance with all currently retrieved dcbxTlv resources using find and the newly added dcbxTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dcbxTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, Error=None, ErrorOverride=None, FeatureEnable=None, FeatureType=None, MaxVersion=None, Name=None, ObjectId=None, SubType=None, Willing=None):
        """Finds and retrieves dcbxTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlv resources from the server.

        Args
        ----
        - Enabled (bool): Specifies if this TLV is used in the configuration.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): True to override the error bit.
        - FeatureEnable (bool): Indicates whether the DCB feature is enabled or not.
        - FeatureType (number): Type code of the DCB Feature. The codes translate to: 2 - Priority Group 3 - PFC 4 - Application (IEEE 1.01) / Custom(BCN) (Intel 1.0) 5 - Custom (IEEE 1.01) / FCoE (Intel 1.0) 6 - Custom (IEEE 1.01) / Logical Link (Intel 1.0) 7 - NIV 8 - Custom (IEEE 1.01 / Intel 1.0) 9/10 - Custom (IEEE 1.01 / Intel 1.0) / ETS Configuration/Recommendation (802.1Qaz) 11 - Custom (IEEE 1.01 / Intel 1.0) / PFC (802.1Qaz) 12 - Custom (IEEE 1.01 / Intel 1.0) / Application Priority (802.1Qaz) 13 to 127 - Custom (IEEE 1.01 / Intel 1.0)
        - MaxVersion (number): Highest feature version supported by the system.
        - Name (str): Name of TLV
        - ObjectId (str): Unique identifier for this object
        - SubType (number): Indicates specific types of network traffic.
        - Willing (bool): Indicates whether this feature accepts its configuration from the peer or not.

        Returns
        -------
        - self: This instance with matching dcbxTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

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
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
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
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
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
