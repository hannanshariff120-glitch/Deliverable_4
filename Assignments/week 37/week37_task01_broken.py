

# Below is a Python script that calculates grade statistics for a list of students and prints a summary. The script defines two functions: `calculate_grade_stats` and `print_summary`.
def calculate_grade_stats(student_list,pass_threshold = 50):
    total_score = 0
    passed_students = []
    for s in student_list:
        score = float(s['score'])
        if score >= pass_threshold:
            passed_students.append(s['name'])
        total_score += score
    avg=total_score/len(student_list) if len(student_list)>0 else 0.0
    return {'average':avg,'passed':passed_students,'total_count':len(student_list)}


# And now, we define the `print_summary` function that takes the statistics dictionary and an optional course name to print a summary of the results.
def print_summary( stats_dict,course_name="Python 101"):
    print(f"=== Summary for {course_name} ===")
    print(f"Average Score: {stats_dict['average']}")
    print(f"Passed Students: {', '.join(stats_dict['passed'])}")


# Finally, we create a list of student data and call the `calculate_grade_stats` function to compute the statistics, followed by calling `print_summary` to display the results.
data = [{'name':'Charlie','score':'85.5'},{'name':'River','score':'42.0'},{'name':'Jordan','score':'68.0'}]
res = calculate_grade_stats(data)
print_summary(res, course_name="Python 101")