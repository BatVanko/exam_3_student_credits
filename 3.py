def students_credits(*args):
    course_credit = {}
    sum_credits = 0
    course_list = []
    for command in args:
        commands = command.split('-')
        course_name = commands[0]
        credits = int(commands[1])
        max_test_points = int(commands[2])
        diyans_points = int(commands[3])
        coef = diyans_points  / max_test_points
        diyan_credits = credits * coef
        sum_credits += diyan_credits
        course_credit[course_name] = diyan_credits
    if sum_credits >= 240:
        message =  f"Diyan gets a diploma with {sum_credits:.1f} credits."
    else:
        message =  f"Diyan needs {(240 - sum_credits):.1f} credits more for a diploma."

    # print(message)
    course_list.append(message)
    for k,v in sorted(course_credit.items(), key= lambda x:(-x[1])):
        # print(f'{k} - {v:.1f}')
        course_list.append(f'{k} - {v:.1f}')
    return '\n'.join(course_list)




# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
