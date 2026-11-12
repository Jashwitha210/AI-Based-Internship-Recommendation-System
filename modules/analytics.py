def calculate_statistics(internships, recommendations):

    statistics = {
        "total_internships": len(internships),
        "total_recommendations": len(recommendations),
    }

    if recommendations:
        scores = [
            recommendation["score"]
            for recommendation in recommendations
        ]

        statistics["average_score"] = round(
            sum(scores) / len(scores),
            2
        )

    else:
        statistics["average_score"] = 0

    return statistics