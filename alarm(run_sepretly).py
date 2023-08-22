import json
import time
from alarm_time_class import Tm
from datetime import datetime
import notify2


notify2.init('app name')


def log(mssg):
    print(mssg)


def update():
    a = list()

    with open("ls.txt", "r") as f:
        for i in json.load(f):
            a.append(i)

    times = list()

    for i in a:
        times.append(Tm(i))

    return times


def deploy_the_alerts(name):
    n = notify2.Notification(name,
                             "yes you goddam it do your chores",
                             "notification-message-im"  # Icon name
                             )
    n.show()


def act_alarm(times):
    today = datetime.now()
    h = today.strftime("%H")
    m = today.strftime("%M")

    currents = list()
    log("isce uro")
    for i in times:
        # log(i.hour)
        if i.hour == int(h) or i.hour + 1 == int(h):
            currents.append(i)

    soon = list()
    slp = list()
    log("gleda min")
    for i in currents:
        log(i.min)
        log(m)
        if i.min == int(m) + 5 or i.min == int(m) + 1 or i.min == int(m) + 2 or i.min == int(m) + 3 or i.min + 4 == int(m):
            soon.append(i)
            slp.append(i.min)

    deployed_alarms = 0

    while len(soon) != 0:
        log("caka na alarm")

        for i in soon:
            time.sleep(15.00)
            today = datetime.now()
            m = today.strftime("%M")
            if i.min == int(m):
                deploy_the_alerts(i.name)
                soon.remove(i)


def today(times):
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    today = days[datetime.today().weekday()]
    todays = list()

    log("Gleda todays")
    for i in times:
        for ii in i.days:
            if ii == today:
                todays.append(i)

    act_alarm(todays)


while True:
    log("Updatanje")
    times = update()
    today(times)
    time.sleep(290.00)
    today(times)
    time.sleep(290.00)
    today(times)
    time.sleep(290.00)
