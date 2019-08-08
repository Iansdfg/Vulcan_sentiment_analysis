from sentiment_functions import get_senti
from sentiment_functions import get_data
<<<<<<< HEAD

from CRUD_m import create_data
from CRUD_m import read_data
from CRUD_m import close_connection
from CRUD_m import get_connection

=======
>>>>>>> 28c84762a7ffa2836db0febf6ebfcfb6e76b7ac0

if __name__ == '__main__':
    documents = get_data('test.json')
    senti_res = get_senti(documents)
<<<<<<< HEAD

    connection = get_connection()

    for sigle_dic in senti_res:
        video_id = '001'
        value = 0.7

        data = {
                'Document Id': sigle_dic['Document Id'],
                'Sentiment Score':sigle_dic['Sentiment Score'],
                'Time':sigle_dic['Time'],
                'Sentence':sigle_dic['Sentence']
                }

        print(data)
        table_name = 'text_analytics'
        create_data(table_name, data, connection)
=======

    for ele in senti_res:
        print(ele['Document Id'],ele['Sentiment Score'], ele['Time'],ele['Sentence'])
>>>>>>> 28c84762a7ffa2836db0febf6ebfcfb6e76b7ac0
