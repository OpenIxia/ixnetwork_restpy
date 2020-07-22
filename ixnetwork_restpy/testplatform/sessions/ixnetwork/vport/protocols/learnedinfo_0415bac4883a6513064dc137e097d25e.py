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


class LearnedInfo(Base):
    """This object contains the learned information for the LACP port.
    The LearnedInfo class encapsulates a list of learnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInfo'
    _SDM_ATT_MAP = {
        'ActorCollectingFlag': 'actorCollectingFlag',
        'ActorDefaultedFlag': 'actorDefaultedFlag',
        'ActorDistributingFlag': 'actorDistributingFlag',
        'ActorExpiredFlag': 'actorExpiredFlag',
        'ActorLacpActivity': 'actorLacpActivity',
        'ActorLacpTimeout': 'actorLacpTimeout',
        'ActorLinkAggregationStatus': 'actorLinkAggregationStatus',
        'ActorOperationalKey': 'actorOperationalKey',
        'ActorPortNumber': 'actorPortNumber',
        'ActorPortPriority': 'actorPortPriority',
        'ActorSyncFlag': 'actorSyncFlag',
        'ActorSystemId': 'actorSystemId',
        'ActorSystemPriority': 'actorSystemPriority',
        'AdministrativeKey': 'administrativeKey',
        'EnabledAggregation': 'enabledAggregation',
        'OtherLagMemberCount': 'otherLagMemberCount',
        'OtherLagMemberDetails': 'otherLagMemberDetails',
        'PartnerCollectingFlag': 'partnerCollectingFlag',
        'PartnerCollectorMaxDelay': 'partnerCollectorMaxDelay',
        'PartnerDefaultedFlag': 'partnerDefaultedFlag',
        'PartnerDistributingFlag': 'partnerDistributingFlag',
        'PartnerExpiredFlag': 'partnerExpiredFlag',
        'PartnerLacpActivity': 'partnerLacpActivity',
        'PartnerLacpTimeout': 'partnerLacpTimeout',
        'PartnerLinkAggregationStatus': 'partnerLinkAggregationStatus',
        'PartnerOperationalKey': 'partnerOperationalKey',
        'PartnerPortNumber': 'partnerPortNumber',
        'PartnerPortPriority': 'partnerPortPriority',
        'PartnerSyncFlag': 'partnerSyncFlag',
        'PartnerSystemId': 'partnerSystemId',
        'PartnerSystemPriority': 'partnerSystemPriority',
    }

    def __init__(self, parent):
        super(LearnedInfo, self).__init__(parent)

    @property
    def ActorCollectingFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Actor Collecting Flag status, either True of False. If True, the Collecting Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorCollectingFlag'])

    @property
    def ActorDefaultedFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Actor Defaulted Flag status, either True of False. If True, the Defaulted Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorDefaultedFlag'])

    @property
    def ActorDistributingFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Actor Distributing Flag status, either True of False. If True, the Distributing Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorDistributingFlag'])

    @property
    def ActorExpiredFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Actor Expired Flag status, either True of False. If True, the Expired Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorExpiredFlag'])

    @property
    def ActorLacpActivity(self):
        """
        Returns
        -------
        - str(passive | active): (read only) The learned Actor LACP activity mode, either Passive or Active
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorLacpActivity'])

    @property
    def ActorLacpTimeout(self):
        """
        Returns
        -------
        - str(long | short): (read only) The learned Actor LACPDU timeout mode, either Long or Short.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorLacpTimeout'])

    @property
    def ActorLinkAggregationStatus(self):
        """
        Returns
        -------
        - str(individual | aggregatable): (read only) The learned link aggregation status of the actor, either Aggregated or Not Aggregated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorLinkAggregationStatus'])

    @property
    def ActorOperationalKey(self):
        """
        Returns
        -------
        - number: (read only) The learned Actor operation key, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorOperationalKey'])

    @property
    def ActorPortNumber(self):
        """
        Returns
        -------
        - number: (read only) The learned Actor port number in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortNumber'])

    @property
    def ActorPortPriority(self):
        """
        Returns
        -------
        - number: (read only) The learned Actor port priority, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorPortPriority'])

    @property
    def ActorSyncFlag(self):
        """
        Returns
        -------
        - str(inSync | outOfSync): (read only) The learned Actor synchronized status, either OUT_OF_SYNC/IN_SYNC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSyncFlag'])

    @property
    def ActorSystemId(self):
        """
        Returns
        -------
        - str: (read only) The learned Actor system identifier, in 6 byte format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemId'])

    @property
    def ActorSystemPriority(self):
        """
        Returns
        -------
        - number: (read only) The learned Actor system priority, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActorSystemPriority'])

    @property
    def AdministrativeKey(self):
        """
        Returns
        -------
        - number: (read only) This field controls the aggregation of ports of the same system with similar Actor Key.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdministrativeKey'])

    @property
    def EnabledAggregation(self):
        """
        Returns
        -------
        - bool: (read only) The learned Actor aggregation status (whether the port is Individual or Aggregated).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledAggregation'])

    @property
    def OtherLagMemberCount(self):
        """
        Returns
        -------
        - number: (read only) The total number of ports,excluding the individual port that are a part of the LAG
        """
        return self._get_attribute(self._SDM_ATT_MAP['OtherLagMemberCount'])

    @property
    def OtherLagMemberDetails(self):
        """
        Returns
        -------
        - str: (read only) The detailed information of the other member ports of the same LAG, visible in card:port format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OtherLagMemberDetails'])

    @property
    def PartnerCollectingFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Partner Collecting Flag status, either True of False. If True, the Collecting Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerCollectingFlag'])

    @property
    def PartnerCollectorMaxDelay(self):
        """
        Returns
        -------
        - number: (read only) The learned maximum Collection Delay for the partner, in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerCollectorMaxDelay'])

    @property
    def PartnerDefaultedFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Partner Defaulted Flag status, either True of False. If True, the Defaulted Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerDefaultedFlag'])

    @property
    def PartnerDistributingFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Partner Distributing Flag status, either True of False. If True, the Distributing Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerDistributingFlag'])

    @property
    def PartnerExpiredFlag(self):
        """
        Returns
        -------
        - bool: (read only) The learned Partner Expired Flag status, either True of False. If True, the Expired Flag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerExpiredFlag'])

    @property
    def PartnerLacpActivity(self):
        """
        Returns
        -------
        - str(passive | active): (read only) The learned Partner LACP activity mode, either Passive or Active
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerLacpActivity'])

    @property
    def PartnerLacpTimeout(self):
        """
        Returns
        -------
        - str(long | short): (read only) The learned Partner LACPDU timeout mode, either Long or Short.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerLacpTimeout'])

    @property
    def PartnerLinkAggregationStatus(self):
        """
        Returns
        -------
        - str(individual | aggregatable): (read only) The learned link aggregation status of the partner, either Aggregated or Not Aggregated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerLinkAggregationStatus'])

    @property
    def PartnerOperationalKey(self):
        """
        Returns
        -------
        - number: (read only) The learned Partner operation key, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerOperationalKey'])

    @property
    def PartnerPortNumber(self):
        """
        Returns
        -------
        - number: (read only) The learned Partner port number in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerPortNumber'])

    @property
    def PartnerPortPriority(self):
        """
        Returns
        -------
        - number: (read only) The learned Partner port priority, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerPortPriority'])

    @property
    def PartnerSyncFlag(self):
        """
        Returns
        -------
        - str(inSync | outOfSync): (read only) The learned Partner synchronized status, either OUT_OF_SYNC/IN_SYNC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerSyncFlag'])

    @property
    def PartnerSystemId(self):
        """
        Returns
        -------
        - str: (read only) The learned Partner system identifier, in 6 byte format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerSystemId'])

    @property
    def PartnerSystemPriority(self):
        """
        Returns
        -------
        - number: (read only) The learned Partner system priority, in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PartnerSystemPriority'])

    def find(self, ActorCollectingFlag=None, ActorDefaultedFlag=None, ActorDistributingFlag=None, ActorExpiredFlag=None, ActorLacpActivity=None, ActorLacpTimeout=None, ActorLinkAggregationStatus=None, ActorOperationalKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSyncFlag=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, EnabledAggregation=None, OtherLagMemberCount=None, OtherLagMemberDetails=None, PartnerCollectingFlag=None, PartnerCollectorMaxDelay=None, PartnerDefaultedFlag=None, PartnerDistributingFlag=None, PartnerExpiredFlag=None, PartnerLacpActivity=None, PartnerLacpTimeout=None, PartnerLinkAggregationStatus=None, PartnerOperationalKey=None, PartnerPortNumber=None, PartnerPortPriority=None, PartnerSyncFlag=None, PartnerSystemId=None, PartnerSystemPriority=None):
        """Finds and retrieves learnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfo resources from the server.

        Args
        ----
        - ActorCollectingFlag (bool): (read only) The learned Actor Collecting Flag status, either True of False. If True, the Collecting Flag is enabled.
        - ActorDefaultedFlag (bool): (read only) The learned Actor Defaulted Flag status, either True of False. If True, the Defaulted Flag is enabled.
        - ActorDistributingFlag (bool): (read only) The learned Actor Distributing Flag status, either True of False. If True, the Distributing Flag is enabled.
        - ActorExpiredFlag (bool): (read only) The learned Actor Expired Flag status, either True of False. If True, the Expired Flag is enabled.
        - ActorLacpActivity (str(passive | active)): (read only) The learned Actor LACP activity mode, either Passive or Active
        - ActorLacpTimeout (str(long | short)): (read only) The learned Actor LACPDU timeout mode, either Long or Short.
        - ActorLinkAggregationStatus (str(individual | aggregatable)): (read only) The learned link aggregation status of the actor, either Aggregated or Not Aggregated.
        - ActorOperationalKey (number): (read only) The learned Actor operation key, in hexadecimal format.
        - ActorPortNumber (number): (read only) The learned Actor port number in hexadecimal format.
        - ActorPortPriority (number): (read only) The learned Actor port priority, in hexadecimal format.
        - ActorSyncFlag (str(inSync | outOfSync)): (read only) The learned Actor synchronized status, either OUT_OF_SYNC/IN_SYNC.
        - ActorSystemId (str): (read only) The learned Actor system identifier, in 6 byte format.
        - ActorSystemPriority (number): (read only) The learned Actor system priority, in hexadecimal format.
        - AdministrativeKey (number): (read only) This field controls the aggregation of ports of the same system with similar Actor Key.
        - EnabledAggregation (bool): (read only) The learned Actor aggregation status (whether the port is Individual or Aggregated).
        - OtherLagMemberCount (number): (read only) The total number of ports,excluding the individual port that are a part of the LAG
        - OtherLagMemberDetails (str): (read only) The detailed information of the other member ports of the same LAG, visible in card:port format.
        - PartnerCollectingFlag (bool): (read only) The learned Partner Collecting Flag status, either True of False. If True, the Collecting Flag is enabled.
        - PartnerCollectorMaxDelay (number): (read only) The learned maximum Collection Delay for the partner, in microseconds.
        - PartnerDefaultedFlag (bool): (read only) The learned Partner Defaulted Flag status, either True of False. If True, the Defaulted Flag is enabled.
        - PartnerDistributingFlag (bool): (read only) The learned Partner Distributing Flag status, either True of False. If True, the Distributing Flag is enabled.
        - PartnerExpiredFlag (bool): (read only) The learned Partner Expired Flag status, either True of False. If True, the Expired Flag is enabled.
        - PartnerLacpActivity (str(passive | active)): (read only) The learned Partner LACP activity mode, either Passive or Active
        - PartnerLacpTimeout (str(long | short)): (read only) The learned Partner LACPDU timeout mode, either Long or Short.
        - PartnerLinkAggregationStatus (str(individual | aggregatable)): (read only) The learned link aggregation status of the partner, either Aggregated or Not Aggregated.
        - PartnerOperationalKey (number): (read only) The learned Partner operation key, in hexadecimal format.
        - PartnerPortNumber (number): (read only) The learned Partner port number in hexadecimal format.
        - PartnerPortPriority (number): (read only) The learned Partner port priority, in hexadecimal format.
        - PartnerSyncFlag (str(inSync | outOfSync)): (read only) The learned Partner synchronized status, either OUT_OF_SYNC/IN_SYNC.
        - PartnerSystemId (str): (read only) The learned Partner system identifier, in 6 byte format.
        - PartnerSystemPriority (number): (read only) The learned Partner system priority, in hexadecimal format.

        Returns
        -------
        - self: This instance with matching learnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
