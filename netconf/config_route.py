from connection import connect_router

route_config = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
            <route>
                <ip-route-interface-forwarding-list>
                    <prefix>172.16.10.0</prefix>
                    <mask>255.255.255.0</mask>
                    <fwd-list>
                        <fwd>192.168.56.1</fwd>
                    </fwd-list>
                </ip-route-interface-forwarding-list>
            </route>
        </ip>
    </native>
</config>
"""

try:
    with connect_router() as m:

        m.edit_config(target="running", config=route_config)

        print("==================================================")
        print("NETCONF CONFIGURATION REPORT")
        print("==================================================")
        print("Status          : SUCCESS")
        print("Device          : SSRF")
        print("Configuration   : Static Route")
        print("Destination     : 172.16.10.0/24")
        print("Next Hop        : 192.168.56.1")
        print("Protocol        : NETCONF")
        print("Session ID      :", m.session_id)
        print("==================================================")

except Exception as error:

    print("==================================================")
    print("NETCONF CONFIGURATION REPORT")
    print("==================================================")
    print("Status          : FAILED")
    print("Device          : SSRF")
    print("Configuration   : Static Route")
    print("Protocol        : NETCONF")
    print("Error           :", error)
    print("==================================================")