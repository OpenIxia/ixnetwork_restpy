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


class Rfc3918burdenedJoinDelay(Base):
    """This object allows to configure the attributes for the RFC 3918 Burdened Join Latency test
    The Rfc3918burdenedJoinDelay class encapsulates a list of rfc3918burdenedJoinDelay resources that are managed by the user.
    A list of resources can be retrieved from the server using the Rfc3918burdenedJoinDelay.find() method.
    The list can be managed by using the Rfc3918burdenedJoinDelay.add() and Rfc3918burdenedJoinDelay.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "rfc3918burdenedJoinDelay"
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
        super(Rfc3918burdenedJoinDelay, self).__init__(parent, list_op)

    @property
    def BurdenFramedata(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.burdenframedata_1b0e034dbb49e880ccfc211d8714ac76.BurdenFramedata): An instance of the BurdenFramedata class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.burdenframedata_1b0e034dbb49e880ccfc211d8714ac76 import (
            BurdenFramedata,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BurdenFramedata", None) is not None:
                return self._properties.get("BurdenFramedata")
        return BurdenFramedata(self)

    @property
    def BurdenTrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.burdentrafficmapping_40ac205f736187652180d82141b59dea.BurdenTrafficMapping): An instance of the BurdenTrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.burdentrafficmapping_40ac205f736187652180d82141b59dea import (
            BurdenTrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BurdenTrafficMapping", None) is not None:
                return self._properties.get("BurdenTrafficMapping")
        return BurdenTrafficMapping(self)

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
    def Ipv4WizardBurden(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizardburden_858c9c84061b12a2435b2765d7541eeb.Ipv4WizardBurden): An instance of the Ipv4WizardBurden class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizardburden_858c9c84061b12a2435b2765d7541eeb import (
            Ipv4WizardBurden,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4WizardBurden", None) is not None:
                return self._properties.get("Ipv4WizardBurden")
        return Ipv4WizardBurden(self)._select()

    @property
    def Ipv4WizardMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizardmulticast_bf6edf883ffb9d37797350edc53fadf7.Ipv4WizardMulticast): An instance of the Ipv4WizardMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizardmulticast_bf6edf883ffb9d37797350edc53fadf7 import (
            Ipv4WizardMulticast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4WizardMulticast", None) is not None:
                return self._properties.get("Ipv4WizardMulticast")
        return Ipv4WizardMulticast(self)._select()

    @property
    def Ipv6WizardBurden(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizardburden_c4de5b106f2e608280829701b8957d2f.Ipv6WizardBurden): An instance of the Ipv6WizardBurden class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizardburden_c4de5b106f2e608280829701b8957d2f import (
            Ipv6WizardBurden,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6WizardBurden", None) is not None:
                return self._properties.get("Ipv6WizardBurden")
        return Ipv6WizardBurden(self)._select()

    @property
    def Ipv6WizardMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizardmulticast_c003900070c57f2652869613c9dbe1e5.Ipv6WizardMulticast): An instance of the Ipv6WizardMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizardmulticast_c003900070c57f2652869613c9dbe1e5 import (
            Ipv6WizardMulticast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6WizardMulticast", None) is not None:
                return self._properties.get("Ipv6WizardMulticast")
        return Ipv6WizardMulticast(self)._select()

    @property
    def LearnFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_45a2d708e5ecc3f03b74f0ff6e319516.LearnFrames): An instance of the LearnFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_45a2d708e5ecc3f03b74f0ff6e319516 import (
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
    def MulticastFramedata(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastframedata_d5f19374fbfd2d2b4f9b34c85b1ddfca.MulticastFramedata): An instance of the MulticastFramedata class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastframedata_d5f19374fbfd2d2b4f9b34c85b1ddfca import (
            MulticastFramedata,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastFramedata", None) is not None:
                return self._properties.get("MulticastFramedata")
        return MulticastFramedata(self)

    @property
    def MulticastJoinLeaveConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastjoinleaveconfig_f3bc8f2d648be37f3a30700f28567012.MulticastJoinLeaveConfig): An instance of the MulticastJoinLeaveConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastjoinleaveconfig_f3bc8f2d648be37f3a30700f28567012 import (
            MulticastJoinLeaveConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastJoinLeaveConfig", None) is not None:
                return self._properties.get("MulticastJoinLeaveConfig")
        return MulticastJoinLeaveConfig(self)

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
    def MulticastTrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicasttrafficmapping_ebc1c6a8e8d26a717c8076d47dd80273.MulticastTrafficMapping): An instance of the MulticastTrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicasttrafficmapping_ebc1c6a8e8d26a717c8076d47dd80273 import (
            MulticastTrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastTrafficMapping", None) is not None:
                return self._properties.get("MulticastTrafficMapping")
        return MulticastTrafficMapping(self)

    @property
    def PassCriteria(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_44084f33d556acbc2526ef4cc22792c5.PassCriteria): An instance of the PassCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_44084f33d556acbc2526ef4cc22792c5 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_459470918b9a01b5ac4b950c57b3a857.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_459470918b9a01b5ac4b950c57b3a857 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_c55621ae26f729a747264a8de03a7c98.TestConfig): An instance of the TestConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_c55621ae26f729a747264a8de03a7c98 import (
            TestConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestConfig", None) is not None:
                return self._properties.get("TestConfig")
        return TestConfig(self)._select()

    @property
    def TrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_8d5f9713a7501c19cac3bbf3a3763ed6.TrafficSelection): An instance of the TrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_8d5f9713a7501c19cac3bbf3a3763ed6 import (
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
        # type: (bool, str, str, str) -> Rfc3918burdenedJoinDelay
        """Updates rfc3918burdenedJoinDelay resource on the server.

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
        # type: (bool, str, str, str) -> Rfc3918burdenedJoinDelay
        """Adds a new rfc3918burdenedJoinDelay resource on the server and adds it to the container.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with all currently retrieved rfc3918burdenedJoinDelay resources using find and the newly added rfc3918burdenedJoinDelay resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rfc3918burdenedJoinDelay resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> Rfc3918burdenedJoinDelay
        """Finds and retrieves rfc3918burdenedJoinDelay resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rfc3918burdenedJoinDelay resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rfc3918burdenedJoinDelay resources from the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with matching rfc3918burdenedJoinDelay resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rfc3918burdenedJoinDelay data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rfc3918burdenedJoinDelay resources from the server available through an iterator or index

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
