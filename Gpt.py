import openai

# Set your API key here
openai.api_key = "sk-proj-m654ueDo3URP0ibr32vVT3BlbkFJM2LfYU7BIzpM31LFZAeL"

# Define the prompts you want to use
prompt = "For the following instruction, For the given message, generate a response in JSON format that includes the following information: \
    {Measurability: \"value\", Specificity: \"value\", Attainability: \"value\", Frequency:\"value\"} \
    Specificity should be the activity mentioned. All walking activities represented with \"steps\". If the specificity is not provided, the response should include Specificity: \"steps\" \
    Measurability should be a single value, the value of the goal. If the measurability is not provided, the response should include Measurability: \"0\" . \
    If the given measurability is a range, use the lower boundary. \
    Frequency should be one of these values: [\"daily\", \"Monday - Friday\", \"Monday - Saturday\", \"weekly\", \"weekend\"]. \
    If terms like weekdays occur, use \"Monday - Friday\". If terms like \"Saturday and Sunday\" occur, use \"weekend\". \
    If any different frequency is observed, map it to the appropriate from the list or make it daily. If the frequency is not provided, the response should include Frequency: \"daily\" \
    The attainability value should be given on a scale of 1 to 10 based on the goal's specificity, measurability, and frequency, and calculated its attainability. \
   "

# Function to generate responses from ChatGPT
def get_responses(prompt, instruction):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can use other models like text-davinci-002
        messages=[{"role": "system", "content": prompt},
                  {"role": "user", "content": instruction},],
    ) 
    return response.choices[0]

# Get and print responses
instruction = "I wanna walk 1000 steps daily."
responses = get_responses(prompt, instruction)
print(responses.message.content)