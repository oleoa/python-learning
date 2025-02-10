import math

def mean(arr: list):
    mean = 0
    for s in arr:
        mean += s
    mean /= len(arr)
    return mean

def median(arr: list):
    median = 0
    arr.sort()
    if len(arr) % 2 == 0:
        median = (arr[math.floor(len(arr)/2)] + arr[math.floor(len(arr)/2)-1]) / 2
    else:
        median = arr[math.floor(len(arr)/2)]
    return median

def mode(arr: list):
    arr.sort()
    separation = []
    separation_index = 0
    separation.append([])
    last_number = arr[0]
    for item in arr:
        if item == last_number:
            separation[separation_index].append(item)
        else:
            separation_index += 1
            separation.append([])
            separation[separation_index].append(item)
            last_number = item
    longest_number = {
        "key": 0,
        "value": 0,
        "len": 0
    }
    for key_item in range(len(separation)):
        if len(separation[key_item]) > longest_number["len"]:
            longest_number["key"] = key_item
            longest_number["value"] = separation[key_item][0]
            longest_number["len"] = len(separation[key_item])
    return longest_number["value"]
