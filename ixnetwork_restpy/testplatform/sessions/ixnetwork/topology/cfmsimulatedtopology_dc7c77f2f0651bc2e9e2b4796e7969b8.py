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


class CfmSimulatedTopology(Base):
    """CFM Simulated Topology specific configuration
    The CfmSimulatedTopology class encapsulates a list of cfmSimulatedTopology resources that are managed by the system.
    A list of resources can be retrieved from the server using the CfmSimulatedTopology.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'cfmSimulatedTopology'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(CfmSimulatedTopology, self).__init__(parent)

    @property
    def ConfigMANamesParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configmanamesparams_122374d4856af71309d8e8b3391bfdcd.ConfigMANamesParams): An instance of the ConfigMANamesParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configmanamesparams_122374d4856af71309d8e8b3391bfdcd import ConfigMANamesParams
        return ConfigMANamesParams(self)._select()

    @property
    def ConfigMDLevelsParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configmdlevelsparams_1bf3d8514855f50e409c0aef7ac6bf1e.ConfigMDLevelsParams): An instance of the ConfigMDLevelsParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configmdlevelsparams_1bf3d8514855f50e409c0aef7ac6bf1e import ConfigMDLevelsParams
        return ConfigMDLevelsParams(self)._select()

    @property
    def ConfigVLANParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configvlanparams_ab1a6e3f956da910a4175820dceb06bd.ConfigVLANParams): An instance of the ConfigVLANParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.configvlanparams_ab1a6e3f956da910a4175820dceb06bd import ConfigVLANParams
        return ConfigVLANParams(self)._select()

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

    def update(self, Name=None):
        """Updates cfmSimulatedTopology resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves cfmSimulatedTopology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cfmSimulatedTopology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cfmSimulatedTopology resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching cfmSimulatedTopology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cfmSimulatedTopology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cfmSimulatedTopology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None):
        """Base class infrastructure that gets a list of cfmSimulatedTopology device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active

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

    def ConfigMANames(self, *args, **kwargs):
        """Executes the configMANames operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        DEPRECATED configMANames(Arg2=enum, Arg3=string, Arg4=bool)list
        ---------------------------------------------------------------
        - Arg2 (str(megIdFormatTypeIccBasedFormat | megIdFormatTypePrimaryVid | megIdFormatTypeCharStr | megIdFormatTypeTwoOctetInt | megIdFormatTypeRfc2685VpnId)): Import only the best routes (provided route file has this information).
        - Arg3 (str): Import only the best routes (provided route file has this information).
        - Arg4 (bool): Import only the best routes (provided route file has this information).
        - Returns list(str): ID to associate each asynchronous action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configMANames', payload=payload, response_object=None)

    def ConfigMDLevels(self, *args, **kwargs):
        """Executes the configMDLevels operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        DEPRECATED configMDLevels(Arg2=number, Arg3=number, Arg4=enum, Arg5=string, Arg6=number, Arg7=enum, Arg8=string, Arg9=number, Arg10=enum, Arg11=string, Arg12=number, Arg13=enum, Arg14=string, Arg15=number, Arg16=enum, Arg17=string, Arg18=number, Arg19=enum, Arg20=string, Arg21=number, Arg22=enum, Arg23=string, Arg24=number, Arg25=enum, Arg26=string)list
        -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): Import only the best routes (provided route file has this information).
        - Arg3 (number): Text
        - Arg4 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg5 (str): Network Address Step Value.
        - Arg6 (number): Text
        - Arg7 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg8 (str): Network Address Step Value.
        - Arg9 (number): Text
        - Arg10 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg11 (str): Network Address Step Value.
        - Arg12 (number): Text
        - Arg13 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg14 (str): Network Address Step Value.
        - Arg15 (number): Text
        - Arg16 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg17 (str): Network Address Step Value.
        - Arg18 (number): Text
        - Arg19 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg20 (str): Network Address Step Value.
        - Arg21 (number): Text
        - Arg22 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg23 (str): Network Address Step Value.
        - Arg24 (number): Text
        - Arg25 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - Arg26 (str): Network Address Step Value.
        - Returns list(str): ID to associate each asynchronous action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configMDLevels', payload=payload, response_object=None)

    def ConfigVLAN(self, *args, **kwargs):
        """Executes the configVLAN operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        DEPRECATED configVLAN(Arg2=bool, Arg3=enum, Arg4=number, Arg5=number, Arg6=number, Arg7=enum, Arg8=number, Arg9=number, Arg10=number, Arg11=enum, Arg12=number, Arg13=number, Arg14=number, Arg15=enum)list
        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (bool): Import only the best routes (provided route file has this information).
        - Arg3 (str(vlanStackingTypeSingleVlan | vlanStackingTypeStackedVlan)): Import only the best routes (provided route file has this information).
        - Arg4 (number): Import only the best routes (provided route file has this information).
        - Arg5 (number): Import only the best routes (provided route file has this information).
        - Arg6 (number): Import only the best routes (provided route file has this information).
        - Arg7 (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - Arg8 (number): Import only the best routes (provided route file has this information).
        - Arg9 (number): Import only the best routes (provided route file has this information).
        - Arg10 (number): Import only the best routes (provided route file has this information).
        - Arg11 (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - Arg12 (number): Import only the best routes (provided route file has this information).
        - Arg13 (number): Import only the best routes (provided route file has this information).
        - Arg14 (number): Import only the best routes (provided route file has this information).
        - Arg15 (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - Returns list(str): ID to associate each asynchronous action invocation.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configVLAN', payload=payload, response_object=None)

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
