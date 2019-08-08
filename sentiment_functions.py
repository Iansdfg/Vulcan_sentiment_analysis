from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import json


def get_data(jason_file):
    with open(jason_file) as json_file:
        output_data = []
        input_data = json.load(json_file)
        count = 1
        for input_datum in input_data:
            output_datum = {}
            output_datum['id'] = count
            count += 1
            output_datum['text'] = input_datum['DisplayText']
            output_datum['time'] = input_datum['Offset']
<<<<<<< HEAD
            # time:
=======
>>>>>>> 28c84762a7ffa2836db0febf6ebfcfb6e76b7ac0
            output_data.append(output_datum)
    return output_data


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
    return res
