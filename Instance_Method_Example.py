class Employee:
    def __init__(self, n1, i1, s1, d1):
        self.name = n1
        self.id = i1
        self.salary = s1
        self.dept = d1
        
E1 = Employee("Arjun", "EMP001", 50000, "IT")
E2 = Employee("Priya", "EMP002", 60000, "HR")
E3 = Employee("Karan", "EMP003", 55000, "Finance")

print(E1.name)
print(E2.salary)
print(E3.dept)