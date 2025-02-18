from openai import OpenAI

client = OpenAI(api_key="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")

prompt = ""

while True:
    prompt = input("You :")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        model="gpt-4o-mini"
    )

    #Print the response
    response_message = chat_completion.choices[0].message.content
    print("AI :",response_message)




