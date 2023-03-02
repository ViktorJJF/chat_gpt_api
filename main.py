import openai

openai.api_key = "YOUR_ULTRA_SECRET_API_KEY"

message_convo = []


def respond(input_text):
    message_convo.append({"role": "user", "content": input_text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_convo
    )
    response_message = response["choices"][0]["message"]
    message_convo.append(response_message)
    return response_message["content"]


while True:
    text = input("User: ")
    print(f"GPT: {respond(text)}")
