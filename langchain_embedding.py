
from langchain.embeddings import OpenAIEmbeddings
import os

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
print("OPENAI_KEY:" + OPENAI_KEY)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
text = "Hi! It's time for the beach"
text_embedding = embeddings.embed_query(text)
print (f"Your embedding is length {len(text_embedding)}")
print (f"Here's a sample: {text_embedding[:5]}...")