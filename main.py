def greet_user(username) -> str:
    """
    Function to print hello world message with username
    Args:
        username (str): Name of the user to greet
    """
    from _tasks.hello_world import greet_user
    return greet_user(username)  # Call the imported function to get the greeting message


# Example usage
if __name__ == "__main__":
    # Test the function
    greet_user("John") 