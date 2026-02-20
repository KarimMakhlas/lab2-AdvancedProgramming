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
    total_users = 4
    matrix = build_matrix(total_users)

    follow(matrix, 0, 1)
    follow(matrix, 1, 0)
    follow(matrix, 2, 1)

    print("Is 0 following 1?", is_following(matrix, 0, 1))
    print("Followers of 1:", get_followers(matrix, 1, total_users))
    print("Following of 1:", get_following(matrix, 1, total_users))
    print("Mutual follows:", detect_mutual_follows(matrix, total_users))
    print("Influence of user 1:", calculate_influence(matrix, 1, total_users))
