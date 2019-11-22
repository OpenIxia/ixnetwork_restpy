# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class EgtpS11SgwRange(Base):
    """
    The EgtpS11SgwRange class encapsulates a required egtpS11SgwRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpS11SgwRange'

    def __init__(self, parent):
        super(EgtpS11SgwRange, self).__init__(parent)

    @property
    def CpIpRange(self):
        """An instance of the CpIpRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpiprange_2d2dc54cb792d683ff17aa471d9a8091.CpIpRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpiprange_2d2dc54cb792d683ff17aa471d9a8091 import CpIpRange
        return CpIpRange(self)._select()

    @property
    def CpMacRange(self):
        """An instance of the CpMacRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpmacrange_c5c3aa2b373339d88e6f8c8b2e1256a3.CpMacRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpmacrange_c5c3aa2b373339d88e6f8c8b2e1256a3 import CpMacRange
        return CpMacRange(self)._select()

    @property
    def CpVlanRange(self):
        """An instance of the CpVlanRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpvlanrange_d8b57f66559d190d0f38bce11b93a3f9.CpVlanRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpvlanrange_d8b57f66559d190d0f38bce11b93a3f9 import CpVlanRange
        return CpVlanRange(self)._select()

    @property
    def UpIpRange(self):
        """An instance of the UpIpRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upiprange_94cf7e83dd3167351c37182e5b16f23b.UpIpRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upiprange_94cf7e83dd3167351c37182e5b16f23b import UpIpRange
        return UpIpRange(self)._select()

    @property
    def UpMacRange(self):
        """An instance of the UpMacRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upmacrange_c1df72d32e01c63bd145bd4233ab30fb.UpMacRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upmacrange_c1df72d32e01c63bd145bd4233ab30fb import UpMacRange
        return UpMacRange(self)._select()

    @property
    def UpVlanRange(self):
        """An instance of the UpVlanRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upvlanrange_fabc7254a11c1f1749de3b278b50dfe4.UpVlanRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upvlanrange_fabc7254a11c1f1749de3b278b50dfe4 import UpVlanRange
        return UpVlanRange(self)._select()

    @property
    def ChangeReportingMode(self):
        """OBSOLETE: Use changeReportingList instead.

        Returns:
            number
        """
        return self._get_attribute('changeReportingMode')
    @ChangeReportingMode.setter
    def ChangeReportingMode(self, value):
        self._set_attribute('changeReportingMode', value)

    @property
    def ControlPlaneLbType(self):
        """The type of Control Plane load balancing used. * For R1, the Create Session Response is sent from the slave SGW. * For R2, the Create Session Response is sent from the controller SGW.

        Returns:
            str
        """
        return self._get_attribute('controlPlaneLbType')
    @ControlPlaneLbType.setter
    def ControlPlaneLbType(self, value):
        self._set_attribute('controlPlaneLbType', value)

    @property
    def EnableEchoRequest(self):
        """Set to true to send echo request

        Returns:
            bool
        """
        return self._get_attribute('enableEchoRequest')
    @EnableEchoRequest.setter
    def EnableEchoRequest(self, value):
        self._set_attribute('enableEchoRequest', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IpType(self):
        """The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def N3CreateBearerReq(self):
        """Number of retransmissions for Create Bearer request

        Returns:
            number
        """
        return self._get_attribute('n3CreateBearerReq')
    @N3CreateBearerReq.setter
    def N3CreateBearerReq(self, value):
        self._set_attribute('n3CreateBearerReq', value)

    @property
    def N3DeleteBearerReq(self):
        """Number of retransmissions for Delete Bearer request

        Returns:
            number
        """
        return self._get_attribute('n3DeleteBearerReq')
    @N3DeleteBearerReq.setter
    def N3DeleteBearerReq(self, value):
        self._set_attribute('n3DeleteBearerReq', value)

    @property
    def N3EchoReq(self):
        """Number of retransmissions for Echo request

        Returns:
            number
        """
        return self._get_attribute('n3EchoReq')
    @N3EchoReq.setter
    def N3EchoReq(self, value):
        self._set_attribute('n3EchoReq', value)

    @property
    def N3MmeHandoverInProgress(self):
        """Number of retransmissions for MME Handover in Progress response cause

        Returns:
            number
        """
        return self._get_attribute('n3MmeHandoverInProgress')
    @N3MmeHandoverInProgress.setter
    def N3MmeHandoverInProgress(self, value):
        self._set_attribute('n3MmeHandoverInProgress', value)

    @property
    def N3UpdateBearerReq(self):
        """Number of retransmissions for Update Bearer request

        Returns:
            number
        """
        return self._get_attribute('n3UpdateBearerReq')
    @N3UpdateBearerReq.setter
    def N3UpdateBearerReq(self, value):
        self._set_attribute('n3UpdateBearerReq', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def T3CreateBearerReq(self):
        """Response timeout for a Create Bearer request (seconds)

        Returns:
            number
        """
        return self._get_attribute('t3CreateBearerReq')
    @T3CreateBearerReq.setter
    def T3CreateBearerReq(self, value):
        self._set_attribute('t3CreateBearerReq', value)

    @property
    def T3DeleteBearerReq(self):
        """Response timeout for a Delete Bearer request (seconds)

        Returns:
            number
        """
        return self._get_attribute('t3DeleteBearerReq')
    @T3DeleteBearerReq.setter
    def T3DeleteBearerReq(self, value):
        self._set_attribute('t3DeleteBearerReq', value)

    @property
    def T3EchoReq(self):
        """Response timeout for a Echo request (seconds).

        Returns:
            number
        """
        return self._get_attribute('t3EchoReq')
    @T3EchoReq.setter
    def T3EchoReq(self, value):
        self._set_attribute('t3EchoReq', value)

    @property
    def T3MmeHandoverInProgress(self):
        """Retry timeout for a MME Handover in Progress response cause (seconds).

        Returns:
            number
        """
        return self._get_attribute('t3MmeHandoverInProgress')
    @T3MmeHandoverInProgress.setter
    def T3MmeHandoverInProgress(self, value):
        self._set_attribute('t3MmeHandoverInProgress', value)

    @property
    def T3UpdateBearerReq(self):
        """Response timeout for a Update Bearer request (seconds)

        Returns:
            number
        """
        return self._get_attribute('t3UpdateBearerReq')
    @T3UpdateBearerReq.setter
    def T3UpdateBearerReq(self, value):
        self._set_attribute('t3UpdateBearerReq', value)

    @property
    def UseCpIp(self):
        """Use Control Plane Load Balancer

        Returns:
            bool
        """
        return self._get_attribute('useCpIp')
    @UseCpIp.setter
    def UseCpIp(self, value):
        self._set_attribute('useCpIp', value)

    @property
    def UseUpIp(self):
        """Use User Plane Load Balancer

        Returns:
            bool
        """
        return self._get_attribute('useUpIp')
    @UseUpIp.setter
    def UseUpIp(self, value):
        self._set_attribute('useUpIp', value)

    def update(self, ChangeReportingMode=None, ControlPlaneLbType=None, EnableEchoRequest=None, Enabled=None, IpType=None, N3CreateBearerReq=None, N3DeleteBearerReq=None, N3EchoReq=None, N3MmeHandoverInProgress=None, N3UpdateBearerReq=None, Name=None, T3CreateBearerReq=None, T3DeleteBearerReq=None, T3EchoReq=None, T3MmeHandoverInProgress=None, T3UpdateBearerReq=None, UseCpIp=None, UseUpIp=None):
        """Updates a child instance of egtpS11SgwRange on the server.

        Args:
            ChangeReportingMode (number): OBSOLETE: Use changeReportingList instead.
            ControlPlaneLbType (str): The type of Control Plane load balancing used. * For R1, the Create Session Response is sent from the slave SGW. * For R2, the Create Session Response is sent from the controller SGW.
            EnableEchoRequest (bool): Set to true to send echo request
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
            N3CreateBearerReq (number): Number of retransmissions for Create Bearer request
            N3DeleteBearerReq (number): Number of retransmissions for Delete Bearer request
            N3EchoReq (number): Number of retransmissions for Echo request
            N3MmeHandoverInProgress (number): Number of retransmissions for MME Handover in Progress response cause
            N3UpdateBearerReq (number): Number of retransmissions for Update Bearer request
            Name (str): Name of range
            T3CreateBearerReq (number): Response timeout for a Create Bearer request (seconds)
            T3DeleteBearerReq (number): Response timeout for a Delete Bearer request (seconds)
            T3EchoReq (number): Response timeout for a Echo request (seconds).
            T3MmeHandoverInProgress (number): Retry timeout for a MME Handover in Progress response cause (seconds).
            T3UpdateBearerReq (number): Response timeout for a Update Bearer request (seconds)
            UseCpIp (bool): Use Control Plane Load Balancer
            UseUpIp (bool): Use User Plane Load Balancer

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
