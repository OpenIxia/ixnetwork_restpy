"""Mocks all request/responses needed for unit tests
"""
import re

class Mocks(object):
    PLATFORMS =  {
        'windows': 'SelfHost',
        'linux': 'Jetty',
        'connection_manager': 'Microsoft-HTTPAPI/2.0'
    }
    _PLATFORM = 'windows'

    REQUEST_RESPONSE = {
        'api/v1/redirect': {
            'GET': {
                'data': [
                    {
                        'href': 'api/v1/sessions/1',
                        'id': '1',
                        'userId': 'admin',
                        'userName': 'admin',
                        'applicationType': 'ixnetwork',
                        'state': 'ACTIVE'
                    }
                ],
                'status_code': 307
            }
        },
        'api/v1/sessions': {
            'GET': {
                'data': [
                    {
                        'href': 'api/v1/sessions/1',
                        'id': '1',
                        'userId': 'admin',
                        'userName': 'admin',
                        'applicationType': 'ixnetwork',
                        'state': 'ACTIVE'
                    }
                ],
                'status_code': 200
            }
        },
        'api/v1/auth/session' : {
            'GET': {
                'data': {
                    'apiKey': '0000000000000000',
                    'trace': 'request_response',
                    'userName': 'admin'
                },
                'status_code': 200
            },
            'POST': {
                'data': {
                    'apiKey': '0000000000000000',
                    'trace': 'request_response',
                    'userName': 'admin'
                },
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork': {
            'GET': {
                'data': {
                    'href': 'api/v1/sessions/1/ixnetwork'
                },
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/operations/select': {
            'POST': {
                'data': [
                    {
                        "href": "/api/v1/sessions/1/ixnetwork",
                        "vport": [
                            {
                                "href": "/api/v1/sessions/1/ixnetwork/vport/1",
                                "id": 1,
                                "name": "Ethernet - 001",
                            },
                            {
                                "href": "/api/v1/sessions/1/ixnetwork/vport/2",
                                "id": 2,
                                "name": "Ethernet - 002",
                            }
                        ],
                        "statistics": [
                            {
                                "href": "/api/v1/sessions/1/ixnetwork/statistics",
                                "pollInterval": "2",
                            }
                        ]
                    },
                    {
                        "href": "/api/v1/sessions/1/ixnetwork/statistics",
                        "view": [
                            {
                                "href":"/api/v1/sessions/1/ixnetwork/statistics/view/1",
                                "id":1,
                                "caption":"Port Statistics"
                            },
                            {
                                "href":"/api/v1/sessions/1/ixnetwork/statistics/view/2",
                                "id":2,
                                "caption":"Tx-Rx Frame Rate Statistics"
                            },
                            {
                                "href":"/api/v1/sessions/1/ixnetwork/statistics/view/3",
                                "id":3,
                                "caption":"PCS Lane Statistics"
                            }    
                        ]
                    },
                    {
                        "executionTimeMs":4.0,
                        "id":"",
                        "state":"SUCCESS",
                        "progress":100,
                        "message":"null",
                        "url":"",
                        "resultUrl":"",
                        "result":[
                            {
                                "href":"/api/v1/sessions/1/ixnetwork/statistics/view/1",
                                "id":1,
                                "data":{
                                    "href":"/api/v1/sessions/1/ixnetwork/statistics/view/1/data",
                                    "allowPaging":False,
                                    "pageValues":[
                                        [
                                            [
                                                "10.39.35.12/Card02/Port01",
                                                "Port1",
                                                "Full",
                                                "1000 Mbps",
                                                "Link Up",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0"
                                            ]
                                        ],
                                        [
                                            [
                                                "10.39.35.12/Card02/Port02",
                                                "Port2",
                                                "Full",
                                                "1000 Mbps",
                                                "Link Up",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0"
                                            ]
                                        ]
                                    ],
                                    "columnCaptions":[
                                        "Stat Name",
                                        "Port Name",
                                        "Duplex Mode",
                                        "Line Speed",
                                        "Link State",
                                        "Frames Tx.",
                                        "Valid Frames Rx.",
                                        "Frames Tx. Rate",
                                        "Valid Frames Rx. Rate",
                                        "Data Integrity Frames Rx.",
                                        "Data Integrity Errors",
                                        "Bytes Tx.",
                                        "Bytes Rx.",
                                        "Bits Sent",
                                        "Bits Received",
                                        "Bytes Tx. Rate",
                                        "Tx. Rate (bps)",
                                        "Tx. Rate (Kbps)",
                                        "Tx. Rate (Mbps)",
                                        "Bytes Rx. Rate",
                                        "Rx. Rate (bps)",
                                        "Rx. Rate (Kbps)",
                                        "Rx. Rate (Mbps)",
                                        "Scheduled Frames Tx.",
                                        "Scheduled Frames Tx. Rate",
                                        "Collisions",
                                        "Control Frames Tx",
                                        "Control Frames Rx",
                                        "Ethernet OAM Information PDUs Sent",
                                        "Ethernet OAM Information PDUs Received",
                                        "Ethernet OAM Event Notification PDUs Received",
                                        "Ethernet OAM Loopback Control PDUs Received",
                                        "Ethernet OAM Organisation PDUs Received",
                                        "Ethernet OAM Variable Request PDUs Received",
                                        "Ethernet OAM Variable Response Received",
                                        "Ethernet OAM Unsupported PDUs Received",
                                        "Rx Pause Priority Group 0 Frames",
                                        "Rx Pause Priority Group 1 Frames",
                                        "Rx Pause Priority Group 2 Frames",
                                        "Rx Pause Priority Group 3 Frames",
                                        "Rx Pause Priority Group 4 Frames",
                                        "Rx Pause Priority Group 5 Frames",
                                        "Rx Pause Priority Group 6 Frames",
                                        "Rx Pause Priority Group 7 Frames",
                                        "Misdirected Packet Count",
                                        "CRC Errors"
                                        ],
                                    "pageSize":0,
                                    "egressMode":"conditional",
                                    "rowValues":
                                    {
                                        "arg1":[
                                            [
                                                "10.39.35.12/Card02/Port01",
                                                "Port1",
                                                "Full",
                                                "1000 Mbps",
                                                "Link Up",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0"
                                            ]
                                        ],
                                        "arg2":[
                                            [
                                                "10.39.35.12/Card02/Port02",
                                                "Port2",
                                                "Full",
                                                "1000 Mbps",
                                                "Link Up",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0",
                                                "0"
                                            ]
                                        ]
                                    },
                                    "egressPageSize":8,
                                    "isReady":True,
                                    "columnCount":46,
                                    "totalPages":1,
                                    "totalRows":0,
                                    "currentPage":1,
                                    "timestamp":256994000,
                                    "isBlocked":False,
                                    "rowCount":2
                                }
                            }
                        ]
                    }
              
            ],
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/globals': {
            'GET': {
                'data': {
                    'href': 'api/v1/sessions/1/ixnetwork/globals',
                    'buildNumber': '9.00.0.1314',
                    'username': 'tests/mocks/username-sessionid-processid'
                },
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/topology': {
            'GET': {
                'data': [
                    {
                        'href': 'api/v1/sessions/1/ixnetwork/topology/1',
                        'name': 'Topology 1',
                    }
                ],
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/topology/1/deviceGroup': {
            'GET': {
                'data': [
                    {
                        'href': 'api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1',
                        'name': 'DeviceGroup 1',
                    }
                ],
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/multivalue/1/nest': {
            'GET': {
                'data': [
                    {
                        'href': 'api/v1/sessions/1/multivalue/1/nest/1',
                        'enabled': 'false',
                        'owner': 'api/v1/sessions/1/topology/1/deviceGroup/1/ethernet/1/ipv4/1',
                        'step': '0.0.1.0',
                        'description': 'Port Step'
                    },
                    {
                        'href': 'api/v1/sessions/1/multivalue/1/nest/2',
                        'enabled': 'false',
                        'owner': 'api/v1/sessions/1/topology/1/deviceGroup/1/ethernet/1/ipv4/1/bgpIpv4Peer/1',
                        'step': '0.0.1.0',
                        'description': 'PE Router Step'
                    }
                ],
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/vport': {
            'POST' : {
                'data' : {
                            'links':
                            [
                                {
                                'rel':'self',
                                'method':'GET',
                                'href':'/api/v1/sessions/1/ixnetwork/vport/1'
                                }
                            ]
                },
                'status_code': 201
            }
        },
        'api/v1/sessions/1/ixnetwork/vport/1' : {
            'GET' : {
                'data' : {
                        'href':'/api/v1/sessions/1/ixnetwork/vport/1',
                        'id':'1',
                        'useGlobalSettings':'false',
                        'isMapped':'false',
                        'connectedTo':'null',
                        'internalId':'1',
                        'name':'Ethernet - 001'
                },
                'status_code': 200
            }
        },
        'api/v1/sessions/1/ixnetwork/operations/assignports' : {
            'POST' : {
                'data' : {
                        "executionTimeMs":5000.0,
                        "id":"1",
                        "state":"SUCCESS",
                        "progress":100,
                        "message":'null',
                        "url":"/api/v1/sessions/1/ixnetwork/operations/assignports/1",
                        "resultUrl":"",
                        "result":['/api/v1/sessions/1/ixnetwork/vport/1','/api/v1/sessions/1/ixnetwork/vport/2']
                },
                'status_code' : 202
            }
        },
        'api/v1/sessions/1/ixnetwork/files' : {
            'GET' : {
                'data' : {
                    "absolute":"C:/Users/dandelwa/AppData/Local/Ixia/sdmStreamManager/common",
                    "files":
                    [
                        {
                            "name":"ixnetwork.restpy.Port-Statistics.csv",
                            "length":1400,
                            "modifiedUnixTime":1573053161,
                            "createdUnixTime":1573052497
                        },
                        {
                            "name":"ixnetwork.restpy.Port-Statistics.csv.columns",
                            "length":1697,
                            "modifiedUnixTime":1573053161,
                            "createdUnixTime":1573052498
                        },
                        {
                            "name":"two_vports.json",
                            "length":211399,
                            "modifiedUnixTime":1569511205,
                            "createdUnixTime":1569511204
                        }
                    ],
                    "directories":[]
                },
                'status_code' : 200
            }
        }
    }

    @staticmethod
    def set_platform(platform = 'windows'):
        """
        Args:
            platform (windows | linux | connection_manager)
        """
        Mocks._PLATFORM = platform

    @staticmethod
    def mocked_request(**kwargs):
        class MockResponse:
            def __init__(self, response):
                self.json_data = response['data']
                self.status_code = response['status_code']
                self.headers = {
                    'server': Mocks.PLATFORMS[Mocks._PLATFORM]
                }
                if self.json_data is not None:
                    self.headers['Content-Type'] = 'application/json'

            def json(self):
                return self.json_data

        class MockResponseError:
            def __init__(self, url, exception):
                self.status_code = 404
                self.url = url
                self.reason = 'Not Found'
                self.text = exception.message

        try:
            start = kwargs['url'].find('api/v1')
            method = kwargs['method']
            if method == 'PATCH':
                return MockResponse({"data": None, "status_code": 204})
            else:
                request = kwargs['url'][start:]
                mockInstance = Mocks()               
                request_response = mockInstance.REQUEST_RESPONSE[request]
                return MockResponse(request_response[method])
        except Exception as e:
            print(e)
            return MockResponseError(request, e)

    def __init__(self):
        pass