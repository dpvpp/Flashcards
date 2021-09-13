# Create tables

sql_create_stacks_table = '''
    CREATE TABLE IF NOT EXISTS stacks (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        last_reviewed text
    ); '''

sql_create_cards_table = '''
    CREATE TABLE IF NOT EXISTS cards (
        id integer PRIMARY KEY AUTOINCREMENT,
        stack_id integer NOT NULL,
        FOREIGN KEY (stack_id) REFERENCES stacks(id)
    ); '''

sql_create_questions_table = '''
    CREATE TABLE IF NOT EXISTS questions (
        id integer PRIMARY KEY AUTOINCREMENT,
        card_id integer NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    ); '''

sql_create_answers_table = '''
    CREATE TABLE IF NOT EXISTS answers (
        id integer PRIMARY KEY AUTOINCREMENT,
        card_id integer NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    ); '''

sql_create_assets_table = '''
    CREATE TABLE IF NOT EXISTS assets (
        id integer PRIMARY KEY AUTOINCREMENT,
        question_id integer,
        answer_id integer,
        type text NOT NULL,
        content text,
        filename text,
        left real NOT NULL,
        top real NOT NULL,
        width real,
        height real,
        FOREIGN KEY (question_id) REFERENCES questions (id),
        FOREIGN KEY (answer_id) REFERENCES answers (id)
    ); '''


# Stacks

sql_insert_stack = '''
    INSERT INTO stacks(name, last_reviewed)
    VALUES(?,?)
    '''

sql_delete_stack = '''
    DELETE FROM stacks WHERE id=?
    '''

sql_update_stack_date = '''
    UPDATE stacks
    SET last_reviewed=?
    WHERE id=?
    '''

sql_check_stack_exists = '''
    SELECT * FROM stacks
    WHERE name = ?
    '''

# Cards

sql_insert_card = '''
    INSERT INTO cards(stack_id)
    VALUES(?)
    '''

sql_delete_card = '''
    DELETE FROM cards WHERE id=?
    '''

sql_select_stack_cards = '''
    SELECT * FROM cards WHERE stack_id=?
    '''

sql_delete_stack_cards = '''
    DELETE FROM cards WHERE stack_id=?
    '''


# Questions

sql_insert_question = '''
    INSERT INTO questions(card_id)
    VALUES(?)
    '''

sql_delete_card_questions = '''
    DELETE FROM questions WHERE card_id=?
    '''

sql_delete_stack_questions = '''
    DELETE FROM questions
    WHERE card_id IN (
        SELECT id
        FROM cards
        WHERE stack_id = ?)
    '''

# Answers

sql_insert_answer = '''
    INSERT INTO answers(card_id)
    VALUES(?)
    '''

sql_delete_card_answers = '''
    DELETE FROM answers WHERE card_id=?
    '''

sql_delete_stack_answers = '''
    DELETE FROM answers
    WHERE card_id IN (
        SELECT id
        FROM cards
        WHERE stack_id = ?)
    '''

# Assets

sql_insert_asset = '''
    INSERT INTO assets(question_id, answer_id, type, content, filename, left,
    top, width, height)
    VALUES(?,?,?,?,?,?,?,?,?)
    '''

sql_update_asset = '''UPDATE Assets
    SET content = ? , filename = ?
    WHERE id = ?
    '''

sql_delete_asset = '''
    DELETE FROM assets WHERE id=?
    '''

sql_delete_stack_assets = '''
    DELETE FROM assets
    WHERE question_id IN (
        SELECT q.id FROM questions q
        INNER JOIN cards c ON c.id = q.card_id
        WHERE c.stack_id = ?
    )
    OR answer_id IN (
        SELECT a.id FROM answers a
        INNER JOIN cards c ON c.id = a.card_id
        WHERE c.stack_id = ?
    )
    '''

sql_select_assets_by_card_id = '''SELECT DISTINCT a.id, a.type, a.content, a.filename FROM assets a
    LEFT JOIN questions q ON q.id = a.question_id
    LEFT JOIN answers ans ON ans.id = a.answer_id
    INNER JOIN cards c ON c.id = q.card_id OR c.id = ans.card_id
    WHERE c.id = ?'''

sql_select_asset_by_card_id = '''SELECT DISTINCT a.id, a.type, a.content, a.filename FROM assets a
    LEFT JOIN questions q ON q.id = a.question_id
    LEFT JOIN answers ans ON ans.id = a.answer_id
    INNER JOIN cards c ON c.id = q.card_id OR c.id = ans.card_id
    WHERE c.id = ? AND a.type = ?'''
