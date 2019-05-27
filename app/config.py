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
        'scale_id_1' : 1,
        'scale_id_2' : 2,
        'cal_1_a' : 128,
        'cal_1_b' : 2658,
        'cal_2_a' : 51235,
        'cal_2_b' : 195346,
        'sample_id_1' : 5,
        'sample_id_2' : 6
        },
        {
        'GPIO_1' : 6,
        'GPIO_2' : 7,
        'scale_id_1' : 3,
        'scale_id_2' : 4,
        'cal_1_a' : 7301,
        'cal_1_b' : 998,
        'cal_2_a' : 5643,
        'cal_2_b' : 32253,
        'sample_id_1' : 7,
        'sample_id_2' : 8
        }]
    
    return hx_711

