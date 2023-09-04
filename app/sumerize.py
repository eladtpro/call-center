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
