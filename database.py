import psycopg2

class Database:
    def __init__(self):
        self.connect = psycopg2.connect(
            database="data",
            user="postgres",
            host="localhost",
            password="2007"
        )

    def manager(self, sql, *args, commit=False, fetchall=False, fetchone=False):
        with self.connect as connect:
            result = None
            with connect.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    connect.commit()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
            return result

    def create_categories(self):
        sql = """CREATE TABLE IF NOT EXISTS categories (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT
            );
        """
        self.manager(sql, commit=True)

    def create_news(self):
        sql = """CREATE TABLE IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                content TEXT NOT NULL,
                published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_published BOOL DEFAULT False,
                category_id INTEGER REFERENCES categories(id)
            );
        """
        self.manager(sql, commit=True)

    def create_comments(self):
        sql = """CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY,
                author_name VARCHAR(100),
                comment_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                news_id INTEGER REFERENCES news(id)
            );
        """
        self.manager(sql, commit=True)

    def alter_news(self):
        sql = """ALTER TABLE news ADD COLUMN views INTEGER DEFAULT 0;"""
        self.manager(sql, commit=True)

    def alter_comments(self):
        sql = """ALTER TABLE comments ALTER COLUMN author_name TYPE TEXT;"""
        self.manager(sql, commit=True)

    def insert_categories(self):
        sql = """INSERT INTO categories (name, description) VALUES
        ('Technology', 'This category contains technology news.'),
        ('Sports', 'This category contains news related to sports.'),
        ('Health', 'This category contains health-related news.');
        """
        self.manager(sql, commit=True)

    def insert_news(self):
        sql = """INSERT INTO news (title, content, published_at, category_id) VALUES
        ('The rise of AI', 'Artificial intelligence is transforming industries.', CURRENT_TIMESTAMP - INTERVAL '1 day', 1),
        ('Liverpool vs Real Madrid', 'Liverpool won 2-0 against Real Madrid.', CURRENT_TIMESTAMP, 2),
        ('Health benefits of Yoga!', 'Yoga can improve mental and physical health.', CURRENT_TIMESTAMP - INTERVAL '2 day', 3);
        """
        self.manager(sql, commit=True)

    def insert_comments(self):
        sql = """INSERT INTO comments (author_name, comment_text, created_at, news_id) VALUES
        ('Toxir', 'Good luck', CURRENT_TIMESTAMP - INTERVAL '1 year', 1),
        ('Ali', 'Nice', CURRENT_TIMESTAMP, 2),
        ('Sobir', 'Good', CURRENT_TIMESTAMP, 3);
        """
        self.manager(sql, commit=True)

    def update_news(self):
        sql = "UPDATE news SET views = 1;"
        self.manager(sql, commit=True)

    def update_news_days(self):
        sql = "UPDATE news SET is_published = True WHERE published_at < CURRENT_TIMESTAMP - INTERVAL '1 day';"
        self.manager(sql, commit=True)

    def delete_comments(self):
        sql = "DELETE FROM comments WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 year';"
        self.manager(sql, commit=True)

    def select_alias_news(self):
        sql = "SELECT news.id AS news_id, news.title AS news_title, categories.name AS category_name FROM news JOIN categories ON categories.id = news.category_id;"
        return self.manager(sql, fetchall=True)

    def select_technology(self):
        sql = "SELECT news.* FROM news JOIN categories ON categories.id = news.category_id WHERE name = 'Technology';"
        return self.manager(sql, fetchall=True)

    def select_is_published(self):
        sql = "SELECT * FROM news WHERE is_published = True ORDER BY published_at DESC LIMIT 5;"
        return self.manager(sql, fetchall=True)

    def select_views(self):
        sql = "SELECT id, title, content FROM news WHERE views BETWEEN 10 and 100;"
        return self.manager(sql, fetchall=True)

    def select_author_name(self):
        sql = "SELECT id, author_name, comment_text FROM comments WHERE author_name LIKE %s;"
        return self.manager(sql, 'A%', fetchall=True)

    def select_all_categories(self):
        sql = """
            SELECT categories.name AS name, COUNT(news.category_id) FROM categories LEFT JOIN news ON categories.id = news.category_id GROUP BY categories.name;
        """
        return self.manager(sql, fetchall=True)

    def unique_title(self):
        sql = "ALTER TABLE news ADD CONSTRAINT unique_title UNIQUE (title);"
        self.manager(sql, commit=True)

connect = Database()
