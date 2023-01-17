import json


def write(t, path="./data/", file_name="tmp"):
    f = open(path+file_name+".txt", "w")
    # r a w x
    # rt at wt xt setting
    # rb ab wb xb
    f.write(t)
    f.close()


def read(path="./data/", file_name="tmp"):
    f = open(path+file_name+".txt", "r")
    read = f.read()
    f.close()
    return read


def writeJson(t, path="./data/", file_name="tmp"):
    with open(path+file_name+".json", "w") as f:
        json.dump(t, f, ensure_ascii=False)


def readJson(path="./data/", file_name="tmp"):
    with open(path + file_name+".json", "r") as f:
        context = json.loads(f.read())
        print("Read "+file_name+"'s context type is " + str(type(context)))
        return context
