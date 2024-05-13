# WS_library
### Coding task with the following guidelines:<br>
Your mission, should you choose to accept it, is to write a library which takes in an array of records of variable size and splits the input to batches of records (array of arrays) suitably sized for delivery to a system which has following limits:

- maximum size of output record is 1 MB, larger records should be discarded
- maximum size of output batch is 5 MB
- maximum number of records in an output batch is 500

Input for the library is: record1, record2, record3, ... , recordn

Output is: batch1, batch2, ..., batchn where each batch is an array of records just like in the input.

The records can be assumed to be strings of variable length and they have to pass intact through the system and records should stay in the order that they arrive.

You are free to use any language of your choice. We use a lot of Python and Node.js. Delivery of the project is done either by sending the code to me, or more preferably by simply pointing to a location where we can retrieve it.

### This submission contains:
- library.py: Library class containing the core functionality and the library -method
- main.py: main function, containing the basic test case for 500+ records
- tests.py: unit tests, ensuring the size limits and record count in batch works flawlessly

You can run the code and test out the library by either running _tests.py_ or _main.py_

I always start my progress by mapping out the requirements and putting them into a flow chart, to better sketch out the core functionality of the project.


<img width="1128" alt="Screenshot 2024-05-11 at 18 15 56" src="https://github.com/rosamakinen/WS_library/assets/112611789/b70171c9-1871-4253-9519-b7910f2f81e7">
