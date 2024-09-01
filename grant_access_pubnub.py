from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.enums import PNStatusCategory

pnconfig = PNConfiguration()
pnconfig.publish_key = 'put key here'
pnconfig.subscribe_key = 'put key here'
pnconfig.secret_key = "put key here"  # Required to grant permissions
pnconfig.uuid = 'put uuid here'  # Add this line
pubnub = PubNub(pnconfig)


def grant_callback(result, status):
    if status.is_error():
        print(f"Error granting permissions: {status}")
    else:
        print(f"Permissions granted successfully: {result}")

# Granting Read and Write permissions to the channel
pubnub.grant()\
    .channels("put your channel here")\
    .read(True)\
    .write(True)\
    .manage(True)\
    .ttl(1440)\
    .pn_async(grant_callback)

