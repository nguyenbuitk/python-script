import argparse

def main():
    parser = argparse.ArgumentParser(description="Service Controller")

    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)

    # Add mutually exclusive arguments to the group
    group.add_argument("--start", action="store_true", help="Start the service")
    group.add_argument("--stop", action="store_true", help="Stop the service")

    # Parse arguments
    args = parser.parse_args()
    print(args)
    # Logic based on the arguments
    if args.start:
        print("Starting the service...")
    elif args.stop:
        print("Stopping the service...")

if __name__ == "__main__":
    main()