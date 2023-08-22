import requests
import json
from datetime import datetime
from random import randint
import threading
import time as _time_
import json
from AES import AES

from queue import Queue

def log(mssg):
    # print(mssg)
    pass

def l(mss):
    print(mss)

#ip = "http://192.168.182.228:5000/"
ip = "http://127.0.0.1:5000/"


key = "j#_t9mjGfCHNYD*U"

aes = AES([bytearray(key[0:4], 'UTF-8'), bytearray(key[4:8], 'UTF-8'), bytearray(key[8:12], 'UTF-8'), bytearray(key[12:16], 'UTF-8')])


class Client:

    def __init__(self):
        self.online = True
        self.enter = False
        self.t = threading.Thread(target=self.loop_requests)
        self.request_q = Queue(maxsize=0)
        # self.t.start()

    def snd_requests(self, query):
        log("send request")
        l("v send requests")

        for i in "1234":
            l("pinging")
            try:
                log("ping")
                ping = requests.get(ip + "ping")
                c = ping.status_code
            except requests.exceptions.ConnectionError:
                c = 600
            if c == 200:
                break
        log("c je " + str(c))

        if c != 200:
            l("ping error number: " + str(c))
            return c

        token = ping.content.decode("UTF-8")
        log("token je " + str(token))
        a = 31 + len(query[0:query.find("-")])
        temp_query = list(query)
        log("temp qurey je ")
        log(temp_query)
        temp_query[a] = str(token[0])
        temp_query[a + 1] = str(token[1])
        temp_query[a + 2] = str(token[2])
        log("temp qurey je ")
        log(temp_query)
        g = ""
        for i in temp_query:
            g += i

        query = g
        log("g je " + g)
        l(query[query.find("':'") + 3: -1])
        if not "tsk-cd-" in query:
            for i in range(10):
                log("send")
                try:
                    r = requests.get(ip + query)
                    c = r.status_code
                    if c == 200:
                        l("returned code: " + str(c) + " query: " + ip + query)

                        log("it worked ")
                        return c
                except requests.exceptions.ConnectionError:
                    c = 600
            l("returned code: " + str(c) + " query: " + ip + query)
            return c
        else:
            for i in range(10):
                log("send")
                try:
                    r = requests.get(ip + query.replace(query[query.find("':'") + 3: -1],""), data = {'end': query[query.find("':'") + 3: -1]})
                    l(ip + query.replace(query[query.find("':'") + 3: -1],""))
                    c = r.status_code
                    if c == 200:
                        l("returned code: " + str(c) + " query: " + ip + query)

                        log("it worked ")
                        return c
                except requests.exceptions.ConnectionError:
                    c = 600
            l("returned code: " + str(c) + " query: " + ip + query)
            return c

    def loop_requests(self):
        with open("made.txt", "w") as f:
            log("dumped")
            json.dump([], f)

        while True:

            if self.request_q.empty():
                return

            q = self.request_q.get_nowait()

            with open("querys.txt", "r") as s:
                unmade_qs = json.load(s)
                unmade_qs.append(q)
            with open("querys.txt", "w") as s:
                json.dump(unmade_qs, s)

            a = self.snd_requests(q)
            log("it should have sent " + str(a))
            if a == 200:
                unmade_qs.pop(-1)
                with open("querys.txt", "w") as s:
                    json.dump(unmade_qs, s)

                
    def save_query(self, query):
        log("save query")
        with open("querys.txt", "r") as s:
            a = json.load(s)
        a.append(query)
        with open("querys.txt", "w") as s:
            json.dump(a, s)

    def decode(self, enyc):
        o = aes.deyc_string(enyc)
        return o

    def opend(self):
        with open("abc.txt", "w") as f:
            log("why")
            json.dump([], f)
        log("halo")
        with open("querys.txt", "r") as f:
            ls = json.load(f)
        log("what")
        self.online = True
        connection = True
        ls_ls = "c"
        tsk_ls = "c"
        self.l = [ls_ls, tsk_ls]

        log("pred loopom")

        a = 0

        for i in ls:
            a = self.snd_requests(i)
            l(str(a) + " v opend for loopu 1 request: " + i)
            if a == 400:
                connection = False
                self.online = False
                break

        c = 0
        if connection:
            log("connection")
            if a == 200:
                with open("querys.txt", "w") as f:
                    log("wow")
                    json.dump([], f)

            for i in range(2):
                try:
                    log("triing connecting")
                    r = requests.get(ip + "update_ls")
                    c = r.status_code
                except requests.exceptions.ConnectionError:
                    log("failed")
                    c = 400
                    self.online = False

                log("c je " + str(c))
                if c == 200:
                    log("c je 200")
                    ls_ls = (r.content.decode("utf-8"))
                    break
            log(c)
            if c == 200:
                for i in range(3):
                    try:
                        r = requests.get(ip + "update_tsk")
                        c = r.status_code
                    except requests.exceptions.ConnectionError:
                        c = 400
                        self.online = False

                    if c == 200:
                        tsk_ls = (r.content.decode("utf-8"))
                        break

                new_ls = list()
                for i in json.loads(ls_ls):
                    log(str(i))
                    a = {"name": self.decode(i["name"]), "bool": i["bool"], "reminder": "-"}
                    new_ls.append(a)

                self.l[0] = new_ls
                log("AAAAAAAAAAAAAAAAa")

                index = -1
                new_tsk = list()
                log(tsk_ls)
                for i in json.loads(tsk_ls):
                    log(i)
                    new_tsk.append([])
                    index += 1
                    for ii in i:
                        b = ii["desc"]
                        b = self.decode(b)

                        a = {"name": self.decode(ii["name"]), "desc": b, "completed": ii["completed"]}
                        new_tsk[index].append(a)

                self.l[1] = new_tsk
                log("self l je " + str(self.l))

    def enyc(self, string):
        e = aes.enyc_string(string)
        return e

    def mk_request(self, ls_or_tsk, action, ls_name, ending='', tsk_name=''):

        ls_name = self.enyc(ls_name)
        ###
        t = datetime.now()
        time = t.strftime("%Y-%m-%d %H:%M:%S.%f")
        ###
        if not action == "cs":
            if not ending == '':
                print(":(")
                ending = self.enyc(ending)

        if tsk_name != '':
            tsk_name = self.enyc(tsk_name)

        log("mk request")
        t = datetime.now()
        time = t.strftime("%Y-%m-%d %H:%M:%S.%f")
        if ls_or_tsk == "tsk":

            query = "tsk-" + action + "-" + time + "-" + str(randint(100,999)) + "-" + "'" + str(ls_name) + "'-'" + str(tsk_name) + "':'" + str(ending) + "'"
        else:
            query = "ls-" + action + "-" + time + "-" + str(randint(100,999)) + "-" + "'" + str(ls_name) + "':'" + str(ending) + "'"

        self.request_q.put(query)

        if not self.t.is_alive():
            self.t = threading.Thread(target=self.loop_requests)
            self.t.start()
            _time_.sleep(0.1)

"""        a = "save"
        self.enter = False
        _time_.sleep(0.1)
        with open("made.txt", "r") as f:
            a = json.load(f)
            a.append(query)
        with open("made.txt", "w") as f:
            json.dump(a, f)
        self.enter = True
"""
        # if self.online:
        #    a = self.snd_requests(query)
        # if a == "save":
        #    self.save_query(query)


"""r = requests.get("http://localhost:5000/tsk-ad-2020-11-02 19:55:54.934466-255-'list name'")
print(r.status_code)
print(r.content.decode("utf-8"))
"""
