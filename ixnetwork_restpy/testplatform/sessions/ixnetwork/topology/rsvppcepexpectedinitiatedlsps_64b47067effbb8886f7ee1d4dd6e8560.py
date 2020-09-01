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


class RsvpPcepExpectedInitiatedLsps(Base):
    """RSVP-TE PCEP Expected Initiated LSPs
    The RsvpPcepExpectedInitiatedLsps class encapsulates a required rsvpPcepExpectedInitiatedLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpPcepExpectedInitiatedLsps'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BackupLspId': 'backupLspId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableRRO': 'enableRRO',
        'LocalIp': 'localIp',
        'Name': 'name',
        'NumberOfRroSubObjects': 'numberOfRroSubObjects',
        'SessionInformation': 'sessionInformation',
        'State': 'state',
        'SymbolicPathName': 'symbolicPathName',
    }

    def __init__(self, parent):
        super(RsvpPcepExpectedInitiatedLsps, self).__init__(parent)

    @property
    def RsvpIngressRROSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_cae3516af342fb3a35d3ff26ac4f830e.RsvpIngressRROSubObjectsList): An instance of the RsvpIngressRROSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist_cae3516af342fb3a35d3ff26ac4f830e import RsvpIngressRROSubObjectsList
        return RsvpIngressRROSubObjectsList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def BackupLspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackupLspId']))

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
    def EnableRRO(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable RRO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRRO']))

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

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
    def NumberOfRroSubObjects(self):
        """
        Returns
        -------
        - number: Number Of RRO Sub-Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRroSubObjects'])
    @NumberOfRroSubObjects.setter
    def NumberOfRroSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRroSubObjects'], value)

    @property
    def SessionInformation(self):
        """
        Returns
        -------
        - list(str[lastErrLSPAdmissionControlFailure | lastErrLSPBadAdSpecValue | lastErrLSPBadExplicitRoute | lastErrLSPBadFlowspecValue | lastErrLSPBadInitialSubobject | lastErrLSPBadLooseNode | lastErrLSPBadStrictNode | lastErrLSPBadTSpecValue | lastErrLSPDelayBoundNotMet | lastErrLSPMPLSAllocationFailure | lastErrLSPMTUTooBig | lastErrLSPNonRSVPRouter | lastErrLSPNoRouteAvailable | lastErrLSPPathErr | lastErrLSPPathTearSent | lastErrLSPRequestedBandwidthUnavailable | lastErrLSPReservationTearReceived | lastErrLSPReservationTearSent | lastErrLSPReservationTimeout | lastErrLSPRoutingLoops | lastErrLSPRoutingProblem | lastErrLSPRSVPSystemError | lastErrLSPServiceConflict | lastErrLSPServiceUnsupported | lastErrLSPTrafficControlError | lastErrLSPTrafficControlSystemError | lastErrLSPTrafficOrganizationError | lastErrLSPTrafficServiceError | lastErrLSPUnknownObjectClass | lastErrLSPUnknownObjectCType | lastErrLSPUnsupportedL3PID | lSPAdmissionControlFailure | lSPBadAdSpecValue | lSPBadExplicitRoute | lSPBadFlowspecValue | lSPBadInitialSubobject | lSPBadLooseNode | lSPBadStrictNode | lSPBadTSpecValue | lSPDelayBoundNotMet | lSPMPLSAllocationFailure | lSPMTUTooBig | lSPNonRSVPRouter | lSPNoRouteAvailable | lSPPathErr | lSPPathTearSent | lSPPceInitiatedMsgNotReceived | lSPRequestedBandwidthUnavailable | lSPReservationNotReceived | lSPReservationTearReceived | lSPReservationTearSent | lSPReservationTimeout | lSPRoutingLoops | lSPRoutingProblem | lSPRSVPSystemError | lSPServiceConflict | lSPServiceUnsupported | lSPTrafficControlError | lSPTrafficControlSystemError | lSPTrafficOrganizationError | lSPTrafficServiceError | lSPUnknownObjectClass | lSPUnknownObjectCType | lSPUnsupportedL3PID | mbbCompleted | mbbTriggered | none]): Logs additional information about the RSVP session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInformation'])

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[down | none | notStarted | pceRequestNotReceived | up]): State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is used for generating the traffic for those LSPs from PCE for which the Symbolic Path Name is configured and matches the value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SymbolicPathName']))

    def update(self, Name=None, NumberOfRroSubObjects=None):
        """Updates rsvpPcepExpectedInitiatedLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfRroSubObjects (number): Number Of RRO Sub-Objects

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, BackupLspId=None, EnableRRO=None, SymbolicPathName=None):
        """Base class infrastructure that gets a list of rsvpPcepExpectedInitiatedLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BackupLspId (str): optional regex of backupLspId
        - EnableRRO (str): optional regex of enableRRO
        - SymbolicPathName (str): optional regex of symbolicPathName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
