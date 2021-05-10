import psutil

# print(psutil.cpu_percent(interval=0.5))
# print(psutil.cpu_count(logical=False))
# disk_info = psutil.disk_usage("/")
# memory_info = psutil.virtual_memory()
# print(disk_info.percent)
# print(memory_info.percent)


def get_server_info():
    """
    获取cpu信息
    :return:
    """
    # cpu_usage = psutil.cpu_percent(interval=True)
    # cpu_count_logic = psutil.cpu_count()
    # cpu_count = psutil.cpu_count(logical=False)
    # disk_info = psutil.disk_usage("/")
    cpu_info = psutil.cpu_percent(interval=0.5)
    # print(psutil.cpu_count(logical=False))
    disk_info = psutil.disk_usage("/").percent
    memory_info = psutil.virtual_memory().percent
    server_info_dict = {'cpu_info': cpu_info, 'memory_info': memory_info, 'disk_info': disk_info}
    print(server_info_dict)
    return server_info_dict