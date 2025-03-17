import os

try:
    # Open the file and read its contents
    with open("student_scores.txt", "r") as file:
        lines = file.readlines()

    results = []

    #  Process each line and calculate the average
    for line in lines:
        data = line.strip().split(",")
        name = data[0]
        scores = list(map(int, data[1:]))
        average_score = sum(scores) / len(scores)
        results.append(f"{name}, {average_score:.2f}")

    #  average scores to a new file
    with open("average_scores.txt", "w") as output_file:
        output_file.write("\n".join(results))

    print("Average scores written to 'average_scores.txt'.")

except FileNotFoundError:
    #  Handle missing file error
    print("Error: 'student_scores.txt' file not found.")
