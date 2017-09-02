def kb(value):
    return str(value / 1024) + " KB"


def mb(value):
    return str(value / 1024 / 1024) + " MB"


def gb(value):
    return str(value / 1024 / 1024 / 1024) + " GB"


def uptime(boot_time):
    import time
    upt = time.time() - boot_time

    retval = ""
    days = int(upt / (60 * 60 * 24))

    if days != 0:
        retval += str(days) + " " + ("days" if days > 1 else "day") + ", "

    minutes = int(upt / 60)
    hours = int(minutes / 60)
    hours %= 24
    minutes %= 60

    if hours != 0:
        retval += str(hours) + ":" + (str(minutes) if minutes >= 10 else "0" + str(minutes))
    else:
        retval += str(minutes) + " min"

    return retval


def register_filters(env):
    env.filters['KB'] = kb
    env.filters['MB'] = mb
    env.filters['GB'] = gb
    env.filters['uptime'] = uptime
