import wikipedia
from pip._vendor.distlib.compat import raw_input


question = raw_input("Question: ")
print(wikipedia.summary(question))
