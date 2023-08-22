import pickle

l_file = open("../deleted_list.dat", "rb+")
t_file = open("../deleted_tasks.dat")


class Restore:

    list_names = pickle.load(l_file)
    list_tasks = pickle.load(t_file)

    def save_list(self, name, tasks):
        self.list_names.append(name)
        self.list_tasks.append(tasks)

        pickle.dump(self.list_tasks, t_file)
        pickle.dump(self.list_names, l_file)
