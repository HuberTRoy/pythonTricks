name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

# "Hi Alice!" The key 382 in name_for_userid.
greeting(382)

# "Hi there!" The key 333333 not in name_for_userid.
greeting(333333)