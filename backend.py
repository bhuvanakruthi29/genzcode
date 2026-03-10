from groq import Groq

client = Groq(
    api_key="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"
)

def get_ai_response(user_input):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content