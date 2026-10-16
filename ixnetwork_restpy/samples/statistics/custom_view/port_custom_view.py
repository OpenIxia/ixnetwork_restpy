"""
Creates a port custom view
This sample requires a running ixnetwork instance that has ports in up state.
It uses all possible port filters and statistics when creating the view.
The last step prior to getting data should be to enable the view.

Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux

Requirements:
   - Minimum IxNetwork 9.30
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.8)
"""

from time import sleep
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=False,
)
ixnetwork = session_assistant.Ixnetwork


# remove the view if it already exists
caption = "Port Custom View"
view = ixnetwork.Statistics.View.find(Caption=caption)
if len(view) == 1:
    view.remove()

# create the view
view = ixnetwork.Statistics.View.add(
    Caption=caption, Type="layer23ProtocolPort", Visible=True
)

# set layer 2-3 port filters
l23_port_filter = view.Layer23ProtocolPortFilter.find()

# iterate over the PortFilters and enable them
for port_filter in l23_port_filter.PortFilters.find():
    # set the port filter to True to enable it
    port_filter.Enabled = True

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
print(" ".join(view.Data.ColumnCaptions))

# print the snapshot data
for data in view.Data.PageValues:
    for row in data:
        print(" ".join(row))
