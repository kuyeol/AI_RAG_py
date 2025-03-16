# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from dotenv import load_dotenv

from openai import OpenAI

API_URL = "https://integrate.api.nvidia.com/v1"

API_KEY_REQUIRED = """
 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
  """

GEMINI_API_KEY = "AIzaSyCTFY-MBprutyvpjEodSBSBr0DaK4rcJU8"




CURRENT_MODEL = "deepseek-ai/deepseek-r1"

client = OpenAI(
    base_url=API_URL,
    api_key=API_KEY_REQUIRED
)

prompt = "HELLO WORLD"
context = "word"


def ask_gpt(prompt, context):
    response = client.chat.completions.create(
        model=CURRENT_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# 문서 내용을 컨텍스트로 활용
# context = " ".join(processed_tokens[:500])  # 500토큰으로 제한

question = "post answer retrive"

answer = ask_gpt(question, context)

print("요약 결과:", answer)

#
#
# text = "dfds"
#
# text_splitter = CharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )
# chunks = text_splitter.split_text(text)
#
# # 임베딩 생성
# embeddings = OpenAIEmbeddings()
# vector_store = FAISS.from_texts(chunks, embeddings)
#
# # 유사도 검색
# docs = vector_store.similarity_search("문서에서 중요한 키워드는?", k=2)
