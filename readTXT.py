
def readtxt(var):
    with open(var) as f:
        list = f.readlines()
    return list
    f.close()