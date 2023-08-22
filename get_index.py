def get_index_of_task(task_name, task_list):
    index = 0
    for i in task_list:
        if task_name == i.name:
            return index
        index += 1

    return -1
