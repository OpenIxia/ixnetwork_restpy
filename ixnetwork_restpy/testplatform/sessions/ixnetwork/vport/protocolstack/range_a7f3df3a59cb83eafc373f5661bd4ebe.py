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


class Range(Base):
    """
    The Range class encapsulates a list of range resources that are managed by the user.
    A list of resources can be retrieved from the server using the Range.find() method.
    The list can be managed by using the Range.add() and Range.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'range'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Range, self).__init__(parent, list_op)

    @property
    def DcbxRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxrange_3845f34b74f71b45e4d9bdbe1b234478.DcbxRange): An instance of the DcbxRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxrange_3845f34b74f71b45e4d9bdbe1b234478 import DcbxRange
        if self._properties.get('DcbxRange', None) is not None:
            return self._properties.get('DcbxRange')
        else:
            return DcbxRange(self)._select()

    @property
    def Dot1xRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_db91f816a2054efcce410ed7df5e0e4f.Dot1xRange): An instance of the Dot1xRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_db91f816a2054efcce410ed7df5e0e4f import Dot1xRange
        if self._properties.get('Dot1xRange', None) is not None:
            return self._properties.get('Dot1xRange')
        else:
            return Dot1xRange(self)

    @property
    def EsmcRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_7b453c43cf804630308245466c9451bb.EsmcRange): An instance of the EsmcRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_7b453c43cf804630308245466c9451bb import EsmcRange
        if self._properties.get('EsmcRange', None) is not None:
            return self._properties.get('EsmcRange')
        else:
            return EsmcRange(self)

    @property
    def MacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_e0a4c431e3395ee28493d6a8ae32ce1e.MacRange): An instance of the MacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_e0a4c431e3395ee28493d6a8ae32ce1e import MacRange
        if self._properties.get('MacRange', None) is not None:
            return self._properties.get('MacRange')
        else:
            return MacRange(self)._select()

    @property
    def PtpRangeOverMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_4c751c56141269db1379159a00082960.PtpRangeOverMac): An instance of the PtpRangeOverMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_4c751c56141269db1379159a00082960 import PtpRangeOverMac
        if self._properties.get('PtpRangeOverMac', None) is not None:
            return self._properties.get('PtpRangeOverMac')
        else:
            return PtpRangeOverMac(self)

    @property
    def VicClientRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_5ceeb7b0fde89281cc5cdc837bcda9ae.VicClientRange): An instance of the VicClientRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_5ceeb7b0fde89281cc5cdc837bcda9ae import VicClientRange
        if self._properties.get('VicClientRange', None) is not None:
            return self._properties.get('VicClientRange')
        else:
            return VicClientRange(self)

    @property
    def VlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_f5b2428576d5bbffc1f2da77c41c18a7.VlanRange): An instance of the VlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_f5b2428576d5bbffc1f2da77c41c18a7 import VlanRange
        if self._properties.get('VlanRange', None) is not None:
            return self._properties.get('VlanRange')
        else:
            return VlanRange(self)._select()

    def add(self):
        """Adds a new range resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved range resources using find and the newly added range resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained range resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all range resources from the server.

        Returns
        -------
        - self: This instance with matching range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the range resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

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

    def DcbxApplyChanges(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxApplyChanges operation on the server.

        Apply DCBX TLV changes on the fly.

        dcbxApplyChanges(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxApplyChanges', payload=payload, response_object=None)

    def DcbxChangeTlv(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxChangeTlv operation on the server.

        Change DCBX TLVs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dcbxChangeTlv(Arg2=bool, Arg3=bool, Arg4=bool, async_operation=bool)
        --------------------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - Arg3 (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - Arg4 (bool): Indicates whether this feature accepts its configuration from the peer or not.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        dcbxChangeTlv(Arg2=bool, Arg3=bool, Arg4=bool, Arg5=enum, async_operation=bool)
        -------------------------------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - Arg3 (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - Arg4 (bool): Indicates whether this feature accepts its configuration from the peer or not.
        - Arg5 (str(async | sync)): Indicates whether the DCB feature is enabled or not.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxChangeTlv', payload=payload, response_object=None)

    def DcbxDisableTlv(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxDisableTlv operation on the server.

        Disable DCBX TLVs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dcbxDisableTlv(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        dcbxDisableTlv(Arg2=enum, async_operation=bool)
        -----------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxDisableTlv', payload=payload, response_object=None)

    def DcbxEnableTlv(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxEnableTlv operation on the server.

        Enable DCBX TLVs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dcbxEnableTlv(async_operation=bool)
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        dcbxEnableTlv(Arg2=enum, async_operation=bool)
        ----------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxEnableTlv', payload=payload, response_object=None)

    def DcbxStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxStart operation on the server.

        Start DCBX

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dcbxStart(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        dcbxStart(Arg2=enum, async_operation=bool)
        ------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxStart', payload=payload, response_object=None)

    def DcbxStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the dcbxStop operation on the server.

        Stop DCBX

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dcbxStop(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        dcbxStop(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dcbxStop', payload=payload, response_object=None)

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

    def LldpStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the lldpStart operation on the server.

        Start LLDP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        lldpStart(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        lldpStart(Arg2=enum, async_operation=bool)
        ------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('lldpStart', payload=payload, response_object=None)

    def LldpStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the lldpStop operation on the server.

        Stop LLDP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        lldpStop(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        lldpStop(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('lldpStop', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Negotiate sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(Arg2=enum, async_operation=bool)
        --------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Teardown sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(Arg2=enum, async_operation=bool)
        -------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
