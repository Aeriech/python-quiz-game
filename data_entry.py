def get_int_input(prompt: str):
    while True:
        try:
            amount = int(input(prompt).strip())
            if amount <= 0:
                raise ValueError("❌ Input must be a non-negative non-zero value.")
            return amount
        except ValueError as e:
            print(e)
            
        except KeyboardInterrupt:
            print("\n⚠️ Program interrupted by user.")
            raise  # Exit the program
            
def get_string_input(prompt: str, valid_choices=None) -> str:
    if valid_choices is None:
        valid_choices = []

    while True:
        try:
            str_input = input(prompt).strip()  # Remove leading/trailing spaces
            
            if not str_input:
                raise ValueError("❌ Input cannot be empty.")
            
            if not valid_choices:
                return str_input  # No restrictions, return any input
            
            if str_input.upper() not in [choice.upper() for choice in valid_choices]:
                raise ValueError(f"❌ Invalid choice. Please choose from: {', '.join(valid_choices)}")
            
            return str_input  # Return valid choice

        except ValueError as e:
            print(e)

        except KeyboardInterrupt:
            print("\n⚠️ Program interrupted by user.")
            raise  # Exit the program
