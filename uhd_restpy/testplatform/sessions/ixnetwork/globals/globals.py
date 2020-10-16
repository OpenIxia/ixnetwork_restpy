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


class Globals(Base):
    """This object holds the configurable global values of IxNetwork for interfaces and the protocol stack.
    The Globals class encapsulates a required globals resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'globals'
    _SDM_ATT_MAP = {
        'ApplicationName': 'applicationName',
        'BuildNumber': 'buildNumber',
        'ConfigFileName': 'configFileName',
        'ConfigSummary': 'configSummary',
        'IsConfigDifferent': 'isConfigDifferent',
        'PersistencePath': 'persistencePath',
        'ProductVersion': 'productVersion',
        'RpfPort': 'rpfPort',
        'Username': 'username',
    }

    def __init__(self, parent):
        super(Globals, self).__init__(parent)

    @property
    def AppErrors(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.apperrors.apperrors.AppErrors): An instance of the AppErrors class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.apperrors.apperrors import AppErrors
        return AppErrors(self)

    @property
    def Diagnostics(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.diagnostics.diagnostics.Diagnostics): An instance of the Diagnostics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.diagnostics.diagnostics import Diagnostics
        return Diagnostics(self)._select()

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.interfaces.interfaces.Interfaces): An instance of the Interfaces class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.interfaces.interfaces import Interfaces
        return Interfaces(self)._select()

    @property
    def Licensing(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.licensing.licensing.Licensing): An instance of the Licensing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.licensing.licensing import Licensing
        return Licensing(self)._select()

    @property
    def PortTestOptions(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.porttestoptions.porttestoptions.PortTestOptions): An instance of the PortTestOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.porttestoptions.porttestoptions import PortTestOptions
        return PortTestOptions(self)._select()

    @property
    def Preferences(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.preferences.preferences.Preferences): An instance of the Preferences class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.preferences.preferences import Preferences
        return Preferences(self)._select()

    @property
    def ProtocolStack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.protocolstack.ProtocolStack): An instance of the ProtocolStack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.protocolstack import ProtocolStack
        return ProtocolStack(self)._select()

    @property
    def Testworkflow(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.testworkflow.testworkflow.Testworkflow): An instance of the Testworkflow class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.testworkflow.testworkflow import Testworkflow
        return Testworkflow(self)._select()

    @property
    def Topology(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.topology_678a8dc80c9b4b2b5c741072eab4305d.Topology): An instance of the Topology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.topology_678a8dc80c9b4b2b5c741072eab4305d import Topology
        return Topology(self)._select()

    @property
    def ApplicationName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplicationName'])

    @property
    def BuildNumber(self):
        """
        Returns
        -------
        - str: The IxNetwork software build number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BuildNumber'])

    @property
    def ConfigFileName(self):
        """
        Returns
        -------
        - str: The name of the configuration file.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigFileName'])

    @property
    def ConfigSummary(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str,arg3:list[dict(arg1:str,arg2:str)])): A high level summary description of the currently loaded configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfigSummary'])

    @property
    def IsConfigDifferent(self):
        """
        Returns
        -------
        - bool: (Read only) If true, then the current IxNetwork configuration is different than the configuration that was previously loaded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsConfigDifferent'])

    @property
    def PersistencePath(self):
        """
        Returns
        -------
        - str: This attribute returns a directory of the IxNetwork API server machine, where users can drop their files from the client scripts using IxNetwork APIs. To Put files in this directory, users do not require to run IxNetwork API server in administrative mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['PersistencePath'])

    @property
    def ProductVersion(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProductVersion'])

    @property
    def RpfPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RpfPort'])

    @property
    def Username(self):
        """
        Returns
        -------
        - str: The name of the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Username'])
