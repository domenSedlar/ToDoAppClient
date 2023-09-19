import json
#import son

def err_log(msg):
    print("ERR: " + msg)

def decode(enyc, f):
    #o = aes.deyc_string(enyc).replace('\u0000', '')
    if len(enyc) < 5:
        return enyc
    enyc = enyc[2:len(enyc)-1]
    print()
    print(enyc)
    o = f.decrypt(enyc.encode()).decode()
    return o

def exec_command(query, data, f):
    if query[0] == "t":
        action = query[4] + query[5]
        #time = query[7] + query[8] + query[9] + query[10] + query[11] + query[12] + query[13] + query[14] + query[15] + query[16] + query[17] + query[18] + query[19] + query[20] + query[21] + query[22] + query[23] + query[24] + query[25] + query[26] + query[27] + query[28] + query[29] + query[30] + query[31] + query[32]
        #t = Time(time)
        #token = query[34] + query[35] + query[36]
        ls_name = decode(query[39:query.find("'-'")], f)
        tsk_name = decode(query[query.find("'-'") + 3:query.find("':")], f)

        if action == "ad":
            ending = decode(query[query.find("':") + 3: -1], f)
            add_tsk(ls_name, tsk_name, ending)
            print("adding")
        elif action == "rm":
            del_tsk(ls_name, tsk_name)
        elif action == "cd":
            data = data[2:len(data)-1]
            ending = decode(data, f)
            desc_tsk(ls_name=ls_name, tsk_name=tsk_name, tsk_desc=ending)
        elif action == "cs":
            s = False
            if query[-3] == "u":
                s = True
            state_tsk(ls_name, tsk_name, s)

    elif query[0] == "l":
        action = query[3] + query[4]
        #time = query[6] + query[7] + query[8] + query[9] + query[10] + query[11] + query[12] + query[13] + query[14] + query[15] + query[16] + query[17] + query[18] + query[19] + query[20] + query[21] + query[22] + query[23] + query[24] + query[25] + query[26] + query[27] + query[28] + query[29] + query[30] + query[31]
        #token = query[33:36]
        ls_name = decode(query[38:query.find("':")], f)
        #t = Time(time)

        if action == "ad":
            alarm = decode(query[query.find("':'") + 3:-1], f)
            add_ls(ls_name, alarm)
        if action == "rm":
            del_ls(ls_name)


def add_ls(name, alarm):
    with open("ls.txt", "r") as ls_file:
        ls = json.load(ls_file)

    ls_ls = list()

    for l in ls:
        if l["name"] == name:
            return 0
        ls_ls.append({"name": l["name"], "bool": l["bool"], "reminder": l["reminder"]})
        ls_name = l["name"]
        ending = l["reminder"]

    ls_ls.append({"name": name, "bool": False, "reminder": alarm})

    with open("ls.txt", "w") as ls_file:
        json.dump(ls_ls, ls_file)

    
    with open("tsk.txt", "r") as tsk_file:
        a = json.load(tsk_file)
        a.append([])
    with open("tsk.txt", "w") as tsk_file:
        json.dump(a, tsk_file)

    return 1

def del_ls(name):
    with open("ls.txt", "r") as ls_file:
        ls = json.load(ls_file)

    ls_ls = list()

    i = -1
    j = 0
    found = False
    for l in ls:        
        i += 1

        if l["name"] == name:
            found = True
            j = i
            continue
        
        ls_ls.append({"name": l["name"], "bool": l["bool"], "reminder": l["reminder"]})
        ls_name = l["name"]
        ending = l["reminder"]

    if not found:
        return 0

    with open("ls.txt", "w") as ls_file:
        json.dump(ls_ls, ls_file)


    with open("tsk.txt", "r") as tsk_file:
        a = json.load(tsk_file)
        a.pop(j)
    
    with open("tsk.txt", "w") as tsk_file:
        json.dump(a, tsk_file)

    return 1

def find_ls(ls_name):
    i = -1
    a = True
    with open("ls.txt", "r") as f:
        l = json.load(f)
        for j in l:
            i += 1
            
            if j["name"] == ls_name:
                a = False
                break

    if a:
        return -1
    return i

def find_tsk(ls_ind, tsk_name):
    i = -1
    with open("tsk.txt", "r") as tsk_file:
        tsk_ls = json.load(tsk_file)
    a = True
    for j in tsk_ls[ls_ind]:
        i += 1
        if j["name"] == tsk_name:
            a = False
            break
    if a:
        return -1
    return i

def add_tsk(ls_name, tsk_name, tsk_desc):
    ind = find_ls(ls_name)

    if ind < 0:
        add_ls(ls_name, "-")
        ind = find_ls(ls_name)
        if ind < 0:
            err_log("in add_tsk couldnt find nor create parent list")
            return -1

    tsk_ls = list()

    with open("tsk.txt", "r") as tsk_file:
        tsk_ls = json.load(tsk_file)

    tsk_ind = find_tsk(ind, tsk_name)
    if tsk_ind > -1:
        return desc_tsk(ls_name, tsk_name, tsk_desc)

    tsk_ls[ind].append({"name": tsk_name, "desc": tsk_desc, "completed": False})

    with open("tsk.txt", "w") as tsk_file:
            json.dump(tsk_ls, tsk_file)

    return 1


def del_tsk(ls_name, tsk_name):
    ind = find_ls(ls_name)

    if ind < 0:
        return 0
    
    tsk_ls = list()

    i = -1
    with open("tsk.txt", "r") as tsk_file:
        tsk_ls = json.load(tsk_file)
    a = True
    for j in tsk_ls[ind]:
        i += 1

        if j["name"] == tsk_name:
            a = False
            break
    
    if a:
        return 0

    tsk_ls[ind].pop(i)

    with open("tsk.txt", "w") as tsk_file:
            json.dump(tsk_ls, tsk_file)


def state_tsk(ls_name, tsk_name, state):
    ind = find_ls(ls_name)

    if ind < 0:
        add_ls(ls_name, "-")
        ind = find_ls(ls_name)
        if ind < 0:
            err_log("in state_tsk couldnt find nor create parent list")
            return -1
        
    tsk_ind = find_tsk(ind, tsk_name)
    
    if tsk_ind < 0:
        add_tsk(ls_name, tsk_name, "")
        tsk_ind = find_tsk(ind, tsk_name)
        if tsk_ind < 0:
            err_log("in state_tsk couldnt find nor create task")
            return -1

    tsk_ls = list()

    with open("tsk.txt", "r") as tsk_file:
        tsk_ls = json.load(tsk_file)
    
    tsk_ls[ind][tsk_ind]["completed"] = state

    with open("tsk.txt", "w") as tsk_file:
        json.dump(tsk_ls, tsk_file)
    

def desc_tsk(ls_name, tsk_name, tsk_desc):
    ind = find_ls(ls_name)

    if ind < 0:
        add_ls(ls_name, "-")
        ind = find_ls(ls_name)
        if ind < 0:
            err_log("in state_tsk couldnt find nor create parent list")
            return -1
        
    tsk_ind = find_tsk(ind, tsk_name)
    
    if tsk_ind < 0:
        add_tsk(ls_name, tsk_name, tsk_desc)
        tsk_ind = find_tsk(ind, tsk_name)
        if tsk_ind < 0:
            err_log("in state_tsk couldnt find nor create task")
            return -1
        
        return 0
    
    tsk_ls = list()

    with open("tsk.txt", "r") as tsk_file:
        tsk_ls = json.load(tsk_file)
    
    tsk_ls[ind][tsk_ind]["desc"] = tsk_desc

    with open("tsk.txt", "w") as tsk_file:
            json.dump(tsk_ls, tsk_file)



"""
def ad(self, request):
    ls_ls = son.open_ls_ls()
    tsk_ls = son.open_tsk_ls()
    ls_exists = exists.ls(request.ls_name, ls_ls)

    if not ls_exists:
        return "O:"

    tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

    if not tsk_exist:
        ls_index = 0
        for i in ls_ls:
            if i["name"] == request.ls_name:
                break
            ls_index += 1

        d = {
            "name": request.tsk_name,
            "desc": request.ending,
            "completed": False
        }

        tsk_ls[ls_index].append(d)

        son.save_tsk_ls(tsk_ls)

        self.history.append(request)
        self.del_hs()

    else:
        similar_edits = fn.chc_tsk_history(request, self.history)
        do = True
        for i in similar_edits:
            print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
            a = comp_tm(i.time, request.time)
            if a == "second time is older":
                print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
                do = False
                return ""

        if do:
            ls_index = 0

            for i in ls_ls:
                if i["name"] == request.ls_name:
                    break
                ls_index += 1

            tsk_index = 0

            for i in tsk_ls[ls_index]:
                if i["name"] == request.tsk_name:
                    tsk_ls[ls_index][tsk_index]["desc"] = request.ending
                    son.save_tsk_ls(tsk_ls)
                    break
                tsk_index += 1
            self.history.append(request)
            self.del_hs()

    return ""

"""