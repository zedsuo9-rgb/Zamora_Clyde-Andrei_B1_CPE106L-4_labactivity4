# Zamora_Clyde-Andrei_B1_CPE106L-4_labactivity4

# Lab Activity 4: Design Patterns and Unit Testing

## Selected Pattern: Factory Method Pattern
**Why this pattern fits the problem:** 
The Factory pattern fits perfectly here because it encapsulates the instantiation logic of our objects. Instead of the client needing to know how to initialize specific classes (`Dog`, `Cat`, `Bird`), it simply passes a string to the `AnimalFactory`. This makes the code highly modular, easy to extend, and extremely easy to isolate and test using automated unit tests. 

## How to Run the Activity
1. **Prerequisites:** Ensure you have Python installed in your Ubuntu WSL environment.
2. **Run the Interactive Application:** 
   To run the main program, execute the following command in your terminal:
   `python3 animal_factory.py`
   The program will prompt you 3 times to enter an animal type (e.g., dog, cat, or an invalid type like dragon) and will output the result or catch the error.
3. **Run the Unit Tests:** 
   To execute the automated unit tests and verify the code programmatically, run:
   `python3 -m unittest test_factory.py -v`

## Expected Outputs

### 1. Application Output (`animal_factory.py`)
When you run the main script and input "dog", "cat", and "dragon", the terminal will display:
```text
case 1:
Enter an animal type: dog
Case 1: Created a Dog that says: Woof!

case 2:
Enter an animal type: cat
Case 2: Created a Cat that says: Meow!

case 3:
Enter an animal type: dragon
Case 3: Error - Unknown animal type: dragon
