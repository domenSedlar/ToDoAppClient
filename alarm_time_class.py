class Tm:
    def __init__(self, dic):
        a = 0

        self.name = dic["name"]
        time = dic["reminder"]

        if time[a] == "'":
          a += 1
        self.days = list()
        days1 = time[a: time.find("-")]
        c = ""

        for i in days1:
            if i == "+":
                self.days.append(c)
            else:
                c = c + i

        self.hour = int(time[time.find("-") + 1] + time[time.find("-") + 2])
        self.min = int(time[time.find(":") + 1] + time[time.find(":") + 2])