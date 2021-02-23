# PyPing
A simple Python script that pings a network device to check its network status. If off, the script will call an IFTTT hook to turn off, then turn on a smart plug to reconnect the device to the internet.

The inspiration for this simple script came from my smart thermostat perodically disconnecting from my network, no longer rendering the device 'smart'. The only way to fix the network disconnect was by unplugging it and plugging it back in. This script is running constantly on a Raspberry Pi Zero W and it checks network status every 4 hours. The script utilizes python web requests to call two IFTTT WebHooks services, one for turning off and one for turning on the smart plug that the smart thermostat is connected to.
