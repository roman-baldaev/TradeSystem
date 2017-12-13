import psycopg2
import datetime
import random


"""Data generation module

   Generate data for testing the database.

"""
def get_dimension_table(table_name):

    try:
        connect = psycopg2.connect(database='trade_system', user='roman',
                                   host='localhost', password='admin')
        cursor = connect.cursor()
        cursor.execute(
            'SELECT * FROM {};'.format(table_name)
        )
        return len(cursor.fetchall())
    except Exception as database_error:
        print ('Error in get_dimension_table function: {}'.format(database_error))
        return database_error


def workshop_generation(quantity):
    """
        Restriction - kiosks and trays (trade points 3 and 4 types) can not have more than 1 workshop.

    """

    try:
        connect = psycopg2.connect(database='trade_system', user='roman',
                                   host='localhost', password='admin')
        cursor = connect.cursor()
        dimension = get_dimension_table('trade_point_TradePoint')
        index_list = list(range(1,dimension + 1))

        #Получаем список торговых точек 3 и 4 типа
        cursor.execute('SELECT TP.id FROM ' \
            'trade_point_TradePoint as TP ' \
            'WHERE TP.type = 3 OR TP.type = 4')
        small_trade_points = cursor.fetchall()
        index_small_points = [item[0] for item in small_trade_points]

        # Получаем список торговых точек 3 и 4 типа, у которых уже есть торговая секция
        # торговая секция такой торговой точки - и есть торговая точка
        cursor.execute('SELECT TP.id, TP.type, WS.id FROM '\
            'trade_point_TradePoint as TP '\
            'INNER JOIN trade_point_Workshop as WS '\
            'ON TP.id = WS.trade_point_id '\
            'WHERE TP.type = 3 OR TP.type = 4')
        small_trade_point_with_workshop = cursor.fetchall()
        index_for_delete = [small_trade_point_with_workshop[i][0] for i in range(len(small_trade_point_with_workshop))]

        #так как работа идет с индексами - уникальными элементами, можем вычитать списки с помощью множеств
        #что работает гораздо быстрее
        index_list = list(set(index_list) - set(index_for_delete))
        for i in range(quantity):
            index = random.choice(index_list)
            cursor.execute(
                    "INSERT INTO trade_point_Workshop (trade_point_id) \
                      VALUES ({});".format(index))
            if index in index_small_points:
                index_list.remove(index)

        connect.commit()
        connect.close()

    except Exception as database_error:
        print('Error in workshop_generation function: {}'.format(database_error))
        return database_error


print (get_dimension_table('trade_point_TradePoint'))
workshop_generation(20)
# connect = psycopg2.connect(database='trade_system', user='roman',
#                                    host='localhost', password='admin')
# cursor = connect.cursor()
# for i in range(2,7):
#     cursor.execute(
#             "INSERT INTO trade_point_Workshop (trade_point_id) \
#               VALUES ({});".format(i))
# connect.commit()
# connect.close()