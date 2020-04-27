"""Demonstrates how to use the StatViewAssist class

This sample requires an already loaded configuration with at least 2 connected vports.

"""
from ixnetwork_restpy import SessionAssistant, StatViewAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=False)
ixnetwork = session_assistant.Ixnetwork

ixnetwork.info('negative test')
try:
    session_assistant.StatViewAssistant('my test view', Timeout=5)
except Exception as e:
    ixnetwork.info(e)

# get a list of all current statistic views that can be used in the StatViewAssistant
print(StatViewAssistant.GetViewNames(ixnetwork))

# create a stat view assistant for a statistics view
port_statistics = session_assistant.StatViewAssistant('Port Statistics')

# print all the rows for a statistics view
print(port_statistics)

# add a filter so that only a single row is retrieved
port_statistics.AddRowFilter('Port Name', StatViewAssistant.REGEX, 'Port 1$')
print(port_statistics)

# demonstrate cell access
port_statistics.ClearRowFilters()
rows = port_statistics.Rows

# get the cell value at row 0, column 'Port Name'
print(rows[0]['Port Name'])

# get the cell value at row 1, column 'Stat Name'
print(rows[1]['Stat Name'])

# get the cell value at the first row that matches a regex of 'case insensitive endswith port 1', column 'Frames Tx.'
print(rows['(?i)port 1$']['Frames Tx.'])

ixnetwork.info('check that all ipv4 protocols are up')
protocols_summary = session_assistant.StatViewAssistant('Protocols Summary')
protocols_summary.AddRowFilter('Protocol Type', StatViewAssistant.REGEX, '(?i)^ipv4?')
protocols_summary.CheckCondition('Sessions Not Started', StatViewAssistant.EQUAL, 0)
protocols_summary.CheckCondition('Sessions Down', StatViewAssistant.EQUAL, 0)

ixnetwork.info('traffic stat check')
traffic_statistics = session_assistant.StatViewAssistant('Traffic Item Statistics')
tx_frames = traffic_statistics.Rows[0]['Tx Frames']
ixnetwork.info('tx frames: %s' % tx_frames)

ixnetwork.info('drilldown sample')
ixnetwork.info(traffic_statistics.DrillDownOptions())
ixnetwork.info(traffic_statistics.TargetRowFilters())
drilldown = traffic_statistics.Drilldown(0, traffic_statistics.DrillDownOptions()[0], traffic_statistics.TargetRowFilters()[0])
print(drilldown)
