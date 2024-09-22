def explodeObject(name, obj):
   """Print the name and representation (repr) of an object,
   followed by the name and representation of each of its elements,
   if the object is a list, tuple or dict.
   """
   print(f"{name} = {obj!r}")       # !r converts object to its repr!
   
   if isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            explodeObject(f"{name}[{i}]", item)
            
   elif isinstance(obj, dict):
        for key, value in obj.items():
            explodeObject(f"{name}[{repr(key)}]", value)

def main():
   obj1 = [1, ["a", ["b", 2], 3], 4]
   obj2 = [1, "ola", (2, [[3, 4], 5, ("adeus", 6)], 7)]
   obj3 = [1, {"ola": "hello", "adeus": ["bye", "adieu"]}, (2, [[3, 4], 5], 6)]
   
   
   explodeObject("obj1", obj1)
   explodeObject("obj2", obj2)
   explodeObject("obj3", obj3)


if __name__ == "__main__":
   main()