def size_of_zander(length):
    if length >= 42:
        print("Congratulations! The zander meets the size limit.")
    else:
        difference = 42 - length
        print("The zander is below the size limit. Please release it back into the lake.")
        print("The zander is", difference, "centimeters below the size limit.")

length = float(input("Enter the length of the zander in centimeters: "))
size_of_zander(length)

