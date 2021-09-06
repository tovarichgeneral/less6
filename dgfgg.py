def main():
    try:
        my_file = open("text/push.text.txt", "rb")
        my_file_write = open("text/write.txt", "wb")
        while True:
            cont = my_file.read(1024)
            if not cont:
                break
            my_file_write.write(cont)
        my_file.close()
        my_file_write.close()
    except FileNotFoundError:
        print("Error")


if __name__ == '__main__':
    main()
