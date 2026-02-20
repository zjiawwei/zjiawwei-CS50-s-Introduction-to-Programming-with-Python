str_input = input("输入问候语:").strip().lower()
if str_input == "hello" or str_input.startswith("hello"):
    print ("$0")
elif str_input.startswith("h"):
    print ("$20")
else:
    print ("$100")