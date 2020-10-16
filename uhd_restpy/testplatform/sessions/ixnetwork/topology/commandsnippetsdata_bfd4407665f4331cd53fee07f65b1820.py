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


class CommandSnippetsData(Base):
    """Command Snippets Data allows user to fire Yang commands to DUT
    The CommandSnippetsData class encapsulates a required commandSnippetsData resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'commandSnippetsData'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'CommandSnippetDirectory': 'commandSnippetDirectory',
        'CommandSnippetFile': 'commandSnippetFile',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'PeriodicTransmissionInterval': 'periodicTransmissionInterval',
        'TransmissionBehaviour': 'transmissionBehaviour',
        'TransmissionCount': 'transmissionCount',
    }

    def __init__(self, parent):
        super(CommandSnippetsData, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def CommandSnippetDirectory(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Directory containing XML based Netconf compliant command snippets.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CommandSnippetDirectory']))

    @property
    def CommandSnippetFile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): File containing XML based Netconf compliant command snippet. For multiple command snippets with assymetric file names( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CommandSnippetFile']))

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

    @property
    def PeriodicTransmissionInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Minimum interval between scheduling of two transmits of the Command Snippet.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicTransmissionInterval']))

    @property
    def TransmissionBehaviour(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Transmission behaviour for command snippet.Don't Send : This means that command will not be automatically executed. This choice should beused if user wants to control the order or/and timing of sending the command snippet to the DUTusing Test Composer or Automation Script.Once: The command will be sent only once to the DUT every time session comes up with the DUT.Periodic - Continuous: The command will be sent every Transmission Interval for the full lifetime of the session.Capture should be enabled with care if this option is selected.Periodic - Fixed Count: The command will be sent Transmission Count number of times, every Periodic Transmission Interval.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TransmissionBehaviour']))

    @property
    def TransmissionCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of times to transmit the Command Snippet.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TransmissionCount']))

    def update(self, Name=None):
        """Updates commandSnippetsData resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, CommandSnippetDirectory=None, CommandSnippetFile=None, PeriodicTransmissionInterval=None, TransmissionBehaviour=None, TransmissionCount=None):
        """Base class infrastructure that gets a list of commandSnippetsData device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CommandSnippetDirectory (str): optional regex of commandSnippetDirectory
        - CommandSnippetFile (str): optional regex of commandSnippetFile
        - PeriodicTransmissionInterval (str): optional regex of periodicTransmissionInterval
        - TransmissionBehaviour (str): optional regex of transmissionBehaviour
        - TransmissionCount (str): optional regex of transmissionCount

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ExecuteCommand(self, *args, **kwargs):
        """Executes the executeCommand operation on the server.

        Send the selected command snippet if the Netconf session is established with the Netconf Server

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        executeCommand(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        executeCommand(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        executeCommand(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('executeCommand', payload=payload, response_object=None)
