name = input("What's your name? ") # ask input from user

match name: # match with name parameter
    case "Andi" | "Joko": # case Andi will print class a string if name = Andi or Joko
        print("class a")
    case "Sandi":
        print("class b")
    case "Jono":
        print("class c")
    case _: # this case will run when nothing is matched (same concept with else)
        print("not in any class")

