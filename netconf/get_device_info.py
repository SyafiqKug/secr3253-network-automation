from connection import connect_router
import xml.dom.minidom

filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
    </native>
</filter>
"""

try:
    with connect_router() as m:

        result = m.get_config(
            source="running",
            filter=filter
        )

        hostname = xml.dom.minidom.parseString(
            result.xml
        ).getElementsByTagName("hostname")[0].firstChild.nodeValue

        print("==================================================")
        print("NETCONF DEVICE INFORMATION")
        print("==================================================")
        print("Connection      : SUCCESS")
        print("Device          :", hostname)
        print("Protocol        : NETCONF")
        print("Session ID      :", m.session_id)
        print("Hostname        :", hostname)
        print("==================================================")

except Exception as error:

    print("==================================================")
    print("NETCONF DEVICE INFORMATION")
    print("==================================================")
    print("Connection      : FAILED")
    print("Error           :", error)
    print("==================================================")