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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class DslPools(Base):
    """Represents an Access Loop connected to a DSLAM running ANCP
    The DslPools class encapsulates a list of dslPools resources that are managed by the user.
    A list of resources can be retrieved from the server using the DslPools.find() method.
    The list can be managed by using the DslPools.add() and DslPools.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dslPools'
    _SDM_ATT_MAP = {
        'ActualBandwidthDownstream': 'actualBandwidthDownstream',
        'ActualBandwidthUpstream': 'actualBandwidthUpstream',
        'ActualNetDataRateDownstream': 'actualNetDataRateDownstream',
        'ActualNetDataRateDownstreamTolerance': 'actualNetDataRateDownstreamTolerance',
        'ActualNetDataRateUpstream': 'actualNetDataRateUpstream',
        'ActualNetDataRateUpstreamTolerance': 'actualNetDataRateUpstreamTolerance',
        'CircuitId': 'circuitId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DslLineState': 'dslLineState',
        'DslType': 'dslType',
        'EnableActualNetDataRateDownstream': 'enableActualNetDataRateDownstream',
        'EnableActualNetDataRateUpstream': 'enableActualNetDataRateUpstream',
        'EnableDslType': 'enableDslType',
        'EnablePonType': 'enablePonType',
        'EnableRemoteId': 'enableRemoteId',
        'FlappingMode': 'flappingMode',
        'InnerVlanId': 'innerVlanId',
        'LineDownInterval': 'lineDownInterval',
        'LineUpInterval': 'lineUpInterval',
        'Name': 'name',
        'OuterVlanId': 'outerVlanId',
        'PonType': 'ponType',
        'PortDownSent': 'portDownSent',
        'PortUpSent': 'portUpSent',
        'RemoteId': 'remoteId',
        'TechType': 'techType',
        'VlanAllocationModel': 'vlanAllocationModel',
    }

    def __init__(self, parent):
        super(DslPools, self).__init__(parent)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c import TlvProfile
        return TlvProfile(self)

    @property
    def ActualBandwidthDownstream(self):
        """
        Returns
        -------
        - list(number): Subscriber Line Actual Bandwidth Downstream
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualBandwidthDownstream'])

    @property
    def ActualBandwidthUpstream(self):
        """
        Returns
        -------
        - list(number): Subscriber Line Actual Bandwidth Upstream
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualBandwidthUpstream'])

    @property
    def ActualNetDataRateDownstream(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Actual downstream net data rate on a DSL access line. Rate in kbits/s as a 32-bit unsigned integer
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualNetDataRateDownstream']))

    @property
    def ActualNetDataRateDownstreamTolerance(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Percentage for variation of Actual Net Data Rate Downstream TLV value when sending port-up messages in flapping behavior
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualNetDataRateDownstreamTolerance']))

    @property
    def ActualNetDataRateUpstream(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Actual upstream net data rate on a DSL access line. Rate in kbits/s as a 32-bit unsigned integer
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualNetDataRateUpstream']))

    @property
    def ActualNetDataRateUpstreamTolerance(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Percentage for variation of Actual Net Data Rate Upstream TLV value when sending port-up messages in flapping behavior
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualNetDataRateUpstreamTolerance']))

    @property
    def CircuitId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A locally administered human-readable string generated by or configured on the Access Node, identifying the corresponding access loop logical port on the user side of the Access Node
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CircuitId']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DslLineState(self):
        """
        Returns
        -------
        - list(str[disabled | idle | none | showTime | silent | tlvNa]): The state of the DSL line as defined in DSL Line State TLV SHOWTIME - Status Info TLV has value 1 IDLE - Status Info TLV has value 2 SILENT - Status Info TLV has value 3 TLV N/A - Status Info TLV was not configured for this message None - The DSL Line did not send any messages Disabled - The DSL Line is disabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['DslLineState'])

    @property
    def DslType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): DSL Type value for DSL Type TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DslType']))

    @property
    def EnableActualNetDataRateDownstream(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Actual-Net-Data-Rate-Downstream TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableActualNetDataRateDownstream']))

    @property
    def EnableActualNetDataRateUpstream(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Actual-Net-Data-Rate-Upstream TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableActualNetDataRateUpstream']))

    @property
    def EnableDslType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable DSL Type TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDslType']))

    @property
    def EnablePonType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable PON Type TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePonType']))

    @property
    def EnableRemoteId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Access-Loop-Remote-ID TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRemoteId']))

    @property
    def FlappingMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable a flapping profile. Resync will send Port-Up messages, one message every 'Flap Interval' seconds. Reset will send Port-Up followed by Port-Down messages, one message every 'Flap Interval' seconds. Stop will stop the flapping profile, and send one Port-Up message if the line is silent at the time of stopping the flapping profile.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlappingMode']))

    @property
    def InnerVlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Inner VLAN ID for N:1 and 1:1 VLAN mapping in Access-Aggregation-Circuit-ID-Binary TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InnerVlanId']))

    @property
    def LineDownInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval in milliseconds to wait after sending port-down message when flapping is enabled
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LineDownInterval']))

    @property
    def LineUpInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval in milliseconds to wait after sending port-up message when flapping is enabled
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LineUpInterval']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OuterVlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Outer VLAN ID for 1:1 VLAN mapping in Access-Aggregation-Circuit-ID-Binary TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OuterVlanId']))

    @property
    def PonType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): PON Type value for PON Type TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PonType']))

    @property
    def PortDownSent(self):
        """
        Returns
        -------
        - list(number): Number of Topology Discovery Port Down messages sent
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDownSent'])

    @property
    def PortUpSent(self):
        """
        Returns
        -------
        - list(number): Number of Topology Discovery Port Up messages sent
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortUpSent'])

    @property
    def RemoteId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): An operator-configured string that uniquely identifies the user on the associated access line
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteId']))

    @property
    def TechType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Type of Access Loop Technology
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TechType']))

    @property
    def VlanAllocationModel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Access-Aggregation-Circuit-ID-Binary TLV disable, enable N:1 vlan allocation model or 1:1 vlan allocation model
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanAllocationModel']))

    def update(self, Name=None):
        """Updates dslPools resource on the server.

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
        """Adds a new dslPools resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved dslPools resources using find and the newly added dslPools resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dslPools resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActualBandwidthDownstream=None, ActualBandwidthUpstream=None, Count=None, DescriptiveName=None, DslLineState=None, Name=None, PortDownSent=None, PortUpSent=None):
        """Finds and retrieves dslPools resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dslPools resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dslPools resources from the server.

        Args
        ----
        - ActualBandwidthDownstream (list(number)): Subscriber Line Actual Bandwidth Downstream
        - ActualBandwidthUpstream (list(number)): Subscriber Line Actual Bandwidth Upstream
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DslLineState (list(str[disabled | idle | none | showTime | silent | tlvNa])): The state of the DSL line as defined in DSL Line State TLV SHOWTIME - Status Info TLV has value 1 IDLE - Status Info TLV has value 2 SILENT - Status Info TLV has value 3 TLV N/A - Status Info TLV was not configured for this message None - The DSL Line did not send any messages Disabled - The DSL Line is disabled
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PortDownSent (list(number)): Number of Topology Discovery Port Down messages sent
        - PortUpSent (list(number)): Number of Topology Discovery Port Up messages sent

        Returns
        -------
        - self: This instance with matching dslPools resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dslPools data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dslPools resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActualNetDataRateDownstream=None, ActualNetDataRateDownstreamTolerance=None, ActualNetDataRateUpstream=None, ActualNetDataRateUpstreamTolerance=None, CircuitId=None, DslType=None, EnableActualNetDataRateDownstream=None, EnableActualNetDataRateUpstream=None, EnableDslType=None, EnablePonType=None, EnableRemoteId=None, FlappingMode=None, InnerVlanId=None, LineDownInterval=None, LineUpInterval=None, OuterVlanId=None, PonType=None, RemoteId=None, TechType=None, VlanAllocationModel=None):
        """Base class infrastructure that gets a list of dslPools device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActualNetDataRateDownstream (str): optional regex of actualNetDataRateDownstream
        - ActualNetDataRateDownstreamTolerance (str): optional regex of actualNetDataRateDownstreamTolerance
        - ActualNetDataRateUpstream (str): optional regex of actualNetDataRateUpstream
        - ActualNetDataRateUpstreamTolerance (str): optional regex of actualNetDataRateUpstreamTolerance
        - CircuitId (str): optional regex of circuitId
        - DslType (str): optional regex of dslType
        - EnableActualNetDataRateDownstream (str): optional regex of enableActualNetDataRateDownstream
        - EnableActualNetDataRateUpstream (str): optional regex of enableActualNetDataRateUpstream
        - EnableDslType (str): optional regex of enableDslType
        - EnablePonType (str): optional regex of enablePonType
        - EnableRemoteId (str): optional regex of enableRemoteId
        - FlappingMode (str): optional regex of flappingMode
        - InnerVlanId (str): optional regex of innerVlanId
        - LineDownInterval (str): optional regex of lineDownInterval
        - LineUpInterval (str): optional regex of lineUpInterval
        - OuterVlanId (str): optional regex of outerVlanId
        - PonType (str): optional regex of ponType
        - RemoteId (str): optional regex of remoteId
        - TechType (str): optional regex of techType
        - VlanAllocationModel (str): optional regex of vlanAllocationModel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def SendPortDown(self, *args, **kwargs):
        """Executes the sendPortDown operation on the server.

        Send Port Down event from selected Access Loop items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortDown(SessionIndices=list)
        ---------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendPortDown(SessionIndices=string)
        -----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPortDown', payload=payload, response_object=None)

    def SendPortUp(self, *args, **kwargs):
        """Executes the sendPortUp operation on the server.

        Send Port Up event from selected Access Loop items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortUp(SessionIndices=list)
        -------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendPortUp(SessionIndices=string)
        ---------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPortUp', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
