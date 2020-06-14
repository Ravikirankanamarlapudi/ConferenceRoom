# All candidates must submit answer to this programming question before being reviewed by the hiring team. 
# Programming Test Conference room scheduling. Find the nearest open conference room for a team 
# in which a team can hold its meeting. Given n team members with the floor on which they work and the time 
# they want to meet, and a list of conference rooms identified by their floor and room number as a decimal 
# number, maximum number of people it fits and pairs of times they are open - find the best place for the 
# team to have their meeting. If there is more than one room available that fits the team at the chosen time 
# then the best place is on the floor the closest to where the team works. E.g. rooms.txt 
# 7.11,8,9:00,9:15,14:30,15:00 
# 8.23,6,10:00,11:00,14:00,15:00 
# 8.43,7,11:30,12:30,17:00,17:30 
# 9.511,9,9:30,10:30,12:00,12:15,15:15,16:15 
# 9.527,4,9:00,11:00,14:00,16:00 
# 9.547,8,10:30,11:30,13:30,15:30,16:30,17:30 
# Input: 5,8,10:30,11:30 # 5 team members, located on the 8th floor, meeting time 10:30 - 11:30 
# Output: 9.547

from datetime import datetime

def timediff(time1, time2):
    timea = datetime.strptime(time1, "%H:%M")
    timeb = datetime.strptime(time2, "%H:%M")
    if timea >= timeb:
        newtime = timea - timeb
        return int(newtime.seconds / 60)
    else:
        newtime = timea - timeb
        return int(-newtime.seconds / 60)


def getclosest(lst, K):
    num = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
    return num

input1 = "5,8,10:30,11:30"  
#Input 5 team members, located on the 8th floor, meeting time 10:30 - 11:30 
ipcapacity, ipfloor, ipstart, ipend = input1.split(",")
#print("ipcapacity:" + ipcapacity + "\nipfloor:" + ipfloor + "\nipstart:" + ipstart + "\nipend:" + ipend)
availablerooms = []

file1 = open('rooms.txt', 'r')
while True:
    # Read next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    #strip the line for all white space etc and split it with comma
    x = line.strip().split(",")
    #further the first string from above split to get floor and room details 
    floor = x[0].split('.')[0]
    room = x[0].split('.')[1]
    capacity = x[1]
    #check the capacity of meeting room
    if capacity >= ipcapacity:
        for i in range(2, len(x), 2):
            #check the starting time and its availability 
            checkStarttime = timediff(ipstart, x[i])
            if checkStarttime >= 0:
                checkEndtime = timediff(x[i + 1], ipend)
                # check meeting end time availability if starting time available as per the duration of meeting
                if checkEndtime >= 0:
                    #collect info for all available meeting room 
                    availablerooms.append(x[0])


file1.close()
if not availablerooms:
    #if no room is available as per the requirement 
    print("There is no meeting available which meets your requirement")
else:
#   converting list of available meeting rooms into dict
    floorrooms = {int(fr.split('.')[0]): int(fr.split('.')[1]) for fr in availablerooms}
#   sorting the dict on floor and picking the closest floor
#   same logic could be use to get the nearest meeting room in case needed
    closestfloor = getclosest(sorted(floorrooms), int(ipfloor))
    print("{0}.{1}".format(closestfloor, floorrooms[closestfloor]))
