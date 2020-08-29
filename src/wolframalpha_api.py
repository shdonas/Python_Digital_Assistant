import wolframalpha
from pip._vendor.distlib.compat import raw_input


def api_response(api_Id, question):
    api_id = "JH5JK7-E87Y6G3W8K"
    client = wolframalpha.Client(api_id)
    response = client.query(question)
    return response


def fetch_ans(api_response):
    answer = next(api_response.results).text
    print(answer)
    return answer


if __name__ == '__main__':
    api_id = "JH5JK7-E87Y6G3W8K"
    print("Hello World")

    question = raw_input("Question: ")
    fetch_ans(api_response(api_id, question))
