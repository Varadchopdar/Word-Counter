# Define a function to count words
def count_words(text):
    # Split the text into individual words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count


# Main program
def main():
    while True:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")

        # Check if input is empty
        if not user_input.strip():
            print("Error: Empty input. Please try again.")
            continue

        # Call the word counting function
        word_count = count_words(user_input)

        # Display the word count
        print(f"The word count is: {word_count}")


if __name__ == "__main__":
    main()
    