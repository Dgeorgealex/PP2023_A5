import sys
import os

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        raise SystemExit

    directory = sys.argv[1]
    extension = sys.argv[2]

    try:
        if not os.path.exists(directory):
            raise Exception("Directory path does not exist")

        for filename in os.listdir(directory):   # Can throw NotADirectoryError
            if filename.endswith(extension):
                file_path = os.path.join(directory, filename)

                try:
                    f = open(filename)
                    data = f.read()
                    print(f"{filename}:")
                    print(data)

                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    except Exception as e:
        print(e)
