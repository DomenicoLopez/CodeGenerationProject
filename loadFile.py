from humaneval import get_human_eval_plus
from openai import OpenAI

# TODO: Include your API key here
# api_key = ''

# Comment this code if you want to specify the key directly using the api_key parameter
client = OpenAI(api_key = api_key)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt }]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    for task_id, problem in get_human_eval_plus().items():
        print(task_id)
        print("\n")
        print(problem)
    prompt = f"""
    Hello World! How are you today?
    """
    response = get_completion(prompt)
    print(response)

