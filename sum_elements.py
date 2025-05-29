MAX = 100

def calculate_sum(arr):
   return sum(arr)

def get_integer(prompt, min_value=None, max_value=None):
   while True:
      try:
         value = int(input(prompt))
         if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
            print(f"Please enter a number between {min_value} and {max_value}.")
            continue
         return value
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   print("=== Sum Elements Program ===")
   n = get_integer(f"How many numbers do you want to sum? (1-{MAX}): ", 1, MAX)

   arr = []
   print(f"Enter {n} integers separated by spaces:")
   while True:
      try:
         user_input = input("> ").strip()
         arr = [int(x) for x in user_input.split()]
         if len(arr) != n:
            print(f"Please enter exactly {n} integers.")
            continue
         break
      except ValueError:
         print("Invalid input. Please enter only integers separated by spaces.")

   total = calculate_sum(arr)
   print(f"\nSum of the numbers: {total}")

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
