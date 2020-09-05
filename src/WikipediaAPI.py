import wikipedia
from pip._vendor.distlib.compat import raw_input


class WikipediaAPI:
    @staticmethod
    def wikiResponse(question):
        wikipedia.set_lang("en")
        return wikipedia.summary(question, sentences=2)

    # if __name__ == '__main__':
    #     while True:
    #         question = raw_input("Question: ")
    #         print(wikiResponse(question))
