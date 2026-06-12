
import bcrypt
from database.db import get_connection


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def register_user(name, email, password, role):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        hashed_password = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users
            (name, email, password, role)
            VALUES (?, ?, ?, ?)
            """,
            (
                name,
                email,
                hashed_password,
                role
            )
        )

        conn.commit()

        return True

    except Exception as e:

        print("REGISTER ERROR:", e)

        return False

    finally:
        conn.close()


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        print("USER NOT FOUND")
        return None

    stored_hash = user[3]

    print("EMAIL FOUND")
    print("HASH:", stored_hash)

    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ):
        print("PASSWORD MATCH")
        return user

    print("PASSWORD NOT MATCH")

    return None

