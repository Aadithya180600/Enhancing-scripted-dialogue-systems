from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

def llama2_70b_chat_0_shot(input, model, tokenizer):

        default = "steps"

        inputs = tokenizer.encode(
        f'''
        <<sys>>For the given message, generate a JSON response in following format
        <result>
        {{ Measurability: "value",
                Specificity: "value",
                Attainability: "value",
                Frequency:"value"}} </result>
        surround the answer in between <result> and </result> tags.<<sys>>\
        [INST] {input[0]} [/INST]\
        ''', return_tensors="pt")
        outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.5)
        print(tokenizer.decode(outputs[0]))
        outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.3)
        print(tokenizer.decode(outputs[0]))
        outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.75)
        print(tokenizer.decode(outputs[0]))

def llama2_70b_chat_1_shot(input, model, tokenizer):
        for i in input:
        
                default = "steps"
        
                inputs = tokenizer.encode(
                f'''
                <<sys>>
                surround the answer in between <result> and </result> tags.
                <<sys>>\
                [INST]"the goal for this week is to walk 2,000 steps per day every day from Monday to Saturday." [/INST]\
                "<result>{{ \
                        "Measurability": "2000",\
                        "Specificity": "steps",\
                        "Attainability": "8",\
                        "Frequency": "Monday - Saturday"\
                }}</result>"\
                [INST] {i} [/INST]\
                ''', return_tensors="pt")

                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.1)
                print("At temp = 0.1", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.3)
                print("At temp = 0.3", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.5)
                print("At temp = 0.5", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.75)
                print("At temp = 0.75", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=1)
                print("At temp = 1.0", tokenizer.decode(outputs[0]))
                print()

def llama2_70b_chat_2_shot(input, model, tokenizer):
        for i in input:
        
                default = "steps"
        
                inputs = tokenizer.encode(
                f'''
                <<sys>>
                surround the answer in between <result> and </result> tags.
                <<sys>>\
                [INST]"the goal for this week is to walk 2,000 steps per day every day." [/INST]\
                "<result>{{ \
                        "Measurability": "2000",\
                        "Specificity": "steps",\
                        "Attainability": "8",\
                        "Frequency": "daily"\
                }}</result>"\
                [INST]"I Wanna TRY between 1,000 to 2000 from Monday to Friday"[/INST]\
                "<result>{{ \
                        "Measurability": "1000",\
                        "Specificity": "steps",\
                        "Attainability": "8",\
                        "Frequency": "Monday - Friday"\
                }}</result>"\
                [INST] {i} [/INST]\
                ''', return_tensors="pt")

                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.1)
                print("At temp = 0.1", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.3)
                print("At temp = 0.3", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.5)
                print("At temp = 0.5", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.75)
                print("At temp = 0.75", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=1)
                print("At temp = 1.0", tokenizer.decode(outputs[0]))
                print()

def llama2_70b_chat_5_shot(input, model, tokenizer):
        for i in input:
                print("Input: ", i)
                print()
        
                default = "steps"
        
                inputs = tokenizer.encode(
                f'''
                <<SYS>> surround the answer in between <result> and </result> tags.
                If the specificity is not available, use {default} as the default value.\
                If the measurability is not available, use 0 as the default value.\
                If the frequency is not available, use "daily" as the default value. \
                <</SYS>>\
                [INST]"the goal for this week is to walk 2,000 steps per day every day." [/INST]\
                "<result>{{ \
                        "Measurability": "2000",\
                        "Specificity": "steps",\
                        "Attainability": "8",\
                        "Frequency": "daily"\
                }}</result>"\
                [INST]"I Wanna TRY between 1,000 to 2000 from Monday to Friday"[/INST]\
                "<result>{{ \
                        "Measurability": "1000",\
                        "Specificity": "steps",\
                        "Attainability": "8",\
                        "Frequency": "Monday-Friday"\
                }}</result>"\
                [INST]"Hi! Ive been struggling a bit lately, so lets aim for a more achievable goal of 3,000 steps per day."[/INST]\
                "<result>{{ \
                        "Measurability": "3000", \
                        "Specificity": "steps",\
                        "Attainability": "5",\
                        "Frequency": "daily"\
                }}</result>"\
                [INST]"Good morning! Im feeling really determined this week. Lets push for 9,000 steps Sunday through Sunday."[/INST] \
                "<result>{{ \
                        "Measurability": "9000",\
                        "Specificity": "steps",\
                        "Attainability": "10",\
                        "Frequency": "daily"\
                }}</result>" \
                [INST] "15,000 steps....."[/INST]\
                "<result>{{ \
                        "Measurability": "15000", \
                        "Specificity": "steps",\
                        "Attainability": "7",\
                        "Frequency": "daily"\
                }}</result>"\
                [INST] {i} [/INST]\
                ''', return_tensors="pt")

                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.1)
                print("At temp = 0.1", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.3)
                print("At temp = 0.3", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.5)
                print("At temp = 0.5", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=0.75)
                print("At temp = 0.75", tokenizer.decode(outputs[0]))
                outputs = model.generate(inputs, max_new_tokens=2000, temperature=1)
                print("At temp = 1.0", tokenizer.decode(outputs[0]))
                print()
                print()

# Check if command line arguments are provided
if len(sys.argv) > 1:
    # Remove the script name from the arguments
    args = sys.argv[1:]

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-chat-hf")
    
    # Pass the arguments to the method
    llama2_70b_chat_0_shot(args, model, tokenizer)
    llama2_70b_chat_1_shot(args, model, tokenizer)
    llama2_70b_chat_2_shot(args, model, tokenizer)
    llama2_70b_chat_5_shot(args, model, tokenizer)
else:
    print("No command line arguments provided.")