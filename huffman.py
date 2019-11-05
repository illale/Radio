
CHARS = {
    "a": 5,
    "b": 9,
    "c": 12,
    "d": 13,
    "e": 16,
    "f": 45,
}

list = [CHARS["a"], CHARS["b"], CHARS["c"], CHARS["d"], CHARS["e"], CHARS["f"]]
end_list = []

while len(list) > 1:
    min1 = min(list)
    list.remove(min1)
    min2 = min(list)
    list.remove(min2)
    list.append(min1 + min2)
    end_list.append([min1, min2, min1 + min2])
    
    
list = [CHARS["a"], CHARS["b"], CHARS["c"], CHARS["d"], CHARS["e"], CHARS["f"]]    

if (end_list[-1][0] in list):
    print("0")
