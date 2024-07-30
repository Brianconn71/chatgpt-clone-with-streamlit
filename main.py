import streamlit as st
import openai
import os
from dotenv import load_dotenv, find_dotenv


# we need to lad the env variables
load_dotenv(find_dotenv())

# need to set the openai api key
openai.api_key = os.environ["OPENAI_PASSWORD"]

