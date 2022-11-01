from gtts import gTTS
import os

myText="what are you doing Rruddra nee oru paithiyam unakku ariway illya unga amma oru loose, un appa mattumtha genious"
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("E:/output.mp3")