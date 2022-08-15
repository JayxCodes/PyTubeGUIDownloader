import PySimpleGUI as sg
from pytube import YouTube


# Function for downloading YouTube videos
def GetYoutubeFromLink(link, outputPath):
    my_video = YouTube(link)

    print("Video title: ")
    print(my_video.title)

    my_video = my_video.streams.get_highest_resolution()
    my_video.download(output_path=outputPath)


# Function to determine if the link is a YouTube link(I've only seen three formats so far)
def IsYoutubeLink(StringTest):
    if (
        StringTest.startswith('https://youtu.be/') or StringTest.startswith('https://www.youtube.com/') or
        StringTest.startswith('https://music.youtube.com')):
        return True
    else:
        return False


# Define the window's contents
sg.theme('PythonPlus')
layout = [[sg.Text("Input youtube link here, you can input multiple URLs by changing the link after pressing okay")],
          [sg.Text("Please note, while the Ok button is white the video is downloading.")],
          [sg.Input()],
          [sg.Button('Ok'), sg.Button('Exit')]]

# Create the window
window = sg.Window('Youtube Video Downloader', layout)  # Part 3 - Window Definition

# Get the video output path prior to accepting link
filename = sg.popup_get_folder('Where do you want the files to be saved?')

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # Reads to see if provided a valid download link, and path. Allows multiple prior to exit
    if event == 'Ok':
        if values[0] == '' or IsYoutubeLink(values[0]) == False:
            # User failed to provide a valid YouTube link, after warning it resumes back to the loop.
            sg.popup("Please provide a valid youtube link.", title="error", custom_text="I understand.")
        elif not filename:
            # User failed to provide a valid download location. Reapply the old box for an answer.
            sg.popup("Please provide a valid download location", title="error", custom_text="I understand.")
            filename = sg.popup_get_folder('Where do you want the files to be saved?')
        else:
            # Everything worked, it will download the file and the reported area and allow it to loop again with a
            # popup saying it's done!
            GetYoutubeFromLink(values[0], filename)
            sg.popup("Download completed. You can download as many videos as you'd like", title="Completed!",
                     custom_text="Epic, thanks fam!")
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        # Exit the loop because the user clicked Exit
        break

# Finish up by removing from the screen
window.close()
