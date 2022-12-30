


def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds - hh*3600) // 60
    ss = seconds - hh*3600 - mm*60
    return f"{hh:0>2}:{mm:0>2}:{ss:0>2}"


print(make_readable(0)) #"00:00:00"
print(make_readable(5)) #"00:00:05"
print(make_readable(60)) #"00:01:00"
print(make_readable(86399)) #"23:59:59"
print(make_readable(359999)) #"59:59:59"
