def getAllStrings(obj):
   """Get a list with all the strings contained in the given object."""

   lst = []
   
   if isinstance(obj, str):
        lst.append(obj)
        
   elif isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        for item in obj:
            lst.extend(getAllStrings(item))
            
   elif isinstance(obj, dict):
        for value in obj.values():
            lst.extend(getAllStrings(value))

   return lst


def main():
   obj1 = ["one", 2, ["three", 4, [5, "six"]]]
   obj2 = [1, "a", ("b", [{"c", "d", 2}, 3, (4, "e")], "f")]
   obj3 = {"a": 1, "b": ["c", "d"], (2, ("x", 3)): obj1}
   print(eval(input()))


if __name__ == "__main__":
   main()