def course_grader(test_scores):
    # Your code here
    cumulative = 0
    divide_by = 0
    score = 0
    for each in test_scores:
        if each < 50:
            return("fail")
        cumulative = cumulative + each
        divide_by += 1
    score = cumulative / divide_by
    if score >= 70:
        return("pass")
    return("fail")

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
main()
