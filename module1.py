def fibs(num):
    fabs = [0, 1]
    for i in range(num):
        fabs.append(fabs[-2] + fabs[-1])
    return fabs

def fun(num):
    return 99