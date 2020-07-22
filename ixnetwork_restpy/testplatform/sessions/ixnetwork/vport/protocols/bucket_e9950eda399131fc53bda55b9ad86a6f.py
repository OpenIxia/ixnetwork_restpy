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


class Bucket(Base):
    """Buckets imply some actions that are applied to packets sent to the group
    The Bucket class encapsulates a list of bucket resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bucket.find() method.
    The list can be managed by using the Bucket.add() and Bucket.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bucket'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'WatchGroup': 'watchGroup',
        'WatchPort': 'watchPort',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(Bucket, self).__init__(parent)

    @property
    def BucketAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucketaction_096bc17289bdf1d8e25741ca5cedec5d.BucketAction): An instance of the BucketAction class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucketaction_096bc17289bdf1d8e25741ca5cedec5d import BucketAction
        return BucketAction(self)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the bucket.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def WatchGroup(self):
        """
        Returns
        -------
        - number: A group whose state determines whether this bucket is live.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchGroup'])
    @WatchGroup.setter
    def WatchGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WatchGroup'], value)

    @property
    def WatchPort(self):
        """
        Returns
        -------
        - number: A Port whose state determines whether this bucket is live.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchPort'])
    @WatchPort.setter
    def WatchPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WatchPort'], value)

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: Specify the weight of buckets. The range allowed is 0-65535
        """
        return self._get_attribute(self._SDM_ATT_MAP['Weight'])
    @Weight.setter
    def Weight(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Weight'], value)

    def update(self, Description=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Updates bucket resource on the server.

        Args
        ----
        - Description (str): A description of the bucket.
        - WatchGroup (number): A group whose state determines whether this bucket is live.
        - WatchPort (number): A Port whose state determines whether this bucket is live.
        - Weight (number): Specify the weight of buckets. The range allowed is 0-65535

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Adds a new bucket resource on the server and adds it to the container.

        Args
        ----
        - Description (str): A description of the bucket.
        - WatchGroup (number): A group whose state determines whether this bucket is live.
        - WatchPort (number): A Port whose state determines whether this bucket is live.
        - Weight (number): Specify the weight of buckets. The range allowed is 0-65535

        Returns
        -------
        - self: This instance with all currently retrieved bucket resources using find and the newly added bucket resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bucket resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Description=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Finds and retrieves bucket resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bucket resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bucket resources from the server.

        Args
        ----
        - Description (str): A description of the bucket.
        - WatchGroup (number): A group whose state determines whether this bucket is live.
        - WatchPort (number): A Port whose state determines whether this bucket is live.
        - Weight (number): Specify the weight of buckets. The range allowed is 0-65535

        Returns
        -------
        - self: This instance with matching bucket resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bucket data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bucket resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
