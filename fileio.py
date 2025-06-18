try:
    with open("students.txt", "r") as input_file:
        student_lines = input_file.readlines()

    processed_students = []

    for student_line in student_lines:
        student_line = student_line.strip()
        fields = student_line.split(",")

        student_name = fields[0].split(":")[1].strip()
        math_score = int(fields[1].split(":")[1])
        science_score = int(fields[2].split(":")[1])
        english_score = int(fields[3].split(":")[1])

        average_score = (math_score + science_score + english_score) / 3
        result_status = "fail" if average_score < 60 else "pass"

        processed_students.append((student_name, round(average_score, 2), result_status))

    with open("results.txt", "w") as output_file:
        for name, avg, status in processed_students:
            output_file.write(f"{name} - Average: {avg} - {status}\n")

except FileNotFoundError:
    print("File not found")
