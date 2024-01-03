import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of parameters")
        raise SystemExit

    directory = sys.argv[1]

    try:
        if not os.path.exists(directory):
            raise Exception("Directory path does not exist")

        files = os.listdir(directory)

        if not files:
            raise Exception(f"{directory} is empty")

        extensions = {}

        for file in files:
            file_extension = os.path.splitext(file)[1]
            if not file_extension:
                continue
            if file_extension not in extensions:
                extensions[file_extension] = 1
            else:
                extensions[file_extension] += 1

        for key, value in extensions.items():
            print(f"{key} - {value}")

    except Exception as e:
        print(e)


