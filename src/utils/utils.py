class Utils:
    """
    Static helper class for console input validation.
    """

    @staticmethod
    def get_int(prompt: str) -> int:
        """Repeatedly asks for an integer until valid."""
        valid = False
        value = 0
        while not valid:
            try:
                user_input = input(prompt)
                value = int(user_input)
                valid = True
            except ValueError:
                print("Error: Please enter a valid integer.")
        return value

    @staticmethod
    def get_float(prompt: str) -> float:
        """Repeatedly asks for a float until valid."""
        valid = False
        value = 0.0
        while not valid:
            try:
                user_input = input(prompt)
                value = float(user_input)
                # Check for negative check if needed, but keeping it generic here.
                if value < 0:
                    print("Warning: Value is negative.")
                valid = True
            except ValueError:
                print("Error: Please enter a valid number.")
        return value

    @staticmethod
    def get_non_empty_str(prompt: str) -> str:
        """Repeatedly asks for a string until non-empty."""
        valid = False
        value = ""
        while not valid:
            value = input(prompt).strip()
            if value:
                valid = True
            else:
                print("Error: Input cannot be empty.")
        return value
