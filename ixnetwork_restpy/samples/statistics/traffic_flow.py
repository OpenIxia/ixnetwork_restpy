"""Demonstrates creating a custom traffic flow statistics view
This sample requires a running ixnetwork instance that has traffic being transmitted.
It uses all possible port filters, traffic item filters and tracking filters when creating the view.
It enables all possible statistics.
The last step prior to getting data should be to enable the view.
"""

from time import sleep
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork


# remove the view if it already exists
caption = 'Custom Traffic Flow View'
view = ixnetwork.Statistics.View.find(Caption=caption)
if len(view) == 1:
    view.remove()

# create the view
view = ixnetwork.Statistics.View.add(Caption=caption, Type='layer23TrafficFlow', Visible=True)

# set filters
traffic_flow_filter = view.Layer23TrafficFlowFilter.find()
traffic_flow_filter.PortFilterIds = view.AvailablePortFilter.find()
traffic_flow_filter.TrafficItemFilterIds = view.AvailableTrafficItemFilter.find()
for tracking_filter in view.AvailableTrackingFilter.find():
    traffic_flow_filter.EnumerationFilter.add(SortDirection='ascending', TrackingFilterId=tracking_filter)

# enable statistics
for statistic in view.Statistic.find():
    statistic.Enabled = True

# enable the view
view.Enabled = True

# wait for data to become available
attempts = 0
while view.Data.IsReady is False and attempts < 10:
    sleep(1)
    attempts += 1

# print the column headers
print(' '.join(view.Data.ColumnCaptions))

# print the ingress and egress rows
for ingress_egress_rows in view.Data.PageValues:
    for row in ingress_egress_rows:
        print(' '.join(row))
