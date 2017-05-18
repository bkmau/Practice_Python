import os
import locale

splitter = "{:+<200}".format("")
r_size_char = 5

def list_module(f_name):
    print(splitter)
    print("Print return type of open(FILE_NAME, [MODE]):{}".format(type(open(f_name, "r"))))
    print("List available properties and methods of type(open(FILE_NAME, [MODE]))\r\n{}".format(
        dir(type(open(f_name, "r")))))
    print("Python Doc: https://docs.python.org/3.5/library/io.html")
    print(splitter)

def read_only_file_in_text_mod(f_name):
    print(splitter)
    print("Start read {} in read only text mode".format(f_name))
    with open(f_name, "r") as f:
        pass
    print(splitter)

def read_only_file_in_binary_mod(f_name):
    print(splitter)
    print("Start read {} in read only binary mode".format(f_name))
    with open(f_name, "br") as f:
        print("Is seekable:{}".format(f.seekable()))
        # for whence parameter of file object check out
        #  https://docs.python.org/3.2/tutorial/inputoutput.html#methods-of-file-objects
        print("Using f.seek(offset[, whence]),"
              "offset is interpreted relative to the position indicated by whence."
              "The default value for whence is SEEK_SET. Values for whence are")
        print("SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive")
        print("SEEK_CUR or 1 – current stream position; offset may be negative")
        print("SEEK_END or 2 – end of the stream; offset is usually negative")

        print("Call f.seek(0) seeks relative to the beginning of the file...")
        f.seek(0)
        print("Get current stream position: {}".format(f.tell()))

        print("Call f.seek(20) seeks relative to the beginning of the file...")
        f.seek(20)
        print("Get current stream position: {}".format(f.tell()))

        f.seek(20)
        print("Get current stream position: {}".format(f.tell()))

        print("Call f.seek(5, os.SEEK_CUR) seeks relative to the current position of the file in binary mode...")
        f.seek(5, os.SEEK_CUR)
        print(f.readline())
        print("Get current stream position: {}".format(f.tell()))

        print("Call f.seek(20, os.SEEK_END) seeks relative to the end of the file in binary mode...")
        f.seek(20, os.SEEK_END)
        print("Get current stream position: {}".format(f.tell()))
    print(splitter)


def main():
    print(locale.getpreferredencoding(False))
    file_to_read = "test1.txt"
    file_to_write = "test2.txt"



    # list_module(file_to_read)
    #
    read_only_file_in_text_mod(file_to_read)
    # read_only_file_in_binary_mod(file_to_read)


print(locale.getdefaultlocale())



# with open(file_to_read, "r") as f:
#     print("Decode stream by {}".format(f.encoding))
#     print("Use f.tell() to get current stream position: {}".format(f.tell()))
#     print(splitter)
#
#     print("Using f.readline(size=-1)")
#     print("Get current stream position: {}".format(f.tell()))
#     print("Using f.readline() to read stream: \r\n===\r\n{}\r\n===".format(f.readline()))
#     print("Get current stream position: {}\r\n".format(f.tell()))
#
#     print("Get current stream position: {}".format(f.tell()))
#     print("Using f.readline({}) to read stream: \r\n===\r\n{}\r\n===".format(r_size_char, f.readline(r_size_char)))
#     print("Get current stream position: {}\r\n".format(f.tell()))
#
#     print("Get current stream position: {}".format(f.tell()))
#     print("Using f.readline() to read stream: \r\n===\r\n{}\r\n===".format(f.readline()))
#     print("Get current stream position: {}\r\n".format(f.tell()))
#
#     print("Get current stream position: {}".format(f.tell()))
#     print("Using f.readline() to read stream: \r\n===\r\n{}\r\n===".format(f.readline()))
#     print("Get current stream position: {}\r\n".format(f.tell()))
#     print(splitter)


    # print("Read {} characters for each time.".format(r_size_char))
    # print("First Read: {}".format(f.read(r_size_char)))
    # print("Second: {}".format(f.read(r_size_char)))
    #
    # f.seek(0)
    #
    #
    # f.seek(0)
    # print("Call list(f)\r\n{}".format(list(f)))
    # print("Call list(f) again\r\n{}".format(list(f)))
    #
    # f.seek(0)
    # print("First Read: {}".format(f.readline()))
    # print("Second: {}".format(f.readline()))
    # print("Call f.tell() to get position: {}".format(f.tell()))
    #
    # f.seek(f.tell() + 24)
    # print("Call f.seek(f.tell() + 20) to set location and call f.readline() again...\r\n{}".format(f.readline()))

    # f.seek(0)
    # for line in f:
    #     print(line.strip("\r\n"))
