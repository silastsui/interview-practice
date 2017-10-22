#anthony@karat.io

def get_ad_info(purchased_ids, ad_clicks, user_ips):
    condensed_ad_clicks = {}
    for item in ad_clicks:
        item = item.split(",")
        if item[0] == "IP_Address":
            continue
        if item[2] not in condensed_ad_clicks.keys():
            condensed_ad_clicks[item[2]] = item[0]
        else:
            # print condensed_ad_clicks[item[2]]
            list(condensed_ad_clicks[item[2]]).append(item[0])

def common_browsing_history(user1, user2):
    largest_chain = []
    for link in user1:
        if link in user2:
            user1_index = user1.index(link)
            user2_index = user2.index(link)
            temp_chain = []
            while user1[user1_index] == user2[user2_index] :
                temp_chain.append(user1[user1_index])
                user1_index += 1
                user2_index += 1
                if user1_index == len(user1) or user2_index == len(user2):
                    break
            if len(temp_chain) > len(largest_chain):
                largest_chain = temp_chain
    return largest_chain

def get_domain_count(counts):
    domain_counts = {}
    for item in counts:
        item = item.split(",")
        domain_count = item[0]
        domain_name = item[1]
        while domain_name != "":
            if domain_name not in domain_counts:
                domain_counts[domain_name] = int(domain_count)
            else:
                domain_counts[domain_name] += int(domain_count)
            domain_name_prefix = len(domain_name.split(".")[0])
            domain_name = domain_name[domain_name_prefix+1::]
    return domain_counts
