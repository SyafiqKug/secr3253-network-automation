from connection import connect_router

user_config = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username>
            <name>adminnetconf</name>
            <privilege>15</privilege>
            <secret>
                <encryption>0</encryption>
                <secret>cisco123</secret>
            </secret>
        </username>
    </native>
</config>
"""

try:
    with connect_router() as m:

        m.edit_config(
            target="running",
            config=user_config
        )

        print("==================================================")
        print("NETCONF CONFIGURATION REPORT")
        print("==================================================")
        print("Status          : SUCCESS")
        print("Device          : SSRF")
        print("Configuration   : Local User")
        print("Username        : adminnetconf")
        print("Privilege       : 15")
        print("Protocol        : NETCONF")
        print("Session ID      :", m.session_id)
        print("==================================================")

except Exception as error:

    print("==================================================")
    print("NETCONF CONFIGURATION REPORT")
    print("==================================================")
    print("Status          : FAILED")
    print("Configuration   : Local User")
    print("Error           :", error)
    print("==================================================")