import sys
import argparse

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

if __name__ == "__main__":
    print(len(sys.argv))
    print(str(sys.argv))
    status = {}
    status['server_id'] = sys.argv[1]
    status['cpu_utilization'] = float(sys.argv[2])
    status['memory_utilization'] = float(sys.argv[3])
    status['disk_utilization'] = float(sys.argv[4])
    alerter(status)

# e.g: python3 alerter_cmd_line.py server_id_7089 55.5 89.6 45.3

