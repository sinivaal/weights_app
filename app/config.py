import os

#How to set env variables
def db_config(params):
    prod_db = {'host' : os.environ.get('DB_HOST'),
               'user' : os.environ.get('DB_USER'),
               'password' : os.environ.get('DB_PW'),
               'dbname' : os.environ.get('DB_NAME'),
               'port' : os.environ.get('DB_PORT')}
    local_db = {'host' : os.environ.get('DB_HOST'),
               'user' : os.environ.get('DB_USER'),
               'password' : os.environ.get('DB_PW'),
               'dbname' : os.environ.get('DB_NAME'),
               'port' : os.environ.get('DB_PORT')}
    
    if params == 1:
        return prod_db
    elif params == 2:
        return local_db


def hx_config_test():
    hx_711 = [{
        'GPIO_1' : 5,
        'GPIO_2' : 6,
        'scale_id_1' : 5,
        'scale_id_2' : 6,
        'cal_1_a' : 535,
        'cal_1_b' : 35,
        'cal_2_a' : 5643,
        'cal_2_b' : 32253,
        'sample_id_1' : 5,
        'sample_id_2' : 6
        },
        {
        'GPIO_1' : 5,
        'GPIO_2' : 6,
        'scale_id_1' : 5,
        'scale_id_2' : 6,
        'cal_1_a' : 535,
        'cal_1_b' : 35,
        'cal_2_a' : 5643,
        'cal_2_b' : 32253,
        'sample_id_1' : 5,
        'sample_id_2' : 6
        }]
    
    return hx_711

