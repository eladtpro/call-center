import openai


def extract_keywords(text,model_name):
    response = openai.Completion.create(
        engine=model_name,
        prompt=f'Extract keywords from: {text}',
        max_tokens=1024,
        n=1,
        temperature=0.5,
        stop=None
    )

    result = response.choices[0].text
    return result.strip().replace("Keywords:","**:blue[Keywords:]**")

def chat_completion(text, question):
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        messages=[
            {"role": "system", "content": text},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']


def ask_model(text,request,model_name):
    response = openai.Completion.create(
        engine=model_name,
        prompt=f'{request}, Context: {text}',
        max_tokens=1024,
        n=1,
        temperature=0.5,
        stop=None

    )

    result = response.choices[0].text
    return f'**:blue[Answer:]** {result.strip()}'
