import pymongo

import myutils.c_user as cu


def createConnection():
    myclient = pymongo.MongoClient(
        "mongodb://" + cu.user['mongoDB']['username']+":"
        + cu.user['mongoDB']['password'] + "@"
        + cu.user['IP']+":"+cu.user['port']
    )  # Host以及port
    db = myclient[cu.user['database']]
    return db
