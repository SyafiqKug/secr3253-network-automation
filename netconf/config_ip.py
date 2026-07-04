from connection import connect_router

ip_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>1</name>
        <description>Configured by NETCONF</description>
        <ip>
          <address>
            <primary>
              <address>10.10.10.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

try:
    with connect_router() as m:
        reply = m.edit_config(target="running", config=ip_config)

        print("=" * 50)
        print("NETCONF CONFIGURATION REPORT")
        print("=" * 50)
        print("Status          : SUCCESS")
        print("Device          : SSRF")
        print("Configuration   : Loopback1")
        print("IP Address      : 10.10.10.1/24")
        print("Description     : Configured by NETCONF")
        print("Protocol        : NETCONF")
        print("Session ID      :", m.session_id)
        print("=" * 50)

except Exception as error:
    print("=" * 50)
    print("NETCONF CONFIGURATION REPORT")
    print("=" * 50)
    print("Status          : FAILED")
    print("Error           :", error)
    print("=" * 50)