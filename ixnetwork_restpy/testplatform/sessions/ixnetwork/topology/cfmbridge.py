# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class CfmBridge(Base):
    """
    The CfmBridge class encapsulates a list of cfmBridge resources that is be managed by the user.
    A list of resources can be retrieved from the server using the CfmBridge.find() method.
    The list can be managed by the user by using the CfmBridge.add() and CfmBridge.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'cfmBridge'

    def __init__(self, parent):
        super(CfmBridge, self).__init__(parent)

    @property
    def AdvancedLearnedInfoOptions(self):
        """An instance of the AdvancedLearnedInfoOptions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.advancedlearnedinfooptions.AdvancedLearnedInfoOptions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.advancedlearnedinfooptions import AdvancedLearnedInfoOptions
        return AdvancedLearnedInfoOptions(self)._select()

    @property
    def CustomTLV(self):
        """An instance of the CustomTLV class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.customtlv.CustomTLV)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.customtlv import CustomTLV
        return CustomTLV(self)._select()

    @property
    def LearnedInfo(self):
        """An instance of the LearnedInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
        return LearnedInfo(self)

    @property
    def Link(self):
        """An instance of the Link class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.link.Link)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.link import Link
        return Link(self)._select()

    @property
    def MdLevels(self):
        """An instance of the MdLevels class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mdlevels.MdLevels)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mdlevels import MdLevels
        return MdLevels(self)._select()

    @property
    def Mp(self):
        """An instance of the Mp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mp.Mp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mp import Mp
        return Mp(self)._select()

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def AllowCfmMaidFormatsinY1731(self):
        """Allow CFM MAID Formats in Y.1731

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allowCfmMaidFormatsinY1731')

    @property
    def ConnectedVia(self):
        """DEPRECATED List of layers this layer used to connect to the wire

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def EnableOutOfSequenceCcmDetection(self):
        """Enable Out of Sequence CCM Detection

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableOutOfSequenceCcmDetection')

    @property
    def EncapsulationType(self):
        """Encapsulation

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('encapsulationType')

    @property
    def Errors(self):
        """A list of errors that have occurred

        Returns:
            list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
        """
        return self._get_attribute('errors')

    @property
    def EtherType(self):
        """Ether Type

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('etherType')

    @property
    def GarbageCollectionTime(self):
        """Garbage Collection Time (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('garbageCollectionTime')

    @property
    def Multiplier(self):
        """Number of layer instances per parent instance (multiplier)

        Returns:
            number
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NumberOfCustomTLVs(self):
        """Number of Custom TLVs

        Returns:
            number
        """
        return self._get_attribute('numberOfCustomTLVs')
    @NumberOfCustomTLVs.setter
    def NumberOfCustomTLVs(self, value):
        self._set_attribute('numberOfCustomTLVs', value)

    @property
    def NumberOfLinks(self):
        """Number of Links

        Returns:
            number
        """
        return self._get_attribute('numberOfLinks')
    @NumberOfLinks.setter
    def NumberOfLinks(self, value):
        self._set_attribute('numberOfLinks', value)

    @property
    def NumberOfMPs(self):
        """Number of MPs

        Returns:
            number
        """
        return self._get_attribute('numberOfMPs')
    @NumberOfMPs.setter
    def NumberOfMPs(self, value):
        self._set_attribute('numberOfMPs', value)

    @property
    def NumberOfMdLevels(self):
        """Number of MD/MEG Levels

        Returns:
            number
        """
        return self._get_attribute('numberOfMdLevels')
    @NumberOfMdLevels.setter
    def NumberOfMdLevels(self, value):
        self._set_attribute('numberOfMdLevels', value)

    @property
    def OperationMode(self):
        """Operation Mode

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('operationMode')

    @property
    def SessionStatus(self):
        """Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

        Returns:
            list(str[down|notStarted|up])
        """
        return self._get_attribute('sessionStatus')

    @property
    def StackedLayers(self):
        """List of secondary (many to one) child layer protocols

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

        Returns:
            dict(total:number,notStarted:number,down:number,up:number)
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            str(configured|error|mixed|notStarted|started|starting|stopping)
        """
        return self._get_attribute('status')

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfCustomTLVs=None, NumberOfLinks=None, NumberOfMPs=None, NumberOfMdLevels=None, StackedLayers=None):
        """Updates a child instance of cfmBridge on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfCustomTLVs (number): Number of Custom TLVs
            NumberOfLinks (number): Number of Links
            NumberOfMPs (number): Number of MPs
            NumberOfMdLevels (number): Number of MD/MEG Levels
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfCustomTLVs=None, NumberOfLinks=None, NumberOfMPs=None, NumberOfMdLevels=None, StackedLayers=None):
        """Adds a new cfmBridge node on the server and retrieves it in this instance.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfCustomTLVs (number): Number of Custom TLVs
            NumberOfLinks (number): Number of Links
            NumberOfMPs (number): Number of MPs
            NumberOfMdLevels (number): Number of MD/MEG Levels
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

        Returns:
            self: This instance with all currently retrieved cfmBridge data using find and the newly added cfmBridge data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the cfmBridge data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NumberOfCustomTLVs=None, NumberOfLinks=None, NumberOfMPs=None, NumberOfMdLevels=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves cfmBridge data from the server.

        All named parameters support regex and can be used to selectively retrieve cfmBridge data from the server.
        By default the find method takes no parameters and will retrieve all cfmBridge data from the server.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfCustomTLVs (number): Number of Custom TLVs
            NumberOfLinks (number): Number of Links
            NumberOfMPs (number): Number of MPs
            NumberOfMdLevels (number): Number of MD/MEG Levels
            SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
            Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            self: This instance with matching cfmBridge data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of cfmBridge data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the cfmBridge data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AllowCfmMaidFormatsinY1731=None, EnableOutOfSequenceCcmDetection=None, EncapsulationType=None, EtherType=None, GarbageCollectionTime=None, OperationMode=None):
        """Base class infrastructure that gets a list of cfmBridge device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            AllowCfmMaidFormatsinY1731 (str): optional regex of allowCfmMaidFormatsinY1731
            EnableOutOfSequenceCcmDetection (str): optional regex of enableOutOfSequenceCcmDetection
            EncapsulationType (str): optional regex of encapsulationType
            EtherType (str): optional regex of etherType
            GarbageCollectionTime (str): optional regex of garbageCollectionTime
            OperationMode (str): optional regex of operationMode

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        clearAllLearnedInfo()

        clearAllLearnedInfo(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        clearAllLearnedInfo(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearAllLearnedInfo(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetAllLearnedInfo(self, *args, **kwargs):
        """Executes the getAllLearnedInfo operation on the server.

        Get All Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getAllLearnedInfo()

        getAllLearnedInfo(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getAllLearnedInfo(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getAllLearnedInfo(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

    def GetCfmAISDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmAISDbLearnedInformation operation on the server.

        Get Learned AIS Information

        getCfmAISDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmAISDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmCcmLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmCcmLearnedInformation operation on the server.

        Get CCM Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getCfmCcmLearnedInformation()

        getCfmCcmLearnedInformation(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getCfmCcmLearnedInformation(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getCfmCcmLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmCcmLearnedInformation', payload=payload, response_object=None)

    def GetCfmDMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmDMDbLearnedInformation operation on the server.

        Get Learned DM Information

        getCfmDMDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmDMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLCKDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLCKDbLearnedInformation operation on the server.

        Get Learned LCK Information

        getCfmLCKDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLCKDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLinkTraceDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLinkTraceDbLearnedInformation operation on the server.

        Get LinkTrace Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getCfmLinkTraceDbLearnedInformation()

        getCfmLinkTraceDbLearnedInformation(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getCfmLinkTraceDbLearnedInformation(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getCfmLinkTraceDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLinkTraceDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLMDbLearnedInformation operation on the server.

        Get Learned LM Information

        getCfmLMDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLoopbackDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLoopbackDbLearnedInformation operation on the server.

        Get LoopBack Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getCfmLoopbackDbLearnedInformation()

        getCfmLoopbackDbLearnedInformation(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getCfmLoopbackDbLearnedInformation(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getCfmLoopbackDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLoopbackDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmTSTDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmTSTDbLearnedInformation operation on the server.

        Get Learned TST Information

        getCfmTSTDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmTSTDbLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicOAMLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicOAMLearnedInformation operation on the server.

        Get All Periodic Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getPeriodicOAMLearnedInformation()

        getPeriodicOAMLearnedInformation(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getPeriodicOAMLearnedInformation(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPeriodicOAMLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPeriodicOAMLearnedInformation', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        restartDown()

        restartDown(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CFM Bridge

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        start()

        start(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CFM Bridge

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        stop()

        stop(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
