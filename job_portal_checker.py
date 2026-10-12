import random

data = {
    "Python Developer": ["Python Programming", "Flask"],
    "Java Developer": ["Java Programming", "Spring Boot"],
    "Full Stack Developer": ["HTML", "CSS", "Python or Java Programming", "Flask"],
    "Data Science": ["Python", "SQL", "Power BI", "Data Visualization", "Machine Learning and AI"],
    "Data Analysis": ["Python", "Power BI", "Microsoft Excel"]
}


def search_engine(keyword):
    keyword = keyword.lower()

    found = False

    for title, description in data.items():

        if keyword in title.lower():

            print("\nResult:")
            print("Job Title:", title)
            print("Required Skills:", description)

            found = True

    if found == False:
        print("\nNo results found.")


def add_data():

    title = input("Enter job title: ")

    description = input("Enter required skills separated by comma: ")

    description = description.split(",")

    data[title] = description

    print("Data added successfully!")


def show_data():

    print("\nAvailable Jobs:")

    for title in data:
        print("-", title)


while True:

    print("\n===== Job Portal Checker =====")
    print("1. Search Job Description")
    print("2. Add Jobs")
    print("3. Show Jobs")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        keyword = input("What do you want to search? ")

        search_engine(keyword)

    elif choice == 2:

        add_data()

    elif choice == 3:

        show_data()

    elif choice == 4:

        print("Thank you for using My Job Search Portal!")

        break

    else:

        print("Invalid choice")