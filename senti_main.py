from sentiment_functions import get_senti
from sentiment_functions import get_data

from CRUD_m import create_data
from CRUD_m import read_data
from CRUD_m import close_connection
from CRUD_m import get_connection


if __name__ == '__main__':
    documents = get_data('test.json')
    senti_res = get_senti(documents)
    

    connection = get_connection()

    for sigle_dic in senti_res:
        video_id = '001'
        #value = 0.7
        data = {
                'video_id': video_id,
                'doc_id': sigle_dic['Document Id'],
                'senti_score': sigle_dic['Sentiment Score'],
                'time': (sigle_dic['Time']/10000000),
                'sentence': sigle_dic['Sentence']
                }


        
        # print(data)
        table_name = 'texts_analytics'
        create_data(table_name, data, connection)
