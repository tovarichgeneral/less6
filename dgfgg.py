try:
    my_file = open("text/push.text.txt", "r")
    cont = my_file.readlines()
    my_file_write = open("text/write.txt", "w")
    for line in cont:
        my_file_write.write(line)
    my_file.close()
    print(my_file_write)
    my_file_write.close()
except:
    print("Error")

