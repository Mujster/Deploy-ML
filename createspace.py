from huggingface_hub import HfApi
import os

def create_space():
    api = HfApi()
    api.create_repo(repo_id='my-space', repo_type='space', token=os.getenv('HF_TOKEN'))

if __name__ == "__main__":
    create_space()
