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


class Services(Base):
    """The services parameters.
    The Services class encapsulates a list of services resources that are managed by the user.
    A list of resources can be retrieved from the server using the Services.find() method.
    The list can be managed by using the Services.add() and Services.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "services"
    _SDM_ATT_MAP = {
        "Actualcbs": "actualcbs",
        "Actualcir": "actualcir",
        "Actualebs": "actualebs",
        "Actualeir": "actualeir",
        "BwProfile": "bwProfile",
        "Cbs": "cbs",
        "Cir": "cir",
        "Cirtolerance": "cirtolerance",
        "Ebs": "ebs",
        "Eir": "eir",
        "Fdv": "fdv",
        "Fdvtolerance": "fdvtolerance",
        "Flr": "flr",
        "Flrtolerance": "flrtolerance",
        "FrameSize": "frameSize",
        "Ftd": "ftd",
        "Ftdtolerance": "ftdtolerance",
        "IncludeInTest": "includeInTest",
        "IsCirPerFlowGroup": "isCirPerFlowGroup",
        "IsColorAware": "isColorAware",
        "IsPerformance": "isPerformance",
        "Mesh": "mesh",
        "ServiceName": "serviceName",
        "UseSameInterfaces": "useSameInterfaces",
    }
    _SDM_ENUM_MAP = {
        "bwProfile": [
            "ip",
            "ipv4AssuredForwardingPhb",
            "ipv4ClassSelectorPhb",
            "ipv4DefaultPhb",
            "ipv4ExpeditedForwardingPhb",
            "ipv4Precedence",
            "ipv6TrafficClass",
            "port",
            "tcp",
            "udp",
            "vlanCos",
            "vlanId",
        ],
        "mesh": ["elan", "eline"],
    }

    def __init__(self, parent, list_op=False):
        super(Services, self).__init__(parent, list_op)

    @property
    def GreenLevelConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.greenlevelconfig_517851c36830cc0744aeabdc06a04062.GreenLevelConfig): An instance of the GreenLevelConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.greenlevelconfig_517851c36830cc0744aeabdc06a04062 import (
            GreenLevelConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GreenLevelConfig", None) is not None:
                return self._properties.get("GreenLevelConfig")
        return GreenLevelConfig(self)._select()

    @property
    def YellowLevelConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.yellowlevelconfig_95c6dc684b15286eeef288bd07db14dd.YellowLevelConfig): An instance of the YellowLevelConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.yellowlevelconfig_95c6dc684b15286eeef288bd07db14dd import (
            YellowLevelConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("YellowLevelConfig", None) is not None:
                return self._properties.get("YellowLevelConfig")
        return YellowLevelConfig(self)._select()

    @property
    def Actualcbs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual CBS
        """
        return self._get_attribute(self._SDM_ATT_MAP["Actualcbs"])

    @Actualcbs.setter
    def Actualcbs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Actualcbs"], value)

    @property
    def Actualcir(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual CIR
        """
        return self._get_attribute(self._SDM_ATT_MAP["Actualcir"])

    @Actualcir.setter
    def Actualcir(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Actualcir"], value)

    @property
    def Actualebs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual EBS
        """
        return self._get_attribute(self._SDM_ATT_MAP["Actualebs"])

    @Actualebs.setter
    def Actualebs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Actualebs"], value)

    @property
    def Actualeir(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual EIR
        """
        return self._get_attribute(self._SDM_ATT_MAP["Actualeir"])

    @Actualeir.setter
    def Actualeir(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Actualeir"], value)

    @property
    def BwProfile(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ip | ipv4AssuredForwardingPhb | ipv4ClassSelectorPhb | ipv4DefaultPhb | ipv4ExpeditedForwardingPhb | ipv4Precedence | ipv6TrafficClass | port | tcp | udp | vlanCos | vlanId): The BW profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BwProfile"])

    @BwProfile.setter
    def BwProfile(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BwProfile"], value)

    @property
    def Cbs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of allocated bytes available for bursts of ingress service frames transmitted at temporary rates above the CIR while meeting the SLA guarantees provided at the CIR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cbs"])

    @Cbs.setter
    def Cbs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cbs"], value)

    @property
    def Cir(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The committed information rate in the network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cir"])

    @Cir.setter
    def Cir(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cir"], value)

    @property
    def Cirtolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of CIR tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cirtolerance"])

    @Cirtolerance.setter
    def Cirtolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cirtolerance"], value)

    @property
    def Ebs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of allocated bytes available for bursts of ingress service frames sent at temporary rates above the CIR+EIR while remaining EIR-conformant.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ebs"])

    @Ebs.setter
    def Ebs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ebs"], value)

    @property
    def Eir(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The excess information rate above the CIR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Eir"])

    @Eir.setter
    def Eir(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Eir"], value)

    @property
    def Fdv(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The jitter, which is the interval between timestamps of PGID packet arrivals.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Fdv"])

    @Fdv.setter
    def Fdv(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Fdv"], value)

    @property
    def Fdvtolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of jitter tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Fdvtolerance"])

    @Fdvtolerance.setter
    def Fdvtolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Fdvtolerance"], value)

    @property
    def Flr(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage value of the number of frames transmitted minus the number of frames received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Flr"])

    @Flr.setter
    def Flr(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Flr"], value)

    @property
    def Flrtolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of FLR tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Flrtolerance"])

    @Flrtolerance.setter
    def Flrtolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Flrtolerance"], value)

    @property
    def FrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The frame size used by the service.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSize"])

    @FrameSize.setter
    def FrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSize"], value)

    @property
    def Ftd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The FTD parameters.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ftd"])

    @Ftd.setter
    def Ftd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ftd"], value)

    @property
    def Ftdtolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of FTD tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ftdtolerance"])

    @Ftdtolerance.setter
    def Ftdtolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ftdtolerance"], value)

    @property
    def IncludeInTest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeInTest"])

    @IncludeInTest.setter
    def IncludeInTest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeInTest"], value)

    @property
    def IsCirPerFlowGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true it enables the cir per flowgroup
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsCirPerFlowGroup"])

    @IsCirPerFlowGroup.setter
    def IsCirPerFlowGroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsCirPerFlowGroup"], value)

    @property
    def IsColorAware(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it becomes aware of the color.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsColorAware"])

    @IsColorAware.setter
    def IsColorAware(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsColorAware"], value)

    @property
    def IsPerformance(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the performance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPerformance"])

    @IsPerformance.setter
    def IsPerformance(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsPerformance"], value)

    @property
    def Mesh(self):
        # type: () -> str
        """
        Returns
        -------
        - str(elan | eline): The pattern in which you want to send traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mesh"])

    @Mesh.setter
    def Mesh(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mesh"], value)

    @property
    def ServiceName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the service.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServiceName"])

    @ServiceName.setter
    def ServiceName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServiceName"], value)

    @property
    def UseSameInterfaces(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it uses the same interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseSameInterfaces"])

    @UseSameInterfaces.setter
    def UseSameInterfaces(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseSameInterfaces"], value)

    def update(
        self,
        Actualcbs=None,
        Actualcir=None,
        Actualebs=None,
        Actualeir=None,
        BwProfile=None,
        Cbs=None,
        Cir=None,
        Cirtolerance=None,
        Ebs=None,
        Eir=None,
        Fdv=None,
        Fdvtolerance=None,
        Flr=None,
        Flrtolerance=None,
        FrameSize=None,
        Ftd=None,
        Ftdtolerance=None,
        IncludeInTest=None,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        Mesh=None,
        ServiceName=None,
        UseSameInterfaces=None,
    ):
        # type: (int, int, int, int, str, int, int, int, int, int, int, int, int, int, int, int, int, bool, bool, bool, bool, str, str, bool) -> Services
        """Updates services resource on the server.

        Args
        ----
        - Actualcbs (number): Actual CBS
        - Actualcir (number): Actual CIR
        - Actualebs (number): Actual EBS
        - Actualeir (number): Actual EIR
        - BwProfile (str(ip | ipv4AssuredForwardingPhb | ipv4ClassSelectorPhb | ipv4DefaultPhb | ipv4ExpeditedForwardingPhb | ipv4Precedence | ipv6TrafficClass | port | tcp | udp | vlanCos | vlanId)): The BW profile.
        - Cbs (number): The number of allocated bytes available for bursts of ingress service frames transmitted at temporary rates above the CIR while meeting the SLA guarantees provided at the CIR.
        - Cir (number): The committed information rate in the network.
        - Cirtolerance (number): The percentage of CIR tolerance.
        - Ebs (number): The number of allocated bytes available for bursts of ingress service frames sent at temporary rates above the CIR+EIR while remaining EIR-conformant.
        - Eir (number): The excess information rate above the CIR.
        - Fdv (number): The jitter, which is the interval between timestamps of PGID packet arrivals.
        - Fdvtolerance (number): The percentage of jitter tolerance.
        - Flr (number): The percentage value of the number of frames transmitted minus the number of frames received.
        - Flrtolerance (number): The percentage of FLR tolerance.
        - FrameSize (number): The frame size used by the service.
        - Ftd (number): The FTD parameters.
        - Ftdtolerance (number): The percentage of FTD tolerance.
        - IncludeInTest (bool): NOT DEFINED
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - Mesh (str(elan | eline)): The pattern in which you want to send traffic.
        - ServiceName (str): The name of the service.
        - UseSameInterfaces (bool): If true, it uses the same interfaces.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Actualcbs=None,
        Actualcir=None,
        Actualebs=None,
        Actualeir=None,
        BwProfile=None,
        Cbs=None,
        Cir=None,
        Cirtolerance=None,
        Ebs=None,
        Eir=None,
        Fdv=None,
        Fdvtolerance=None,
        Flr=None,
        Flrtolerance=None,
        FrameSize=None,
        Ftd=None,
        Ftdtolerance=None,
        IncludeInTest=None,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        Mesh=None,
        ServiceName=None,
        UseSameInterfaces=None,
    ):
        # type: (int, int, int, int, str, int, int, int, int, int, int, int, int, int, int, int, int, bool, bool, bool, bool, str, str, bool) -> Services
        """Adds a new services resource on the server and adds it to the container.

        Args
        ----
        - Actualcbs (number): Actual CBS
        - Actualcir (number): Actual CIR
        - Actualebs (number): Actual EBS
        - Actualeir (number): Actual EIR
        - BwProfile (str(ip | ipv4AssuredForwardingPhb | ipv4ClassSelectorPhb | ipv4DefaultPhb | ipv4ExpeditedForwardingPhb | ipv4Precedence | ipv6TrafficClass | port | tcp | udp | vlanCos | vlanId)): The BW profile.
        - Cbs (number): The number of allocated bytes available for bursts of ingress service frames transmitted at temporary rates above the CIR while meeting the SLA guarantees provided at the CIR.
        - Cir (number): The committed information rate in the network.
        - Cirtolerance (number): The percentage of CIR tolerance.
        - Ebs (number): The number of allocated bytes available for bursts of ingress service frames sent at temporary rates above the CIR+EIR while remaining EIR-conformant.
        - Eir (number): The excess information rate above the CIR.
        - Fdv (number): The jitter, which is the interval between timestamps of PGID packet arrivals.
        - Fdvtolerance (number): The percentage of jitter tolerance.
        - Flr (number): The percentage value of the number of frames transmitted minus the number of frames received.
        - Flrtolerance (number): The percentage of FLR tolerance.
        - FrameSize (number): The frame size used by the service.
        - Ftd (number): The FTD parameters.
        - Ftdtolerance (number): The percentage of FTD tolerance.
        - IncludeInTest (bool): NOT DEFINED
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - Mesh (str(elan | eline)): The pattern in which you want to send traffic.
        - ServiceName (str): The name of the service.
        - UseSameInterfaces (bool): If true, it uses the same interfaces.

        Returns
        -------
        - self: This instance with all currently retrieved services resources using find and the newly added services resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained services resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Actualcbs=None,
        Actualcir=None,
        Actualebs=None,
        Actualeir=None,
        BwProfile=None,
        Cbs=None,
        Cir=None,
        Cirtolerance=None,
        Ebs=None,
        Eir=None,
        Fdv=None,
        Fdvtolerance=None,
        Flr=None,
        Flrtolerance=None,
        FrameSize=None,
        Ftd=None,
        Ftdtolerance=None,
        IncludeInTest=None,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        Mesh=None,
        ServiceName=None,
        UseSameInterfaces=None,
    ):
        # type: (int, int, int, int, str, int, int, int, int, int, int, int, int, int, int, int, int, bool, bool, bool, bool, str, str, bool) -> Services
        """Finds and retrieves services resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve services resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all services resources from the server.

        Args
        ----
        - Actualcbs (number): Actual CBS
        - Actualcir (number): Actual CIR
        - Actualebs (number): Actual EBS
        - Actualeir (number): Actual EIR
        - BwProfile (str(ip | ipv4AssuredForwardingPhb | ipv4ClassSelectorPhb | ipv4DefaultPhb | ipv4ExpeditedForwardingPhb | ipv4Precedence | ipv6TrafficClass | port | tcp | udp | vlanCos | vlanId)): The BW profile.
        - Cbs (number): The number of allocated bytes available for bursts of ingress service frames transmitted at temporary rates above the CIR while meeting the SLA guarantees provided at the CIR.
        - Cir (number): The committed information rate in the network.
        - Cirtolerance (number): The percentage of CIR tolerance.
        - Ebs (number): The number of allocated bytes available for bursts of ingress service frames sent at temporary rates above the CIR+EIR while remaining EIR-conformant.
        - Eir (number): The excess information rate above the CIR.
        - Fdv (number): The jitter, which is the interval between timestamps of PGID packet arrivals.
        - Fdvtolerance (number): The percentage of jitter tolerance.
        - Flr (number): The percentage value of the number of frames transmitted minus the number of frames received.
        - Flrtolerance (number): The percentage of FLR tolerance.
        - FrameSize (number): The frame size used by the service.
        - Ftd (number): The FTD parameters.
        - Ftdtolerance (number): The percentage of FTD tolerance.
        - IncludeInTest (bool): NOT DEFINED
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - Mesh (str(elan | eline)): The pattern in which you want to send traffic.
        - ServiceName (str): The name of the service.
        - UseSameInterfaces (bool): If true, it uses the same interfaces.

        Returns
        -------
        - self: This instance with matching services resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of services data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the services resources from the server available through an iterator or index

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
