def new_group(db, value):
    cursor = db.cursor()
    query = "INSERT INTO auth_group (id, name) VALUES (%s, %s);"
    values = value
    cursor.execute(query, (1, values))
    db.commit()
    cursor.close()
