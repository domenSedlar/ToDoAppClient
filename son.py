import json
from client.client import Client
from list_class import List_class
from todo import Todo

client = Client()


class Files:
    index = 0

    def get_index(self, name):
        with open("ls.txt", "r") as ls_file:
            ls_ls = json.load(ls_file)

        self.index = 0
        while name != ls_ls[self.index]["name"]:
            self.index += 1

    def load_ls(self):
        with open("ls.txt", "r") as ls_file:
            ls_ls = json.load(ls_file)

        ls = list()
        for i in ls_ls:
            objc = List_class(i["name"], i["bool"], i["reminder"])
            ls.append(objc)
        return ls

    def load_tsk(self):
        with open("tsk.txt", "r") as ls_file:
            ls_ls = json.load(ls_file)

        index = 0
        ls = []
        for i in ls_ls:
            a = []
            ls.append(a)

            for ii in i:
                objc = Todo(ii["name"], ii["desc"], ii["completed"])
                ls[index].append(objc)
            index += 1
        return ls

# ADD, CD, RM TSK /
    def save_tsk(self, ls, action, ls_name, tsk_name, ending=''):
        client.mk_request("tsk", action, ls_name, ending, tsk_name)
        ls_d = []
        index = 0
        for i in ls:
            ls_d.append([])
            for ii in i:
                ls_d[index].append({"name": ii.name, "desc": ii.desc, "completed": ii.completed})
            index += 1
        with open("tsk.txt", "w") as tsk_file:
            json.dump(ls_d, tsk_file)

# Samo za updatanje taskov /

    def upd_tsk(self, ls):
        # ls = json.loads(ls)

        ls_d = []
        index = 0
        for i in ls:
            ls_d.append([])
            for ii in i:
                ls_d[index].append({"name": ii["name"], "desc": ii["desc"], "completed": ii["completed"]})
            index += 1
        with open("tsk.txt", "w") as tsk_file:
            json.dump(ls_d, tsk_file)

# ADD LS /
    def save_ls(self, ls):
        ls_ls = list()
        for i in ls:
            ls_ls.append({"name": i.name, "bool": i.completed, "reminder": i.reminder})
            ls_name = i.name
            ending = i.reminder

        client.mk_request("ls", "ad", ls_name, ending)

        with open("ls.txt", "w") as ls_file:
            json.dump(ls_ls, ls_file)

        with open("tsk.txt", "r") as tsk_file:
            a = json.load(tsk_file)
            a.append([])
        with open("tsk.txt", "w") as tsk_file:
            json.dump(a, tsk_file)

# Updatanje listov /
    def upd_ls(self, ls):
        # print(ls)
        # ls = json.loads(ls)
        ls_ls = list()
        for i in ls:
            ls_ls.append({"name": i['name'], "bool": i['bool'], "reminder": i['reminder']})

        with open("ls.txt", "w") as ls_file:
            json.dump(ls_ls, ls_file)

        with open("tsk.txt", "r") as tsk_file:
            a = json.load(tsk_file)
            a.append([])
        with open("tsk.txt", "w") as tsk_file:
            json.dump(a, tsk_file)

# CA LS /
    def ls_ca(self, ls_ls, name, ending):
        ls = list()
        for i in ls_ls:
            ls.append({"name": i.name, "bool": i.completed, "reminder": i.reminder})

        client.mk_request("ls", "ca", name, ending)
        with open("ls.txt", "w") as a:
            json.dump(ls, a)

# RM LS /
    def del_ls(self, ls_name):

        client.mk_request("ls", "rm", ls_name)

        with open("ls.txt", "r") as ls_file:
            ls_ls = json.load(ls_file)

        with open("tsk.txt", "r") as tsk_file:
            tsk_ls = json.load(tsk_file)

        index = 0
        for i in ls_ls:
            if ls_name == i["name"]:
                del_ls = i
                ls_ls.remove(i)
                break
            index += 1

        del_tsks = tsk_ls[index]
        tsk_ls.pop(index)

        with open("ls.txt", "w") as ls_file:
            json.dump(ls_ls, ls_file)

        with open("tsk.txt", "w") as tsk_file:
            json.dump(tsk_ls, tsk_file)

        with open("del_ls.text", "w") as del_ls_file:
            json.dump(del_ls, del_ls_file)

        with open("del_tsks.text", "w") as del_tsks_file:
            json.dump(del_tsks, del_tsks_file)

# CS TSK
    def comp(self, tsk_index, ls_index):
        with open("tsk.txt", "r") as tsk_file:
            tsk_ls = json.load(tsk_file)

        if tsk_ls[ls_index][tsk_index]["completed"]:
            tsk_ls[ls_index][tsk_index]["completed"] = False
        else:
            tsk_ls[ls_index][tsk_index]["completed"] = True

        with open("ls.txt", "r") as f:
            a = json.load(f)

        client.mk_request("tsk", "cs", a[ls_index]["name"], str(tsk_ls[ls_index][tsk_index]["completed"]), tsk_ls[ls_index][tsk_index]["name"])
        print("CS")
        print(str(tsk_ls[ls_index][tsk_index]["completed"]))

        with open("tsk.txt", "w") as tsk_file:
            json.dump(tsk_ls, tsk_file)

# Pregleda ce je kak zbrisan seznam /
    def chec(self):
        with open("del_ls.text", "r") as del_ls_file:
            ls = json.load(del_ls_file)

        if ls != "":
            a = List_class(ls["name"], ls["bool"], ls["reminder"])

        return a

# AD LS (zdej ga restora) /
    def restore(self, i):
        ls_d = {"name": i.name, "bool": i.completed, "reminder": i.reminder}

        client.mk_request("ls", "ad", i.name, i.reminder)

        with open("ls.txt", "r") as ls_file:
            ls_ls = json.load(ls_file)
        ls_ls.append(ls_d)
        with open("ls.txt", "w") as ls_file:
            json.dump(ls_ls, ls_file)

        with open("del_tsks.text", "r") as del_tsk_file:
            del_tsks = json.load(del_tsk_file)

        with open("del_tsks.text", "w") as del_tsk_file:
            json.dump("", del_tsk_file)

        with open("tsk.txt", "r") as tsk_file:
            tsks = json.load(tsk_file)

        tsks.append(del_tsks)

        with open("tsk.txt", "w") as tsk_file:
            json.dump(tsks, tsk_file)


