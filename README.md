# Trustworthy Deep Learning Spring 2023 Project
## Socratic Method: Priming Large Language Models for Downstream Tasks with  ChatGPT 
To reproduce the results from the project report, clone the repo and run the ipynb notebook ```experiments_w_json_responses.ipynb```. All the data required for the results has been stored statically in the ```data``` folder. The prompts that use the OpenAI API have been commented out. If you need to prompt the language models yourself then you need to include an env file with a valid API key. 

The jupyter notebook ```question_answer_embeddings.ipynb``` contains the sentence transformer models and the cosine distance calculations that were used for plotting the similarity scores between generated explanations and the correct answer choice.
The ```experiments.ipynb``` contains most of the code which we tried out to do the first experiments and then the attempts to finetune the model. 

### Contributors
Stacey Naduvilpurakal and Wenfei Zhou in equal parts