""" Sample that demonstrates how to take a CSV snapshot of a statistics view

The sample operates under the following assumptions:
    - it is for an established IxNetwork GUI session
    - traffic is running
    - there is a Flow Statistics view

"""
from ixnetwork_restpy import SessionAssistant
import os

session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO)
ixnetwork = session_assistant.Ixnetwork
session = session_assistant.Session

ixnetwork.info('''
1) setup the csv snapshot parameters
2) ensure the CsvName DOES NOT end with a .csv extension
	the IxNetwork server will add a .csv extension to the final csv filename
3) ensure the CsvLocation is a path on the IxNetwork server that the IxNetwork server has access to, 
	the best practice is to use the Ixnetwork.Statistics.CsvFilePath location
''')
statistics = ixnetwork.Statistics
csvsnapshot = statistics.CsvSnapshot
csvsnapshot.update(CsvName="StatisticsSnapshot",
	CsvLocation=statistics.CsvFilePath,
    SnapshotViewCsvGenerationMode='overwriteCSVFile',
    SnapshotViewContents='allPages',
    Views=statistics.View.find(Caption='Port Statistics'))

ixnetwork.info(csvsnapshot)

ixnetwork.info('''
4) take the csv snapshot
''')
csvsnapshot.TakeCsvSnapshot()

ixnetwork.info('''
5) the csv snapshot file is on the IxNetwork server and can be downloaded
	The csv snapshot file name is the CsvLocation and CsvName and .csv extension
    The snapshot API will always add a .csv extension
''')
file_name = csvsnapshot.CsvName + '.csv'
remote_filename = os.path.normpath(os.path.join(csvsnapshot.CsvLocation, file_name))
local_filename = os.path.normpath(os.path.join('c:/temp', file_name))
session.DownloadFile(remote_filename, local_filename)

with open(local_filename, 'r') as fid:
    print(fid.read())

