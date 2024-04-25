from openai import OpenAI
import pandas as pd
import time
import jsonlines

api_key = ''

client = OpenAI(api_key = api_key, base_url="https://api.deepseek.com/v1")

#completion function used to call the API
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
    # Calling prompts from HumanEval directly
    jsonObj = pd.read_json(path_or_buf="https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz", lines=True)
    i = 0
    durationTimes = []
    with jsonlines.open('deepseek.jsonl', mode='w') as writer:
        with jsonlines.open('deepseektimer.jsonl', mode='w') as timer:
            while i < 164:
                #making API Call and timing execution only
                start_time = time.time()
                response = get_completion(jsonObj["prompt"][i])
                duration = time.time() - start_time

                #writing to file
                timer.write({jsonObj["task_id"][i]: duration})
                completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                writer.write(completion)
                i = i + 1
