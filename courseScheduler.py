from queue import Queue


def findOrder(numCourses, prerequisites):
    childCourses = {}

    noDependency = set()

    counter = {}

    dep = {}

    for i in range(numCourses):
        noDependency.add(i)

    for l in prerequisites:
        if(l[1] in childCourses):
            childCourses[l[1]].append(l[0])
        else:
            childCourses[l[1]] = [l[0]]

        if(l[0] in counter):
            counter[l[0]] += 1
        else:
            counter[l[0]] = 1

        # if(counter[l[0]] == 1):
        #     if(1 in dep):
        #         dep.append(l[0])
        #     else:
        #         dep[1] = [l[0]]
        # else:
        #     dep[counter[l[0]]-1].pop(l[0])
        #     if(counter[l[0]] in dep):
        #         dep.append(l[0])
        #     else:
        #         dep[counter[l[0]]] = [l[0]]

        if(l[0] in noDependency):
            noDependency.remove(l[0])

    print(noDependency)
    print(childCourses)
    print(counter)

    q = Queue()

    for i in noDependency:
        q.put(i)

    result = []
    while(not q.empty()):
        course = q.get()
        result.append(course)

        if(course in childCourses):
            for i in childCourses[course]:
                counter[i] -= 1
                if(counter[i] == 0):
                    q.put(i)

    if(len(result) != numCourses):
        return []
    else:
        return result


findOrder(3, [[1, 0], [1, 2], [0, 1]])
