In this exercise, you will be given a few lines of code that perform a certain task (that you will have to understand) and then write an automated test that checks whether that task is performed correctly.

## Step 0

Make sure you have read the note chapters on [Testing basics](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/01testingbasics.html), [The Fields of Saskatchewan](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/02SaskatchewanFields.html) and [Test frameworks](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/03pytest.html).

If you haven't already, fork this repository and clone it on your computer.

## Step 1: Understanding the existing code
- Spend some time reading the code, try to run it and see whether you understand what's going on.
- Have you seen [`datetime`](https://docs.python.org/3.7/library/datetime.html) before?
- Play using your favourite tool (notebook, terminal, scripts) with the functions and objects used in `times.py`.

## Step 2: Writing a unit test

- Create a new file called `test_times.py` in the same directory where `times.py` is.
- Make the `overlap_time` function accessible to that file. (*Hint*: You need to `import` the file).
- Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py`
  and fill the gaps for `result` and `expected`. (For now, you can copy the output of the program as the expected value)
```python
def test_given_input():
    ... 
    result = ... 
    expected = ...
    assert result == expected
```

## Step 3: Running the tests
- run `pytest` on that directory and see whether the test is picked up by `pytest` and whether it passes. If the test doesn't pass, see if you can find what is going wrong.

## Step 4: Push to GitHub
- When you are happy with your solution (or want some feedback!):
    - Push your new code to your own fork.
    - On GitHub, open a pull request from your fork to the original repository.
    - In the description, include the text "Answers UCL-MPHY0021-21-22/RSE-Classwork#16". This will link your PR to this issue.
    - On the PR text, comment on what you found difficult or interesting, or something you learned.
- Continue with the remaining steps (7. - 9.) on [Classwork issue #16](https://github.com/UCL-MPHY0021-21-22/RSE-Classwork/issues/16)

## GROUP EXERCISE - WORKSHOP WEEK 5!!!

** Create 3 further tests
create a test each in test_times.py for:
two time ranges that do not overlap
two time ranges that both contain several intervals each
two time ranges that end exactly at the same time when the other starts
run pytest and see whether all tests are picked up by pytest and whether they pass.
fix any bugs in times.py the tests may have helped you find.

** Negative tests - Test that something that is expected to fail actually does fail
time_range may still work when end_time is before start_time, but that may make overlap_time not working as expected.
- Write a test that tries to generate a time range for a date going backward.
Modify time_range to produce an error (ValueError) with a meaningful message.
Use pytest.raises to check for that error (including the error message!) in the test.