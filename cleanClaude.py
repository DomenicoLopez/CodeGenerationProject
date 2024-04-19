import pandas as pd
import jsonlines

if __name__ == '__main__':
    jsonObj = pd.read_json(path_or_buf="./claude-3-opus.jsonl", lines=True)
    i = 0
    with jsonlines.open('cleanedClaude_2.jsonl', mode='w') as writer:
            while i < 164:
                if jsonObj["completion"][i][0:3] == "ere":
                    index = jsonObj["completion"][i].index("\n")
                    response = jsonObj["completion"][i][index+2:]
                    indexReturn = response.rfind("    return")
                    if response.find("\n", indexReturn) != -1:
                        indexEnd = response.index("\n", indexReturn)
                        response = response[:indexEnd]
                print(response)
                completion = {'task_id': jsonObj["task_id"][i], 'completion': response}
                writer.write(completion)
                i = i + 1