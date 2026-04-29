from functions.run_python_file import run_python_file


def main():
    files = [("main.py", ""), ("main.py", ["3 + 5"]), ("tests.py", ""), ("../main.py", ""), ("nonexistent.py", ""), ("lorem.txt", "")]
    for (file, args) in files:
        res = run_python_file("calculator", file, args)
        print(f"Result for '{file}' file:\n {res}")


if __name__ == "__main__":
    main()
