In this project I tested a few files in the EvalPlus Github.

In loadfile, I was able to run Open AI using the API key. Temperature is set to zero. You can try as well with your own key you received in class or one from a different LLM and modify the prompting function. Ask me for my key if you need. I will be testing Github Copilot for the project.

In loadfile, I was able to print out the dataset. This is to give a sense of how we can manipulate the json data which you can call by tag and work directly from the json.

In evaluate_coverage, is where we can create the code and evaluate it against the tests. The code gets saved into a file called tmp_src. And it gets evaluated in different functions. You should evaluate it docker.

The next files to incorporate is evaluate_runtime from the EvalPlus project where we will clock the code. And we will have to create our own files for different parameters we want to test for like LOC.




