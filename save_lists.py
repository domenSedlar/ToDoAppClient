from son import Files
from list_class import List_class

son = Files()


class Save_Lists:

    def save(self, name, remndr):
        objc = List_class(name, False, remndr)
        lists = son.load_ls()

        lists.append(objc)
        son.save_ls(lists)

    def restore(self, ls):
        son.restore(ls)
