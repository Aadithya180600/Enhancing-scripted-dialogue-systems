# Enhancing-scripted-dialogue-systems
Research on integrating large language models with pattern-matching to improve health-coaching dialogues' adaptability and naturalness.

# Abstract
This thesis investigates the feasibility and effectiveness of integrating large language models (LLMs) and pattern-matching functions into scripted dialogue systems for health-coaching applications. The objective is to determine which integration method enhances the adaptability and naturalness of conversational agents more effectively, considering both coverage and real-time performance. By using advanced LLMs alongside efficient pattern-matching functions, the study examines their ability to address traditional scripted dialogues' limitations, which rely heavily on predefined user inputs. Experiments are conducted across zero-shot, few-shot, and fine-tuned learning paradigms using models such as Meta-Llama, Gemma, and ChatGPT. The results indicate that while pattern-matching functions offer rapid response times and closely adhere to scripts, LLMs provide superior enhancements in handling diverse and complex inputs. The comparative analysis reveals that LLMs significantly improve the conversational quality and flexibility of dialogue systems in health coaching despite their higher computational demands. This suggests a promising direction for future research and application in scripted dialogue systems.

# How To Use

Requirements:
Python [python](https://www.python.org/downloads)
Huggingface `pip install huggingface-hub`
[Huggingface Login](https://huggingface.co/docs/huggingface_hub/en/guides/cli)
Transformers `pip install transformers`

For Apple Users, MLX can also be used. Follow this link for installation and usage. [MLX](https://github.com/ml-explore/mlx).

## Pattern Matching Functions:
To run the pattern matching functions code, execute `RegExCode.py` file.

## LLMs
ChatGPT API and three different open-source LLMs were used in the research. All the experiments were recorded in their respective files.

### LLaMA 2 7B
To Experiment with the LLama 2 7B model, use the `llama27BChathf.py` file.
This will automatically download the model, which is around 30GB in size, for the first time and use it for the following runs.
Alternatively, you can download and use the model directly from Hugging Face to your system. [LLaMA-2-7B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)

### LLaMA 2 70B
