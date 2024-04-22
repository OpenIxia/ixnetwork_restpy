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


class IsisPseudoInterface(Base):
    """Information for Simulated Router Interfaces
    The IsisPseudoInterface class encapsulates a list of isisPseudoInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisPseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "isisPseudoInterface"
    _SDM_ATT_MAP = {
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "LinkType": "linkType",
        "Name": "name",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisPseudoInterface, self).__init__(parent, list_op)

    @property
    def IsisDcePseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_1c86fa3992ce0fd24a3980c360d8868a.IsisDcePseudoIfaceAttPoint1Config): An instance of the IsisDcePseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_1c86fa3992ce0fd24a3980c360d8868a import (
            IsisDcePseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisDcePseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisDcePseudoIfaceAttPoint1Config")
        return IsisDcePseudoIfaceAttPoint1Config(self)

    @property
    def IsisDcePseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_ccee80f0e3b46537138b8f528ef26472.IsisDcePseudoIfaceAttPoint2Config): An instance of the IsisDcePseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_ccee80f0e3b46537138b8f528ef26472 import (
            IsisDcePseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisDcePseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisDcePseudoIfaceAttPoint2Config")
        return IsisDcePseudoIfaceAttPoint2Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_fba88625727b27e259a6fefcf3fe66b2.IsisL3PseudoIfaceAttPoint1Config): An instance of the IsisL3PseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_fba88625727b27e259a6fefcf3fe66b2 import (
            IsisL3PseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisL3PseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisL3PseudoIfaceAttPoint1Config")
        return IsisL3PseudoIfaceAttPoint1Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_0204b3dc43c585ae158544fee37480a0.IsisL3PseudoIfaceAttPoint2Config): An instance of the IsisL3PseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_0204b3dc43c585ae158544fee37480a0 import (
            IsisL3PseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisL3PseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisL3PseudoIfaceAttPoint2Config")
        return IsisL3PseudoIfaceAttPoint2Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_092b727de5b08e6f5f9e63b9a006b7e1.IsisSpbPseudoIfaceAttPoint1Config): An instance of the IsisSpbPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_092b727de5b08e6f5f9e63b9a006b7e1 import (
            IsisSpbPseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisSpbPseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisSpbPseudoIfaceAttPoint1Config")
        return IsisSpbPseudoIfaceAttPoint1Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_39508f250dc5c6ad5bffd3fc89ed10ac.IsisSpbPseudoIfaceAttPoint2Config): An instance of the IsisSpbPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_39508f250dc5c6ad5bffd3fc89ed10ac import (
            IsisSpbPseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisSpbPseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisSpbPseudoIfaceAttPoint2Config")
        return IsisSpbPseudoIfaceAttPoint2Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_6812126cb30044d635b18984fe3b5ccf.IsisTrillPseudoIfaceAttPoint1Config): An instance of the IsisTrillPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_6812126cb30044d635b18984fe3b5ccf import (
            IsisTrillPseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisTrillPseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisTrillPseudoIfaceAttPoint1Config")
        return IsisTrillPseudoIfaceAttPoint1Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_391dc09e39440c04d9fb0809e7dafb50.IsisTrillPseudoIfaceAttPoint2Config): An instance of the IsisTrillPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_391dc09e39440c04d9fb0809e7dafb50 import (
            IsisTrillPseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisTrillPseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisTrillPseudoIfaceAttPoint2Config")
        return IsisTrillPseudoIfaceAttPoint2Config(self)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def LinkType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LinkType"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    def update(self, Name=None):
        # type: (str) -> IsisPseudoInterface
        """Updates isisPseudoInterface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        # type: (str) -> IsisPseudoInterface
        """Adds a new isisPseudoInterface resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved isisPseudoInterface resources using find and the newly added isisPseudoInterface resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> IsisPseudoInterface
        """Finds and retrieves isisPseudoInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisPseudoInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisPseudoInterface resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisPseudoInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisPseudoInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisPseudoInterface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
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
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        stop(async_operation=bool)
        --------------------------
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
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, LinkType=None):
        """Base class infrastructure that gets a list of isisPseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - LinkType (str): optional regex of linkType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
