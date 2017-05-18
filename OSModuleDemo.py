import os
import stat
import winshell
import datetime
import random

splitter = "{:+<200}".format("")

print("List available properties and methods of module os and winshell")
print("{: <35}:{}".format("os", dir(os)))
print("{: <35}:{}".format("winshell", dir(winshell)))
print(splitter)

print("os module")
curr_dir = os.getcwd()
m_dir = r"C:\python3"
print("{: <35}:{}".format("os.getcwd", os.getcwd()))
print("{: <35}:{}".format("os.listdir()", os.listdir()))
print("{: <35}:{}".format("os.listdir(\"{}\")".format(m_dir), os.listdir(m_dir)))
os.chdir(m_dir)
print("After os.chdir(\"{}\")".format(m_dir))
print("{: <35}:{}".format("os.getcwd", os.getcwd()))
os.chdir(curr_dir)
print(splitter)

print("os.stat(<FILE>) & stat module")
m_file = os.listdir()
m_select = []
for item in m_file:
    ext = os.path.splitext(str(item))[1]
    if ext == ".py":
        m_select.append(str(item))
f = m_select[random.randint(0, len(m_select))]
state = os.stat(f)
print("{: <35}:{}".format("Mode", stat.filemode(state.st_mode)))
print("{: <35}:{} Bytes".format("Size", state.st_size))
print("{: <35}:{:%Y/%m/%d %H:%M:%S}".format("Last Access at", datetime.datetime.fromtimestamp(state.st_atime)))
print("{: <35}:{:%Y/%m/%d %H:%M:%S}".format("Last Modify at", datetime.datetime.fromtimestamp(state.st_mtime)))
print("{: <35}:{:%Y/%m/%d %H:%M:%S}".format("Create at", datetime.datetime.fromtimestamp(state.st_ctime)))
print(splitter)

print("os.path")
f = r"c:\abc.txt"
print("{: <35}:{}".format("os.path.basename(\"{}\")".format(f), os.path.basename(f)))
print("{: <35}:{}".format("os.path.dirname(\"{}\")".format(f), os.path.dirname(f)))
print("{: <35}:{}".format("os.path.split(\"{}\")".format(f), os.path.split(f)))
print("{: <35}:{}".format("os.path.exists(\"{}\")".format(f), os.path.exists(f)))
print("{: <35}:{}".format("os.path.isdir(\"{}\")".format(f), os.path.isdir(f)))
print("{: <35}:{}".format("os.path.isfile(\"{}\")".format(f), os.path.isfile(f)))
print("{: <35}:{}".format("os.path.splitdrive(\"{}\")".format(f), os.path.splitdrive(f)))
print("{: <35}:{}".format("os.path.splitext(\"{}\")".format(f), os.path.splitext(f)))
print(splitter)

print("os.environ")
print("{: <30}:{}".format("os.environ.keys()", os.environ.keys()))

print("Get environment variable by os.environ.get(<variable_name>)")
for p in os.environ.get("PATH").split(";"):
    print(p)
print(splitter)


print("{: ^45}|{: ^25}|{: ^60}".format("Root", "DirName", "FileName"))
print("{:=<130}".format(""))
for root, dirs, files in os.walk(r"C:\Users\Ben Mau\Desktop\test"):
    print("{: <45}|{: <25}|{: <60}".format(root, str(dirs), str(files)))
    if files:
        print("Files:")
        for f in files:
            print(os.path.join(root, f))
        print("{:=<130}".format(""))
    else:
        print("{:=<130}".format(""))
print(splitter)









