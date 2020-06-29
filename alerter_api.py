import requests
import json
from requests.exceptions import HTTPError

def alerter(status):
    cpu_flag, mem_flag, disk_flag = False, False, False
    if (status['cpu_utilization']>=85): cpu_flag = True
    if (status['memory_utilization']>=75): mem_flag = True
    if (status['disk_utilization']>=60): disk_flag = True
    if not (cpu_flag or mem_flag or disk_flag):
        print("No alerts: "+"Server ID: "+status['server_id'])
        return
    alert = ""
    if(cpu_flag): alert += "CPU_Utilization,"
    if(mem_flag): alert += " Memory_Utilization,"
    if(disk_flag): alert += " Disk_Utilization"
    print("ALERT: "+"Server ID:"+status['server_id']+" ||" +alert+" Rules Violated")
    return

try:
    #I hosted a django projected and used its api to call objects from database
    #this link has to be replaced with a server link that sends the status details of servers as JSON
    response = requests.get('http://localhost:8000/server/')
    response.raise_for_status()
    
    statuses = json.loads(response.text)
    for status in statuses:
        alerter(status)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
