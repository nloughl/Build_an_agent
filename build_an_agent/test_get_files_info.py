from functions.get_files_info import get_files_info


def main():
    dirs = [".", "pkg", "/bin", "../"]
    for dir in dirs:
        res = get_files_info("calculator", dir)
        print(f"Result for '{dir}' directory:\n {res}")


if __name__ == "__main__":
    main()
