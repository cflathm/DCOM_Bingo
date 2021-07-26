# DCOM_Bingo

Bongo card generator that uses a list of defined options to generate random bingo cards. Originally designed to be used for Disney Channel Original Movies.

My buddy Wayne and I decided to watch every Disney Channel Original Movie together and rank them. Rather than letting all of that information go to waste, we decided to make a BINGO game out of it with the goal of watching the last half of the movies with a bit more fun. We also think this would be a great way to get other people involved and spread our love of DCOMS. While this BINGO card generator can be easily adapted for literally any other type of bingo system, I would highly recommend watching a DCOM and playing along. I'll add more to this later with instructions. 

## Requirements

A requirements file is provided to help get you started with the project. This was built using python3 and some basic libraries. Before installing the pip file, make sure you have installed the dependencies for imgkit. Information on installing those dependencies can be found at the following link. 
[https://pypi.org/project/imgkit/](https://pypi.org/project/imgkit/)

Once those dependencies are taken care of, you can simply install the needed libraries using the requirements file. Make sure you are using python3 and pip3. 
[pip install -r requirements.txt]

## Running the Program

Once everything is install you should be fairly ready to run the program. You can use the sample document provided, which will generate you a DCOM bingo card. By default, this will make a new folder for bingo codes and generate a single, random bingo card in that folder for you to use. 
```
python Bingo_Card.py
```

### Using your own bingo squares

Additionally, you can specify you own text file, which will be used as the data for the squares in the bingo card. The formate for this file is simply having a multi-line file where each line is a single option for a square. As a warning, you should make sure you Bingo card input file has at least 25 lines or it will error out for not having enough data. Using more than 25 lines is fine as it will simply pick a random 25 and leave the others out. Specifying your own text uses the **--filename** flag. An example of this is as follows:
```
python Bingo_Card.py --filename=custom_file.txt
```

### Custom Titles and Labels

If you are making your own bingo card, you probably want to change the name from DCOM Bingo. Or you could just play DCOM Bingo. If you want a custom tile, you can use the **--title** or **--label** flag. Both, Either, or Neither can be used at the same time. The title flag lets you change the title at the top of the card, which is "DCOM BINGO" by default. The label flag lets you change the letters above the bingo square, which is "DCOMS" by default. If your label is larger than 5 characters it will cut off the trailing characters, and if it is shorter it will leave some blank space. If you want to use multiple words or spaces with the label or title, they must be enclosed in quotes. Using the following command is an example of building a custom card with custom labels and titles. 
```
python Bingo_Card.py --filename=custom_file.txt --title="My Super Bingo Card" --label=SUPER
```

### Using a Free Space

If you want your bingo cards to have a free space, you can simply use the **--free** flag. The way to code is written, the free space is actually taken from the first line of your input file and the flag simply tells the system to get remember it as your freespace. Using the following code you help you build a custom bingo card with a free space (this also works with the basic bingo card if you remove the filename):
```
python Bingo_Card.py --filename=custom_file.txt --free 
```

### Making a bunch of cards

Bingo is always more fun with friends, with the initial goal of this project allowing some friends and me to play bingo together. Bingo isn't very fun if everyone has the same card so this program can make multiple random cards in one batch. This is the main reason why a separate folder is made and the cards are stored in that folder. You can simply use the **--count** argument to specify the number of cards you want to make. When you make more cards, the old cards will always be deleted, just an FYI. The following is an example of how to use the count flag to make five custom cards without free spaces (as before these flags are interchangeable).
```
python Bingo_Card.py --filename=custom_file.txt --count=5
```

## Changing card style
The basic implementation of the cards is done by making an html document then rendering the document as an image. If you want to change the style of your bingo cards, you can simply change the css file that is included. at the moment, you cannot specify you won css file, and you have to modify the one in the repo. The main modifications you may want to do are to the colors used on the card. Right now, it has blue text, purple background, and yellow boxes. You can simply change those variable in the css file to change the colors. You could change other stuff as well, but I can't ensure how that will play out. You may want to change the font size in the td elements or the size of the td elements if you have different lengths of content for the boxes. Right now, the sizes chosen work best for the DCOM list chosen. 

## Check Out My DCOM Ranking
Thanks for reading this far, and I hope you have a fun time playing bingo. If you are curious about my viewpoints of DCOMS, feel free to check out the list I made after watching them (this may still be in progress). [My DCOM Rankings](https://boxd.it/cuNjA)