 matches = []
    
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            match = (teams[i], teams[j])
            if match not in matches and (match[1], match[0]) not in matches:
                matches.append(match)
    
    return matches