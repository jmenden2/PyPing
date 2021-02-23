import platform
import requests
import subprocess
import time

while(1):

    # Get current OS to determine parameters to use in ping call
    current_os = platform.system().lower()
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"

    # setup ip and ping that ip
    ip = "{Device IP}"
    # calls 'ping {-n/-c} 1 {ip}'
    command = ['ping', parameter, '1', ip]
    response = subprocess.call(command)

    # expected response is 0 if working
    # if non-zero restart device by powering off, powering on
    if(response != 0):
        # turn off Lux
        requests.post("https://maker.ifttt.com/trigger/{event_name}/with/key/{key}")

        # wait 5 seconds in order to let hard reboot
        time.sleep(5)

        # turn on Lux
        requests.post("https://maker.ifttt.com/trigger/{event_name}/with/key/{key}")

    # sleep for 4 hours and run again
    time.sleep(14400)