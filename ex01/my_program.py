from local_lib import path

def read_write():
    try:
        path.Path("new_dir").mkdir()
    except:
        pass
    f = path.Path("./new_dir/new_file.txt").touch()
    f.write_text("write something in this file")
    print(f.text())

if __name__ == "__main__":
    read_write()