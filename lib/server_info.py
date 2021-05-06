import psutil

print(psutil.cpu_percent(interval=True))
print(psutil.cpu_count(logical=False))


def get_cpu_detail():
    """
    获取cpu信息
    :return:
    """
    cpu_usage = psutil.cpu_percent(interval=True)
    cpu_count_logic = psutil.cpu_count()
    cpu_count = psutil.cpu_count(logical=False)