from gtts import gTTS
import os
mytext = " My Name is Kushagra Gupta, student at SRM Institute of Science and Technology, Ghaziabad"

language = 'en'

output = gTTS(text=mytext,lang=language, slow=False)

output.save("Kushagra.mp3")

os.system("start Kushagra.mp3")
