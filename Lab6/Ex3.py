import os
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong number of parameters")
        raise SystemExit

    directory = sys.argv[1]

    try:
        total_size = 0
        if not os.path.exists(directory):
            raise Exception("Directory path does not exist")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"{directory} is not a directory")

        for (root, directories, files) in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)
                    total_size += size

                except OSError as e:
                    print(f"Could not get the size of {file}")

        print(f"Total size of files in directory {directory} is {total_size}")

    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(e)
