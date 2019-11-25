import sys
from os import system
def main():
    print("Welcome to your Todo list app.\nEnter your name to continue.")
    cmd = input()
    todo = ToDoList(cmd)

    while(1):
        clear()
        show_actions()
        cmd = input()
        if(cmd=="1"):
            todo.add_task()

        
def get_names():
    print("Enter names")
    li =[]
    name = input()
    while name != "\n":
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
        return len(self.q==0)
    def enq(self,item):
        print("adding to queue")
        self.q.append(item)
    def deq():
        ret = self.q.pop(0) #remove head
        return ret
    def __str__(self):
        if self.is_empty:
            return "Nothing to do~"
        else:
            return "Sise of to do list : {}\n".format(len(self.q))

class ToDoList(MyQueue):

    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def add_task(self):
        stop = False
        while not(stop):
            print("Enter a valid date in form dd/mm/yyyy")
            d,m,y = input().split("/")
            print(d,m,y)
            date = Date(d,m,y)
            valid = date.validate()
            print(valid)
            if valid:
                stop = True
        stop = False
        while not(stop):
            print("Enter a valid start time in form hh:mm")
            h,m = input().split(':')
            time = Time(h,m)
            valid = time.validate()
            if valid:
                stop = True
        stop = False
        while not(stop):
            try:
                print("Enter a valid time duration in form hh:mm")
                h,m = input().split(':')
                dtime = Time(h,m)
                valid = dtime.validate()
                if valid:
                    stop = True
            except: 
        var_task = Task(date,time,dtime)
        names = get_names()
        var_task.add_people(names)
        super().enq(var_task)
        
    def deq(self):
        ret = super().deq()
        print(ret)
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
        if len(str(self.year)) > 4:
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
        return "{%02d:%02d}".format(self.hours,self.mins)

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
    def add_people(self,li):
        for name in li:
            self.people.append(name)

    def __str__(self):
        x = super().__str__()
        return "{}\n{}\n".format(x,self.duration,str(self.people))

class Event(GeneralType):
    def __init__(self,date,start_time,location):
        super().__init__(date,start_time)
        self.location = location
    
    def __str__(self):
        x = super().__str__()
        return "{}\n{}\n".format(x,self.location)


if __name__=='__main__':
    main()