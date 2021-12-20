# PicoCTF - script me
# Note: This program is VERY disorganized. I edited the program as errors came up
# during the attempts at getting the flag, and I didn't bother cleaning up the code.
# So, this is REALLY messy. I am sorry for any raging this may cause. :)

while True:
    problem = input("Problem: ").split(" + ")
    paren_count = 0
    high_count1 = 0
    high_count2 = 0
    # current_state values
    # 0 = None
    # 1 = Open
    # 2 = Closed
    # 3 = Done
    current_state = 0
    # Locations to insert (combine) the paretheses
    insert_locs = []
    insert_terms = []
    i = 0
    t = 0
    answer = ""
    newterm = ""
    while len(problem) >= 2:
        for curr in problem:
            t += 1
            print(curr)
            if t == 1:
                # Counting parentheses
                for c in curr:
                    i += 1
                    if c == '(':
                        paren_count += 1
                        if current_state == 0 or current_state == 2:
                            current_state = 1
                    elif c == ')':
                        paren_count -= 1
                        if current_state == 0 or current_state == 1:
                            current_state = 2
                        if current_state != 3 and paren_count == 1:
                            insert_locs.append(i)
                            insert_terms.append(t)
                            current_state = 3
                    if high_count1 < paren_count:
                        high_count1 = paren_count
                        
            if t == 2:
                # Counting parentheses
                for c in curr:
                    i += 1
                    if c == '(':
                        paren_count += 1
                        if current_state == 0 or current_state == 2:
                            current_state = 1
                    elif c == ')':
                        paren_count -= 1
                        if current_state == 0 or current_state == 1:
                            current_state = 2
                        if current_state != 3 and paren_count == 1:
                            insert_locs.append(i)
                            insert_terms.append(t)
                            current_state = 3
                    if high_count2 < paren_count:
                        high_count2 = paren_count
                print(insert_terms)
                # Actual solving
                if insert_terms != []:
                    if insert_terms[0] == 1 and len(insert_terms) == 1:
                        newterm = problem[0][:-1] + problem[1] + ')'
                    elif insert_terms[0] == 2 and len(insert_terms) == 1:
                        newterm = '(' + problem[0] + problem[1][1:]
                    elif high_count1 < high_count2:
                        newterm = '(' + problem[0] + problem[1][1:]
                    elif high_count1 > high_count2:
                        newterm = problem[0][:-1] + problem[1] + ')'
                    else:
                        #newterm = problem[0][:-1] + problem[1] + ')'
                        newterm = problem[0] + problem[1]
                else:
                    newterm = problem[0] + problem[1]
                problem.pop(0)
                problem[0] = newterm
                insert_terms.clear()
                t = 0
                current_state = 0
                high_count1 = 0
                high_count2 = 0
                break

            current_state = 0
    
    # Actual solving of the problem
    for curr in problem:
        answer += curr
    
    print(answer)

                    


    # If at any time the state is 2, and there is 1 parentheses left (()here), then
    # add the thing on the left into the thing on the right before the closing
    # parentheses. If it never gets to 2 opening parentheses, just combine the two
    # from left to right.

        
