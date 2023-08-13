def try_covert_int(input_string: str) -> int:
    while True:
        try:
            num = int(input_string)
            return num
        except:
            print("Invalid Number")
            input_string = input("Please Enter a valid number: ")
