def findRunnerup():
    if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        arr= sorted(arr)
        runnerUp=0
        maxVal=arr[len(arr)-1]
        for i in arr[::-1]:
            if i!=maxVal:
                print(i)
                break


def NestedLists():
    if __name__ == '__main__':
        studentsandScores=[]
        scores=[]
        names=[]
        lowScore=0.0
        for _ in range(int(input())):
            name = input()
            score = float(input())
            scores.append(score)
            studentsandScores.append([name,score])
        scores.sort()
        lowScore= scores[0]
        for i in scores:
            if i!=lowScore:
                lowScore=i
                break

        for name,score in studentsandScores:
            if score==lowScore:
                names.append(name)

        names.sort()

        for name in names:
            print(name)



def findPercentage():
    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        studentGrade=student_marks[query_name]
        avg=0
        for mark in studentGrade:
            avg+=mark
        
        avg=avg/len(studentGrade)
        print("{:.2f}".format(avg))



def lists():
    if __name__ == '__main__':
        N = int(input())
        list_=[]
        for i in range(N):
            commandVal= input()
            command=commandVal.split(" ")
            
            if(command[0]=="print"):
                print (list_)

            elif (command[0]=="insert"):
                list_.insert(int(command[1]),int(command[2]))

            elif(command[0]=="append"):
                list_.append(int(command[1]))

            elif(command[0]=="remove"):
                list_.remove(int(command[1]))

            elif (command[0]=="pop"):
                list_.pop()

            elif(command[0]=="sort"):
                list_.sort()
                
            elif(command[0]=="reverse"):
                list_.reverse()

def tuples():
    if __name__ == '__main__':
        n = int(input())
        integer_list = map(int, input().split())
        tuple_=tuple(integer_list)
        hash_=hash(tuple_)
        print(hash_)
