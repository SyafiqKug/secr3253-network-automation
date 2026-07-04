from connection import connect_router

try:
    with connect_router() as m:
        print("Connected Successfully")
        print("NETCONF Session ID:", m.session_id)

except Exception as error:
    print("Connection Failed")
    print(error)