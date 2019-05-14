from app import connect, config, helpers, hx711

def main():
    
    for conf in config.hx_config_test():
        
        hx = hx711.HX711(conf['GPIO_1'], conf['GPIO_2'])
        hx.set_reading_format("MSB", "MSB")
        hx.set_reference_unit(conf['cal_1_a'])
        hx.set_reference_unit_B(conf['cal_1_b'])
        hx.reset()

        try:
            tuple = helpers.get_weight(hx, conf['cal_2_a'],conf['cal_2_b'])
            weight_A = tuple[0]
            weight_B = tuple[1]
            time = helpers.get_time()
            date = helpers.get_date()
            values_a = (conf['sample_id_1'], conf['scale_id_1'], date, time, weight_A, conf['sample_id_2'], conf['scale_id_2'], date, time, weight_B)
            query = """INSERT INTO weights (sample_id, sensor_id, date, time, weight) VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s);"""
                   
            connect.db_connect(query, values_a, 1)
            #connect.connect(query, values_a, 2)
        except:
            helpers.cleanAndExit()
                

#if __name__ == '__main__':
#    main()
