# LangChain HuggingFace Demo

This project demonstrates how to use [LangChain](https://python.langchain.com/) with [HuggingFace](https://huggingface.co/) models for question answering and summarization tasks in Python.

## Features

- Ask questions interactively using a HuggingFace LLM (`bigscience/bloomz-560m`)
- Experiment with summarization and other tasks in a notebook

---

## Getting Started

### 1. Install dependencies

```sh
pip install python-dotenv langchain langchain-huggingface transformers
```

### 2. Get your HuggingFace API token

See [How to get your HuggingFace token](#how-to-get-your-huggingface-api-token) below.

### 3. Set up your `.env` file

Create a file named `.env` in the project folder and add:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## Usage


### Run the main script

```sh
python main.py
```

You will be prompted to enter your question. The model will generate an answer.

---

## Demo Example

Here is a sample run of the script:

```
$ python main.py
Enter your question: What is the capital of India?
{'text': 'Q: What is the capital of India?\nA: The capital of India is New Delhi.'}
```

You can ask any question and the model will respond accordingly.

---

### Use the Jupyter Notebook

The `notebook.ipynb` file demonstrates similar functionality and lets you experiment with summarization and other tasks.

---

## How to get your HuggingFace API token

1. Go to [HuggingFace.co](https://huggingface.co/)
2. Sign up or log in.
3. Click your profile icon > **Settings** > **Access Tokens**
4. Click **New token**, give it a name, and copy the token.

---

## More Details

For a detailed explanation of how `main.py` works, including parameter descriptions, model choices, and more, see  
👉 [How main.py works and model options](Readme_mainpy.md)

---

## License

This project is for educational purposes.