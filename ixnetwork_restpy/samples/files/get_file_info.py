"""
Demonstrates use the filter option to get a custom set of files with its details
"""

from ixnetwork_restpy import SessionAssistant

# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    RestPort=11009,
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_ALL,
    ClearConfig=False,
)
ixnetwork = session_assistant.Ixnetwork

# get custom set of files from the server by applying the filter, e.g. here we are querying for only config files
file_list = ixnetwork.parent.GetFileList(filter="*.ixncfg|*.json")
# ensure we got files key in our response
if file_list.get("files") is not None:
    # print the no of diagnostic files received
    print(len(file_list["files"]))
    # loop through each of file to get file information
    for file in file_list["files"]:
        # print some file information
        print(file["name"], file["length"], file["createdUnixTime"])
else:
    raise Exception("Files not present in the server response")
