"""
Author: Sai Sangameswara Aadithya Kanduri
Version: 1.0
"""

'''
This is a sample code to demonstrate how to use the Wool class to generate a dialog using MLX and LLMs.
and how to use the LLMs to convert a free form text input into a structured output.

NOTE: If you want to run this code without mlx, 
You need to call the functions specified in the respective llm files you want to use.
Also, Need to Change the #Step 2 of Example usage to run the respective file with the input text.

NOTE: If you want to test with pattern_matching functions,
Simply call that function with the input text and store the output in a new variable.
Use this new variable in the place of the output variable in the Example usage.
(Don't need to call the get_value function as the pattern_matching functions will return the structured dictionary directly.)

The code generates a dialog based on the user's health goal and then asks the user to input the number of steps they want to walk. 
The code then uses the LLMs to convert the free form text input into a structured output 
and generates a new dialog based on the structured output. 
The code then asks the user if they want to change their daily goal and repeats the process 
and if the user wants to change their daily goal, the code generates a new dialog based on the updated health goal by repeating the process.
'''
import os
from Wool import Wool

# By default the 5 shot prompt is used with meta-llama/Llama-2-7b-chat-hf model.
# Change the model name and the prompt according to the requirement.
def generate_prompt(text, default="steps"):
        prompt = f'''python3 -m mlx_lm.generate --model meta-llama/Llama-2-7b-chat-hf\
                --max-tokens 2000\
                --prompt \'<s>[INST]\
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
                [INST]"{text}"[/INST]\
                [/INST]\'\
                --temp 0.3 >output.json'''
        print(prompt)
        return prompt

# Function to get the structured output from the LLMs
import json

def get_value():
    k = open("output.json").read()
    print(k)
    k = k.split("<result>")
    k = k[-1].split("</result>")
    output = {
        "Reply": "Nan",
        "Measurability": "0",
        "Specificity": "Nan",
        "Attainability": "0",
        "Frequency": "Nan"
    }
    try:
        json_str = k[0]
        output = json.loads(json_str)
    except:
        print("Error")
    print(output)

    return output

# Example of how to use the Wool class to generate a dialog
ob = Wool()
ob.color="red"
dialog1 = ob.dialog("Hello Robin",[("Hello", "newNode1"), ("Exit", "End")], "Start")
dialog2 = ob.dialog("How many steps you want to walk?",[('<<input type="text" value="$input">>', "newNode2"), ("Exit","End")], "newNode1")
dialog4 = ob.dialog("",[], "End")
new_dialog = open("new_dialog.wool", "w")
new_dialog.write(dialog1)
new_dialog.write(dialog2)
new_dialog.write(dialog4)

# Steps of How to take the free form text input and convert it into a structured output using LLMs
# 1. Take input and Generate a prompt for the LLMs
input_text = input("Enter you health goal: ")
prompt = generate_prompt(input_text)

# 2. Run the prompt using the LLMs
os.system(prompt)

# 3. Get the output from the LLMs
ob.value = get_value()["Measurability"]

# 4. Generate a new dialog using the structured output
dialog3 = ob.dialog(f"Okay let's start walking {ob.value} steps from today",[("Okayy!", "NewNode3"),("Exit","End")], "newNode2")
new_dialog.write(dialog3)

# 5. Run the new dialog
dialog5 = ob.dialog("You have walked 8000 steps today. That's better than your daily goal. Great job",[("Thank you", "newNode4"), ("Exit", "End")], "newNode3")
new_dialog.write(dialog5)

# 6. Run the new dialog
dialog6 = ob.dialog("Do you want to change your daily goal?",[("Yes", "changeGoal"), ("No", "NewNode5"), ("Exit", "End")], "newNode4")
new_dialog.write(dialog6)

# 7. Run the new dialog and repeat the process from setp 1
dialog7 = ob.dialog("What is your new goal?",[('Steps =  <<input type="text" value="$num_of_steps">>', "newNode6"), ("Exit","End")], "changeGoal")
new_dialog.write(dialog7)

input_text = input("Enter your updated health goal: ")
prompt = generate_prompt(input_text)

os.system(prompt)
ob.value = get_value()["Measurability"]
dialog8 = ob.dialog(f"Okay let's start walking {ob.value} steps from today",[("Exit","End")], "newNode6")
new_dialog.write(dialog8)
new_dialog.close()

# The output of the complete code will be a new_dialog.wool file 
# which contains the dialog generated based on the user's health goal and the updated health goal.

# For an example of inputs, I used the following inputs:
# Enter you health goal: I want to set my goal to walk 2000 steps daily
# Enter your updated health goal: I want to update my goal to walk 10000 steps daily

# The outputs generated by the LLM are as follows:
# For the first input:

# <result>{
#     "Measurability": "2000",
#     "Specificity": "steps",
#     "Attainability": "8",
#     "Frequency": "daily"
# }
# </result>

# For the second input:
# <result>{
#     "Measurability": "10000",
#     "Specificity": "steps",
#     "Attainability": "7",
#     "Frequency": "daily"
# }
# </result>

# Refer to the new_dialog.wool file for the complete dialog generated by the code.