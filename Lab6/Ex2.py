import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        raise SystemExit

    directory = sys.argv[1]

    try:
        if not os.path.exists(directory):
            raise Exception("Directory path does not exist")

        files = os.listdir(directory)

        nr = 1

        for file in files:
            old_path = os.path.join(directory, file)
            extension = os.path.splitext(file)[1]
            new_name = f"Ex{nr}{extension}"
            new_path = os.path.join(directory, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed {file} to {new_name}")
                nr += 1
            except Exception as e:
                print(f"Could not rename {file}: {e}")

    except Exception as e:
        print(e)