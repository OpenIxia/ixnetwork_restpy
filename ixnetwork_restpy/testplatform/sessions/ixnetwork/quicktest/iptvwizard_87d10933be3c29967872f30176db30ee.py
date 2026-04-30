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


class IptvWizard(Base):
    """It describes the iptv wizard functionality for iptv channel zapping.
    The IptvWizard class encapsulates a required iptvWizard resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "iptvWizard"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IptvWizard, self).__init__(parent, list_op)

    @property
    def Dhcp4Page(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcp4page_4eb3dcdff9534dbd981408659cefe0ba.Dhcp4Page): An instance of the Dhcp4Page class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcp4page_4eb3dcdff9534dbd981408659cefe0ba import (
            Dhcp4Page,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcp4Page", None) is not None:
                return self._properties.get("Dhcp4Page")
        return Dhcp4Page(self)

    @property
    def Dhcp6Page(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcp6page_547289864108ef5686c47baab90b1184.Dhcp6Page): An instance of the Dhcp6Page class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcp6page_547289864108ef5686c47baab90b1184 import (
            Dhcp6Page,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcp6Page", None) is not None:
                return self._properties.get("Dhcp6Page")
        return Dhcp6Page(self)

    @property
    def DhcpMacPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpmacpage_cb9f4f32d1e389b517d62454fce12256.DhcpMacPage): An instance of the DhcpMacPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpmacpage_cb9f4f32d1e389b517d62454fce12256 import (
            DhcpMacPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpMacPage", None) is not None:
                return self._properties.get("DhcpMacPage")
        return DhcpMacPage(self)

    @property
    def DhcpPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcppage_f95f90c0a34ea4757eb815c6d8b59cb7.DhcpPage): An instance of the DhcpPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcppage_f95f90c0a34ea4757eb815c6d8b59cb7 import (
            DhcpPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpPage", None) is not None:
                return self._properties.get("DhcpPage")
        return DhcpPage(self)

    @property
    def DhcpSelectPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpselectpage_bd1d05ccb1a8b85e38141e7b5d129980.DhcpSelectPage): An instance of the DhcpSelectPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpselectpage_bd1d05ccb1a8b85e38141e7b5d129980 import (
            DhcpSelectPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpSelectPage", None) is not None:
                return self._properties.get("DhcpSelectPage")
        return DhcpSelectPage(self)

    @property
    def DhcpVlanPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpvlanpage_ee367a5506c84ca1787abb92d9955207.DhcpVlanPage): An instance of the DhcpVlanPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpvlanpage_ee367a5506c84ca1787abb92d9955207 import (
            DhcpVlanPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpVlanPage", None) is not None:
                return self._properties.get("DhcpVlanPage")
        return DhcpVlanPage(self)

    @property
    def IpMacPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipmacpage_661ea8dbb17154075414b0598687c469.IpMacPage): An instance of the IpMacPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipmacpage_661ea8dbb17154075414b0598687c469 import (
            IpMacPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpMacPage", None) is not None:
                return self._properties.get("IpMacPage")
        return IpMacPage(self)

    @property
    def IpPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ippage_b4c223c380360e5be642cff0b6d5e86e.IpPage): An instance of the IpPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ippage_b4c223c380360e5be642cff0b6d5e86e import (
            IpPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpPage", None) is not None:
                return self._properties.get("IpPage")
        return IpPage(self)

    @property
    def IpSelectPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipselectpage_e29c9977227f808910ea1c82a9ad0784.IpSelectPage): An instance of the IpSelectPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipselectpage_e29c9977227f808910ea1c82a9ad0784 import (
            IpSelectPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpSelectPage", None) is not None:
                return self._properties.get("IpSelectPage")
        return IpSelectPage(self)

    @property
    def IpVlanPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipvlanpage_5d8538e31092dc30f095336d9f594a7c.IpVlanPage): An instance of the IpVlanPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipvlanpage_5d8538e31092dc30f095336d9f594a7c import (
            IpVlanPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpVlanPage", None) is not None:
                return self._properties.get("IpVlanPage")
        return IpVlanPage(self)

    @property
    def IptvExistingConfigPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvexistingconfigpage_a1a40bbc6c2d126e603981672cbd2a9a.IptvExistingConfigPage): An instance of the IptvExistingConfigPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvexistingconfigpage_a1a40bbc6c2d126e603981672cbd2a9a import (
            IptvExistingConfigPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvExistingConfigPage", None) is not None:
                return self._properties.get("IptvExistingConfigPage")
        return IptvExistingConfigPage(self)

    @property
    def IptvMulticastGroupsPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvmulticastgroupspage_c7500692ee3458c6a3cf6fb5c0f25051.IptvMulticastGroupsPage): An instance of the IptvMulticastGroupsPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvmulticastgroupspage_c7500692ee3458c6a3cf6fb5c0f25051 import (
            IptvMulticastGroupsPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvMulticastGroupsPage", None) is not None:
                return self._properties.get("IptvMulticastGroupsPage")
        return IptvMulticastGroupsPage(self)

    @property
    def IptvSelectPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvselectpage_2e8986c6658c228b1ab40387cb8c80d0.IptvSelectPage): An instance of the IptvSelectPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvselectpage_2e8986c6658c228b1ab40387cb8c80d0 import (
            IptvSelectPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvSelectPage", None) is not None:
                return self._properties.get("IptvSelectPage")
        return IptvSelectPage(self)

    @property
    def IptvSubscribersPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvsubscriberspage_98c39652de2dafe31e4e0805e1a73993.IptvSubscribersPage): An instance of the IptvSubscribersPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvsubscriberspage_98c39652de2dafe31e4e0805e1a73993 import (
            IptvSubscribersPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvSubscribersPage", None) is not None:
                return self._properties.get("IptvSubscribersPage")
        return IptvSubscribersPage(self)

    @property
    def PppoxClientAtmPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientatmpage_ed903eea9d16a0a709e93af3a1a132a6.PppoxClientAtmPage): An instance of the PppoxClientAtmPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientatmpage_ed903eea9d16a0a709e93af3a1a132a6 import (
            PppoxClientAtmPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientAtmPage", None) is not None:
                return self._properties.get("PppoxClientAtmPage")
        return PppoxClientAtmPage(self)

    @property
    def PppoxClientMacPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientmacpage_c939bdc6b70d4e8dc3e612bef75d3b62.PppoxClientMacPage): An instance of the PppoxClientMacPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientmacpage_c939bdc6b70d4e8dc3e612bef75d3b62 import (
            PppoxClientMacPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientMacPage", None) is not None:
                return self._properties.get("PppoxClientMacPage")
        return PppoxClientMacPage(self)

    @property
    def PppoxClientNcpPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientncppage_ace670b9a209720752530f9302f957b5.PppoxClientNcpPage): An instance of the PppoxClientNcpPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientncppage_ace670b9a209720752530f9302f957b5 import (
            PppoxClientNcpPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientNcpPage", None) is not None:
                return self._properties.get("PppoxClientNcpPage")
        return PppoxClientNcpPage(self)

    @property
    def PppoxClientPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientpage_e7256e0a27ec7c2e27fd23da512e7902.PppoxClientPage): An instance of the PppoxClientPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientpage_e7256e0a27ec7c2e27fd23da512e7902 import (
            PppoxClientPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientPage", None) is not None:
                return self._properties.get("PppoxClientPage")
        return PppoxClientPage(self)

    @property
    def PppoxClientPppoePage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientpppoepage_b36bf8526d1e8299c73cc27f88f38786.PppoxClientPppoePage): An instance of the PppoxClientPppoePage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientpppoepage_b36bf8526d1e8299c73cc27f88f38786 import (
            PppoxClientPppoePage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientPppoePage", None) is not None:
                return self._properties.get("PppoxClientPppoePage")
        return PppoxClientPppoePage(self)

    @property
    def PppoxClientSelectPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientselectpage_c2465317bc84031e1ed14cbdf3dcbc82.PppoxClientSelectPage): An instance of the PppoxClientSelectPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientselectpage_c2465317bc84031e1ed14cbdf3dcbc82 import (
            PppoxClientSelectPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientSelectPage", None) is not None:
                return self._properties.get("PppoxClientSelectPage")
        return PppoxClientSelectPage(self)

    @property
    def PppoxClientVlanPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientvlanpage_c52236468c91df32799dade5f96cbed5.PppoxClientVlanPage): An instance of the PppoxClientVlanPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxclientvlanpage_c52236468c91df32799dade5f96cbed5 import (
            PppoxClientVlanPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxClientVlanPage", None) is not None:
                return self._properties.get("PppoxClientVlanPage")
        return PppoxClientVlanPage(self)

    def find(self):
        """Finds and retrieves iptvWizard resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve iptvWizard resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all iptvWizard resources from the server.

        Returns
        -------
        - self: This instance with matching iptvWizard resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of iptvWizard data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the iptvWizard resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

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
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

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
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("waitForTest", payload=payload, response_object=None)
