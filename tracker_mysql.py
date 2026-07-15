from datetime import date
import time
import matplotlib.pyplot as plt
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="",         
        database="fitness_tracker"
    )
    cursor = connection.cursor(dictionary=True) 
except mysql.connector.Error as err:
    print(f"Database Connection Error: {err}")
    print("Make sure your XAMPP Control Panel has MySQL started (green background)!")
    exit()

cursor.execute("SELECT workout_date, num_sprints, sprint_time_sec, rest_time_sec FROM sprint_sessions ORDER BY workout_date ASC")
history = cursor.fetchall()

user_input = input("Do you want to view your history? Y/N: ").strip().lower()
if user_input in ["yes", "y", "yeah", "yea"]:
    print("\n=== Saved Workout History ===")
    for session in history:
        print("----------------")
        print(f"Date: {session['workout_date']}")
        print(f"Sprints: {session['num_sprints']}")
        print(f"Sprint Time: {session['sprint_time_sec']} sec")
        print(f"Rest Time: {session['rest_time_sec']} sec\n")
else:
    print("\nOk, Start today's workout!")

print(f"Today's Date: {date.today()}")

while True:
    try:
        num_sprint = int(input("Enter the number of sprints you want to track: "))
        sprint_time = int(input("Enter the time for each sprint in seconds: "))
        rest_time = int(input("Enter the time for rest between each sprint in seconds: "))
        break
    except ValueError:
        print("Please enter a valid whole number!\n")

def countdown_timer(seconds, reps, rest):
    for i in range(reps):
        print(f"\nRound {i+1}")
        current_time = seconds
        while current_time > 0:
            print(f"Sprint: {current_time}s")
            time.sleep(1)
            current_time -= 1
        print("It is time to rest!")
        
        if i + 1 < reps:
            current_rest = rest
            while current_rest > 0:
                print(f"Rest: {current_rest}s")
                time.sleep(1)
                current_rest -= 1
            print("It is time to run!")

countdown_timer(sprint_time, num_sprint, rest_time)

insert_query = """
    INSERT INTO sprint_sessions (workout_date, num_sprints, sprint_time_sec, rest_time_sec)
    VALUES (%s, %s, %s, %s)
"""
record_values = (date.today(), num_sprint, sprint_time, rest_time)
cursor.execute(insert_query, record_values)
connection.commit() 

cursor.execute("SELECT workout_date, num_sprints, sprint_time_sec, rest_time_sec FROM sprint_sessions ORDER BY workout_date ASC")
history = cursor.fetchall()

dates = [str(session["workout_date"]) for session in history]
sprint_times = [session["sprint_time_sec"] for session in history]
rest_times = [session["rest_time_sec"] for session in history]

plt.figure(figsize=(8,5))
plt.plot(dates, sprint_times, marker="o", label="Sprint Time")
plt.plot(dates, rest_times, marker="s", label="Rest Time")
plt.legend()
plt.title("Sprint vs Rest Time (Database Live Feed)")
plt.xlabel("Date")
plt.ylabel("Seconds")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

if len(history) > 0:
    print("\n=== Career Summary Statistics ===")
    total_sprints = sum(session["num_sprints"] for session in history)
    longest = max(session["sprint_time_sec"] for session in history)
    avg_rest = sum(session["rest_time_sec"] for session in history) / len(history)

    print(f"Total sprints completed: {total_sprints}")
    print(f"Longest sprint: {longest} sec")
    print(f"Average rest time: {avg_rest:.2f} sec")
print("\nGood Job!")

cursor.close()
connection.close()
