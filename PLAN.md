For our notice about plan and etc... 

 1. Read and make a plan
 2. Write code
 3. Revision and fix bugs

1. MONDAY: study assignment, sketches.
2. TUESDAY: write tests and functions.
3. WEDNSDAY: edge check the system's functionality.
4. THURSDAY: reserv day.

# Skills Assessed
Understanding and following code specifications
Reading tests
Creating classes with attributes and instance methods
Importing modules
Working with attributes that are lists of instances
Implementing instance methods that interact with other instances and objects
Implementing inheritance
Overriding methods from superclasses and Object


# General informtion:

- Each person is to register online as a vendor. Also, they should be able to add a list of things as their inventory.
- envision an app where vendors can swap items between different inventories
- read the tests to help understand what each wave is asking us to do
- pay close attention to the requirements to make sure the requirements are all being applied.
- remember that the test cases for each wave are NOT exhaustive.
- it's important to understand what a wave is asking us to do, and to try to devise logically consistent behaviors
- be sure NOT to modify the behaviors of any existing tests other than those that explicitly ask us to complete them.

**Requirements:**

1. 6 Waves
2. finish writing some of the tests! Waves 1, 3, 6. 
- Watch for the tests with raised Exceptions and the comment with what we're looking for
- When unskipping, do NOT remove the @pytest mark. integration_test decorator
- run **integration tests after  the unit tests**
3. The only methods you are allowed to import are from the uuid module:
- add the import for uuid yourself
- you are not allowed to import any other modules.
- Do not use built-in global functions such as min, max, sum, etc
Note that you are still allowed to implement your own versions of any of these functions and then use them!
4. add additional tests if that helps you understand the requirements
5. Review the [code coverage exercise](https://github.com/adaGold/code-coverage-exercise) on how to use `pytest-cov` to generate a code coverage report. We will need to change the directory where the application code is located from `student` to `swap_meet`.
    
    `pytest --cov=swap_meet --cov-report html --cov-report term`
    
6. consider how `swap_best_by_category` and `swap_first_item` might be able to make use of `swap_items`
7. **optional Enhancements**




