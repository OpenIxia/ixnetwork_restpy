import time
from ixnetwork_restpy import SessionAssistant


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

# setup test ports and virtual ports
chassis_ip = "10.39.51.187"
test_ports = [
    dict(Arg1=chassis_ip, Arg2=1, Arg3=9),
    dict(Arg1=chassis_ip, Arg2=1, Arg3=10),
]
virtual_ports = ixnetwork.Vport.add().add()

# here we are assigning ports asynchronously using async_operation attribute
ixnetwork.info("Assigning ports asynchronously")
ixnetwork.AssignPorts(test_ports, [], virtual_ports, True, async_operation=True)

# now while the config is loading asynchronously we can do some other operations
# generally we can do some DUT operations but here we are just doing some operation as an example
ixnetwork.info("Doing some other operations")
for i in range(20):
    print("operation " + str(i + 1))
    time.sleep(2)

# finally we get the async response after doing some other operations
ixnetwork.info("Fetching the response of the asynchronous operation")
assigned_ports = ixnetwork.get_async_response()
print("connected ports = " + str(assigned_ports))

ixnetwork.info("End")
