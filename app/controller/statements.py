import os

CREATE_TABLES_STMT = """
    
"""

insert_task_stmt = """
    INSERT INTO tasks (title, content, image_content, starting_date, completion_status) 
    VALUES (%(title)s, %(content)s, %(image_content)s, %(starting_date)s, %(completion_status)s)
"""