# How `main.py` Works

## Overview

`main.py` is the main script for interacting with a HuggingFace language model using LangChain. It prompts the user for a question, sends it to the model, and prints the response.

## Code Walkthrough

```python
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="bigscience/bloomz-560m",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.01},
)

prompt = PromptTemplate.from_template("Q: {text}\nA:")

chain = prompt | llm

user_question = input("Enter your question: ")
result = chain.invoke({"text": user_question})
print(result)
```

### Parameters Explained

- **model_id**:  
  The HuggingFace model used. Here, `bigscience/bloomz-560m` is a free, open-source model suitable for basic Q&A.

- **task**:  
  `"text-generation"` tells the pipeline to generate text based on the prompt.

- **pipeline_kwargs**:
  - `max_new_tokens`:  
    Limits the number of tokens (words/pieces) generated in the response. Higher values give longer answers.
  - `temperature`:  
    Controls randomness. Lower values (e.g., 0.01) make responses more deterministic and focused. Higher values (e.g., 0.7) make responses more creative and varied.

### Prompt Template

The prompt is formatted as:
```
Q: {text}
A:
```
This helps guide the model to answer questions.

---

## Model Choices

You can use other HuggingFace models by changing `model_id`.  
Some popular options:

- `bigscience/bloomz-560m` (free, open-source)
- `google/flan-t5-base` (free, open-source)
- `meta-llama/Llama-2-7b-chat-hf` (may require special access)
- `gpt2` (free, but limited capabilities)

> **Note:** Some models require approval or payment. Always check the [model page](https://huggingface.co/models) for license and usage details.

---

## Tips

- For more creative answers, increase `temperature` (e.g., 0.7).
- For longer answers, increase `max_new_tokens`.
- Try different models for different tasks (summarization, translation, etc.).

---

## Further Reading

- [LangChain Documentation](https://python.langchain.com/docs/)