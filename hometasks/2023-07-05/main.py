import json
import os
from datetime import datetime

from sqlalchemy import func, update, MetaData, delete
from sqlalchemy.exc import SQLAlchemyError

import create_database as db_creator
from models.customers import Customer
from models.database import DATABASE_NAME, Session, engine, Base
from models.sales import Sale
from models.salesmen import Salesman

if __name__ == '__main__':
    session = Session()
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database(session)

    filename = 'export.json'


    def save_file(filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            try:
                json.dump([str(item) for item in content], file)
                print(f"Data saved to '{filename}'. Customize filename in settings", '', sep='\n')
            except Exception as e:
                print(f'Failed to export data. Error: {e}', '', sep='\n')


    while True:
        action = input('Select action: '
                       '(1) show all transactions, '
                       '(2) show min and max transactions, '
                       '(3) show salesmen with min and max transaction amount, '
                       '(4) show customer with max transaction amount, '
                       '(5) show average transaction amounts, '
                       '(6) insert data, '
                       '(7) update data, '
                       '(8) delete data, '
                       '(9) settings, '
                       '(0) exit \n')

        if action not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            print('Incorrect input. Try again', "", sep='\n')

        elif action == '0':
            break

        elif action == '1':
            results = []
            for transaction in session.query(Sale).all():
                results.append(transaction)
                print(transaction)
            print()
            while True:
                sub_action = input('Select further action: '
                                   '(1) filter by salesman, '
                                   '(2) save to file, '
                                   '(0) exit \n')
                if sub_action not in ['1', '2', '0']:
                    print('Incorrect input. Try again', "", sep='\n')
                elif sub_action == '0':
                    break
                elif sub_action == '1':
                    query = input('Enter salesman name: ')
                    print('Search results: ')
                    results = []
                    for line in session.query(Salesman.sname, Sale).join(Sale).filter(
                            Salesman.sname.like(f'%{query}%')):
                        results.append(line)
                        print(line)
                    print()
                    while True:
                        fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                        if fin_action == 's':
                            save_file(filename, results)
                            break
                        else:
                            break
                    break
                elif sub_action == '2':
                    save_file(filename, results)
                    break

        elif action == '2':
            min_value = session.query(func.min(Sale.amount)).scalar()
            max_value = session.query(func.max(Sale.amount)).scalar()

            min_amt_trans = session.query(Sale).filter(Sale.amount == min_value).all()
            max_amt_trans = session.query(Sale).filter(Sale.amount == max_value).all()
            print(f'Minimum amount transaction: {min_amt_trans if min_amt_trans else "not found"}')
            print(f'Maximum amount transaction: {max_amt_trans if max_amt_trans else "not found"}')
            print()

            results = [min_amt_trans, max_amt_trans]

            while True:
                sub_action = input('Select further action: '
                                   '(1) filter by salesman, '
                                   '(2) filter by customer, '
                                   '(3) save to file, '
                                   '(0) exit \n')
                if sub_action not in ['1', '2', '3', '0']:
                    print('Incorrect input. Try again', "", sep='\n')
                elif sub_action == '0':
                    break
                elif sub_action == '1':
                    min_value = session.query(Sale.sid, func.min(Sale.amount).label('min_amount')).group_by(
                        Sale.sid).subquery()
                    max_value = session.query(Sale.sid, func.max(Sale.amount).label('max_amount')).group_by(
                        Sale.sid).subquery()

                    query = input('Enter salesman name: ')

                    min_amt_trans = session.query(Sale).join(Salesman).join(min_value, Sale.sid == min_value.c.sid). \
                        filter(Salesman.sname == query, Sale.amount == min_value.c.min_amount).all()

                    max_amt_trans = session.query(Sale).join(Salesman).join(max_value, Sale.sid == max_value.c.sid). \
                        filter(Salesman.sname == query, Sale.amount == max_value.c.max_amount).all()
                    print(f'Minimum amount transaction: {min_amt_trans if min_amt_trans else "not found"}')
                    print(f'Maximum amount transaction: {max_amt_trans if max_amt_trans else "not found"}')
                    print()

                    results = [min_amt_trans, max_amt_trans]

                    while True:
                        fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                        if fin_action == 's':
                            save_file(filename, results)
                            break
                        else:
                            break
                    break

                elif sub_action == '2':
                    min_value = session.query(Sale.cid, func.min(Sale.amount).label('min_amount')).group_by(
                        Sale.cid).subquery()
                    max_value = session.query(Sale.cid, func.max(Sale.amount).label('max_amount')).group_by(
                        Sale.cid).subquery()

                    query = input('Enter customer name: ')

                    min_amt_trans = session.query(Sale).join(Customer).join(min_value, Sale.cid == min_value.c.cid). \
                        filter(Customer.cname == query, Sale.amount == min_value.c.min_amount).all()

                    max_amt_trans = session.query(Sale).join(Customer).join(max_value, Sale.cid == max_value.c.cid). \
                        filter(Customer.cname == query, Sale.amount == max_value.c.max_amount).all()
                    print(f'Minimum amount transaction: {min_amt_trans if min_amt_trans else "not found"}')
                    print(f'Maximum amount transaction: {max_amt_trans if max_amt_trans else "not found"}')
                    print()

                    results = [min_amt_trans, max_amt_trans]

                    while True:
                        fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                        if fin_action == 's':
                            save_file(filename, results)
                            break
                        else:
                            break
                    break

                elif sub_action == '3':
                    save_file(filename, results)
                    break

        elif action == '3':
            try:
                min_amt_salesman = session.query(Salesman.sname, func.sum(Sale.amount), Sale.date).join(Sale).group_by(
                    Salesman.sname).order_by(func.sum(Sale.amount).desc()).all()[-1]

                max_amt_salesman = session.query(Salesman.sname, func.sum(Sale.amount), Sale.date).join(Sale).group_by(
                    Salesman.sname).order_by(func.sum(Sale.amount).desc()).limit(1).first()

                print('Salesman with minimum total transaction amount:')
                print(*min_amt_salesman)
                print('Salesman with maximum total transaction amount:')
                print(*max_amt_salesman)
                print()

                results = [min_amt_salesman, max_amt_salesman]
            except IndexError:
                print('No data found', '', sep='\n')
                results = []
            while True:
                fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                if fin_action == 's':
                    save_file(filename, results)
                    break
                else:
                    break

        elif action == '4':
            try:
                max_amt_customer = session.query(Customer.cname, func.sum(Sale.amount), Sale.date).join(Sale).group_by(
                    Customer.cname).order_by(func.sum(Sale.amount).desc()).limit(1).first()

                print('Customer with maximum total transaction amount:')
                print(*max_amt_customer)
                print()

                results = [max_amt_customer]
            except (IndexError, TypeError):
                print('No data found', '', sep='\n')
                results = []
            while True:
                fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                if fin_action == 's':
                    save_file(filename, results)
                    break
                else:
                    break

        elif action == '5':
            while True:
                sub_action = input('Select further action: '
                                   '(1) filter by salesman, '
                                   '(2) filter by customer, '
                                   '(0) exit \n')

                if sub_action not in ['1', '2', '0']:
                    print('Incorrect input. Try again', "", sep='\n')
                elif sub_action == '0':
                    break
                elif sub_action == '1':
                    query = input('Enter salesman name: ')
                    try:
                        avg_amt_salesman = session.query(Salesman.sname, func.round(func.avg(Sale.amount), 2)).join(
                            Sale).group_by(Salesman.sname).filter(Salesman.sname == query).first()
                        print(f'Average transaction amount:')
                        print(*avg_amt_salesman)
                        print()

                        results = [avg_amt_salesman]

                        while True:
                            fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                            if fin_action == 's':
                                save_file(filename, results)
                                break
                            else:
                                break
                        break

                    except (TypeError, IndexError):
                        print('Not found', '', sep='\n')
                        break

                elif sub_action == '2':
                    query = input('Enter customer name: ')
                    try:
                        avg_amt_customer = session.query(Customer.cname, func.round(func.avg(Sale.amount), 2)).join(
                            Sale).group_by(Customer.cname).filter(Customer.cname == query).first()
                        print(f'Average transaction amount:')
                        print(*avg_amt_customer)
                        print()

                        results = [avg_amt_customer]

                        while True:
                            fin_action = input('Enter (s) to save to file, (any other key) to exit: \n')
                            if fin_action == 's':
                                save_file(filename, results)
                                break
                            else:
                                break
                        break

                    except (TypeError, IndexError):
                        print('Not found', '', sep='\n')
                        break

        elif action == '6':
            while True:
                all_tables = Base.metadata.tables
                tables_arr = list(dict(all_tables).keys())

                print("Enter table to insert data to:")
                for i, table_name in enumerate(all_tables, 1):
                    print(f"- ({i}) {table_name}")
                print(f"- (0) exit")

                table_No = input()
                if table_No not in [str(i) for i in range(len(tables_arr) + 1)]:
                    print('Incorrect input. Try again', "", sep='\n')
                elif table_No == '0':
                    break
                else:
                    table = tables_arr[int(table_No) - 1]
                    try:
                        cls = next((cls for cls in Base.__subclasses__() if cls.__tablename__ == table), None)
                        if cls:
                            props = []
                            for attr_name in dir(cls):
                                if not attr_name.startswith('_'):
                                    attr_value = getattr(cls, attr_name)
                                    if not (hasattr(attr_value, 'primary_key') and attr_value.primary_key):
                                        props.append(attr_name)
                            props = [prop for prop in props if
                                     prop not in ['metadata', 'registry']]

                            values = {}
                            for prop in props:
                                if prop != 'date':
                                    input_value = input(f'Enter {prop}: ')
                                    if input_value:
                                        values[prop] = input_value
                                else:
                                    year_input = input('Enter year: ')
                                    month_input = input('Enter month: ')
                                    day_input = input('Enter day: ')
                                    if year_input != '' and month_input != '' and day_input != '':
                                        values[prop] = datetime(int(year_input), int(month_input), int(day_input))
                            if values:
                                with engine.begin() as conn:
                                    conn.execute(cls.__table__.insert().values(**values))
                                print('Data added successfully', '', sep='\n')
                            else:
                                print('No data entered, no changes applied', '', sep='\n')
                            break
                        else:
                            print('Invalid table name', '', sep='\n')
                            break
                    except (ValueError, SQLAlchemyError) as e:
                        print('You seem to have entered incorrect data. Try again', f'Error: {e}', '', sep='\n')
                        break

        elif action == '7':
            while True:
                all_tables = Base.metadata.tables
                tables_arr = list(dict(all_tables).keys())

                print("Select table to update:")
                for i, table_name in enumerate(all_tables, 1):
                    print(f"- ({i}) {table_name}")
                print(f"- (0) exit")

                table_No = input()
                if table_No not in [str(i) for i in range(len(tables_arr) + 1)]:
                    print('Incorrect input. Try again', "", sep='\n')
                elif table_No == '0':
                    break
                else:
                    table = tables_arr[int(table_No) - 1]
                    while True:
                        target_id = input('Enter ID of the record to update: ')

                        table_class = Base.metadata.tables[table]
                        pk_column = table_class.primary_key.columns.values()[0].name
                        primary_keys = session.query(getattr(table_class.c, pk_column)).all()

                        if target_id not in [str(i[0]) for i in primary_keys]:
                            print('ID not found', '', sep='\n')
                            break
                        else:
                            try:
                                cls = next((cls for cls in Base.__subclasses__() if cls.__tablename__ == table), None)
                                if cls:
                                    pk = None
                                    props = []
                                    for attr_name in dir(cls):
                                        if not attr_name.startswith('_'):
                                            attr_value = getattr(cls, attr_name)
                                            if hasattr(attr_value, 'primary_key') and attr_value.primary_key:
                                                pk = attr_value
                                            else:
                                                props.append(attr_name)
                                    props = [prop for prop in props if
                                             prop not in ['metadata', 'registry']]

                                    values = {}
                                    for prop in props:
                                        if prop != 'date':
                                            input_value = input(f'Enter {prop} (leave blank to keep as is): ')
                                            if input_value != '':
                                                values[prop] = input_value
                                        else:
                                            print('To keep the date as is, leave any date field '
                                                  '(year, month or day) blank:')
                                            year_input = input('Enter year: ')
                                            month_input = input('Enter month: ')
                                            day_input = input('Enter day: ')
                                            if year_input != '' and month_input != '' and day_input != '':
                                                values[prop] = datetime(int(year_input), int(month_input),
                                                                        int(day_input))
                                    if values:
                                        upd = update(cls).values(**values).where(pk == int(target_id))
                                        session.execute(upd)
                                        session.commit()
                                        print('Data updated successfully', '', sep='\n')
                                    else:
                                        print('No data entered, no changes applied', '', sep='\n')
                                    break
                                else:
                                    print('Invalid table name', '', sep='\n')
                                    break
                            except ValueError:
                                print('You seem to have entered incorrect data. Try again', '', sep='\n')
                                break
                break

        elif action == '8':
            while True:
                all_tables = Base.metadata.tables
                tables_arr = list(dict(all_tables).keys())

                print("Select table to delete data from:")
                for i, table_name in enumerate(all_tables, 1):
                    print(f"- ({i}) {table_name}")
                print(f"- (0) exit")

                table_No = input()
                if table_No not in [str(i) for i in range(len(tables_arr) + 1)]:
                    print('Incorrect input. Try again', "", sep='\n')
                elif table_No == '0':
                    break
                else:
                    try:
                        table = tables_arr[int(table_No) - 1]
                        while True:
                            target_id = input('Enter ID of the record to delete: ')

                            table_class = Base.metadata.tables[table]
                            pk_column = next(c.name for c in table_class.primary_key.columns)

                            primary_keys = session.query(getattr(table_class.c, pk_column)).all()

                            if target_id not in [str(i[0]) for i in primary_keys]:
                                print('ID not found', '', sep='\n')
                                break
                            else:
                                metadata = MetaData()
                                metadata.reflect(bind=engine)
                                target_table = metadata.tables[table]
                                delete = delete(target_table).where(target_table.c[pk_column] == int(target_id))

                                with engine.begin() as conn:
                                    conn.execute(delete)
                                    print('Data deleted successfully', '', sep='\n')
                                    break
                        break
                    except SQLAlchemyError as e:
                        print(f'Failed to perform action, error: {str(e)}', '', sep='\n')
                        break

        elif action == '9':
            query = input('Enter filename for data export (without extension): ')
            filename = query + '.json'
            print(f"Filename has been changed to '{filename}'", '', sep='\n')
