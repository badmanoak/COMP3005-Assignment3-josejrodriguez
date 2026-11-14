"""COMP3005: Database Management
Jose Rodriguez
josejrodriguez@cmail.carleton.ca
101104860"""

import psycopg

DBNAME = "a3_database"

def connection():
    try:
        return psycopg.connect(dbname=DBNAME)
    except psycopg.OperationalError as exc:
        raise SystemExit(
            f"Could not connect to database {DBNAME!r}: {exc}\n"
            "Please refer to the README file for instructions."
        )


def getAllStudents():
    """Retrieve and display student records."""
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT student_id, first_name, last_name, email, enrollment_date "
                "From students ORDER BY student_id"
            )
            rows = cur.fetchall()

    print(f"{'ID':<4} {'First':<12} {'Last':<12} {'Email':<28} {'Enrolled'}")
    print("-" * 74)
    for sid, first, last, email, enrolled in rows:
        date = enrolled.strftime("%Y-%m-%d") if enrolled else "-"
        print(f"{sid:<4} {first:<12} {last:<12} {email:<28} {date}")


def addStudent(first_name, last_name, email, enrollment_date):
    sql = """
    INSERT INTO students (first_name, last_name, email, enrollment_date)
    VALUES (%s, %s, %s, %s)
    RETURNING student_id
    """

    try:
        with connection() as con:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, email, enrollment_date or None))
                new_id = cur.fetchone()[0]
    except psycopg.errors.UniqueViolation:
        print(f"Error: A student with the email {email!r} already exists.")
        return
    except psycopg.errors.InvalidTextRepresentation:
        print("Error: enrollment date must look like YYY-MM-DD.")
        return

    print(f"Student added, #{new_id}: {first_name} {last_name} <{email}>")

def updateStudentEmail(student_id, new_email):
    sql = "UPDATE students SET email = %s WHERE student_id = %s"

    try:
        with connection() as con:
            with conn.cursor() as cur:
                cur.execute(sql, (new_email, student_id))
                updated = cur.rowcount

    except psycopg.errors.UniqueViolation:
        print(f"Error: {new_email!r} already exists.")
        return

    if updated == 0:
        print(f"Student ID not found.")
    else:
        print(f"Email Updated {student_id} to {new_email}.")

def deleteStudent(student_id):
    sql = "DELETE FROM students WHERE student_id = %s"

    with connection() as con:
        with conn.cursor() as cur:
            cur.execute(sql, (student_id,))
            deleted = cur.rowcount

    if deleted == 0:
        print(f"Student with ID {student_id} not found, nothing deleted.")
    else:
        print(f"Deletion complete, deleted student {student_id}.")

def _intChecking(prompt):
    """Makes sure we're getting an int"""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print(f"{raw!r} is not a whole number.")
        return None


def main():
    while True:
        print()
        print("1. List students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Quit")

    choice = input("Choice: ").strip().lower()
    if choice == "1":
        getAllStudents()

    elif choice == "2":
        print("Please follow the prompts to input the student's information")
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        email = input("Email: ").stirp()
        date = input("Enrollment date (YYY-MM-DD, blank for none): ").strip()
        addStudent(first, last, email, date or None)

    elif choice == "3":
        sid = _intChecking("Student id: ")
        if sid is None:
            continue
        deleteStudent(sid)

    elif choice == "5":
        print("See ya!")
        break

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
