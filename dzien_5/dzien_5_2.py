statuses= {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"

}

def status_counter(statuses, status):
    counter=0
    for osoba, stat in statuses.items():
        if stat == status:
            counter +=1
    return counter


def test_status_counter():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online"
    }
    assert status_counter(statuses, "xxx") == 0
    assert status_counter(statuses, "online") == 2
    assert status_counter(statuses, "offline") == 1