import sys

def main():
    arguments = sys.argv
    script_name = arguments[0]
    passed_args = arguments[1:]

    print("Script name:", script_name)
    print("Passed arguments:", passed_args)

if __name__ == "__main__":
    main()
