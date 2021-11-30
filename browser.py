import os
import sys
from os import path

import re

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here


def mkdir(directory, url, text):
    print("URL is:", url)
    filename = re.search(r"(\w+)\.", url).group()[:-1]

    print("filename is: ", filename)

    #current_dir = os.getcwd()
    #print(current_dir)

    if path.exists(directory):
        try:
            os.mkdir(directory)
            os.chdir(os.path(directory))
            print(os.getcwd())
        except FileExistsError:
            pass
        else:
            with open(filename, "w") as file:
                file.write(text)



def main():
    directory = sys.argv[0]

    while True:
        url = input()
        if url == "bloomberg.com":
            # print(bloomberg_com)
            mkdir(directory, url, bloomberg_com)

        elif url == "nytimes.com":
            # print(nytimes_com)
            mkdir(directory, url, nytimes_com)
        elif url == "exit":
            break
        else:
            print("ERROR!")


if __name__ == "__main__":
    main()
