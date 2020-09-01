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


class PimRouter(Base):
    """Pim Port Specific Data
    The PimRouter class encapsulates a required pimRouter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pimRouter'
    _SDM_ATT_MAP = {
        'BootstrapMessagePerInterval': 'bootstrapMessagePerInterval',
        'CRpAdvertiseMessagePerInterval': 'cRpAdvertiseMessagePerInterval',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardJoinPruneProcessing': 'discardJoinPruneProcessing',
        'EnableRateControl': 'enableRateControl',
        'HelloMessagePerInterval': 'helloMessagePerInterval',
        'Interval': 'interval',
        'JoinPruneMessagePerInterval': 'joinPruneMessagePerInterval',
        'Name': 'name',
        'RegisterMessagePerInterval': 'registerMessagePerInterval',
        'RegisterStopMessagePerInterval': 'registerStopMessagePerInterval',
        'RowNames': 'rowNames',
    }

    def __init__(self, parent):
        super(PimRouter, self).__init__(parent)

    @property
    def BootstrapMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bootstrap Messages Per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BootstrapMessagePerInterval']))

    @property
    def CRpAdvertiseMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-RP Advertise Messages per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRpAdvertiseMessagePerInterval']))

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
    def DiscardJoinPruneProcessing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard join/Prune Processing
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardJoinPruneProcessing']))

    @property
    def EnableRateControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Rate Control
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRateControl']))

    @property
    def HelloMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello Messages per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloMessagePerInterval']))

    @property
    def Interval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Interval']))

    @property
    def JoinPruneMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Join/Prune Messages per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JoinPruneMessagePerInterval']))

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
    def RegisterMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Register Messages Per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RegisterMessagePerInterval']))

    @property
    def RegisterStopMessagePerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Register Stop Messages Per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RegisterStopMessagePerInterval']))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    def update(self, Name=None):
        """Updates pimRouter resource on the server.

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

    def get_device_ids(self, PortNames=None, BootstrapMessagePerInterval=None, CRpAdvertiseMessagePerInterval=None, DiscardJoinPruneProcessing=None, EnableRateControl=None, HelloMessagePerInterval=None, Interval=None, JoinPruneMessagePerInterval=None, RegisterMessagePerInterval=None, RegisterStopMessagePerInterval=None):
        """Base class infrastructure that gets a list of pimRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BootstrapMessagePerInterval (str): optional regex of bootstrapMessagePerInterval
        - CRpAdvertiseMessagePerInterval (str): optional regex of cRpAdvertiseMessagePerInterval
        - DiscardJoinPruneProcessing (str): optional regex of discardJoinPruneProcessing
        - EnableRateControl (str): optional regex of enableRateControl
        - HelloMessagePerInterval (str): optional regex of helloMessagePerInterval
        - Interval (str): optional regex of interval
        - JoinPruneMessagePerInterval (str): optional regex of joinPruneMessagePerInterval
        - RegisterMessagePerInterval (str): optional regex of registerMessagePerInterval
        - RegisterStopMessagePerInterval (str): optional regex of registerStopMessagePerInterval

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
