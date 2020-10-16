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


class Buckets(Base):
    """Bucket configuration
    The Buckets class encapsulates a list of buckets resources that are managed by the system.
    A list of resources can be retrieved from the server using the Buckets.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'buckets'
    _SDM_ATT_MAP = {
        'BucketDescription': 'bucketDescription',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'GroupIndex': 'groupIndex',
        'GroupName': 'groupName',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'WatchGroup': 'watchGroup',
        'WatchPort': 'watchPort',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(Buckets, self).__init__(parent)

    @property
    def ActionsProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.actionsprofile_c65384e18e20517e184ef23474b0b960.ActionsProfile): An instance of the ActionsProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.actionsprofile_c65384e18e20517e184ef23474b0b960 import ActionsProfile
        return ActionsProfile(self)._select()

    @property
    def BucketDescription(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A description for the bucket.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BucketDescription']))

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
    def GroupIndex(self):
        """
        Returns
        -------
        - list(str): Group Index
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupIndex'])

    @property
    def GroupName(self):
        """
        Returns
        -------
        - str: Parent Group Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupName'])

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def WatchGroup(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A group whose state determines whether this bucket is live or not.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WatchGroup']))

    @property
    def WatchPort(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A Port whose state determines whether this bucket is live or not.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WatchPort']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specify the weight of buckets. The permissible range is 0-65535.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Multiplier=None, Name=None):
        """Updates buckets resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, GroupIndex=None, GroupName=None, Multiplier=None, Name=None):
        """Finds and retrieves buckets resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve buckets resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all buckets resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - GroupIndex (list(str)): Group Index
        - GroupName (str): Parent Group Name
        - Multiplier (number): Number of instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching buckets resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of buckets data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the buckets resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BucketDescription=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Base class infrastructure that gets a list of buckets device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BucketDescription (str): optional regex of bucketDescription
        - WatchGroup (str): optional regex of watchGroup
        - WatchPort (str): optional regex of watchPort
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
