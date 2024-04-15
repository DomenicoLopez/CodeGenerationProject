from openai import OpenAI
import pandas as pd
import time
import jsonlines

# TODO: Include your API key here
api_key = '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'

# Comment this code if you want to specify the key directly using the api_key parameter
client = OpenAI(api_key = api_key)

def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt }]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

# def get_human_eval() -> Dict[str, Dict]:
#     """Get HumanEval from OpenAI's github repo and return as a list of parsed dicts.
#
#     Returns:
#         List[Dict[str, str]]: List of dicts with keys "prompt", "test", "entry_point"
#
#     Notes:
#         "task_id" is the identifier string for the task.
#         "prompt" is the prompt to be used for the task (function signature with docstrings).
#         "test" is test-cases wrapped in a `check` function.
#         "entry_point" is the name of the function.
#     """
#     # Check if human eval file exists in CACHE_DIR
#     human_eval_path = os.path.join(CACHE_DIR, "HumanEval.jsonl")
#     make_cache(
#         "https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz",
#         human_eval_path,
#     )
#
#     human_eval = open(human_eval_path, "r").read().split("\n")
#     human_eval = [json.loads(line) for line in human_eval if line]
#
#     # Handle 115_max_fill.py to make its docstring well-formed
#     human_eval[115]["prompt"] = "import math\n" + human_eval[115]["prompt"].replace(
#         "import math\n", ""
#     )
#
#     return {task["task_id"]: task for task in human_eval}

if __name__ == '__main__':
    jsonObj = pd.read_json(path_or_buf="https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz", lines=True)
    command = 0
    i = 0
    with jsonlines.open('data1106.jsonl', mode='w') as writer:
        while i < 164:
            if command < 4:
                writer.write({'task_id': jsonObj["task_id"][i], 'completion': get_completion(jsonObj["prompt"][i])})
                command = command + 1
                i = i + 1
            else:
                command = 0
                time.sleep(60)


    # data = [{'task_id': jsonObj["task_id"][i], 'completion': get_completion(jsonObj["prompt"][i])} for i in range(163)];
    # with jsonlines.open('data.jsonl', mode='w') as writer:
    #     for item in data:
    #         writer.write(item)

    # response = get_completion(jsonObj["prompt"][23])
    # print(response)

    # print(jsonObj["task_id"][1])
    # for task_id, problem in get_human_eval_plus().items():
    #     print(task_id)
    #     print("\n")
    #     print(problem)
    # prompt = f"""
    # Hello World! How are you today?
    # """

