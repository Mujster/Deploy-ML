from huggingface_hub import HfApi
import os

api = HfApi()
api.create_repo(name='my-space', repo_type='space', token=os.getenv('HF_TOKEN'))
