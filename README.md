# Sample Python Chatbot Using Chatterbot

This is a python code that creates and runs a self-learning chatbot, using the `chatterbot` library in python. In order to make it work, before you need to install `chatterbot`:

```pip3 install chatterbot==1.0.4 pytz```

Then, in order to train the chatbot on specific datasets, run:

```python3 chatbot.py --train path/to/input/datasets```

For example, we can use the sample dataset from the `train_data` folder:
```python3 chatbot.py --train ./train_data/english/```

If you want to only run the chatbot without training it on any data manually, then avoid the `--train` argument:
```python3 chatbot.py```

