import sys
from os import system
import time
def main():
    print("Welcome to your Todo list app.\nEnter your name to continue.")
    cmd = input()
    todo = ToDoList(cmd)

    while(1):
        clear()
        show_actions()
        cmd = input()
        if(cmd=="1"):
            print("Enter date in dd/mm/yyyy format")
            d,m,y = input().split('/')
            date = Date(d,m,y)
            print("Enter start time in hh:mm format")
            h,m = input().split(":")
            stime = Time(h,m)
            print("Enter duration in hh:mm format")
            h,m = input().split(":")
            dtime = Time(h,m)
            vtask = Task(d,stime,dtime)
            li = get_names()
            vtask.add_people(li)
            todo.add(vtask)
        elif(cmd=="2"):
            print("Enter date in dd/mm/yyyy format")
            d,m,y = input().split('/')
            date = Date(d,m,y)
            print("Enter start time in hh:mm format")
            h,m = input().split(":")
            stime = Time(h,m)
            print("Enter location")
            loc = input()
            vevent = Event(date,stime,loc)
            todo.add(vevent)
        elif(cmd=="3"):
            tmp = todo.rm()
            if tmp.type == "Task":
                print("{} {} {} {}".format(tmp.date,tmp.start_time,tmp.duration,tmp.people))
            else:
                print("{} {} {}".format(tmp.date,tmp.start_time,tmp.location))   
            time.sleep(3)
        elif(cmd=="4"):
            sys.exit()
            
def get_names():
    print("Enter names")
    li =[]
    name = input()
    while name != "":
        li.append(name)
        name=input()
    return li

def show_actions():
    x = "1 to enqueue task"
    y = "2 to enqueue event"
    z = "3 to dequeue"
    a = "4 to exit"
    print("\n".join([x,y,z,a]))

def clear():
    system("clear")

class MyQueue(object):
    def __init__(self):
        self.q = []
    def is_empty(self):
        return self.q == []
    def enq(self,item):
        print("adding to queue")
        self.q.insert(0,item)
    def deq(self):
        ret = self.q.pop()
        return ret
    

class ToDoList():
    def __init__(self,name):
        self.name = name
        self.q = MyQueue()
    def add(self,item):
        self.q.enq(item)
    def rm(self):
        return self.q.deq()
    
class Date():

    months = range(1,13)
    days = range(1,32)
    def __init__(self,day,month,year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        
    
    def validate(self):
        if self.month not in self.months:
            return 0
        if self.day not in self.days:
            return 0
        if len(str(self.year)) != 4:
            return 0
        return 1

    def __str__(self):
        return "{}/{}/{}".format(self.day,self.month,self.year)

class Time():
    hours = range(0,24)
    mins = range(0,60)
    def __init__(self,hour=0,min=0):
        self.hour = int(hour)
        self.min = int(min)
    
    def validate(self):
        if self.hour not in self.hours:
            return 0
        if self.min not in self.mins:
            return 0
        return 1
    def __str__(self):
        return "{}:{}".format(self.hour,self.min)

class GeneralType():
    
    def __init__(self,date,start_time):
        self.date = date
        self.start_time = start_time

    def __str__(self):
        return "{}\n{}\n".format(self.date,self.start_time)

class Task(GeneralType):
    def __init__(self,date,start_time,duration):
        super().__init__(date,start_time)
        self.duration = duration
        self.people = []
        self.type = "Task"
    def add_people(self,li):
        for name in li:
            self.people.append(name)

    def __str__(self):
        x = super().__str__()
        return "{}\n{}\n{}\n".format(x,self.duration,str(self.people))

class Event(GeneralType):
    def __init__(self,date,start_time,location):
        super().__init__(date,start_time)
        self.location = location
        self.type = "Event"
    def __str__(self):
        x = super().__str__()
        return "{}\n{}\n".format(x,self.location)


if __name__=='__main__':
    main()