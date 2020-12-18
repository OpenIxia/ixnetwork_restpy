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


class Ospfv3Router(Base):
    """Ospfv3 Device level Configuration
    The Ospfv3Router class encapsulates a list of ospfv3Router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ospfv3Router.find() method.
    The list can be managed by using the Ospfv3Router.add() and Ospfv3Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv3Router'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Algorithm': 'algorithm',
        'BBit': 'bBit',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DisableAutoGenerateLinkLsa': 'disableAutoGenerateLinkLsa',
        'DisableAutoGenerateRouterLsa': 'disableAutoGenerateRouterLsa',
        'DiscardLearnedLsa': 'discardLearnedLsa',
        'EBit': 'eBit',
        'EFlag': 'eFlag',
        'EnableGracefulRestartHelperMode': 'enableGracefulRestartHelperMode',
        'EnableSrMpls': 'enableSrMpls',
        'EnableStrictLsaChecking': 'enableStrictLsaChecking',
        'EnableSupportReasonSwReloadUpgrade': 'enableSupportReasonSwReloadUpgrade',
        'EnableSupportReasonSwRestart': 'enableSupportReasonSwRestart',
        'EnableSupportReasonSwitchToRedundantControlProcessor': 'enableSupportReasonSwitchToRedundantControlProcessor',
        'EnableSupportReasonUnknown': 'enableSupportReasonUnknown',
        'Errors': 'errors',
        'LFlag': 'lFlag',
        'LocalRouterId': 'localRouterId',
        'LoopbackAddress': 'loopbackAddress',
        'LsaRefreshTime': 'lsaRefreshTime',
        'LsaRetransmitTime': 'lsaRetransmitTime',
        'MFlag': 'mFlag',
        'MaxNumLsaPerSecond': 'maxNumLsaPerSecond',
        'Name': 'name',
        'NpFlag': 'npFlag',
        'PrefixOptions': 'prefixOptions',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'SidIndexLabel': 'sidIndexLabel',
        'SrgbRangeCount': 'srgbRangeCount',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(Ospfv3Router, self).__init__(parent)

    @property
    def Ospfv3SRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist_be527e153c8e6d4e5c3f4321aa8409c4.Ospfv3SRGBRangeSubObjectsList): An instance of the Ospfv3SRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist_be527e153c8e6d4e5c3f4321aa8409c4 import Ospfv3SRGBRangeSubObjectsList
        return Ospfv3SRGBRangeSubObjectsList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Algorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm for the Node SID/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def BBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA B-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BBit']))

    @property
    def ConfigureSIDIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Lets the corresponding router send Prefix SID. By default, it is selected
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

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
    def DisableAutoGenerateLinkLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unknown and unplanned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateLinkLsa']))

    @property
    def DisableAutoGenerateRouterLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unknown and unplanned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateRouterLsa']))

    @property
    def DiscardLearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard Learned LSAs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa']))

    @property
    def EBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA E-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EBit']))

    @property
    def EFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): E Flag: Explicit-Null Flag: If set, any upstream neighbor of the Prefix-SID originator MUST replace the Prefix-SID with a Prefix-SID having an Explicit-NULL value (0 for IPv4 and 2 for IPv6)before forwarding the packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EnableGracefulRestartHelperMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Graceful Restart helper Mode,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode']))

    @property
    def EnableSrMpls(self):
        """
        Returns
        -------
        - bool: Makes the Segment Routing configuration enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSrMpls'])
    @EnableSrMpls.setter
    def EnableSrMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSrMpls'], value)

    @property
    def EnableStrictLsaChecking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Terminate graceful restart when an LSA has changed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableStrictLsaChecking']))

    @property
    def EnableSupportReasonSwReloadUpgrade(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is Software Reload or Upgrade.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwReloadUpgrade']))

    @property
    def EnableSupportReasonSwRestart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is Ospfv3 software restart.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwRestart']))

    @property
    def EnableSupportReasonSwitchToRedundantControlProcessor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unplanned switchover.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwitchToRedundantControlProcessor']))

    @property
    def EnableSupportReasonUnknown(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unknown and unplanned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonUnknown']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def LoopbackAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node IPv6 loopback address advertised in Extended Intra Area LSAs by OSPFv3 routers
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LoopbackAddress']))

    @property
    def LsaRefreshTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSA Refresh time (s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsaRefreshTime']))

    @property
    def LsaRetransmitTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSA Retransmit time(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsaRetransmitTime']))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): M-Flag: Mapping Server Flag: If set, the SID was advertised bya Segment Routing Mapping Server
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def MaxNumLsaPerSecond(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter Flood LSUpdate burst gap (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxNumLsaPerSecond']))

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
    def NpFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): NP Flag: No-PHP Flag: If set, then the penultimate hop MUST NOT pop thePrefix-SID before delivering the packet to the node that advertised the Prefix-SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NpFlag']))

    @property
    def PrefixOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix options bits (N, DN, P, x, LA, NU) advertised along with Node Loopback Address in Extended Intra Area LSAs by OSPFv3 routers. Default value is 0x20 which indicates N (Node) bit is set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixOptions']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[noIfaceUp | up]): Logs additional information about the session Information
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SidIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label value associated with the IGP Prefix segment attached to the specific IPv6 prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexLabel']))

    @property
    def SrgbRangeCount(self):
        """
        Returns
        -------
        - number: count of the configurable list of SRGB
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrgbRangeCount'])
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrgbRangeCount'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): V-Flag: Value flag. If set, then the SID carries an absolute value label value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Updates ospfv3Router resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSrMpls (bool): Makes the Segment Routing configuration enabled
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrgbRangeCount (number): count of the configurable list of SRGB

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Adds a new ospfv3Router resource on the server and adds it to the container.

        Args
        ----
        - EnableSrMpls (bool): Makes the Segment Routing configuration enabled
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrgbRangeCount (number): count of the configurable list of SRGB

        Returns
        -------
        - self: This instance with all currently retrieved ospfv3Router resources using find and the newly added ospfv3Router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ospfv3Router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, EnableSrMpls=None, Errors=None, LocalRouterId=None, Name=None, SessionInfo=None, SessionStatus=None, SrgbRangeCount=None, StateCounts=None, Status=None):
        """Finds and retrieves ospfv3Router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv3Router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv3Router resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSrMpls (bool): Makes the Segment Routing configuration enabled
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterId (list(str)): Router ID
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[noIfaceUp | up])): Logs additional information about the session Information
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SrgbRangeCount (number): count of the configurable list of SRGB
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ospfv3Router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv3Router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv3Router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EBit=None, EFlag=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, LFlag=None, LoopbackAddress=None, LsaRefreshTime=None, LsaRetransmitTime=None, MFlag=None, MaxNumLsaPerSecond=None, NpFlag=None, PrefixOptions=None, SidIndexLabel=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfv3Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Algorithm (str): optional regex of algorithm
        - BBit (str): optional regex of bBit
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DisableAutoGenerateLinkLsa (str): optional regex of disableAutoGenerateLinkLsa
        - DisableAutoGenerateRouterLsa (str): optional regex of disableAutoGenerateRouterLsa
        - DiscardLearnedLsa (str): optional regex of discardLearnedLsa
        - EBit (str): optional regex of eBit
        - EFlag (str): optional regex of eFlag
        - EnableGracefulRestartHelperMode (str): optional regex of enableGracefulRestartHelperMode
        - EnableStrictLsaChecking (str): optional regex of enableStrictLsaChecking
        - EnableSupportReasonSwReloadUpgrade (str): optional regex of enableSupportReasonSwReloadUpgrade
        - EnableSupportReasonSwRestart (str): optional regex of enableSupportReasonSwRestart
        - EnableSupportReasonSwitchToRedundantControlProcessor (str): optional regex of enableSupportReasonSwitchToRedundantControlProcessor
        - EnableSupportReasonUnknown (str): optional regex of enableSupportReasonUnknown
        - LFlag (str): optional regex of lFlag
        - LoopbackAddress (str): optional regex of loopbackAddress
        - LsaRefreshTime (str): optional regex of lsaRefreshTime
        - LsaRetransmitTime (str): optional regex of lsaRetransmitTime
        - MFlag (str): optional regex of mFlag
        - MaxNumLsaPerSecond (str): optional regex of maxNumLsaPerSecond
        - NpFlag (str): optional regex of npFlag
        - PrefixOptions (str): optional regex of prefixOptions
        - SidIndexLabel (str): optional regex of sidIndexLabel
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def Ospfv3StartRouter(self, *args, **kwargs):
        """Executes the ospfv3StartRouter operation on the server.

        Start OSPFv3 Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ospfv3StartRouter(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ospfv3StartRouter(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ospfv3StartRouter', payload=payload, response_object=None)

    def Ospfv3StopRouter(self, *args, **kwargs):
        """Executes the ospfv3StopRouter operation on the server.

        Stop OSPFv3 Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ospfv3StopRouter(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ospfv3StopRouter(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ospfv3StopRouter', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
