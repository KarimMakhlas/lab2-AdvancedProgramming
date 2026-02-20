import math


# -------------------- Exercise 1 --------------------
def analyze_message(message):
    upper_count = 0
    punct_count = 0
    alpha_count = 0
    consecutive_count = 1
    is_spam = False

    total_chars = len(message)

    for i in range(total_chars):
        char = message[i]

        if char.isupper():
            upper_count += 1

        if char.isalpha():
            alpha_count += 1

        if char == '!' or char == '?':
            punct_count += 1

        if i > 0:
            if message[i] == message[i - 1]:
                consecutive_count += 1
                if consecutive_count > 3:
                    is_spam = True
            else:
                consecutive_count = 1

    caps_ratio = 0
    if alpha_count > 0:
        caps_ratio = upper_count / alpha_count

    if caps_ratio >= 0.6 or punct_count >= 5:
        category = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punct_count >= 3:
        category = "URGENT"
    else:
        category = "CALM"

    return category, is_spam


# -------------------- Exercise 2 --------------------
def get_intersection(set1, set2):
    result = set()
    for element in set1:
        if element in set2:
            result.add(element)
    return result


def get_difference(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    return result


def get_union(set1, set2):
    result = set(set1)
    for element in set2:
        result.add(element)
    return result


def analyze_social_circle(user_a_friends, user_b_friends):
    mutual = get_intersection(user_a_friends, user_b_friends)
    unique_a = get_difference(user_a_friends, user_b_friends)
    unique_b = get_difference(user_b_friends, user_a_friends)
    total_union = get_union(user_a_friends, user_b_friends)

    if len(total_union) == 0:
        jaccard = 0
    else:
        jaccard = len(mutual) / len(total_union)

    return mutual, unique_a, unique_b, jaccard


def get_suggestions(target_user, network):
    suggestions = set()
    user_friends = network.get(target_user, set())

    for friend in user_friends:
        friends_of_friend = network.get(friend, set())
        for fof in friends_of_friend:
            if fof != target_user and fof not in user_friends:
                suggestions.add(fof)

    return suggestions


# -------------------- Exercise 3 --------------------
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


# -------------------- Exercise 4 --------------------
def build_matrix(total_users):
    matrix = []
    for i in range(total_users):
        row = []
        for j in range(total_users):
            row.append(False)
        matrix.append(row)
    return matrix


def follow(matrix, follower, followee):
    matrix[follower][followee] = True


def is_following(matrix, follower, followee):
    return matrix[follower][followee]


def get_followers(matrix, user, total_users):
    followers_list = []
    for i in range(total_users):
        if matrix[i][user] is True:
            followers_list.append(i)
    return followers_list


def get_following(matrix, user, total_users):
    following_list = []
    for j in range(total_users):
        if matrix[user][j] is True:
            following_list.append(j)
    return following_list


def detect_mutual_follows(matrix, total_users):
    pairs = []
    for i in range(total_users):
        for j in range(i + 1, total_users):
            if matrix[i][j] is True and matrix[j][i] is True:
                pairs.append((i, j))
    return pairs


def calculate_influence(matrix, user, total_users):
    followers = len(get_followers(matrix, user, total_users))
    following = len(get_following(matrix, user, total_users))
    return (followers + following) / total_users


if __name__ == "__main__":
    print("===== Exercise 1 =====")
    message = "HELLO!!! Are you there????"
    category, is_spam = analyze_message(message)
    print("Message:", message)
    print("Category:", category)
    print("Spam:", is_spam)

    print("\n===== Exercise 2 =====")
    user_a = {"u1", "u2", "u3"}
    user_b = {"u2", "u3", "u4"}
    mutual, unique_a, unique_b, jaccard = analyze_social_circle(user_a, user_b)
    print("Mutual:", mutual)
    print("Unique A:", unique_a)
    print("Unique B:", unique_b)
    print("Jaccard:", jaccard)

    network = {
        "alice": {"bob", "claire"},
        "bob": {"alice", "david"},
        "claire": {"alice", "emma"},
        "david": {"bob"},
        "emma": {"claire"},
    }
    print("Suggestions for alice:", get_suggestions("alice", network))

    print("\n===== Exercise 3 =====")
    matrix = [
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
    ]
    target_user = 0
    top_k = get_top_k_recommendations(target_user, matrix, 4, 4, 2)
    print("Top similar users:", top_k)
    recs = collaborative_filtering(target_user, matrix, 4, top_k)
    print("Predicted interests:", recs)

    print("\n===== Exercise 4 =====")
    total_users = 4
    follow_matrix = build_matrix(total_users)
    follow(follow_matrix, 0, 1)
    follow(follow_matrix, 1, 0)
    follow(follow_matrix, 2, 1)

    print("Is 0 following 1?", is_following(follow_matrix, 0, 1))
    print("Followers of 1:", get_followers(follow_matrix, 1, total_users))
    print("Following of 1:", get_following(follow_matrix, 1, total_users))
    print("Mutual follows:", detect_mutual_follows(follow_matrix, total_users))
    print("Influence of user 1:", calculate_influence(follow_matrix, 1, total_users))
