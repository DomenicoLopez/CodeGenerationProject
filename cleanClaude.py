from openai import OpenAI
import pandas as pd
import time
import jsonlines
import numpy as np

if __name__ == '__main__':
    jsonObj = pd.read_json(path_or_buf="./claude-3-opus.jsonl", lines=True)
    i = 0
    with jsonlines.open('cleanedClaude.jsonl', mode='w') as writer:
            while i < 164:
                if jsonObj["completion"][i][0:3] == "ere":
                    index = jsonObj["completion"][i].index("\n")
                    response = jsonObj["completion"][i][index+2:]
                if jsonObj["completion"][i].find("Explanation:\n") != -1:
                    index2 = response.index("Explanation:")
                    response = response[:index2]
                print(response)
                completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                writer.write(completion)
                i = i + 1