from connection import connect_router

hostname_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>SSRF</hostname>
  </native>
</config>
"""

try:
    with connect_router() as m:

        print("=" * 50)
        print("Connecting to Router...")
        print("=" * 50)

        reply = m.edit_config(
            target="running",
            config=hostname_config
        )

        print("\nNETCONF Reply:")
        print(reply.xml)

        print("\nConfiguration completed successfully.")

except Exception as error:
    print("\nConfiguration Failed!")
    print(error)