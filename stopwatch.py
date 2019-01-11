import time
permission = input("Welcome to Xander'(siva) python stopwatch press \'Enter\' to continue:- ")
h = m = s = 0
while s >= 0:
    stop_watch = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    print(stop_watch + "\r", end="")
    s += 1
    time.sleep(1)
    if s == 60:
        m += 1
        s = 0
    else:
        pass
    if m == 60:
        h += 1
        m = 0
    else:
        pass

