import argparse
from random import sample 
import imgkit
import os
import shutil
import tkinter

BOARD_SIZE = 5 #Make this variable one day, not super important
CSS = "Bingo_Card.css"

html_start = '<html lang="en"><head><link rel="stylesheet" href="Bingo_Card.css"></head><body><script>function Change(node){if (node.className==="on"){node.className="off";}else{node.className="on"} }</script>'
html_end = '</table></body></html>'
#Parser for the optional filname or whether or not to use a freespace
parser = argparse.ArgumentParser()
parser.add_argument('--filename', nargs='?', default="DCOM_Bingo.txt")
parser.add_argument('--free', action='store_true')
parser.add_argument('--html', action='store_true')
parser.add_argument('--count', type=int, nargs='?', default=1)
parser.add_argument('--title', nargs='?', default="DCOM BINGO")
parser.add_argument('--label', nargs='?', default="DCOMS")
args = parser.parse_args()

#Pull lines of the input file into a list for storage
possible_values = [line.rstrip() for line in open(args.filename)]

#Pull out the freespace value and set the new array
if args.free: 
    freespace = possible_values[0]
    possible_values = possible_values[1:]
else:
    freespace = None

dir = "Bingo_Cards"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

#Generate the specified number of cards
for i in range(args.count):
    #Make a new card
    card = html_start

    #Add Title to the Card
    card += "<h2>" + args.title + "</h2>"

    #Buld the topside label row for the bingo card
    card += '<table><tr>'
    for ind, c in enumerate(args.label[0:5]):
        card += '<th id="' + 'label' + str(ind) + '"><div>' + c + '</div></th>'
    card += '</tr>'

    #Pull the values randomly for the bingo card, designate freespace if told to
    if freespace:
        card_values = sample(possible_values, (BOARD_SIZE**2)-1)
        card_values.insert(int((BOARD_SIZE**2)/2), freespace)
    else:
        card_values = sample(possible_values, (BOARD_SIZE**2))

    #Add the actual content of the bingo card via table cells
    for row in range(BOARD_SIZE):
        card += '<tr>'
        for col in range(BOARD_SIZE):
            card += '<td onclick="Change(this)" id="' + 'box' + str(row*BOARD_SIZE+col) + '">' + card_values[row*BOARD_SIZE+col] + '</th>'
        card += '</tr>'

    #HTML for card is now complete, saving to an image
    if not args.html:
        card += html_end
        imgkit.from_string(card, dir+'/Card_' +str(i)+'.jpg', css=CSS)
    else:
        with open(CSS, 'r') as file:
            data = file.read().replace('\n','')
            html_end = "<style>" + data + "</style>" + html_end
            card += html_end
            with open(dir+'/Card_' +str(i)+'.html', 'w+') as output:
                output.write(card)