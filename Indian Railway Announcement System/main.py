# Title :- Indian Railway Announcement System Project.
# Description :- An Indian Railway Announcement System using Python can be a software project that announces the train arrival and departure information, platform numbers, and other relevant details. The system would require a database to store information about the trains and their schedules, which could be updated by the user in this project. For store the data of trains in this project we use the xlsx file that store the train data like name,number,platform etc.

"""
How System Works:-
   --> In the code file there is one railway.mp3 file this is the pre-recorded railway announcement audio. For make new announcement from this announcement we slice the file in such sub-parts like 1_Hindi to 11_Hindi. After divide the audio in subpart we use xlsx database file and generate new train information audio and then run the code or the python can merge all the audio with the subpart and at the end create a announcement for each train and store it into the folder itself.
"""

import pandas as pd #--> use for create dataframe of train data
from pydub import AudioSegment
from gtts import gTTS #--> It converts the text into speech

def textToSpeech(text,filename):
    '''
    This method is use to convert the text data into speck formate from xlsx file
    '''

    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)

def mergeAudios(audios):
    '''
    This method is merge all the subparts with the data that created in TextToSpeech function
    '''

    finalmp3 = AudioSegment.empty()
    for audio in audios:
        finalmp3 += AudioSegment.from_mp3(audio)
    return finalmp3

def generateSkeleton():
    '''
    This method is slicing the railway.mp3 file into the subpart as user requirement and in this function the remaining slice like 2, 4, 6, 8, 10 is generate in generateAnnouncement() method in below.
    '''

    audio = AudioSegment.from_mp3('railway.mp3')

    #1. Generate (kripya dhyan dijiye)
    start = 88000 #--> work in a miliseconds.
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_Hindi.mp3", format="mp3")

    #2. Generate (is from city)

    #3. Geneate (se chalkar)
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_Hindi.mp3", format="mp3")

    #4. Generate (is via city)

    #5. Generate (ke raste)
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_Hindi.mp3", format="mp3")

    #6. Generate (is to city)

    #7. Generate (ko jane wali gaadi sankhya)
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_Hindi.mp3", format="mp3")

    #8. Generate (is train num and name)

    #9. Generate (kuch hi samay me platform number)
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_Hindi.mp3", format="mp3")

    #10. Generate (platform number)

    #11. Generate (par aa rahi hai)
    start = 109000
    finish = 112200
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_Hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    '''
     This method is generate the remaining audio part of the above function and this function is created the different audio for each train based on the xlsx databse.
    '''
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():

        #2. Generate (from city)
        textToSpeech(item['from'],'2_Hindi.mp3')

        #4. Generate (is via city)
        textToSpeech(item['via'], '4_Hindi.mp3')

        #6. Generate (is to city)
        textToSpeech(item['to'], '6_Hindi.mp3')

        #8. Generate (is train num and name)
        textToSpeech(str(item['train_no']) + " " + item['train_name'], '8_hindi.mp3')

        #10. Generate (platform number)
        textToSpeech(item['platform'], '10_Hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcement = mergeAudios(audios)
        announcement.export(f"For_{item['train_name']}_{index+1}.mp3",format="mp3")

if __name__ == '__main__':
    '''
    This is the main method and the program will be executed from this function
    '''

    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...Please Wait!!")
    generateAnnouncement("announcement_hindi.xlsx")
    print("Announcement Genreted Succesfully...")

