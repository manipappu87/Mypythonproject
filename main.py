"""Simple command-line app that echoes user input."""


def main() -> None:
    """Prompt the user for text and print it back."""
    user_input = input("Enter something: ")
    print(user_input)


if __name__ == "__main__":
    main()
