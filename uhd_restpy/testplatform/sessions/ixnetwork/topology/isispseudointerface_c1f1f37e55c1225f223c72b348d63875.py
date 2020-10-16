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


class IsisPseudoInterface(Base):
    """Information for Simulated Router Interfaces
    The IsisPseudoInterface class encapsulates a list of isisPseudoInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisPseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoInterface'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'LinkType': 'linkType',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(IsisPseudoInterface, self).__init__(parent)

    @property
    def IsisDcePseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_dce0066317952a09c055b9f568621953.IsisDcePseudoIfaceAttPoint1Config): An instance of the IsisDcePseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_dce0066317952a09c055b9f568621953 import IsisDcePseudoIfaceAttPoint1Config
        return IsisDcePseudoIfaceAttPoint1Config(self)

    @property
    def IsisDcePseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_08c96458d8806c0878ba2591f7235870.IsisDcePseudoIfaceAttPoint2Config): An instance of the IsisDcePseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_08c96458d8806c0878ba2591f7235870 import IsisDcePseudoIfaceAttPoint2Config
        return IsisDcePseudoIfaceAttPoint2Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_e6b2374da4892fed3474f1ab974dbf1c.IsisL3PseudoIfaceAttPoint1Config): An instance of the IsisL3PseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_e6b2374da4892fed3474f1ab974dbf1c import IsisL3PseudoIfaceAttPoint1Config
        return IsisL3PseudoIfaceAttPoint1Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_37681cb7f2d7b1eb6c812c1b9f243542.IsisL3PseudoIfaceAttPoint2Config): An instance of the IsisL3PseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_37681cb7f2d7b1eb6c812c1b9f243542 import IsisL3PseudoIfaceAttPoint2Config
        return IsisL3PseudoIfaceAttPoint2Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_04ab03c0f19e657e435c655358111db5.IsisSpbPseudoIfaceAttPoint1Config): An instance of the IsisSpbPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_04ab03c0f19e657e435c655358111db5 import IsisSpbPseudoIfaceAttPoint1Config
        return IsisSpbPseudoIfaceAttPoint1Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_0781ccf029e86f2c708647212802930e.IsisSpbPseudoIfaceAttPoint2Config): An instance of the IsisSpbPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_0781ccf029e86f2c708647212802930e import IsisSpbPseudoIfaceAttPoint2Config
        return IsisSpbPseudoIfaceAttPoint2Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_4c83cc199df8becee43d785e9ef03dc7.IsisTrillPseudoIfaceAttPoint1Config): An instance of the IsisTrillPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_4c83cc199df8becee43d785e9ef03dc7 import IsisTrillPseudoIfaceAttPoint1Config
        return IsisTrillPseudoIfaceAttPoint1Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_1910327d5bcdde39c812851ec539a846.IsisTrillPseudoIfaceAttPoint2Config): An instance of the IsisTrillPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_1910327d5bcdde39c812851ec539a846 import IsisTrillPseudoIfaceAttPoint2Config
        return IsisTrillPseudoIfaceAttPoint2Config(self)

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
    def LinkType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Link Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkType']))

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
        """Updates isisPseudoInterface resource on the server.

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
        """Finds and retrieves isisPseudoInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisPseudoInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisPseudoInterface resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisPseudoInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisPseudoInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisPseudoInterface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, LinkType=None):
        """Base class infrastructure that gets a list of isisPseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - LinkType (str): optional regex of linkType

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
