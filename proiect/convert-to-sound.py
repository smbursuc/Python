import sys
import os
import re
import re
from gtts import gTTS


try:
    if len(sys.argv) != 3:
        print("Usage: py convert-to-sound.py <input directory> <output directory>")
        raise Exception("Wrong number of arguments")
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir) or not os.path.isdir(output_dir):
        print("Usage: py convert-to-sound.py <input directory> <output directory>, directories must exist")
        print("If using absolute paths make sure to use quotation marks for the path")
        print(output_dir)
        raise Exception("Arguments are not directories")

    if not os.access(input_dir, os.R_OK):
        print("Input directory is not readable")
        raise Exception("Input directory is not readable")

    if not os.access(output_dir, os.W_OK | os.X_OK):
        print("Output directory is not writable")
        raise Exception("Output directory is not writable")
    
    for dir, subdirs, root in os.walk(input_dir):
        for file in root:
            file = os.path.join(dir, file)
            f = open(os.path.abspath(file), 'r')
            data = f.read().splitlines()
            if len(data) > 5:
                raise Exception("File has more than 5 lines. There can only be 5 lines or less in the file.")
            for line in data:
                if len(line) > 100:
                    raise Exception("Line is too long. There can only be 100 characters or less in each line.")
                tts = gTTS(text=line, lang="en")
                name = line.replace(" ", "_")
                name = re.sub('\W+','', name) #replace all special characters with nothing \W = not \w and \w = [a-zA-Z0-9_]
                name = name[:20]
                filename = name + ".mp3"
                os.makedirs(output_dir + '\\' + dir,exist_ok=True)
                tts.save(output_dir + '\\' + dir + '\\' + filename)
except Exception as e:
    print()
    print("Exception: " + str(e))
    sys.exit(-1)
