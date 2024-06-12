from utils import llama


def test_llama():
    prompt = "Help me write a birthday card for my dear friend Andrew."
    response = llama(prompt)
    print(response)


if __name__ == "__main__":
    test_llama()