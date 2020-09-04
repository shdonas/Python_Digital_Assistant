import wolframalpha
from pip._vendor.distlib.compat import raw_input

# appID/apiKey from WolframAlpha
api_id = "JH5JK7-E87Y6G3W8K"


# this app will return response from the WolframAplha
def api_response(question):
    # client request to connect to WolframAplha using the api key
    client = wolframalpha.Client(api_id)

    # response from the WRA based on the client question
    response = client.query(question)
    return response


# this app will fetch answer using the response from WRA server
def fetch_ans(api_response):
    answer = next(api_response.results).text
    print(answer)
    return answer


if __name__ == '__main__':
    print("Hello Friends!!")

    question = raw_input("Question: ")
    fetch_ans(api_response(question))
