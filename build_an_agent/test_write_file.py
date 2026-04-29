from functions.write_file import write_file


def main():
    files = [("lorem.txt", "wait, this isn't lorem ipsum"), ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"), ("/tmp/temp.txt", "this should not be allowed")]
    for (file, content) in files:
        res = write_file("calculator", file, content)
        print(f"Result for '{file}' file:\n {res}")


if __name__ == "__main__":
    main()
