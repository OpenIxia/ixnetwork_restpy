""" Sample that demonstrates how to take a CSV snapshot of a statistics view

The sample operates under the following assumptions:
    - it is for an established IxNetwork GUI session
    - traffic is running
    - there is a Flow Statistics view

"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
import os

testplatform = TestPlatform('127.0.0.1')
sessions = testplatform.Sessions.find(Id=1)

testplatform.info('''
1) setup the csv snapshot parameters
2) ensure the CsvName ends with the .csv extension
    if it does not the IxNetwork server will add the .csv extension to the final csv filename
3) ensure the CsvLocation is a path on the IxNetwork server that the IxNetwork server has access to, 
    the best practice is to use the Ixnetwork.Statistics.CsvFilePath location
''')
statistics = sessions.Ixnetwork.Statistics
csvsnapshot = statistics.CsvSnapshot
csvsnapshot.update(CsvName="Flow Statistics Snapshot.csv",
    CsvLocation=statistics.CsvFilePath,
    SnapshotViewCsvGenerationMode='overwriteCSVFile',
    SnapshotViewContents='allPages',
    Views=statistics.View.find(Caption='Flow Statistics'))

testplatform.info('''
4) take the csv snapshot
''')
csvsnapshot.TakeCsvSnapshot()

testplatform.info('''
5) the csv snapshot file is on the IxNetwork server and can be downloaded
    the csv snapshot file name is the CsvLocation and CsvName
''')
remote_filename = os.path.join(csvsnapshot.CsvLocation, csvsnapshot.CsvName)
local_filename = os.path.join('c:/temp', csvsnapshot.CsvName)
sessions.DownloadFile(remote_filename, local_filename)