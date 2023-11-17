"""
Demonstrates how to use the StatViewAssist class to get stats based on a particular filter type.
FilterType can be used to define the high level scope on which view we want the filter.
FilterView property of StatViewAssist can then be used to add more customised filter options according to need.
Finally, calling GetFilteredStats method returns us an instance of StatViewAssist with statics for the filtered view populated.
"""

from ixnetwork_restpy import SessionAssistant, StatViewAssistant

# connecting to an existing session where traffic is running
s = SessionAssistant(IpAddress="127.0.0.1", RestPort=11009, ClearConfig=False)
ixn = s.Ixnetwork

# providing the name of the new filter_view and the type of filter we need to impose on that view
sv = StatViewAssistant(ixn, "filter_flow", FilterType="layer23TrafficFlow")

# customise filter options according to need
flowFilterObj = sv.FilterView.Layer23TrafficFlowFilter.find()
flowFilterObj.AggregatedAcrossPorts = True


availablePortFilter = sv.FilterView.AvailablePortFilter.find()
availableTrafficItemFilter = sv.FilterView.AvailableTrafficItemFilter.find()

# set the port and traffic filters
flowFilterObj.PortFilterIds = availablePortFilter
flowFilterObj.TrafficItemFilterIds = availableTrafficItemFilter

for filter in flowFilterObj.EnumerationFilters.find():
    filter.Enabled = True
    filter.SortDirection = "ascending"

# GetFilteredStats returns a new instance of statViewAssistant with statics for the filtered view populated
print(sv.GetFilteredStats())
