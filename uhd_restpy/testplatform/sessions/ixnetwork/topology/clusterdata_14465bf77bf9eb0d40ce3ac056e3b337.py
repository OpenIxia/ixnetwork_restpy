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


class ClusterData(Base):
    """Ovsdb Controller Cluster Specific Data
    The ClusterData class encapsulates a required clusterData resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'clusterData'
    _SDM_ATT_MAP = {
        'ActionTriggered': 'actionTriggered',
        'AttachAtStart': 'attachAtStart',
        'AutoSyncAtStart': 'autoSyncAtStart',
        'BindingStatus': 'bindingStatus',
        'BindingsCount': 'bindingsCount',
        'Count': 'count',
        'CurrentRetryCount': 'currentRetryCount',
        'DescriptiveName': 'descriptiveName',
        'ErrorStatus': 'errorStatus',
        'LogicalSwitchName': 'logicalSwitchName',
        'MaxRetryCount': 'maxRetryCount',
        'Name': 'name',
        'PhysicalPortName': 'physicalPortName',
        'PhysicalSwitchName': 'physicalSwitchName',
        'ProgressStatus': 'progressStatus',
        'RetryStatus': 'retryStatus',
        'Vlan': 'vlan',
        'Vni': 'vni',
    }

    def __init__(self, parent):
        super(ClusterData, self).__init__(parent)

    @property
    def ActionTriggered(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Displays what Action Triggered for each Binding. Possible values: No Action, Attach, Detach
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActionTriggered']))

    @property
    def AttachAtStart(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Attach at Start
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AttachAtStart']))

    @property
    def AutoSyncAtStart(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Synchronize TOR Database at Start.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoSyncAtStart']))

    @property
    def BindingStatus(self):
        """
        Returns
        -------
        - list(str[attached | attaching | detached | detaching | disconnected]): Additional information about the Binding's state
        """
        return self._get_attribute(self._SDM_ATT_MAP['BindingStatus'])

    @property
    def BindingsCount(self):
        """
        Returns
        -------
        - number: Bindings Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['BindingsCount'])
    @BindingsCount.setter
    def BindingsCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BindingsCount'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CurrentRetryCount(self):
        """
        Returns
        -------
        - number: This field will Show current retry count value Controller is doing to Synchronize TOR Database Automatically when TOR is reconnecting while doing the action.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentRetryCount'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def ErrorStatus(self):
        """
        Returns
        -------
        - list(str[deleteBindingError | deleteBindingTimeout | deleteLsError | deleteLsTimeout | differentLsName | duplicateVlanLsPort | insertBindingError | insertBindingTimeout | insertLsError | insertLsTimeout | none | vlanMappedToDifferentLSs]): Error information about the Binding
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorStatus'])

    @property
    def LogicalSwitchName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Logical_Switch Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogicalSwitchName']))

    @property
    def MaxRetryCount(self):
        """
        Returns
        -------
        - number: Maximum number of Retries Controller will do the TOR Database Synchronization Automatically, If TOR is reconnecting while doing the action
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRetryCount'])
    @MaxRetryCount.setter
    def MaxRetryCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRetryCount'], value)

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
    def PhysicalPortName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Physical_Port name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PhysicalPortName']))

    @property
    def PhysicalSwitchName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Physical_Switch name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PhysicalSwitchName']))

    @property
    def ProgressStatus(self):
        """
        Returns
        -------
        - str: Gives info Controller is busy doing some actions. There are 3 states: 1. None - Default State. 2. In Progress - Processing is in Progress. 3. Done - Controller is done processing all requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProgressStatus'])

    @property
    def RetryStatus(self):
        """
        Returns
        -------
        - str: This field will Show if Controller has failed to complete the entire action even after Max Retry Count attempts There are 2 states: 1. None - Default State. 2. Retry Failed - Controller has done Max Retry Count attempts to complete the action, but failed
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryStatus'])

    @property
    def Vlan(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vlan']))

    @property
    def Vni(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VNI
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vni']))

    def update(self, BindingsCount=None, MaxRetryCount=None, Name=None):
        """Updates clusterData resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - BindingsCount (number): Bindings Count
        - MaxRetryCount (number): Maximum number of Retries Controller will do the TOR Database Synchronization Automatically, If TOR is reconnecting while doing the action
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, ActionTriggered=None, AttachAtStart=None, AutoSyncAtStart=None, LogicalSwitchName=None, PhysicalPortName=None, PhysicalSwitchName=None, Vlan=None, Vni=None):
        """Base class infrastructure that gets a list of clusterData device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActionTriggered (str): optional regex of actionTriggered
        - AttachAtStart (str): optional regex of attachAtStart
        - AutoSyncAtStart (str): optional regex of autoSyncAtStart
        - LogicalSwitchName (str): optional regex of logicalSwitchName
        - PhysicalPortName (str): optional regex of physicalPortName
        - PhysicalSwitchName (str): optional regex of physicalSwitchName
        - Vlan (str): optional regex of vlan
        - Vni (str): optional regex of vni

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Attach(self, *args, **kwargs):
        """Executes the attach operation on the server.

        Attach.

        attach(Arg2=list)list
        ---------------------
        - Arg2 (list(number)): List of indices for which to Attach.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('attach', payload=payload, response_object=None)

    def Detach(self, *args, **kwargs):
        """Executes the detach operation on the server.

        Detach.

        detach(Arg2=list)list
        ---------------------
        - Arg2 (list(number)): List of indices for which to Detach.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('detach', payload=payload, response_object=None)

    def ResetRetryStatus(self, *args, **kwargs):
        """Executes the resetRetryStatus operation on the server.

        This method will reset Current Retry Count to 0 and Retry Status to None.

        resetRetryStatus(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices for which to Reset Retry Status fields.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resetRetryStatus', payload=payload, response_object=None)

    def SyncUmrMmrTables(self, *args, **kwargs):
        """Executes the syncUmrMmrTables operation on the server.

        This method will insert missing UMR and MMR table entries for specified Logical Switches.

        syncUmrMmrTables(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices for which to Sync UMR and MMR tables.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('syncUmrMmrTables', payload=payload, response_object=None)
