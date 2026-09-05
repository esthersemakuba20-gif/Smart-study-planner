sessions = []

def classify_session(duration):

    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"

def add_session():
    print(" Add Study Session ")

    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic covered: ").strip()
    date = input("Enter date/day: ").strip()

    while True:
        try:
            duration = int(input("Enter duration in minutes: "))

            if duration > 0:
                break
            else:
                print("Duration must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    print("Study session added successfully!")


def view_sessions():

    print(" All Study Sessions ")

    if len(sessions) == 0:
        print("No study sessions have been recorded.")
        return

    print("-" * 80)
    print(f"{'Subject':<20}{'Topic':<25}{'Date':<15}{'Minutes':<10}{'Type':<10}")
    print("-" * 80)

    for session in sessions:

        classification = classify_session(session["duration"])

        print(
            f"{session['subject']:<20}"
            f"{session['topic']:<25}"
            f"{session['date']:<15}"
            f"{session['duration']:<10}"
            f"{classification:<10}"
        )

    print("-" * 80)


def search_by_subject(subject):

    print(f" Search Results for {subject} ")

    found_sessions = []

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            found_sessions.append(session)

    if len(found_sessions) == 0:
        print("No study sessions found for that subject.")
        return

    total_time = 0

    print("-" * 80)
    print(f"{'Subject':<20}{'Topic':<25}{'Date':<15}{'Minutes':<10}{'Type':<10}")
    print("-" * 80)

    for session in found_sessions:

        classification = classify_session(session["duration"])

        print(
            f"{session['subject']:<20}"
            f"{session['topic']:<25}"
            f"{session['date']:<15}"
            f"{session['duration']:<10}"
            f"{classification:<10}"
        )

        total_time += session["duration"]

    print("-" * 80)
    print(f"Total time spent on {subject}: {total_time} minutes")
    print(f"Total time: {total_time / 60:.2f} hours")


def study_statistics():

    print("Study Statistics ")

    if len(sessions) == 0:
        print("No study sessions available.")
        return


    total_minutes = 0

    for session in sessions:
        total_minutes += session["duration"]

    print(f"Total hours studied: {total_minutes / 60:.2f} hours")

    subject_totals = {}

    for session in sessions:

        subject = session["subject"]
        duration = session["duration"]

        if subject in subject_totals:
            subject_totals[subject] += duration
        else:
            subject_totals[subject] = duration

    print("\nTotal hours studied per subject:")

    for subject, minutes in subject_totals.items():
        print(f"{subject}: {minutes / 60:.2f} hours")

    # Find the subject with the least study time
    weakest_subject = min(subject_totals, key=subject_totals.get)

    print(
        f"\nSubject with the least study time: "
        f"{weakest_subject}"
    )

    print(
        f"Time spent: "
        f"{subject_totals[weakest_subject] / 60:.2f} hours"
    )

    longest_session = sessions[0]

    for session in sessions:

        if session["duration"] > longest_session["duration"]:
            longest_session = session

    print("Longest study session:")

    print(f"Subject: {longest_session['subject']}")
    print(f"Topic: {longest_session['topic']}")
    print(f"Date: {longest_session['date']}")
    print(f"Duration: {longest_session['duration']} minutes")


def save_sessions():

    try:

        with open(FILE_NAME, "w") as file:

            for session in sessions:

                file.write(
                    f"{session['subject']}|"
                    f"{session['topic']}|"
                    f"{session['date']}|"
                    f"{session['duration']}\n"
                )

        print("Study sessions saved successfully.")

    except Exception as error:
        print("An error occurred while saving the sessions.")
        print(error)


def load_sessions():
    """
    Load previously saved sessions from study_log.txt.
    """

    try:

        with open(FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) == 4:

                    subject = parts[0]
                    topic = parts[1]
                    date = parts[2]
                    duration = int(parts[3])

                    session = {
                        "subject": subject,
                        "topic": topic,
                        "date": date,
                        "duration": duration
                    }

                    sessions.append(session)

    except FileNotFoundError:

        pass

    except Exception as error:
        print("An error occurred while loading the sessions.")
        print(error)


def main():

    load_sessions()

    while True:


        print("       SMART STUDY PLANNER")


        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_session()

        elif choice == "2":

            view_sessions()

        elif choice == "3":

            subject = input("Enter subject to search: ").strip()

            search_by_subject(subject)

        elif choice == "4":

            study_statistics()

        elif choice == "5":

            save_sessions()

            print("Thank you for using Smart Study Planner!")
            print("Goodbye!")

            break

        else:

            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()