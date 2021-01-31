""" Assistant class to simplify the task of virtual ports to test ports connections
"""
import time
import json
from ixnetwork_restpy.select import Select
from ixnetwork_restpy.assistants.statistics.statviewassistant import StatViewAssistant


try:
    basestring
except NameError:
    basestring = str


class PortMapAssistant(object):
    def __init__(self, IxNetwork):
        """Create mappings between test port locations and virtual ports.

        Args
        ----
        - IxNetwork (obj (ixnetwork_restpy.testplatform.sessions.ixnetwork.Ixnetwork)): An Ixnetwork object
        """
        self._map = {}
        self._IxNetwork = IxNetwork
        self._location_supported = True
        try:
            self._IxNetwork._connection._options(self._IxNetwork.href + '/locations')
        except:
            self._location_supported = False

    def Map(self, IpAddress='127.0.0.1', CardId=1, PortId=1, Name=None, Port=None, Location=None):
        """Map a test port to a virtual port
        
        Examples
        --------
            Map(IpAddress='10.36.74.26', CardId=2, PortId=13, Name='Tx')
            Map(Name='Tx', Port=('10.36.74.26', 2, 13))
            Map('10.36.74.26', 2, 13, Name='Tx')
            Map('10.36.74.26', 2, 14, Name=vport.Name)
            Map(Location='10.36.74.26;1;1', Name='Tx')
            Map(Location='localuhd/1', Name='Tx')

        Args
        ----
        - IpAddress (str): The ip address of the platform that hosts the card/port combination.
            If the IpAddress is not specified the default value is 127.0.0.1
        - CardId (number): The id of the card that hosts the port
            If the CardId is not specified the default value is 1
        - PortId (number): The id of the port.
        - Name (str): The name of a virtual port. 
            If the Name is not specified a default named virtual port will be created.
            If the Name is specified an attempt to find it will be made. 
            If it does not exist a virtual port with that name will be created.
            The found or created vport will then be mapped.
        - Port (tuple(IpAddress,CardId,PortId)): A test port location tuple consisting of an IpAddress, CardId, PortId.
            Use this parameter instead of specifying the individual IpAddress, CardId, PortId parameters.
            If this parameter is not None it will override any IpAddress, CardId, PortId parameter values.
        - Location (str): A test port location using the new 9.10 location syntax
            The location syntax for test ports can be discovered by using the /locations API
            If this parameter is not None it will override any IpAddress, CardId, PortId, Port parameter values

        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): A Vport object

        Raises
        ------
        - ValueError: a PortId was not provided
        - RuntimeError: Location API is not supported on the server
        - ServerError: an unexpected error occurred on the server
        """	
        if Port is not None:
            (IpAddress, CardId, PortId) = Port
        if PortId is None:
            raise ValueError('A PortId must be provided')
        if Name is not None:
            vport = self._IxNetwork.Vport.find(Name='^%s$' % Name)
        if Name is None or len(vport) == 0:
            vport = self._IxNetwork.Vport.add(Name=Name)
        self._map[vport.Name] = {
            'location': Location if Location is not None else '%s;%s;%s' % (IpAddress, CardId, PortId),
            'vport': vport
        }  
        return vport

    def Clear(self, Disconnect=False):
        """Clears the map of virtual ports to test port locations

        Args
        ----
        - Disconnect (bool): disconnect virtual ports from test ports
        """
        if Disconnect is True:
            self.Disconnect()
        self._map = {}
        return self

    def Connect(self, ForceOwnership=True, HostReadyTimeout=60, LinkUpTimeout=300, IgnoreLinkUp=False):
        """Connect virtual ports to test ports

        Args
        ----
        - ForceOwnership (bool): Forcefully clear ownership of the test ports
        - HostReadyTimeout (bool): The number of seconds to wait for all 
            test port hosts to achieve a state of 'ready'
        - LinkUpTimeout (int): The number of seconds to wait for all 
            virtual port links to achieve a state of 'Link Up'

        Raises
        ------
        - obj(ixnetwork_restpy.errors.NotFoundError): the HostReadyTimeout or LinkUpTimeout value has been exceeded 
        - obj(ixnetwork_restpy.errors.ServerError): an unexpected error occurred on the server
        """
        start = time.time()
        self._add_hosts(HostReadyTimeout)
        self._IxNetwork.info('PortMapAssistant._add_hosts duration: %ssecs' % (time.time() - start))
        start = time.time()
        self._connect_ports(ForceOwnership)
        self._IxNetwork.info('PortMapAssistant._connect_ports duration: %ssecs' % (time.time() - start))
        if IgnoreLinkUp is False:
            start = time.time()
            self._check_link_state(LinkUpTimeout)
            self._IxNetwork.info('PortMapAssistant._check_link_state duration: %ssecs' % (time.time() - start))
        else:
            self._IxNetwork.warn('Bypassing link state check')
        return self

    def _add_hosts(self, HostReadyTimeout):
        ip_addresses = []
        for map in self._map.values():
            if ';' in map['location']:
                chassis_address = map['location'].split(';')[0]
                ip_addresses.append(chassis_address)
        ip_addresses = set(ip_addresses)
        if len(ip_addresses) > 0:
            self._IxNetwork.info('Adding test port hosts [%s]...' % ', '.join(ip_addresses))
            url = self._IxNetwork.href + '/availableHardware/chassis'
            for ip_address in ip_addresses:
                payload = {'hostname': ip_address}
                self._IxNetwork._connection._create(url, payload)
            start_time = time.time()
            while True:
                select = self._select_chassis('^(%s)$' % '|'.join(ip_addresses))
                not_ready = []
                for chassis in select['chassis']:
                    if chassis['state'] != 'ready':
                        not_ready.append(chassis['hostname'])
                if len(not_ready) == 0:
                    break
                if time.time() - start_time > HostReadyTimeout:
                    raise RuntimeError('After %s seconds, test port hosts [%s] are not in a ready state' % (HostReadyTimeout, ', '.join(not_ready)))
                time.sleep(3)

    def _get_name_regex(self):
        names = []
        for name in self._map:
            names.append(name)
        regex = '^(%s)$' % ('|'.join(names))
        return regex

    def _select_chassis(self, filter):
        children = [
            {
                'child': 'chassis',
                'properties': ['state', 'hostname'],
                'filters': [{'property': 'hostname', 'regex': filter}]
            }
        ]
        select = Select(self._IxNetwork._connection, 
            self._IxNetwork.href + '/availableHardware', 
            children=children)
        return select.go()[0]

    def _select_vports(self):
        children = [
            {
                'child': '^vport$',
                'properties': ['name', 'connectionState'],
                'filters': [
                    {
                        'property': 'name', 
                        'regex': self._get_name_regex()
                    }
                ]
            },
            {
                'child': '^(availableHardware|chassis|card|port)$',
                'properties': [],
                'filters': []
            }
        ]
        select = Select(self._IxNetwork._connection, self._IxNetwork.href, 
            children=children)
        return select.go()[0]

    def _find_xpath(self, nested_dict, card_port):
        for k, v in nested_dict.items():
            if isinstance(v, list):
                for d in v:
                    xpath = self._find_xpath(d, card_port) 
                    if xpath is not None:
                        return xpath
            elif isinstance(v, dict):
                xpath = self._find_xpath(v, card_port)
                if xpath is not None:
                    return xpath
            elif isinstance(v, basestring) and card_port in v: 
                return nested_dict['xpath']
        return None

    def _connect_ports(self, ForceOwnership):
        method = 'location' if self._location_supported else 'connectedTo' 
        self._IxNetwork.info('Connecting virtual ports to test ports using %s' % method)
        payload = []
        select = self._select_vports()
        for vport in select['vport']:
            location = self._map[vport['name']]['location']
            if self._location_supported is True:
                vport['location'] = location
                payload.append({'xpath': vport['xpath'], 'location': location})
            else:
                (hostname, cardid, portid) = location.split(';')
                card_port = "/card/%s/port/%s" % (cardid, portid)
                xpath = self._find_xpath(select['availableHardware'], card_port)
                payload.append({'xpath': vport['xpath'], 'connectedTo': xpath})
        self._IxNetwork.ResourceManager.ImportConfig(json.dumps(payload), False)
        if ForceOwnership is True:
            self._IxNetwork.Vport.find(Name=self._get_name_regex()).ConnectPorts(ForceOwnership)
    
    def _check_link_state(self, LinkUpTimeout):
        self._IxNetwork.info('Checking virtual port link states')
        view = StatViewAssistant(self._IxNetwork, 'Port Statistics', Timeout=LinkUpTimeout)
        view.AddRowFilter('Port Name', StatViewAssistant.REGEX, self._get_name_regex())
        view.CheckCondition('Link State', StatViewAssistant.REGEX, '^Link Up$', Timeout=LinkUpTimeout)

    def Disconnect(self):
        """Disconnect all mapped virtual ports from test port locations
        """
        self._IxNetwork.info('Disconnecting virtual ports from test ports')
        self._IxNetwork.Vport.find(Name=self._get_name_regex()).UnassignPorts(False)
        return self

    def __str__(self):
        map_str = ''
        template = 'Vport[%s] -> TestPort[%s] -> Vport.ConnectionState[%s]\n'
        for vport in self._select_vports()['vport']:
            name = vport['name']
            map_str += template % (name, self._map[name]['location'], vport['connectionState'])
        return map_str.rstrip()
