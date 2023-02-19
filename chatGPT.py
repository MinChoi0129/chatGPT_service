import openai

# Set up the OpenAI API client
with open('api_key', 'r') as f:
    openai.api_key = f.readline()

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input()

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)