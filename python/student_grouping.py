# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
formed_groups = float(students/group_size)
if formed_groups % 2 != 0:
    formed_groups += 1
print(f"Number of groups formed: {int(formed_groups)}")



