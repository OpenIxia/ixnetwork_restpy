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


class CrpRange(Base):
    """Canditate RPs can be configured as a range of RPs responsible for a set of groups in one-to-one or fully-meshed relation. This field is used to create 'N' number of such RP to Group ranges.
    The CrpRange class encapsulates a list of crpRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CrpRange.find() method.
    The list can be managed by using the CrpRange.add() and CrpRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'crpRange'
    _SDM_ATT_MAP = {
        'AdvertisementHoldTime': 'advertisementHoldTime',
        'BackOffInterval': 'backOffInterval',
        'CrpAddress': 'crpAddress',
        'Enabled': 'enabled',
        'GroupAddress': 'groupAddress',
        'GroupCount': 'groupCount',
        'GroupMaskLen': 'groupMaskLen',
        'MeshingType': 'meshingType',
        'PeriodicAdvertisementInterval': 'periodicAdvertisementInterval',
        'PriorityChangeInterval': 'priorityChangeInterval',
        'PriorityType': 'priorityType',
        'PriorityValue': 'priorityValue',
        'RouterCount': 'routerCount',
        'TriggeredCrpMessageCount': 'triggeredCrpMessageCount',
    }

    def __init__(self, parent):
        super(CrpRange, self).__init__(parent)

    @property
    def AdvertisementHoldTime(self):
        """
        Returns
        -------
        - number: The time interval (in seconds) between two consecutive Candidate RP advertisements.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertisementHoldTime'])
    @AdvertisementHoldTime.setter
    def AdvertisementHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertisementHoldTime'], value)

    @property
    def BackOffInterval(self):
        """
        Returns
        -------
        - number: The back off time interval for the C-RP-Adv messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackOffInterval'])
    @BackOffInterval.setter
    def BackOffInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackOffInterval'], value)

    @property
    def CrpAddress(self):
        """
        Returns
        -------
        - str: Start address of the set of candidate RPs to be simulated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CrpAddress'])
    @CrpAddress.setter
    def CrpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CrpAddress'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables/disables a Candidate RP range on the fly. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - str: Starting group address of the group range for which the candidate RP will advertise candidacy.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])
    @GroupAddress.setter
    def GroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupAddress'], value)

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - number: Number of groups in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupCount'])
    @GroupCount.setter
    def GroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupCount'], value)

    @property
    def GroupMaskLen(self):
        """
        Returns
        -------
        - number: Mask width (prefix length in bits) for the group range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupMaskLen'])
    @GroupMaskLen.setter
    def GroupMaskLen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupMaskLen'], value)

    @property
    def MeshingType(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): It indicates if the mappings for groups and RP addresses are Fully-Meshed or One-To-One.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeshingType'])
    @MeshingType.setter
    def MeshingType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeshingType'], value)

    @property
    def PeriodicAdvertisementInterval(self):
        """
        Returns
        -------
        - number: Rate controlling variable indicating how many C-RP-Adv messages can be sent in the specified time interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicAdvertisementInterval'])
    @PeriodicAdvertisementInterval.setter
    def PeriodicAdvertisementInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicAdvertisementInterval'], value)

    @property
    def PriorityChangeInterval(self):
        """
        Returns
        -------
        - number: Time interval after which priority of all the RPs get changed, if priority type is incremental or random.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityChangeInterval'])
    @PriorityChangeInterval.setter
    def PriorityChangeInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityChangeInterval'], value)

    @property
    def PriorityType(self):
        """
        Returns
        -------
        - str(same | incremental | random): It indicates the type of priority to be held by the candidate RPs (CRPs). The options are Same, Incremental, and Random.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityType'])
    @PriorityType.setter
    def PriorityType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityType'], value)

    @property
    def PriorityValue(self):
        """
        Returns
        -------
        - number: Value of priority field sent in candidate RP advertisement messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityValue'])
    @PriorityValue.setter
    def PriorityValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityValue'], value)

    @property
    def RouterCount(self):
        """
        Returns
        -------
        - number: Total number of candidate RPs to be simulated starting from C-RP Address. A contiguous address range is used for this RP range simulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterCount'])
    @RouterCount.setter
    def RouterCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterCount'], value)

    @property
    def TriggeredCrpMessageCount(self):
        """
        Returns
        -------
        - number: The number of times CRP advertisements is sent to the newly elected Bootstrap Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggeredCrpMessageCount'])
    @TriggeredCrpMessageCount.setter
    def TriggeredCrpMessageCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggeredCrpMessageCount'], value)

    def update(self, AdvertisementHoldTime=None, BackOffInterval=None, CrpAddress=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMaskLen=None, MeshingType=None, PeriodicAdvertisementInterval=None, PriorityChangeInterval=None, PriorityType=None, PriorityValue=None, RouterCount=None, TriggeredCrpMessageCount=None):
        """Updates crpRange resource on the server.

        Args
        ----
        - AdvertisementHoldTime (number): The time interval (in seconds) between two consecutive Candidate RP advertisements.
        - BackOffInterval (number): The back off time interval for the C-RP-Adv messages.
        - CrpAddress (str): Start address of the set of candidate RPs to be simulated.
        - Enabled (bool): Enables/disables a Candidate RP range on the fly. The default is disabled.
        - GroupAddress (str): Starting group address of the group range for which the candidate RP will advertise candidacy.
        - GroupCount (number): Number of groups in the range.
        - GroupMaskLen (number): Mask width (prefix length in bits) for the group range.
        - MeshingType (str(fullyMeshed | oneToOne)): It indicates if the mappings for groups and RP addresses are Fully-Meshed or One-To-One.
        - PeriodicAdvertisementInterval (number): Rate controlling variable indicating how many C-RP-Adv messages can be sent in the specified time interval.
        - PriorityChangeInterval (number): Time interval after which priority of all the RPs get changed, if priority type is incremental or random.
        - PriorityType (str(same | incremental | random)): It indicates the type of priority to be held by the candidate RPs (CRPs). The options are Same, Incremental, and Random.
        - PriorityValue (number): Value of priority field sent in candidate RP advertisement messages.
        - RouterCount (number): Total number of candidate RPs to be simulated starting from C-RP Address. A contiguous address range is used for this RP range simulation.
        - TriggeredCrpMessageCount (number): The number of times CRP advertisements is sent to the newly elected Bootstrap Router.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertisementHoldTime=None, BackOffInterval=None, CrpAddress=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMaskLen=None, MeshingType=None, PeriodicAdvertisementInterval=None, PriorityChangeInterval=None, PriorityType=None, PriorityValue=None, RouterCount=None, TriggeredCrpMessageCount=None):
        """Adds a new crpRange resource on the server and adds it to the container.

        Args
        ----
        - AdvertisementHoldTime (number): The time interval (in seconds) between two consecutive Candidate RP advertisements.
        - BackOffInterval (number): The back off time interval for the C-RP-Adv messages.
        - CrpAddress (str): Start address of the set of candidate RPs to be simulated.
        - Enabled (bool): Enables/disables a Candidate RP range on the fly. The default is disabled.
        - GroupAddress (str): Starting group address of the group range for which the candidate RP will advertise candidacy.
        - GroupCount (number): Number of groups in the range.
        - GroupMaskLen (number): Mask width (prefix length in bits) for the group range.
        - MeshingType (str(fullyMeshed | oneToOne)): It indicates if the mappings for groups and RP addresses are Fully-Meshed or One-To-One.
        - PeriodicAdvertisementInterval (number): Rate controlling variable indicating how many C-RP-Adv messages can be sent in the specified time interval.
        - PriorityChangeInterval (number): Time interval after which priority of all the RPs get changed, if priority type is incremental or random.
        - PriorityType (str(same | incremental | random)): It indicates the type of priority to be held by the candidate RPs (CRPs). The options are Same, Incremental, and Random.
        - PriorityValue (number): Value of priority field sent in candidate RP advertisement messages.
        - RouterCount (number): Total number of candidate RPs to be simulated starting from C-RP Address. A contiguous address range is used for this RP range simulation.
        - TriggeredCrpMessageCount (number): The number of times CRP advertisements is sent to the newly elected Bootstrap Router.

        Returns
        -------
        - self: This instance with all currently retrieved crpRange resources using find and the newly added crpRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained crpRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertisementHoldTime=None, BackOffInterval=None, CrpAddress=None, Enabled=None, GroupAddress=None, GroupCount=None, GroupMaskLen=None, MeshingType=None, PeriodicAdvertisementInterval=None, PriorityChangeInterval=None, PriorityType=None, PriorityValue=None, RouterCount=None, TriggeredCrpMessageCount=None):
        """Finds and retrieves crpRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve crpRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all crpRange resources from the server.

        Args
        ----
        - AdvertisementHoldTime (number): The time interval (in seconds) between two consecutive Candidate RP advertisements.
        - BackOffInterval (number): The back off time interval for the C-RP-Adv messages.
        - CrpAddress (str): Start address of the set of candidate RPs to be simulated.
        - Enabled (bool): Enables/disables a Candidate RP range on the fly. The default is disabled.
        - GroupAddress (str): Starting group address of the group range for which the candidate RP will advertise candidacy.
        - GroupCount (number): Number of groups in the range.
        - GroupMaskLen (number): Mask width (prefix length in bits) for the group range.
        - MeshingType (str(fullyMeshed | oneToOne)): It indicates if the mappings for groups and RP addresses are Fully-Meshed or One-To-One.
        - PeriodicAdvertisementInterval (number): Rate controlling variable indicating how many C-RP-Adv messages can be sent in the specified time interval.
        - PriorityChangeInterval (number): Time interval after which priority of all the RPs get changed, if priority type is incremental or random.
        - PriorityType (str(same | incremental | random)): It indicates the type of priority to be held by the candidate RPs (CRPs). The options are Same, Incremental, and Random.
        - PriorityValue (number): Value of priority field sent in candidate RP advertisement messages.
        - RouterCount (number): Total number of candidate RPs to be simulated starting from C-RP Address. A contiguous address range is used for this RP range simulation.
        - TriggeredCrpMessageCount (number): The number of times CRP advertisements is sent to the newly elected Bootstrap Router.

        Returns
        -------
        - self: This instance with matching crpRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of crpRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the crpRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
