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


class EthernetSegments(Base):
    """Configures Ethernet Segments.
    The EthernetSegments class encapsulates a list of ethernetSegments resources that are managed by the user.
    A list of resources can be retrieved from the server using the EthernetSegments.find() method.
    The list can be managed by using the EthernetSegments.add() and EthernetSegments.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ethernetSegments"
    _SDM_ATT_MAP = {
        "AutoConfigureEsImport": "autoConfigureEsImport",
        "BMacPrefix": "bMacPrefix",
        "BMacPrefixLength": "bMacPrefixLength",
        "DfElectionMethod": "dfElectionMethod",
        "DfElectionTimer": "dfElectionTimer",
        "EnableActiveStandby": "enableActiveStandby",
        "EnableRootLeaf": "enableRootLeaf",
        "EnableSecondLabel": "enableSecondLabel",
        "Enabled": "enabled",
        "EsImport": "esImport",
        "Esi": "esi",
        "EsiLabel": "esiLabel",
        "FirstLabel": "firstLabel",
        "IncludeMacMobilityExtendedCommunity": "includeMacMobilityExtendedCommunity",
        "SecondLabel": "secondLabel",
        "SupportFastConvergence": "supportFastConvergence",
        "SupportMultiHomedEsAutoDiscovery": "supportMultiHomedEsAutoDiscovery",
        "TypeOfEthernetVpn": "typeOfEthernetVpn",
        "UseSameSequenceNumber": "useSameSequenceNumber",
    }
    _SDM_ENUM_MAP = {
        "dfElectionMethod": ["serviceCarving"],
        "typeOfEthernetVpn": ["evpn", "pbbEvpn"],
    }

    def __init__(self, parent, list_op=False):
        super(EthernetSegments, self).__init__(parent, list_op)

    @property
    def AdBmacEsRouteAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.adbmacesrouteattributes_85d7cd2c65ac911ee7a94f0d8a9e4e10.AdBmacEsRouteAttributes): An instance of the AdBmacEsRouteAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.adbmacesrouteattributes_85d7cd2c65ac911ee7a94f0d8a9e4e10 import (
            AdBmacEsRouteAttributes,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AdBmacEsRouteAttributes", None) is not None:
                return self._properties.get("AdBmacEsRouteAttributes")
        return AdBmacEsRouteAttributes(self)._select()

    @property
    def BMacMappedIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bmacmappedip_5d1351237be9d86d6e72123aac8c9ca6.BMacMappedIp): An instance of the BMacMappedIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bmacmappedip_5d1351237be9d86d6e72123aac8c9ca6 import (
            BMacMappedIp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BMacMappedIp", None) is not None:
                return self._properties.get("BMacMappedIp")
        return BMacMappedIp(self)

    @property
    def Evi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evi_f4aba0f35140f705a8d5d733d2b2f38e.Evi): An instance of the Evi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evi_f4aba0f35140f705a8d5d733d2b2f38e import (
            Evi,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Evi", None) is not None:
                return self._properties.get("Evi")
        return Evi(self)

    @property
    def AutoConfigureEsImport(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoConfigureEsImport"])

    @AutoConfigureEsImport.setter
    def AutoConfigureEsImport(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoConfigureEsImport"], value)

    @property
    def BMacPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: B-MAC address as a prefix where the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. By default a unique B-MAC is constructed per ethernet segment. it can be changed to any value but multicast and broadcast addresses are not used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BMacPrefix"])

    @BMacPrefix.setter
    def BMacPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BMacPrefix"], value)

    @property
    def BMacPrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The MAC address length field is typically set to 48. However this length value can be changed to specify the MAC address as a prefix; in which case, the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. Default value is 48. Minimum value is 0 and maximum value is 48.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BMacPrefixLength"])

    @BMacPrefixLength.setter
    def BMacPrefixLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BMacPrefixLength"], value)

    @property
    def DfElectionMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(serviceCarving): This is a read only field. user can not change the value of this field. This is just to show that IxNetwork is using Service Carving method for DF election.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DfElectionMethod"])

    @DfElectionMethod.setter
    def DfElectionMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DfElectionMethod"], value)

    @property
    def DfElectionTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time interval in second to wait for DF election process to complete. Default value is 3 seconds. Minimum value is 1 second and maximum value is 300 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DfElectionTimer"])

    @DfElectionTimer.setter
    def DfElectionTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DfElectionTimer"], value)

    @property
    def EnableActiveStandby(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then this ethernet segment operates in active-standby mode. If false then this ethernet segment operates in all-active mode. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableActiveStandby"])

    @EnableActiveStandby.setter
    def EnableActiveStandby(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableActiveStandby"], value)

    @property
    def EnableRootLeaf(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then ESI label is associated with a leaf side. If false then ESI label is associated with a root side. Default value is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRootLeaf"])

    @EnableRootLeaf.setter
    def EnableRootLeaf(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRootLeaf"], value)

    @property
    def EnableSecondLabel(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then second EVPN label is inserted in label stack for ES route, AD per segment route.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSecondLabel"])

    @EnableSecondLabel.setter
    def EnableSecondLabel(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSecondLabel"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, ethernet segment is enabled and is used in evpn. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def EsImport(self):
        # type: () -> str
        """
        Returns
        -------
        - str: When Auto Configure ES-Import is false then user has to put ES-Import here. Default value is 0x00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EsImport"])

    @EsImport.setter
    def EsImport(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EsImport"], value)

    @property
    def Esi(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Ethernet Segment Identifier (ESI) which is encoded as a ten octets integer. Default value is 0x00 00 00 00 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Esi"])

    @Esi.setter
    def Esi(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Esi"], value)

    @property
    def EsiLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Label value carried in ESI Label Extended Community in AD route per segment. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EsiLabel"])

    @EsiLabel.setter
    def EsiLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EsiLabel"], value)

    @property
    def FirstLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: First EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstLabel"])

    @FirstLabel.setter
    def FirstLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstLabel"], value)

    @property
    def IncludeMacMobilityExtendedCommunity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then MAC mobility is performed in EVPN mode. If false then MAC mobility is not performed even if duplicate MAC address is found from remote PE.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IncludeMacMobilityExtendedCommunity"]
        )

    @IncludeMacMobilityExtendedCommunity.setter
    def IncludeMacMobilityExtendedCommunity(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["IncludeMacMobilityExtendedCommunity"], value
        )

    @property
    def SecondLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Second EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SecondLabel"])

    @SecondLabel.setter
    def SecondLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SecondLabel"], value)

    @property
    def SupportFastConvergence(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then fast convergence is performed. Default value is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportFastConvergence"])

    @SupportFastConvergence.setter
    def SupportFastConvergence(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportFastConvergence"], value)

    @property
    def SupportMultiHomedEsAutoDiscovery(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then auto discovery between multihomed PEs is performed.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["SupportMultiHomedEsAutoDiscovery"]
        )

    @SupportMultiHomedEsAutoDiscovery.setter
    def SupportMultiHomedEsAutoDiscovery(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["SupportMultiHomedEsAutoDiscovery"], value
        )

    @property
    def TypeOfEthernetVpn(self):
        # type: () -> str
        """
        Returns
        -------
        - str(evpn | pbbEvpn): Type of ethernet vpn. It can be either EVPN or PBB-EVPN. Default mode is PBB-EVPN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeOfEthernetVpn"])

    @TypeOfEthernetVpn.setter
    def TypeOfEthernetVpn(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeOfEthernetVpn"], value)

    @property
    def UseSameSequenceNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then same sequence number is used in MAC Mobility Extended Community for all MAC route to flush the remote C-MAC forwarding table. If false then subsequent C-MAC route uses unique sequence number in MAC Mobility Extended Community.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseSameSequenceNumber"])

    @UseSameSequenceNumber.setter
    def UseSameSequenceNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseSameSequenceNumber"], value)

    def update(
        self,
        AutoConfigureEsImport=None,
        BMacPrefix=None,
        BMacPrefixLength=None,
        DfElectionMethod=None,
        DfElectionTimer=None,
        EnableActiveStandby=None,
        EnableRootLeaf=None,
        EnableSecondLabel=None,
        Enabled=None,
        EsImport=None,
        Esi=None,
        EsiLabel=None,
        FirstLabel=None,
        IncludeMacMobilityExtendedCommunity=None,
        SecondLabel=None,
        SupportFastConvergence=None,
        SupportMultiHomedEsAutoDiscovery=None,
        TypeOfEthernetVpn=None,
        UseSameSequenceNumber=None,
    ):
        # type: (bool, str, int, str, int, bool, bool, bool, bool, str, str, int, int, bool, int, bool, bool, str, bool) -> EthernetSegments
        """Updates ethernetSegments resource on the server.

        Args
        ----
        - AutoConfigureEsImport (bool): NOT DEFINED
        - BMacPrefix (str): B-MAC address as a prefix where the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. By default a unique B-MAC is constructed per ethernet segment. it can be changed to any value but multicast and broadcast addresses are not used.
        - BMacPrefixLength (number): The MAC address length field is typically set to 48. However this length value can be changed to specify the MAC address as a prefix; in which case, the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. Default value is 48. Minimum value is 0 and maximum value is 48.
        - DfElectionMethod (str(serviceCarving)): This is a read only field. user can not change the value of this field. This is just to show that IxNetwork is using Service Carving method for DF election.
        - DfElectionTimer (number): Time interval in second to wait for DF election process to complete. Default value is 3 seconds. Minimum value is 1 second and maximum value is 300 seconds.
        - EnableActiveStandby (bool): If true then this ethernet segment operates in active-standby mode. If false then this ethernet segment operates in all-active mode. Default value is false.
        - EnableRootLeaf (bool): If true then ESI label is associated with a leaf side. If false then ESI label is associated with a root side. Default value is true.
        - EnableSecondLabel (bool): If true then second EVPN label is inserted in label stack for ES route, AD per segment route.
        - Enabled (bool): If true, ethernet segment is enabled and is used in evpn. Default value is false.
        - EsImport (str): When Auto Configure ES-Import is false then user has to put ES-Import here. Default value is 0x00 00 00 00 00 00.
        - Esi (str): Ethernet Segment Identifier (ESI) which is encoded as a ten octets integer. Default value is 0x00 00 00 00 00 00 00 00 00 00.
        - EsiLabel (number): Label value carried in ESI Label Extended Community in AD route per segment. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - FirstLabel (number): First EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - IncludeMacMobilityExtendedCommunity (bool): If true then MAC mobility is performed in EVPN mode. If false then MAC mobility is not performed even if duplicate MAC address is found from remote PE.
        - SecondLabel (number): Second EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - SupportFastConvergence (bool): If true then fast convergence is performed. Default value is true.
        - SupportMultiHomedEsAutoDiscovery (bool): If true then auto discovery between multihomed PEs is performed.
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): Type of ethernet vpn. It can be either EVPN or PBB-EVPN. Default mode is PBB-EVPN.
        - UseSameSequenceNumber (bool): If true then same sequence number is used in MAC Mobility Extended Community for all MAC route to flush the remote C-MAC forwarding table. If false then subsequent C-MAC route uses unique sequence number in MAC Mobility Extended Community.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AutoConfigureEsImport=None,
        BMacPrefix=None,
        BMacPrefixLength=None,
        DfElectionMethod=None,
        DfElectionTimer=None,
        EnableActiveStandby=None,
        EnableRootLeaf=None,
        EnableSecondLabel=None,
        Enabled=None,
        EsImport=None,
        Esi=None,
        EsiLabel=None,
        FirstLabel=None,
        IncludeMacMobilityExtendedCommunity=None,
        SecondLabel=None,
        SupportFastConvergence=None,
        SupportMultiHomedEsAutoDiscovery=None,
        TypeOfEthernetVpn=None,
        UseSameSequenceNumber=None,
    ):
        # type: (bool, str, int, str, int, bool, bool, bool, bool, str, str, int, int, bool, int, bool, bool, str, bool) -> EthernetSegments
        """Adds a new ethernetSegments resource on the server and adds it to the container.

        Args
        ----
        - AutoConfigureEsImport (bool): NOT DEFINED
        - BMacPrefix (str): B-MAC address as a prefix where the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. By default a unique B-MAC is constructed per ethernet segment. it can be changed to any value but multicast and broadcast addresses are not used.
        - BMacPrefixLength (number): The MAC address length field is typically set to 48. However this length value can be changed to specify the MAC address as a prefix; in which case, the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. Default value is 48. Minimum value is 0 and maximum value is 48.
        - DfElectionMethod (str(serviceCarving)): This is a read only field. user can not change the value of this field. This is just to show that IxNetwork is using Service Carving method for DF election.
        - DfElectionTimer (number): Time interval in second to wait for DF election process to complete. Default value is 3 seconds. Minimum value is 1 second and maximum value is 300 seconds.
        - EnableActiveStandby (bool): If true then this ethernet segment operates in active-standby mode. If false then this ethernet segment operates in all-active mode. Default value is false.
        - EnableRootLeaf (bool): If true then ESI label is associated with a leaf side. If false then ESI label is associated with a root side. Default value is true.
        - EnableSecondLabel (bool): If true then second EVPN label is inserted in label stack for ES route, AD per segment route.
        - Enabled (bool): If true, ethernet segment is enabled and is used in evpn. Default value is false.
        - EsImport (str): When Auto Configure ES-Import is false then user has to put ES-Import here. Default value is 0x00 00 00 00 00 00.
        - Esi (str): Ethernet Segment Identifier (ESI) which is encoded as a ten octets integer. Default value is 0x00 00 00 00 00 00 00 00 00 00.
        - EsiLabel (number): Label value carried in ESI Label Extended Community in AD route per segment. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - FirstLabel (number): First EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - IncludeMacMobilityExtendedCommunity (bool): If true then MAC mobility is performed in EVPN mode. If false then MAC mobility is not performed even if duplicate MAC address is found from remote PE.
        - SecondLabel (number): Second EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - SupportFastConvergence (bool): If true then fast convergence is performed. Default value is true.
        - SupportMultiHomedEsAutoDiscovery (bool): If true then auto discovery between multihomed PEs is performed.
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): Type of ethernet vpn. It can be either EVPN or PBB-EVPN. Default mode is PBB-EVPN.
        - UseSameSequenceNumber (bool): If true then same sequence number is used in MAC Mobility Extended Community for all MAC route to flush the remote C-MAC forwarding table. If false then subsequent C-MAC route uses unique sequence number in MAC Mobility Extended Community.

        Returns
        -------
        - self: This instance with all currently retrieved ethernetSegments resources using find and the newly added ethernetSegments resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ethernetSegments resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AutoConfigureEsImport=None,
        BMacPrefix=None,
        BMacPrefixLength=None,
        DfElectionMethod=None,
        DfElectionTimer=None,
        EnableActiveStandby=None,
        EnableRootLeaf=None,
        EnableSecondLabel=None,
        Enabled=None,
        EsImport=None,
        Esi=None,
        EsiLabel=None,
        FirstLabel=None,
        IncludeMacMobilityExtendedCommunity=None,
        SecondLabel=None,
        SupportFastConvergence=None,
        SupportMultiHomedEsAutoDiscovery=None,
        TypeOfEthernetVpn=None,
        UseSameSequenceNumber=None,
    ):
        # type: (bool, str, int, str, int, bool, bool, bool, bool, str, str, int, int, bool, int, bool, bool, str, bool) -> EthernetSegments
        """Finds and retrieves ethernetSegments resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernetSegments resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernetSegments resources from the server.

        Args
        ----
        - AutoConfigureEsImport (bool): NOT DEFINED
        - BMacPrefix (str): B-MAC address as a prefix where the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. By default a unique B-MAC is constructed per ethernet segment. it can be changed to any value but multicast and broadcast addresses are not used.
        - BMacPrefixLength (number): The MAC address length field is typically set to 48. However this length value can be changed to specify the MAC address as a prefix; in which case, the MAC address length field is set to the length of the prefix. This provides the ability to aggregate MAC addresses if the deployment environment supports that. Default value is 48. Minimum value is 0 and maximum value is 48.
        - DfElectionMethod (str(serviceCarving)): This is a read only field. user can not change the value of this field. This is just to show that IxNetwork is using Service Carving method for DF election.
        - DfElectionTimer (number): Time interval in second to wait for DF election process to complete. Default value is 3 seconds. Minimum value is 1 second and maximum value is 300 seconds.
        - EnableActiveStandby (bool): If true then this ethernet segment operates in active-standby mode. If false then this ethernet segment operates in all-active mode. Default value is false.
        - EnableRootLeaf (bool): If true then ESI label is associated with a leaf side. If false then ESI label is associated with a root side. Default value is true.
        - EnableSecondLabel (bool): If true then second EVPN label is inserted in label stack for ES route, AD per segment route.
        - Enabled (bool): If true, ethernet segment is enabled and is used in evpn. Default value is false.
        - EsImport (str): When Auto Configure ES-Import is false then user has to put ES-Import here. Default value is 0x00 00 00 00 00 00.
        - Esi (str): Ethernet Segment Identifier (ESI) which is encoded as a ten octets integer. Default value is 0x00 00 00 00 00 00 00 00 00 00.
        - EsiLabel (number): Label value carried in ESI Label Extended Community in AD route per segment. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - FirstLabel (number): First EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - IncludeMacMobilityExtendedCommunity (bool): If true then MAC mobility is performed in EVPN mode. If false then MAC mobility is not performed even if duplicate MAC address is found from remote PE.
        - SecondLabel (number): Second EVPN label in label stack for ES route, AD per segment route. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - SupportFastConvergence (bool): If true then fast convergence is performed. Default value is true.
        - SupportMultiHomedEsAutoDiscovery (bool): If true then auto discovery between multihomed PEs is performed.
        - TypeOfEthernetVpn (str(evpn | pbbEvpn)): Type of ethernet vpn. It can be either EVPN or PBB-EVPN. Default mode is PBB-EVPN.
        - UseSameSequenceNumber (bool): If true then same sequence number is used in MAC Mobility Extended Community for all MAC route to flush the remote C-MAC forwarding table. If false then subsequent C-MAC route uses unique sequence number in MAC Mobility Extended Community.

        Returns
        -------
        - self: This instance with matching ethernetSegments resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernetSegments data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernetSegments resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def FlushRemoteCmacForwardingTable(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the flushRemoteCmacForwardingTable operation on the server.

        NOT DEFINED

        flushRemoteCmacForwardingTable(async_operation=bool)string
        ----------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

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
            "flushRemoteCmacForwardingTable", payload=payload, response_object=None
        )
