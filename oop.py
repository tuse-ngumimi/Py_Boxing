class Student:
    def __init__(self,name,email,matric_number,id_number):
        self.name = name
        self.email = email
        self.__matric_number = matric_number
        self.__id_number = id_number

    def get_matric_number(self):
        return self.__matric_number

    def set_matric_number(self, new_matric_number):
        self.__matric_number = new_matric_number

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number


    def display_student_info(self):
        print(f"Name: {self.name}, Email Address: {self.email}, Matric Number: {self.get_matric_number()}, Id Number: {self.get_id_number()}")


student1 = Student("John Doe", "johndoe@testmail.com", "BHU/22/04/05/067", "FYB445")


print(student1.get_matric_number())

student1.set_matric_number("BHU/22/04/09/0109")
print(student1.get_matric_number())


student1.display_student_info()




#code for bank pin verification

class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number  # Private attribute

    def __validate_pin(self, pin):
        # Private method to validate the PIN
        return len(str(pin)) == 4

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def check_pin(self, pin):
        if self.__validate_pin(pin):
            print("PIN is valid")
        else:
            print("PIN is invalid")

def main():
    account = BankAccount("12345-678")
    print(account.get_account_number())  # Output: 12345-678
    account.check_pin(7676)  # Output: PIN is valid
    account.check_pin(12345)  # Output: PIN is invalid

if __name__ == "__main__":
    main()