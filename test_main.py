from CRUD_m import create_data
from CRUD_m import read_data
from CRUD_m import close_connection
from CRUD_m import get_connection


if __name__ == '__main__':
    # create_data
    connection = get_connection()
    video_id = '001'
    value = 0.7
    data =  {'ID': video_id, 'value':value}
    table_name = 'text_analytics'
    create_data(table_name, data, connection)

    # # #read_data
    # table_name = 'packop_transaction'
    # data = {'date': '2019-02-17','device_id':'123'}
    # read_data(table_name, data)
    #
    # #
    # #update_data
    # table_name = 'dp_pair'
    # data =  {'patient_id': None}
    # condition_id = {'device_id': 'SPI001'}
    # update_data(table_name, data, condition_id)
