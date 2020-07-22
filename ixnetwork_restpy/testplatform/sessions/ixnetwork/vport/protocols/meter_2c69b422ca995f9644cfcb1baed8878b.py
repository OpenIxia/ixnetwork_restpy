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


class Meter(Base):
    """A meter is a switch element that can measure and control the rate of packets. The meter triggers a meter band if the packet rate or byte rate passing through the meter exceeds a predefined threshold
    The Meter class encapsulates a list of meter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Meter.find() method.
    The list can be managed by using the Meter.add() and Meter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'meter'
    _SDM_ATT_MAP = {
        'Id__': '__id__',
        'Description': 'description',
        'Enabled': 'enabled',
        'MeterAdvertise': 'meterAdvertise',
        'UpdateMeterModStatus': 'updateMeterModStatus',
    }

    def __init__(self, parent):
        super(Meter, self).__init__(parent)

    @property
    def Band(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.band_f427e2ca205882a99f7a065f52007b5e.Band): An instance of the Band class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.band_f427e2ca205882a99f7a065f52007b5e import Band
        return Band(self)

    @property
    def Flags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flags_6a0e5b7e68fe5d1d336cdd25f1553d3a.Flags): An instance of the Flags class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flags_6a0e5b7e68fe5d1d336cdd25f1553d3a import Flags
        return Flags(self)._select()

    @property
    def Id__(self):
        """
        Returns
        -------
        - number: The value by which a meter is uniquely identified within a switch. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])
    @Id__.setter
    def Id__(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Id__'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the meter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If selected, this meter is used in this controller configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def MeterAdvertise(self):
        """
        Returns
        -------
        - bool: If this check box is selected, the following happens: Meter ADD message is sent automatically after OpenFlow channel comes up. Meter ADD or DEL message is sent out when the Enable is checked or cleared respectively.When this check box is not selected, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is disabled/enabled. This field is useful to send meter ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Meter Mod.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterAdvertise'])
    @MeterAdvertise.setter
    def MeterAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterAdvertise'], value)

    @property
    def UpdateMeterModStatus(self):
        """
        Returns
        -------
        - str: It is a read-only field which indicates if any meter or associated band value is changed in the GUI. If any meter/band is changed then this status indicates to the user to send a Meter MOD request to the switch so that the changed value is updated in switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateMeterModStatus'])

    def update(self, Id__=None, Description=None, Enabled=None, MeterAdvertise=None):
        """Updates meter resource on the server.

        Args
        ----
        - Id__ (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
        - Description (str): A description of the meter.
        - Enabled (bool): If selected, this meter is used in this controller configuration.
        - MeterAdvertise (bool): If this check box is selected, the following happens: Meter ADD message is sent automatically after OpenFlow channel comes up. Meter ADD or DEL message is sent out when the Enable is checked or cleared respectively.When this check box is not selected, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is disabled/enabled. This field is useful to send meter ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Meter Mod.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Id__=None, Description=None, Enabled=None, MeterAdvertise=None):
        """Adds a new meter resource on the server and adds it to the container.

        Args
        ----
        - Id__ (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
        - Description (str): A description of the meter.
        - Enabled (bool): If selected, this meter is used in this controller configuration.
        - MeterAdvertise (bool): If this check box is selected, the following happens: Meter ADD message is sent automatically after OpenFlow channel comes up. Meter ADD or DEL message is sent out when the Enable is checked or cleared respectively.When this check box is not selected, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is disabled/enabled. This field is useful to send meter ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Meter Mod.

        Returns
        -------
        - self: This instance with all currently retrieved meter resources using find and the newly added meter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained meter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Id__=None, Description=None, Enabled=None, MeterAdvertise=None, UpdateMeterModStatus=None):
        """Finds and retrieves meter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve meter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all meter resources from the server.

        Args
        ----
        - Id__ (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
        - Description (str): A description of the meter.
        - Enabled (bool): If selected, this meter is used in this controller configuration.
        - MeterAdvertise (bool): If this check box is selected, the following happens: Meter ADD message is sent automatically after OpenFlow channel comes up. Meter ADD or DEL message is sent out when the Enable is checked or cleared respectively.When this check box is not selected, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is disabled/enabled. This field is useful to send meter ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Meter Mod.
        - UpdateMeterModStatus (str): It is a read-only field which indicates if any meter or associated band value is changed in the GUI. If any meter/band is changed then this status indicates to the user to send a Meter MOD request to the switch so that the changed value is updated in switch.

        Returns
        -------
        - self: This instance with matching meter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of meter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the meter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateMeterMod(self, *args, **kwargs):
        """Executes the updateMeterMod operation on the server.

        NOT DEFINED

        updateMeterMod(Arg2=enum)bool
        -----------------------------
        - Arg2 (str(sendMeterAdd | sendMeterModify | sendMeterRemove)): NOT DEFINED
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('updateMeterMod', payload=payload, response_object=None)
