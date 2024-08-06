import os

class Resume:
    def __init__(self, name, email, phone, objective, education, work_experience, skills):
        self.name = name
        self.email = email
        self.phone = phone
        self.objective = objective
        self.education = education
        self.work_experience = work_experience
        self.skills = skills

class ResumeMakerApp:
    def __init__(self):
        self.resumes = []

    def create_resume(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        objective = input("Enter your objective: ")
        education = input("Enter your education: ")
        work_experience = input("Enter your work experience: ")
        skills = input("Enter your skills: ")

        resume = Resume(name, email, phone, objective, education, work_experience, skills)
        self.resumes.append(resume)

    print("Resume created successfully!")

    def edit_resume(self):
        if not self.resumes:
            print("No resumes to edit.")
            return

        for i, resume in enumerate(self.resumes):
            print(f"{i+1}. {resume.name}")

        try:
            choice = int(input("Enter the number of the resume to edit: ")) - 1
            if choice < 0 or choice >= len(self.resumes):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        resume = self.resumes[choice]

        print("Enter new values (press enter to keep current value):")
        resume.name = input(f"Name ({resume.name}): ") or resume.name
        resume.email = input(f"Email ({resume.email}): ") or resume.email
        resume.phone = input(f"Phone ({resume.phone}): ") or resume.phone
        resume.objective = input(f"Objective ({resume.objective}): ") or resume.objective
        resume.education = input(f"Education ({resume.education}): ") or resume.education
        resume.work_experience = input(f"Work Experience ({resume.work_experience}): ") or resume.work_experience
        resume.skills = input(f"Skills ({resume.skills}): ") or resume.skills

    print("Resume edited successfully!")

    def delete_resume(self):
        if not self.resumes:
            print("No resumes to delete.")
            return

        for i, resume in enumerate(self.resumes):
            print(f"{i+1}. {resume.name}")

        try:
            choice = int(input("Enter the number of the resume to delete: ")) - 1
            if choice < 0 or choice >= len(self.resumes):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        del self.resumes[choice]

    print("Resume deleted successfully!")

    def view_resumes(self):
        if not self.resumes:
            print("No resumes to view.")
            return

        for i, resume in enumerate(self.resumes):
            print(f"{i+1}. {resume.name}")
            print(f"Email: {resume.email}")
            print(f"Phone: {resume.phone}")
            print(f"Objective: {resume.objective}")
            print(f"Education: {resume.education}")
            print(f"Work Experience: {resume.work_experience}")
            print(f"Skills: {resume.skills}")
            print()

    def save_resumes(self):
        if not self.resumes:
            print("No resumes to save.")
            return

        try:
            with open("resumes.txt", "w") as f:
                for resume in self.resumes:
                    f.write(f"{resume.name}\n")
                    f.write(f"{resume.email}\n")
                    f.write(f"{resume.phone}\n")
                    f.write(f"{resume.objective}\n")
                    f.write(f"{resume.education}\n")
                    f.write(f"{resume.work_experience}\n")
                    f.write(f"{resume.skills}\n")
                    f.write("\n")
            print("Resumes saved successfully!")
        except IOError:
            print("An error occurred while saving the resumes.")

def main():
    app = ResumeMakerApp()

    while True:
        print("Resume Maker App")
        print("1. Create a new resume")
        print("2. Edit an existing resume")
        print("3. Delete a resume")
        print("4. View all resumes")
        print("5. Save resumes to a file")
        print("6. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            app.create_resume()
        elif choice == 2:
            app.edit_resume()
        elif choice == 3:
            app.delete_resume()
        elif choice == 4:
            app.view_resumes()
        elif choice == 5:
            app.save_resumes()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
