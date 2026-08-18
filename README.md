# Zamora_Clyde-Andrei_B1_CPE106L-4_labactivity4

# Lab Activity 4: Design Patterns and Unit Testing

## Selected Pattern: Factory Method Pattern
**Why this pattern fits the problem:** 
The Factory pattern fits perfectly here because it encapsulates the instantiation logic of our objects. Instead of the client needing to know how to initialize specific classes (`Dog`, `Cat`, `Bird`), it simply passes a string to the `AnimalFactory`. This makes the code highly modular, easy to extend (if we want to add a `Fish` class later), and extremely easy to isolate and test using automated unit tests.

## How to Run the Activity
1. **Prerequisites:** Ensure you have Python installed in your Ubuntu WSL environment.
2. **Run the Application:** 
   To see a quick manual demonstration of the Factory pattern, run:
   `python3 animal_factory.py`
3. **Run the Unit Tests:** 
   To execute the automated unit tests and verify the three test cases, run:
   `python3 -m unittest test_factory.py -v`

## Expected Output
Running the test command should output an "OK" status, indicating that all 3 test cases passed successfully.
