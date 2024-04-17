from openai import OpenAI
import pandas as pd
import time
import jsonlines
import numpy as np

# TODO: Include your API key here
api_key = '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'

# Comment this code if you want to specify the key directly using the api_key parameter
client = OpenAI(api_key = api_key)

def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [
        {"role": "system",
         "content": "You are an intelligent programmer. You must complete the python function given to you by the user. And you must follow the format they present when giving your answer!"},
        {"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    jsonObj = pd.read_json(path_or_buf="https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz", lines=True)
    command = 0
    i = 0
    durationTimes = []
    with jsonlines.open('data_gpt-3.5-turbo-1106.jsonl', mode='w') as writer:
        while i < 164:
            if command < 4:
                start_time = time.time()
                response = get_completion(jsonObj["prompt"][i])
                duration = time.time() - start_time
                print(duration)
                durationTimes.append(duration)
                response = response.replace("```python\n", "")
                response = response.replace("\n```", "")
                print(response)
                completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                writer.write(completion)
                command = command + 1
                i = i + 1
            else:
                command = 0
                time.sleep(90)
    print(np.sum(duration))
    print(np.average(duration))
