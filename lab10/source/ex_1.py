def analyze_grades(student_scores):
    top_scorers = []
    curr_top = -10 ** 18
    average = sum(student_scores.values()) / len(student_scores)
    print(f"Average score: {average}")

    for name, score in student_scores.items():
        if score > curr_top:
            curr_top = score
            top_scorers.clear()
            top_scorers.append(name)
        elif score == curr_top:
            top_scorers.append(name)

        if score >= average:
            print(f"{name} scored above the average with {score:.2f} points.")

    print(f"Max score: {curr_top:.2f}")
    for name in top_scorers:
        print(f"{name} has the highest score")


scores = {
'Alice': 85,
'Bob': 92,
'Charlie': 78,
'Diana': 88
}
analyze_grades(scores)