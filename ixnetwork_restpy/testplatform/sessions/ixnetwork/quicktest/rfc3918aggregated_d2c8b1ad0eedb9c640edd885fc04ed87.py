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


class Rfc3918aggregated(Base):
    """This object allows to configures the attributes for the rfc3918 aggregated test.
    The Rfc3918aggregated class encapsulates a list of rfc3918aggregated resources that are managed by the user.
    A list of resources can be retrieved from the server using the Rfc3918aggregated.find() method.
    The list can be managed by using the Rfc3918aggregated.add() and Rfc3918aggregated.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "rfc3918aggregated"
    _SDM_ATT_MAP = {
        "ForceApplyQTConfig": "forceApplyQTConfig",
        "InputParameters": "inputParameters",
        "Mode": "mode",
        "Name": "name",
    }
    _SDM_ENUM_MAP = {
        "mode": ["existingMode", "newMode"],
    }

    def __init__(self, parent, list_op=False):
        super(Rfc3918aggregated, self).__init__(parent, list_op)

    @property
    def CpfFrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfframedata_fa910c381a377e4bf2649a04d940a7e2.CpfFrameData): An instance of the CpfFrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfframedata_fa910c381a377e4bf2649a04d940a7e2 import (
            CpfFrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpfFrameData", None) is not None:
                return self._properties.get("CpfFrameData")
        return CpfFrameData(self)

    @property
    def CpfProtocolInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfprotocolinfo_71c49fc5cb80e283ab7511ff4bb519fe.CpfProtocolInfo): An instance of the CpfProtocolInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfprotocolinfo_71c49fc5cb80e283ab7511ff4bb519fe import (
            CpfProtocolInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpfProtocolInfo", None) is not None:
                return self._properties.get("CpfProtocolInfo")
        return CpfProtocolInfo(self)

    @property
    def EndpointMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.endpointmode_17c8bc2d1c5049ba8e6298e774994909.EndpointMode): An instance of the EndpointMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.endpointmode_17c8bc2d1c5049ba8e6298e774994909 import (
            EndpointMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EndpointMode", None) is not None:
                return self._properties.get("EndpointMode")
        return EndpointMode(self)

    @property
    def FrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.framedata_5c34b7e3981fb5d7320658948cdcc1c1.FrameData): An instance of the FrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.framedata_5c34b7e3981fb5d7320658948cdcc1c1 import (
            FrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FrameData", None) is not None:
                return self._properties.get("FrameData")
        return FrameData(self)

    @property
    def IgmpHostWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmphostwizard_bafa77ce5f0405dbcc1708a60994124a.IgmpHostWizard): An instance of the IgmpHostWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmphostwizard_bafa77ce5f0405dbcc1708a60994124a import (
            IgmpHostWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpHostWizard", None) is not None:
                return self._properties.get("IgmpHostWizard")
        return IgmpHostWizard(self)._select()

    @property
    def IgmpQuerierWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmpquerierwizard_a455a104b333bca586796619d765de70.IgmpQuerierWizard): An instance of the IgmpQuerierWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmpquerierwizard_a455a104b333bca586796619d765de70 import (
            IgmpQuerierWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpQuerierWizard", None) is not None:
                return self._properties.get("IgmpQuerierWizard")
        return IgmpQuerierWizard(self)._select()

    @property
    def Ipv4Wizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizard_91a927f614356e9f0b94b89798006948.Ipv4Wizard): An instance of the Ipv4Wizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizard_91a927f614356e9f0b94b89798006948 import (
            Ipv4Wizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Wizard", None) is not None:
                return self._properties.get("Ipv4Wizard")
        return Ipv4Wizard(self)._select()

    @property
    def Ipv6Wizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizard_69e9a4de10dd12f0cbaad0edf0105169.Ipv6Wizard): An instance of the Ipv6Wizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizard_69e9a4de10dd12f0cbaad0edf0105169 import (
            Ipv6Wizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Wizard", None) is not None:
                return self._properties.get("Ipv6Wizard")
        return Ipv6Wizard(self)._select()

    @property
    def LearnFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_608041917b3c6edc6ba87df21638a9b5.LearnFrames): An instance of the LearnFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_608041917b3c6edc6ba87df21638a9b5 import (
            LearnFrames,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnFrames", None) is not None:
                return self._properties.get("LearnFrames")
        return LearnFrames(self)._select()

    @property
    def MldHostWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mldhostwizard_597dbac8b83eaf60150790645e04f2e5.MldHostWizard): An instance of the MldHostWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mldhostwizard_597dbac8b83eaf60150790645e04f2e5 import (
            MldHostWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldHostWizard", None) is not None:
                return self._properties.get("MldHostWizard")
        return MldHostWizard(self)._select()

    @property
    def MldQuerierWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mldquerierwizard_12285140afbb074ddb96eda0894cafc3.MldQuerierWizard): An instance of the MldQuerierWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mldquerierwizard_12285140afbb074ddb96eda0894cafc3 import (
            MldQuerierWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldQuerierWizard", None) is not None:
                return self._properties.get("MldQuerierWizard")
        return MldQuerierWizard(self)._select()

    @property
    def MulticastAggregatedConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastaggregatedconfig_47d9b23a98c10381c9a3a86f7538f4e2.MulticastAggregatedConfig): An instance of the MulticastAggregatedConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastaggregatedconfig_47d9b23a98c10381c9a3a86f7538f4e2 import (
            MulticastAggregatedConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastAggregatedConfig", None) is not None:
                return self._properties.get("MulticastAggregatedConfig")
        return MulticastAggregatedConfig(self)

    @property
    def MulticastQuerierSettingsPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastqueriersettingspage_37059ebc3d68f7b476d15855ebbff598.MulticastQuerierSettingsPage): An instance of the MulticastQuerierSettingsPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastqueriersettingspage_37059ebc3d68f7b476d15855ebbff598 import (
            MulticastQuerierSettingsPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastQuerierSettingsPage", None) is not None:
                return self._properties.get("MulticastQuerierSettingsPage")
        return MulticastQuerierSettingsPage(self)

    @property
    def PassCriteria(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_f53eb813c8a2c4a42f22c32e589972c4.PassCriteria): An instance of the PassCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_f53eb813c8a2c4a42f22c32e589972c4 import (
            PassCriteria,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PassCriteria", None) is not None:
                return self._properties.get("PassCriteria")
        return PassCriteria(self)._select()

    @property
    def Ports(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_f6f455ded478c07acab8e19988c8be03.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_f6f455ded478c07acab8e19988c8be03 import (
            Ports,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ports", None) is not None:
                return self._properties.get("Ports")
        return Ports(self)

    @property
    def ProtocolSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocolsettings_61925f36128e50e1d44e09bf07c0e30d.ProtocolSettings): An instance of the ProtocolSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocolsettings_61925f36128e50e1d44e09bf07c0e30d import (
            ProtocolSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ProtocolSettings", None) is not None:
                return self._properties.get("ProtocolSettings")
        return ProtocolSettings(self)

    @property
    def Results(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.results_23583c0cce1dabf7b75fe7d2ae18cfc4.Results): An instance of the Results class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.results_23583c0cce1dabf7b75fe7d2ae18cfc4 import (
            Results,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Results", None) is not None:
                return self._properties.get("Results")
        return Results(self)._select()

    @property
    def TestConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_e3aadd7010a76cbc7b678933e6905ed0.TestConfig): An instance of the TestConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_e3aadd7010a76cbc7b678933e6905ed0 import (
            TestConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestConfig", None) is not None:
                return self._properties.get("TestConfig")
        return TestConfig(self)._select()

    @property
    def TrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficmapping_2d3494e619a86bce8bf8c64253f5a31d.TrafficMapping): An instance of the TrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficmapping_2d3494e619a86bce8bf8c64253f5a31d import (
            TrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficMapping", None) is not None:
                return self._properties.get("TrafficMapping")
        return TrafficMapping(self)

    @property
    def TrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_22c0efed3052ed5002942a33e331fb3b.TrafficSelection): An instance of the TrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_22c0efed3052ed5002942a33e331fb3b import (
            TrafficSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficSelection", None) is not None:
                return self._properties.get("TrafficSelection")
        return TrafficSelection(self)

    @property
    def ForceApplyQTConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Apply QT config
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceApplyQTConfig"])

    @ForceApplyQTConfig.setter
    def ForceApplyQTConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceApplyQTConfig"], value)

    @property
    def InputParameters(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Input Parameters
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputParameters"])

    @InputParameters.setter
    def InputParameters(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputParameters"], value)

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(existingMode | newMode): Test mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test name
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    def update(
        self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None
    ):
        # type: (bool, str, str, str) -> Rfc3918aggregated
        """Updates rfc3918aggregated resource on the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> Rfc3918aggregated
        """Adds a new rfc3918aggregated resource on the server and adds it to the container.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with all currently retrieved rfc3918aggregated resources using find and the newly added rfc3918aggregated resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rfc3918aggregated resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> Rfc3918aggregated
        """Finds and retrieves rfc3918aggregated resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rfc3918aggregated resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rfc3918aggregated resources from the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with matching rfc3918aggregated resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rfc3918aggregated data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rfc3918aggregated resources from the server available through an iterator or index

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
