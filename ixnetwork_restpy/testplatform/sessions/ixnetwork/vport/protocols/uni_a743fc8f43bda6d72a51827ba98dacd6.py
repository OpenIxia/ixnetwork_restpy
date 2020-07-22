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


class Uni(Base):
    """It signifies the user network interface.
    The Uni class encapsulates a list of uni resources that are managed by the user.
    A list of resources can be retrieved from the server using the Uni.find() method.
    The list can be managed by using the Uni.add() and Uni.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'uni'
    _SDM_ATT_MAP = {
        'DataInstance': 'dataInstance',
        'EnablePollingVerificationTimer': 'enablePollingVerificationTimer',
        'Enabled': 'enabled',
        'IsEvcStatusLearnedInfoRefreshed': 'isEvcStatusLearnedInfoRefreshed',
        'IsLmiStatusLearnedInfoRefreshed': 'isLmiStatusLearnedInfoRefreshed',
        'IsUniStatusLearnedInfoRefreshed': 'isUniStatusLearnedInfoRefreshed',
        'Mode': 'mode',
        'OverrideDataInstance': 'overrideDataInstance',
        'OverrideReceiveSequenceNumber': 'overrideReceiveSequenceNumber',
        'OverrideSendSequenceNumber': 'overrideSendSequenceNumber',
        'PollingCounter': 'pollingCounter',
        'PollingTimer': 'pollingTimer',
        'PollingVerificationTimer': 'pollingVerificationTimer',
        'ProtocolInterface': 'protocolInterface',
        'ProtocolVersion': 'protocolVersion',
        'ReceiveSequenceNumber': 'receiveSequenceNumber',
        'SendSequenceNumber': 'sendSequenceNumber',
        'StatusCounter': 'statusCounter',
    }

    def __init__(self, parent):
        super(Uni, self).__init__(parent)

    @property
    def Evc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_12e3717e356bb6d0913adbe6b9aea4e7.Evc): An instance of the Evc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_12e3717e356bb6d0913adbe6b9aea4e7 import Evc
        return Evc(self)

    @property
    def EvcStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_eb384bea866bea4b73a9ada2107b94b7.EvcStatusLearnedInfo): An instance of the EvcStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_eb384bea866bea4b73a9ada2107b94b7 import EvcStatusLearnedInfo
        return EvcStatusLearnedInfo(self)

    @property
    def LmiStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_b4d933ecf6c225cb4a90db642a03bc62.LmiStatusLearnedInfo): An instance of the LmiStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_b4d933ecf6c225cb4a90db642a03bc62 import LmiStatusLearnedInfo
        return LmiStatusLearnedInfo(self)

    @property
    def UniStatus(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_88c46b8136449e97db339c08b836c2b7.UniStatus): An instance of the UniStatus class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_88c46b8136449e97db339c08b836c2b7 import UniStatus
        return UniStatus(self)

    @property
    def UniStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_40034a9c964ba97ae73772fef2dabd7a.UniStatusLearnedInfo): An instance of the UniStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_40034a9c964ba97ae73772fef2dabd7a import UniStatusLearnedInfo
        return UniStatusLearnedInfo(self)

    @property
    def DataInstance(self):
        """
        Returns
        -------
        - number: This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataInstance'])
    @DataInstance.setter
    def DataInstance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataInstance'], value)

    @property
    def EnablePollingVerificationTimer(self):
        """
        Returns
        -------
        - bool: If enabled, it shows the default value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePollingVerificationTimer'])
    @EnablePollingVerificationTimer.setter
    def EnablePollingVerificationTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePollingVerificationTimer'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: It signifies whether the protocol is enabled or disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IsEvcStatusLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: It checks whether the EVC status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEvcStatusLearnedInfoRefreshed'])

    @property
    def IsLmiStatusLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: It checks whether the LMI status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLmiStatusLearnedInfoRefreshed'])

    @property
    def IsUniStatusLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: It checks whether the UNI status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsUniStatusLearnedInfoRefreshed'])

    @property
    def Mode(self):
        """
        Returns
        -------
        - str(uniC | uniN): It is a type of UNI end point.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def OverrideDataInstance(self):
        """
        Returns
        -------
        - bool: If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideDataInstance'])
    @OverrideDataInstance.setter
    def OverrideDataInstance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideDataInstance'], value)

    @property
    def OverrideReceiveSequenceNumber(self):
        """
        Returns
        -------
        - bool: If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideReceiveSequenceNumber'])
    @OverrideReceiveSequenceNumber.setter
    def OverrideReceiveSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideReceiveSequenceNumber'], value)

    @property
    def OverrideSendSequenceNumber(self):
        """
        Returns
        -------
        - bool: If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideSendSequenceNumber'])
    @OverrideSendSequenceNumber.setter
    def OverrideSendSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideSendSequenceNumber'], value)

    @property
    def PollingCounter(self):
        """
        Returns
        -------
        - number: It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollingCounter'])
    @PollingCounter.setter
    def PollingCounter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PollingCounter'], value)

    @property
    def PollingTimer(self):
        """
        Returns
        -------
        - number: The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollingTimer'])
    @PollingTimer.setter
    def PollingTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PollingTimer'], value)

    @property
    def PollingVerificationTimer(self):
        """
        Returns
        -------
        - number: This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollingVerificationTimer'])
    @PollingVerificationTimer.setter
    def PollingVerificationTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PollingVerificationTimer'], value)

    @property
    def ProtocolInterface(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def ProtocolVersion(self):
        """
        Returns
        -------
        - number: This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolVersion'])
    @ProtocolVersion.setter
    def ProtocolVersion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolVersion'], value)

    @property
    def ReceiveSequenceNumber(self):
        """
        Returns
        -------
        - number: This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveSequenceNumber'])
    @ReceiveSequenceNumber.setter
    def ReceiveSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReceiveSequenceNumber'], value)

    @property
    def SendSequenceNumber(self):
        """
        Returns
        -------
        - number: This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSequenceNumber'])
    @SendSequenceNumber.setter
    def SendSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendSequenceNumber'], value)

    @property
    def StatusCounter(self):
        """
        Returns
        -------
        - number: It signifies the count of consecutive errors. Range is 2 10. Default is 4.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StatusCounter'])
    @StatusCounter.setter
    def StatusCounter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StatusCounter'], value)

    def update(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
        """Updates uni resource on the server.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
        """Adds a new uni resource on the server and adds it to the container.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Returns
        -------
        - self: This instance with all currently retrieved uni resources using find and the newly added uni resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained uni resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, IsEvcStatusLearnedInfoRefreshed=None, IsLmiStatusLearnedInfoRefreshed=None, IsUniStatusLearnedInfoRefreshed=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
        """Finds and retrieves uni resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve uni resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all uni resources from the server.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - IsEvcStatusLearnedInfoRefreshed (bool): It checks whether the EVC status learned info is refreshed or not.
        - IsLmiStatusLearnedInfoRefreshed (bool): It checks whether the LMI status learned info is refreshed or not.
        - IsUniStatusLearnedInfoRefreshed (bool): It checks whether the UNI status learned info is refreshed or not.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Returns
        -------
        - self: This instance with matching uni resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of uni data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the uni resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshEvcStatusLearnedInfo(self):
        """Executes the refreshEvcStatusLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshEvcStatusLearnedInfo', payload=payload, response_object=None)

    def RefreshLmiStatusLearnedInfo(self):
        """Executes the refreshLmiStatusLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLmiStatusLearnedInfo', payload=payload, response_object=None)

    def RefreshUniStatusLearnedInfo(self):
        """Executes the refreshUniStatusLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshUniStatusLearnedInfo', payload=payload, response_object=None)
