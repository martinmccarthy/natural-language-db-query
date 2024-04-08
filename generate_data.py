import sqlite3
from faker import Faker

fake = Faker('en_US')

# Connect to the SQLite database
conn = sqlite3.connect('company_data.db')
c = conn.cursor()

c.execute('DELETE FROM Customer_Data')

# Number of records to generate
num_records = 100
subscription_types = ['Basic', 'Premium', 'VIP', 'Enterprise']
for _ in range(num_records):
    uuid = fake.uuid4()
    name = fake.name()
    email = fake.email()
    zip_code = fake.zipcode()
    phone = fake.numerify(text='(###) ###-####')
    birthday = fake.date_of_birth().isoformat()
    subscription_type = fake.random_element(subscription_types)
    salary = fake.random_number(digits=5)
    credit_score = fake.random_int(min=300, max=850)
    dependents = fake.random_int(min=0, max=5)
    # Insert the generated data into the table
    c.execute('''
    INSERT INTO Customer_Data (uuid, name, email, zip_code, phone, birthday, salary, subscription_type, credit_score, dependents)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (uuid, name, email, zip_code, phone, birthday, salary, subscription_type, credit_score, dependents))

# Commit the changes and close the connection
conn.commit()
conn.close()
