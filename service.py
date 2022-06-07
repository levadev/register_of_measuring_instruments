# from datetime import datetime, timedelta
# import pandas as pd
# import tabulate
# import os
# from cassandra.cluster import Cluster

# cluster = Cluster()
# session = cluster.connect()


# def add_ci_to_reestr():
#     try:

#         print("------Add row to table------")
#         list_of_q = []

#         for i in ['name', 'type', 'field_area', 'manufacturer', 'last_date', 'units']:
#             list_of_q.append(str(input(f'Write the {i} :')))
        
#         for i in ['field', 'life_time', 'release_date', 'interval', 'range1', 'range2', 'pre_result']:
#             list_of_q.append(int(input(f'Write the {i} :')))

#         list_of_q.append(float(input('Write the relative_error :')))

#         session.execute(f"""
#                     INSERT INTO test.app (id, 
#                     name, type, field_area, manufacturer, last_date, units,
#                     field, life_time, release_date, interval, range1, range2, pre_result, relative_error
#                     create_time, delete_time)
#                     VALUES (uuid(),{','.join(str(s) for s in list_of_q)}, toUnixTimestamp(now()), NULL)
#                     """)
#         del list_of_q
#         return print('Mi added successfully!')

#     except:
#         return print("Oops... Something went's wrong :(")

# def see_all_ci_in_reestr(p=True):
#     try:

#         ci = pd.DataFrame(session.execute("""SELECT * FROM test.app"""))
#         ci = ci[ci['delete_time'].isnull()]

#         ci_cat = ci.drop(labels=['id', 'create_time', 'delete_time'], axis=1)
#         if p==True:
#             print("------All ci in reestr------")
#             print(f"index |{' |'.join(str(i) for i in ci_cat.columns)}")
#             print(tabulate.tabulate(ci_cat))

#         del ci_cat

#         return ci

#     except:
#         return print("Oops... Something went's wrong :(")

# def remove_ci_from_reestr():
#     try:

#         print("------Remove row to table------")
#         ci = see_all_ci_in_reestr()

#         delete = [
#             int(i) for i in input('Enter indexes of records to be deleted separated by a space:').split(' ')
#         ]
            
#         for i in delete:
#             row = [str(i) for i in [r for r in session.execute(f"""SELECT * from test.app where id={ci.iloc[i].id}""")]]
#             session.execute(f"""insert into test.app (id, create_time, delete_time, field_area,
#                                 interval, last_date, life_time, manufacturer, name, pre_result,
#                                 range1, range2, relative_error, release_date, type, units)
#                                 values ({str(row[0])}, {str(row[1])}, toUnixTimestamp(now()), {','.join(str(i) for i in row[3:])})
#                             """)
#         del ci
#         return print('Mi deleted successfully!')
        
#     except:
#         return print("Oops... Something went's wrong :(")

# def remove_all_ci_from_reestr():
#     try:

#         print("------Delete all row in table------")
#         session.execute("""TRUNCATE TABLE test.app""")
#         return print('Table cleared successfully!')
        
#     except:
#         return print("Oops... Something went's wrong :(")
# def import_ci_from_csv():
#     try:
#         print("------Import from csv------\n")
#         print("Please, use follow table's columns:")
#         print("field, field_area, name, type, life_time, release_date, manufacturer, relative_error, last_date, interval, units, range1, range2, pre_result")
#         path = input("Take an absolute path to file : ")
#         data = pd.read_csv(path, parse_dates=False)
        
#         for i in range(len(data)):
#             session.execute(f"""
#             INSERT INTO test.app (id, {','.join(str(s) for s in data.columns)}, create_time, delete_time)
#             VALUES (uuid(),{str(list(data.iloc[i,:]))[1:-1]}, toUnixTimestamp(now()), NULL)
#             """)
#         del data
        
#         return print('Mi added successfully!')
        
#     except:
#         return print("Oops... Something went's wrong :(")

# def statistics():
#     try:

#         print("------Some info------\n")
#         ci = see_all_ci_in_reestr(p=False)
#         yesterday = datetime.today()-timedelta(days=1)
#         d = {
#             'Total Mi': len(ci),
#             'Total manufacturers': len(ci.type.drop_duplicates()),
#             'Total manufacturers': len(ci.manufacturer.drop_duplicates()),
#             'Total serviceable Mi': len(ci[ci.pre_result == 0]),
#             'Maximum life time of Mi': max(ci.life_time),
#             'Total Mi added today': len(ci[ci.create_time > yesterday])
#         }

#         del yesterday
#         stat = pd.DataFrame(d, index=['Value']).T

#         del d
#         print(tabulate.tabulate(stat, headers='keys', tablefmt='psql'))
#         del stat
        
#     except:
#         return print("Oops... Something went's wrong :(")

# def cls_cnsl():
#     os.system('cls' if os.name=='nt' else 'clear')

from datetime import datetime, timedelta
import pandas as pd
import tabulate
import os
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()

def add_ci_to_reestr():
    try:

        print("------Add row to table------")
        list_of_q = []

        for i in ['name', 'type', 'field_area', 'manufacturer', 'last_date', 'units']:
            list_of_q.append(str(input(f'Write the {i} :')))
        
        for i in ['field', 'life_time', 'release_date', 'interval', 'range1', 'range2', 'pre_result']:
            list_of_q.append(int(input(f'Write the {i} :')))

        list_of_q.append(float(input('Write the relative_error :')))

        session.execute(f"""
                    INSERT INTO test.app (id, 
                    name, type, field_area, manufacturer, last_date, units,
                    field, life_time, release_date, interval, range1, range2, pre_result, relative_error
                    create_time, delete_time)
                    VALUES (uuid(),{','.join(str(s) for s in list_of_q)}, toUnixTimestamp(now()), NULL)
                    """)
        del list_of_q
        return print('Mi added successfully!')

    except:
        return print("Oops... Something went's wrong :(")

def see_all_ci_in_reestr(p=True):
    try:

        ci = pd.DataFrame(session.execute("""SELECT * FROM test.app"""))
        ci = ci[ci['delete_time'].isnull()]

        ci_cat = ci.drop(labels=['id', 'create_time', 'delete_time'], axis=1)
        if p==True:
            print("------All ci in reestr------")
            print(f"index |{' |'.join(str(i) for i in ci_cat.columns)}")
            print(tabulate.tabulate(ci_cat))

        del ci_cat

        return ci

    except:
        return print("Oops... Something went's wrong :(")

def remove_ci_from_reestr():
    try:

        print("------Remove row to table------")
        ci = see_all_ci_in_reestr()

        delete = [
            int(i) for i in input('Enter indexes of records to be deleted separated by a space:').split(' ')
        ]
            
        for i in delete:
            row = [str(i) for i in [r for r in session.execute(f"""SELECT * from test.app where id={ci.iloc[i].id}""")]]
            session.execute(f"""insert into test.app (id, create_time, delete_time, field_area,
                                interval, last_date, life_time, manufacturer, name, pre_result,
                                range1, range2, relative_error, release_date, type, units)
                                values ({str(row[0])}, {str(row[1])}, toUnixTimestamp(now()), {','.join(str(i) for i in row[3:])})
                            """)
        del ci
        return print('Mi deleted successfully!')
        
    except:
        return print("Oops... Something went's wrong :(")

def clear_reestr():
    try:

        print("------Delete all row in table------")
        session.execute("""TRUNCATE TABLE test.app""")
        return print('Table cleared successfully!')
        
    except:
        return print("Oops... Something went's wrong :(")
def import_ci_from_csv():
    try:
        print("------Import from csv------\n")
        print("Please, use follow table's columns:")
        print("field, field_area, name, type, life_time, release_date, manufacturer, relative_error, last_date, interval, units, range1, range2, pre_result")
        path = input("Take an absolute path to file : ")
        data = pd.read_csv(path, parse_dates=False)
        
        for i in range(len(data)):
            session.execute(f"""
            INSERT INTO test.app (id, {','.join(str(s) for s in data.columns)}, create_time, delete_time)
            VALUES (uuid(),{str(list(data.iloc[i,:]))[1:-1]}, toUnixTimestamp(now()), NULL)
            """)
        del data
        
        return print('Mi added successfully!')
        
    except:
        return print("Oops... Something went's wrong :(")

def statistics():
    try:

        print("------Some info------\n")
        ci = see_all_ci_in_reestr(p=False)
        yesterday = datetime.today()-timedelta(days=1)
        d = {
            'Total Mi': len(ci),
            'Total manufacturers': len(ci.type.drop_duplicates()),
            'Total manufacturers': len(ci.manufacturer.drop_duplicates()),
            'Total serviceable Mi': len(ci[ci.pre_result == 0]),
            'Maximum life time of Mi': max(ci.life_time),
            'Total Mi added today': len(ci[ci.create_time > yesterday])
        }

        del yesterday
        stat = pd.DataFrame(d, index=['Value']).T

        del d
        print(tabulate.tabulate(stat, headers='keys', tablefmt='psql'))
        del stat
        
    except:
        return print("Oops... Something went's wrong :(")

def cls_cnsl():
    os.system('cls' if os.name=='nt' else 'clear')

def see_N_last_added():
    try:
        n_row = input('How many lines do you want to see ? \n')
        ci = pd.DataFrame(session.execute(f"""SELECT * FROM test.app LIMIT {n_row}"""))
        ci = ci[ci['delete_time'].isnull()]

        ci_cat = ci.drop(labels=['id', 'create_time', 'delete_time'], axis=1)
        print("------All ci in reestr------")
        print(f"index |{' |'.join(str(i) for i in ci_cat.columns)}")
        print(tabulate.tabulate(ci_cat))

        del ci_cat

        return ci

    except:
        return print("Oops... Something went's wrong :(")