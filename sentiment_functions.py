from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials


def get_senti(documents):

    subscription_key = "f56de4b340b6472f951a0b5b7cfc8f8c"
    credentials = CognitiveServicesCredentials(subscription_key)

    text_analytics_url = "https://westus2.api.cognitive.microsoft.com/"
    text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)

    response = text_analytics.sentiment(documents=documents)
    res = []
    for pos, document in enumerate(response.documents):
        dic = {}
        dic["Document Id"] = int(document.id)
        dic["Sentence"] = documents[pos]['text']
        dic["Sentiment Score"] = float("{:.2f}".format(document.score))
        dic["Time"] = documents[pos]['time']
        res.append(dic)
        # print("Document Id: ", document.id, ", Sentiment Score: ",
        #       "{:.2f}".format(document.score),", Time: ",  documents[pos]['time'])
        #
    return res
