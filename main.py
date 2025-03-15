def main(username) -> str:
    """
    Function to print hello world message with username
    Args:
        username (str): Name of the user to greet
    """
    from _tasks.hello_world import greet_user
    return greet_user(username)

# Example usage
if __name__ == "__main__":
    # Test the function
    main("John")