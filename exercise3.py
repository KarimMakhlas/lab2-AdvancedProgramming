import math


def cosine_similarity(user_a, user_b, interest_count):
    dot_product = 0
    norm_a = 0
    norm_b = 0

    for i in range(interest_count):
        dot_product += user_a[i] * user_b[i]
        norm_a += user_a[i] * user_a[i]
        norm_b += user_b[i] * user_b[i]

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))


def get_top_k_recommendations(target_user_id, user_matrix, user_count, interest_count, k):
    similarities = []
    target_profile = user_matrix[target_user_id]

    for i in range(user_count):
        if i != target_user_id:
            score = cosine_similarity(target_profile, user_matrix[i], interest_count)
            similarities.append((i, score))

    similarities.sort(key=lambda item: item[1], reverse=True)
    return similarities[:k]


def collaborative_filtering(target_user_id, user_matrix, interest_count, top_k_users):
    recommendations = [0] * interest_count
    target_profile = user_matrix[target_user_id]

    for j in range(interest_count):
        if target_profile[j] == 0:
            sum_scores = 0
            count = 0

            for neighbor_id, score in top_k_users:
                if user_matrix[neighbor_id][j] > 0:
                    sum_scores += user_matrix[neighbor_id][j]
                    count += 1

            if count > 0:
                recommendations[j] = sum_scores / count

    return recommendations


if __name__ == "__main__":
    user_matrix = [
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
    ]

    target_user = 0
    top_k = get_top_k_recommendations(target_user, user_matrix, 4, 4, 2)
    print("Top similar users:", top_k)

    recommendations = collaborative_filtering(target_user, user_matrix, 4, top_k)
    print("Predicted interests:", recommendations)
