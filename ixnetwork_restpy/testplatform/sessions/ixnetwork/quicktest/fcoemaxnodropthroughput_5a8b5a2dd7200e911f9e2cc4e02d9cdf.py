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


class FcoeMaxNoDropThroughput(Base):
    """It signifies the Fibre Channel over Ethernet maximum no drop throughput test feature for quick test.
    The FcoeMaxNoDropThroughput class encapsulates a list of fcoeMaxNoDropThroughput resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcoeMaxNoDropThroughput.find() method.
    The list can be managed by using the FcoeMaxNoDropThroughput.add() and FcoeMaxNoDropThroughput.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "fcoeMaxNoDropThroughput"
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
        super(FcoeMaxNoDropThroughput, self).__init__(parent, list_op)

    @property
    def FcoeConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeconfig_2d064617f8aef2d0313020ca36397a47.FcoeConfig): An instance of the FcoeConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeconfig_2d064617f8aef2d0313020ca36397a47 import (
            FcoeConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeConfig", None) is not None:
                return self._properties.get("FcoeConfig")
        return FcoeConfig(self)._select()

    @property
    def FcoeTrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoetrafficmapping_45e5ad7d95b320f886f6f4c052440de4.FcoeTrafficMapping): An instance of the FcoeTrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoetrafficmapping_45e5ad7d95b320f886f6f4c052440de4 import (
            FcoeTrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeTrafficMapping", None) is not None:
                return self._properties.get("FcoeTrafficMapping")
        return FcoeTrafficMapping(self)

    @property
    def FcoeWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoewizard_4c5278bb58a46d34fc1a28f28dad29c3.FcoeWizard): An instance of the FcoeWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoewizard_4c5278bb58a46d34fc1a28f28dad29c3 import (
            FcoeWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeWizard", None) is not None:
                return self._properties.get("FcoeWizard")
        return FcoeWizard(self)._select()

    @property
    def MultiCastTrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicasttrafficmapping_bd580a23f72e0850fe13b25adc05f506.MultiCastTrafficMapping): An instance of the MultiCastTrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicasttrafficmapping_bd580a23f72e0850fe13b25adc05f506 import (
            MultiCastTrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MultiCastTrafficMapping", None) is not None:
                return self._properties.get("MultiCastTrafficMapping")
        return MultiCastTrafficMapping(self)

    @property
    def MulticastConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastconfig_afe2a6f4d5a6324c76205140fa48a0e4.MulticastConfig): An instance of the MulticastConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastconfig_afe2a6f4d5a6324c76205140fa48a0e4 import (
            MulticastConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastConfig", None) is not None:
                return self._properties.get("MulticastConfig")
        return MulticastConfig(self)._select()

    @property
    def MulticastFrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastframedata_769c7c4ba4941aafb107cb57be6ded30.MulticastFrameData): An instance of the MulticastFrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastframedata_769c7c4ba4941aafb107cb57be6ded30 import (
            MulticastFrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastFrameData", None) is not None:
                return self._properties.get("MulticastFrameData")
        return MulticastFrameData(self)

    @property
    def MulticastGroupCapacityConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastgroupcapacityconfig_5f65ce40200f1aba634dbc216c188bca.MulticastGroupCapacityConfig): An instance of the MulticastGroupCapacityConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastgroupcapacityconfig_5f65ce40200f1aba634dbc216c188bca import (
            MulticastGroupCapacityConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastGroupCapacityConfig", None) is not None:
                return self._properties.get("MulticastGroupCapacityConfig")
        return MulticastGroupCapacityConfig(self)

    @property
    def MulticastLearnFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastlearnframes_6dc393bd6525916204157881db9a0d94.MulticastLearnFrames): An instance of the MulticastLearnFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastlearnframes_6dc393bd6525916204157881db9a0d94 import (
            MulticastLearnFrames,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastLearnFrames", None) is not None:
                return self._properties.get("MulticastLearnFrames")
        return MulticastLearnFrames(self)._select()

    @property
    def PassCriteria(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_2f84ada625563113d3ef4f44b25dd7e2.PassCriteria): An instance of the PassCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_2f84ada625563113d3ef4f44b25dd7e2 import (
            PassCriteria,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PassCriteria", None) is not None:
                return self._properties.get("PassCriteria")
        return PassCriteria(self)._select()

    @property
    def Pfc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pfc_556f34b5fce914554da575e006d990e2.Pfc): An instance of the Pfc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pfc_556f34b5fce914554da575e006d990e2 import (
            Pfc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pfc", None) is not None:
                return self._properties.get("Pfc")
        return Pfc(self)._select()

    @property
    def Ports(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_efcfda96caaf36de660944ce80de4ead.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_efcfda96caaf36de660944ce80de4ead import (
            Ports,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ports", None) is not None:
                return self._properties.get("Ports")
        return Ports(self)

    @property
    def Protocols(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocols_9a915e57e118f974c888001fce6e3692.Protocols): An instance of the Protocols class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocols_9a915e57e118f974c888001fce6e3692 import (
            Protocols,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Protocols", None) is not None:
                return self._properties.get("Protocols")
        return Protocols(self)

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_8a36fe3000b3d22d4022b2fa2ae06acb.TestConfig): An instance of the TestConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_8a36fe3000b3d22d4022b2fa2ae06acb import (
            TestConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestConfig", None) is not None:
                return self._properties.get("TestConfig")
        return TestConfig(self)._select()

    @property
    def TrafficConfigurationPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficconfigurationpage_71901ed3910aeb85b614217df7560ee6.TrafficConfigurationPage): An instance of the TrafficConfigurationPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficconfigurationpage_71901ed3910aeb85b614217df7560ee6 import (
            TrafficConfigurationPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficConfigurationPage", None) is not None:
                return self._properties.get("TrafficConfigurationPage")
        return TrafficConfigurationPage(self)

    @property
    def TrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_206d3c7fd8956cf41e032f8402bda1d7.TrafficSelection): An instance of the TrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_206d3c7fd8956cf41e032f8402bda1d7 import (
            TrafficSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficSelection", None) is not None:
                return self._properties.get("TrafficSelection")
        return TrafficSelection(self)

    @property
    def TxRatio(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.txratio_fe919519e40f8da226c40436977e1fe8.TxRatio): An instance of the TxRatio class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.txratio_fe919519e40f8da226c40436977e1fe8 import (
            TxRatio,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxRatio", None) is not None:
                return self._properties.get("TxRatio")
        return TxRatio(self)._select()

    @property
    def UnicastConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastconfig_6c07afc94f18ffafa04f700ee4d1d484.UnicastConfig): An instance of the UnicastConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastconfig_6c07afc94f18ffafa04f700ee4d1d484 import (
            UnicastConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UnicastConfig", None) is not None:
                return self._properties.get("UnicastConfig")
        return UnicastConfig(self)._select()

    @property
    def UnicastFrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastframedata_e6a12a0cf9b68b55be61e952a242d8b9.UnicastFrameData): An instance of the UnicastFrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastframedata_e6a12a0cf9b68b55be61e952a242d8b9 import (
            UnicastFrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UnicastFrameData", None) is not None:
                return self._properties.get("UnicastFrameData")
        return UnicastFrameData(self)

    @property
    def UnicastLearnFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastlearnframes_45a108168a899f4e4a1b37df25ab7525.UnicastLearnFrames): An instance of the UnicastLearnFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicastlearnframes_45a108168a899f4e4a1b37df25ab7525 import (
            UnicastLearnFrames,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UnicastLearnFrames", None) is not None:
                return self._properties.get("UnicastLearnFrames")
        return UnicastLearnFrames(self)._select()

    @property
    def UnicastTrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicasttrafficmapping_57724f1b390e3fb5ec570554cbb1a90b.UnicastTrafficMapping): An instance of the UnicastTrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.unicasttrafficmapping_57724f1b390e3fb5ec570554cbb1a90b import (
            UnicastTrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UnicastTrafficMapping", None) is not None:
                return self._properties.get("UnicastTrafficMapping")
        return UnicastTrafficMapping(self)

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
        # type: (bool, str, str, str) -> FcoeMaxNoDropThroughput
        """Updates fcoeMaxNoDropThroughput resource on the server.

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
        # type: (bool, str, str, str) -> FcoeMaxNoDropThroughput
        """Adds a new fcoeMaxNoDropThroughput resource on the server and adds it to the container.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with all currently retrieved fcoeMaxNoDropThroughput resources using find and the newly added fcoeMaxNoDropThroughput resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcoeMaxNoDropThroughput resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> FcoeMaxNoDropThroughput
        """Finds and retrieves fcoeMaxNoDropThroughput resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeMaxNoDropThroughput resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeMaxNoDropThroughput resources from the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with matching fcoeMaxNoDropThroughput resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeMaxNoDropThroughput data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeMaxNoDropThroughput resources from the server available through an iterator or index

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
