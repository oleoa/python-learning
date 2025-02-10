# Creating my own sort function

def swap(arr: list, a: int, b: int) -> list:
    new = [item for item in arr]
    new[a] = arr[b]
    new[b] = arr[a]
    return new

def sort(arr: tuple) -> list:
    new = [item for item in arr]
    for item in range(len(new)-1):
        analizing: int = new[item]
        remaining: list = new[item+1:]
        smallest = {
            "value": analizing,
            "key": item
        }
        for comparing in range(len(remaining)):
            if remaining[comparing] < smallest["value"]:
                smallest["value"] = remaining[comparing]
                smallest["key"] = comparing+item+1
        new = swap(new, smallest["key"], item)
    return new

_tuple = (5, 3, 2, 4, 1, 7, 9, 8, 6)
_new = sort(_tuple)
print("New sorted list: ", _new)
