def positive_feedback():
    if not ratings:
        return 0
    count = 0
    for rating in ratings:
        if rating >= 4:
            count +=1
    return round((count / len(ratings)) * 100, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback()}%")
