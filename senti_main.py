from sentiment_functions import get_senti
from sentiment_functions import get_data

if __name__ == '__main__':
    documents = get_data('test.json')
    senti_res = get_senti(documents)

    for ele in senti_res:
        print(ele['Document Id'],ele['Sentiment Score'], ele['Time'],ele['Sentence'])
