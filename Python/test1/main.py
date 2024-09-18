data_format = "sqlserver"
customers = None

if data_format in ["csv", "json", "sqlite", "sqlserver"]:
    from custom.database.model.customer import Customer
    person1 = Customer("Alice", 30, "New York")
    person2 = Customer("Bob", 25, "Los Angeles")
    customers = [person1, person2]
    new_record = Customer("Matt", 30, "Miami")
    customers.append(new_record)

if data_format == "csv":
    from custom.writer.custom_csv import *
    filename = "output/data.csv"
    obj = CustomCsv()
    obj.save_to_file(customers, filename)
elif data_format == "json":
    from custom.writer.custom_json import *
    filename = "output/data.json"
    obj = CustomJson()
    obj.save_to_file(customers, filename)
elif data_format == "sqlite":
    from custom.database.sql_lite.sql_lite_database_manager import SqlLiteDatabaseManager
    # Usage example
    db_mgr = SqlLiteDatabaseManager()  # Create an instance
    for customer in customers:
        db_mgr.insert_data(customer)

    data = db_mgr.fetch_data()
    for row in data:
        print(row)

    db_mgr.commit_and_close()  # Close the connection after use
elif data_format == "sqlserver":
    from custom.database.sql_server.repository.customer_repository import CustomerRepository

    user_repo_obj = CustomerRepository()
    user_repo_obj.create_table()
    print(customers)
    for customer in customers:
        user_repo_obj.insert_data(customer)
    data = user_repo_obj.fetch_data()
    print(data)

    user_repo_obj.db_mgr.commit_and_close()
    
elif data_format == "animal":
    from custom.classes.dog import *
    from custom.classes.cat import *
    dog = Dog("Buddy", "dobarman")
    cat = Cat("Whiskers", "Persian")
    dog.soundslike()
    cat.soundslike()
elif data_format == "thread":
    from custom.classes.mythreadapp import *
    threadobj = mythreadapp()
    threadobj.callthread()
elif data_format == "asyncio":
    from custom.classes.myasynccall import *
    asyncobj = myasynccall()
    asyncio.run(asyncobj.callasyncmethod())