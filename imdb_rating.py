#This script would essentially check all the movies of the defined file types in
#the specified folder over IMDB for their rating, and then it would sort all of 
#in a new folder structure for star rating 0 through 10. Star rating 0 means that
#the movie was not found in the IMDB and/or it actually has zero rating :)
#
#
# Developer: Muralidhar Ramarao
# Contant: muralidhar.ramarao@outlook.com
#
# In case you find any bugs, please report to me at my email.
# How to run?
#-------------
# Pre-requisites:
#  - You need to have Python 2.7 ot higher installed on your system.
#    Does not matter what OS you are using :).
#  - you NEED an active internet connection.
# Just double click on the file, and it will run. It will ask:
# - To enter the movies folder where you have stored the unsorted movies
# - It will not sort the movies already in the Star folder
# - Need help? just type "help"(case in-sensitive) when it asks for the movie folder.

# Last but not the least, I would like to thank IMDB for their service.

#========================================
# Script start                          #
#========================================

import urllib, os, sys, time

def movie_rating(filelist,filepath):
    os.chdir(filepath)
    imdb = "http://www.imdb.com"
    find="/find?q="
    search_tool = "&s=tt"
    movie=filelist
    search_url = imdb + find + movie + search_tool
    url_contents = urllib.urlopen(search_url)
    next_url = ''
    for item in url_contents.readlines():
            if 'findResult odd' in item:
                    next_url = item[(item.find('href=')+ len('href="')):(item.find('img')-5)]
                    break
    search_url = imdb+next_url
    movie_details = urllib.urlopen(search_url)
    if movie_details.code == 200:
        rating = 0
        for item in movie_details.readlines():
                if 'ratingValue' in item:
                        rating = item[(item.find('ratingValue')+ len('ratingValue">')):(item.find('ratingValue')+ len('ratingValue">')+3)]
                        break
        if not float(rating) == 0.0:
            return(float(rating))
        else:
            print("%s was not found. Sorry!" %movie)
            return 0
    else:
        print("I'm experiencing problems connecting to the server. Could you please check the connectivity?")


def main(movie_path, star_path,additional_extn):
    global valid_files
    valid_files = ['mp4','avi','3gp','wmv','vob','mpg','mpeg4','dvx']
    if not additional_extn.strip() == '':
        for i in additional_extn.replace('.','').split(','):
            if i.strip().lower() not in valid_files:
                valid_files.append(i.strip().lower())
        print("New extensions added only for this session: " + str(valid_files))
        time.sleep(2)
    movie_log = movie_path + "\Movies_log.log"
    logging = open(movie_log,"a")
    logging.write(time.ctime())
    logging.write("\n")
    logging.write("Starting the movie Sorting process.\n")
    os.chdir(movie_path)
    count = 0
    for root, subFolders, files in os.walk(movie_path):
        for folder in subFolders:
            pass
        for file in files:
            filename = str(file).rsplit('.',1)[0]
            file_ext = str(file).rsplit('.',1)[1]
            if file_ext.lower() in valid_files:
                source_path = root + "\\"
                source_file = source_path + file
                if 'star' in source_file.lower():
                    pass
                else:
                    count = count + 1
                    rating=movie_rating(filename,movie_path)
                    destination_path = check_destination(star_path,rating)
                    destination_file = destination_path+file
                    logging.write("Source: %s"%source_file)
                    logging.write("Destination: %s"%destination_file)
                    move_files(source_file, destination_file)
                    movie_sorting(filename,rating)
    logging.close()
    return count

def movie_sorting(movie,rating):
    movie_rating = int(rating)
    if movie_rating == 0:
        print("Move to zero Folder")
    else:
        print_rating(movie,movie_rating)

def print_rating(movie,rating):
    print("Moving the movie \"%s\"" %movie + " to \"Star_%d\" folder" %rating)

def move_files(src, dst):
    '''
Moves the src file to destination dst

'''
    try:
        with open(dst) as file:
            pass
    except IOError as e:
        os.rename(src,dst)

def check_destination(dst_path,rating):
    '''(str, int) -> string
This function will check if there is a rating folder in the destination path.
'''
    dst_path1 = dst_path + "\Star_%d\\"%rating
    dst_path2 = dst_path + "\STAR_%d\\"%rating
    dst_path3 = dst_path + "\star_%d\\"%rating
    return_path = ''
    if os.path.exists(dst_path1):
        return_path = dst_path1
    elif os.path.exists(dst_path2):
        return_path = dst_path2
    elif os.path.exists(dst_path3):
        return_path = dst_path3
    else:
        print("Creating Directory " + dst_path1)
        return_path = dst_path
        os.mkdir(dst_path)
    return return_path


def help_me():
    '''
Prints help menu.
'''
    print('''
HELP!!!
This script would sort all the movies in the Movies folder based on the star rating on Internet Movie Database(IMDB).

Note:
1. You Need to provide the Movie Folder and the path where you have(or need to create) the star folder.
2. If you do not enter any path for Star folders(folder where all movies are sorted before), the folders
   will be created in the Movies folder itself.
3. For better results, please enter the exact path(Case Sensitive).
4. A log file will be created in the Movie folder you enter, which will have the infomration about the
   new path of the files.
5. Please note, this will not sort the movies that are already in the Star folders.
6. Currently, the script handles only 'mp4','avi','3gp','wmv','vob','mpg','mpeg4','dvx' files. You have the option to
   consider additional filetypes, but it is restricted to that one time.
7. Please ensure your "star" path does not have any spaces in between.

Created By: Muralidhar Ramarao.
'''
)

if __name__ == '__main__':
    try:
        help_module = ['','help']
        print('''Welcome!

This script can be used to organize your movie collection. It will lookup the rating at IMDB and
sort your movies based on star rating. If you are using this for first time, I would advice to
visit help menu. To go to Help Menu, just type "help" (not case sensitive) in the below prompt.

To exit, Hit Ctrl + C on your keyboard to exit without typing.''')
        print('''--------------------------------------------------------------------------------------''')
        movies_folder = raw_input("Enter the complete folder path where the movies can be found: ")
        movies_moved = 0
        if movies_folder.lower() in help_module:
            if movies_folder:
                help_me()
            else:
                print("\n\n\nHoney, you need to give me the folder. If you need help, enter \"help\" when the script asks for the Movies Folder.")
        else:
            print("Star folder will be from star 1-10. Star 0 for movies not found in IMDB. Otherwise, the folder will look something like \"Star 5\".")
            star_folder = raw_input("Enter the Destination path where Star folder Exists (or to be created): ")
            print("Currently, I consider 'mp4','avi','3gp','wmv','vob','mpg','mpeg4','dvx' files. Do you want me to Consider anything more?")
            additional_extn = raw_input("Enter the additional extensions in comma sep values(optional. hit Enter to exit this): ")
            if star_folder.strip() == '':
                star_folder = movies_folder
            if os.path.exists(movies_folder) and os.path.exists(star_folder):
                movies_moved = main(movies_folder,star_folder,additional_extn)
            else:
                print("Bummer!!! Could not find the folder.")
            print("\n===========END===========")
            print("Finished sorting %d movies. Exiting in 5 Seconds." %movies_moved)
            time.sleep(5)
            exit(0)
    except KeyboardInterrupt:
        pass
    
