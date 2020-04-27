"""Demonstrates ixnetwork_restpy container object functionality.

The sample below shows how to retrieve all instances of a node from the server into a single container object
Each instance can be accessed using the container object's iterator or index functionality
The container implements the following special method names to allow for iteration and indexing:
    __len__, __getitem__, __iter__, __next__

The benefit of a container object is that a single method call can act on many instances without having to pass arrays of references.
For example if a container encapsulates 10 instances, the <container>.remove() method will delete all the encapsulated 
instances without having to add looping code

For more information on containers read the following:  
  https://docs.python.org/2.7/reference/datamodel.html#emulating-container-types
  https://docs.python.org/2.7/library/stdtypes.html#typeiter

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create x number of vports
vport_count = 3
for i in range(vport_count):
    ixnetwork.Vport.add()

# get a container object with all instances
vports = ixnetwork.Vport.find()
assert(len(vports) == 3)

# print the number of insances encapsulated in the container
print('%s instances' % len(vports))

# print all instances in the container
print(vports)

# print the first instance
print(vports[0].href)

# print the last instance
print(vports[-1].href)

# convert the container object into a list
vport_list = list(vports)
print(len(vport_list))

# remove all encapsulated instances in a single method call
vports.remove()


