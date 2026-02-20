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


if __name__ == "__main__":
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
