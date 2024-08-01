# Enhancing-scripted-dialogue-systems
Research on integrating large language models with pattern-matching to improve health-coaching dialogues' adaptability and naturalness.

# Abstract
This thesis investigates the feasibility and effectiveness of integrating large language models (LLMs) and pattern-matching functions into scripted dialogue systems for health-coaching applications. The objective is to determine which integration method enhances the adaptability and naturalness of conversational agents more effectively, considering both coverage and real-time performance. By using advanced LLMs alongside efficient pattern-matching functions, the study examines their ability to address traditional scripted dialogues' limitations, which rely heavily on predefined user inputs. Experiments are conducted across zero-shot, few-shot, and fine-tuned learning paradigms using models such as Meta-Llama, Gemma, and ChatGPT. The results indicate that while pattern-matching functions offer rapid response times and closely adhere to scripts, LLMs provide superior enhancements in handling diverse and complex inputs. The comparative analysis reveals that LLMs significantly improve the conversational quality and flexibility of dialogue systems in health coaching despite their higher computational demands. This suggests a promising direction for future research and application in scripted dialogue systems.

# How To Use

Requirements:
Python [python](https://www.python.org/downloads)
Huggingface `pip install huggingface-hub`.
<br>[Huggingface Login](https://huggingface.co/docs/huggingface_hub/en/guides/cli)
Transformers `pip install transformers`

For Apple Users, MLX can also be used. Follow this link for installation and usage. [MLX](https://github.com/ml-explore/mlx).

## Pattern Matching Functions:
To run the pattern matching functions code, execute `RegExCode.py` file.

## LLMs
The research used ChatGPT API and three different open-source LLMs. All the experiments were recorded in their respective files.

### LLaMA 2 7B
To Experiment with the LLama 2 7B model, use the `llama27BChathf.py` file and pass the inputs as command line arguments.
<br>
For example,
```
python llama27BChathf.py "My goal is to walk 10000 steps every day"
```
It will also take more than one input.
```
python llama27BChathf.py "My goal is to walk 10000 steps every day" "I wanna walk 2K steps on weekdays"
```
This will automatically download the model, which is around 30GB in size, for the first time and use it for the following runs.
<br>Alternatively, you can download and use the model directly from Hugging Face to your system. [LLaMA-2-7B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)

### LLaMA 2 70B
To run this, use the `llama270bchat.py` file and enter the inputs as command line arguments.
```
python llama270bchat.py "My goal for this weekend is 4000 steps."
```
This will automatically download the model, which is around 70GB in size, for the first time and use it for the following runs.
<br>Alternatively, you can download and use the model directly from Hugging Face to your system. [LLaMA-2-70B-Chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf).

### Gemma 7B
Gemma's experiments are recorded in `gemma7bchat.ipynb` file.
<br>The experiments in the notebook were executed using Apple's MLX framework.
<br>Alternatively, one can replace the prompt and model name in any of the above two files and execute them manually.
<br> Hugging face Gemma manual installation [Gemma-7B-Instruct](https://huggingface.co/google/gemma-7b-it)

### GPT
To experiment using GPT,
openAI package needs to be installed `pip install openai`
<br>Also, OpenAI API should be purchased and access token needs to be generated.
Once the token is generated, simply run the `Gpt.py` file to experiment using ChatGPT. <br>For inputs, update the instruction variable with the new input in the file.


# Using the Fine-Tuned model
The open-source Llama2-7B model was fine-tuned using a synthetically generated dataset(Using ChatGPT-4).
The model was available on Huggingface.
Here is the link to the model: [Fine-Tuned Model](https://huggingface.co/Aadithya18/LLaMA2-7B-Chat_FinedTuned_with_health_coach_dataset)
Here is the link to the Dataset: [Dataset](https://huggingface.co/datasets/Aadithya18/Health-Coaching_Dataset)

## Using Fine-Tuned Model
To use this model, Use the model name `Aadithya18/LLaMA2-7B-Chat_FinedTuned_with_health_coach_dataset` in the code.
<br> Example usage with mlx<br>
```
!python3 -m mlx_lm.generate --model Aadithya18/LLaMA2-7B-Chat_FinedTuned_with_health_coach_dataset \
    --max-tokens 2000 \
    --prompt '<<SYS>> surround the answer in between <result> and </result> tags. <</SYS>>\
              [INST]"9000 on Sat and Sun"[/INST]'\
    --temp 0.1
```
