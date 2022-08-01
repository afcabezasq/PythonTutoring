from collections import defaultdict


def detector():
    
    iphone_dict = defaultdict(list)
    with open("./archives/dhcpdsmall.log","r") as log_file:
        for line in log_file:
            l = line.strip()
            if "iPhone" in l:
                line_array = l.split(" ")
                counter = 0
                for word in line_array:
                    
                    if word == "from":
                        iphone_dict[line_array[counter+1]].append("I was here")
                        break                    
                    counter+=1
    
    print(iphone_dict,len(iphone_dict))


if __name__ == '__main__':
    detector()