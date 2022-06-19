import sys
import os


def prime(s):
    # your code goes here
    if s > 1:  
        for j in range(2, int(s/2) + 1):  
            if (s % j) == 0:  
                return False
                break  
        else:  
            return True

    else:  
        return False

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
