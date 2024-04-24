import pandas as pd
import jsonlines

if __name__ == '__main__':
    jsonObj = pd.read_json(path_or_buf="./Gemini.jsonl", lines=True)
    i = 0
    with jsonlines.open('Gemini_2.jsonl', mode='w') as writer:
            while i < 164:
                response = jsonObj["completion"][i]
                if response[0:3] == "Here":
                    index = response.index("\n")
                    response = response[index+2:]
                    indexReturn = response.rfind("    return")
                    if response.find("\n", indexReturn) != -1:
                        indexEnd = response.index("\n", indexReturn)
                        response = response[:indexEnd]
                response = response.replace("```python\n", "")
                response = response.replace("\n```", "")
                response = response.replace("```\n", "")
                if response[0] == " ":
                    response = response[1:]
                completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                writer.write(completion)
                i = i + 1