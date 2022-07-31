import csv


def csv_content(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact number", "E-mail Id"])

        writer.writerow(info_list)


if __name__ == '__main__':
    x = True

    while (x):
        student_info = input("Enter the details in the format--> Name age Contact_Number Email")
        student_info_list = student_info.split(" ")
        print("Entered information is -\nName: {}\nAge: {}\nContact Number: {}\nE-mail ID: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        check = input("Is the entered information correct? (yes/no)")
        if check == "yes":
            csv_content(student_info_list)
            xc = input("Enter yes to add more info, or Enter no to exit")
            if xc == "yes":
                x = True
            elif xc == "no":
                x = False
        elif check == "no":
            print("Please re-enter the information")


