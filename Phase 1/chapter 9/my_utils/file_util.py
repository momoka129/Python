def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"There is an error: {e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    print_file_info("Phase 1/chapter 9/my_utils/new_file.txt")
    append_to_file("Phase 1/chapter 9/my_utils/new_file.txt", "Huiyuan ai is my wife")
