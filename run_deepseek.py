from openai import OpenAI
import pandas as pd
import time
import jsonlines
import numpy as np

# TODO: Include your API key here
api_key = 'sk-3359220fe26e467f8321ee2e20f533d4'

# Comment this code if you want to specify the key directly using the api_key parameter
client = OpenAI(api_key = api_key, base_url="https://api.deepseek.com/v1")

def get_completion(prompt, model="deepseek-chat"):
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
    i = 12
    durationTimes = []
    with jsonlines.open('data_gpt-3.5-turbo-1106_2.jsonl', mode='w') as writer:
        with jsonlines.open('timer_2.jsonl', mode='w') as timer:
            while i < 164:
                if command < 3:
                    start_time = time.time()
                    response = get_completion(jsonObj["prompt"][i])
                    duration = time.time() - start_time
                    print(duration)
                    timer.write({jsonObj["task_id"][i]: duration})
                    durationTimes.append(duration)
                    response = response.replace("```python\n", "")
                    response = response.replace("\n```", "")
                    response = response[1:]
                    print(response)
                    completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                    writer.write(completion)
                    command = command + 1
                    i = i + 1
                else:
                    command = 0
                    # time.sleep(60)
    print(np.sum(duration))
    print(np.average(duration))
