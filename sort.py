# Creating my own sort function

def smallestIn(arr: list) -> dict:
    smallest_item: dict = {
        "key": 0,
        "value": arr[0]
    }
    for comparing in range(len(arr)):
        if arr[comparing] < smallest_item["value"]:
            smallest_item["value"] = arr[comparing]
            smallest_item["key"] = comparing
    return smallest_item

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
        smallest: dict = smallestIn(remaining)
        new = swap(new, smallest["key"], item)
    return new

_tuple = (5, 3, 2, 4, 1, 7, 9, 8, 6)
_new = sort(_tuple)
print("New sorted list: ", _new)

print(smallestIn([2,5,7,1,9]))
