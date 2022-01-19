#Hello thank you for using my program
#This works with Python3
#What does this program do?: replaces the world map with a desired word
#This is project 3 or chapter 3 from "THE BIG BOOK OF SMALL PYHTON PROJECTS"
#Thanks for using!
print("Bitmap Message, by bluedrummer or https://github.com/bluedrummer")
print("This program will replace the world map with a desired word")
print("Enter the message to display with the bitmap.")

while True:
    word = input(">  ")
    word = str(word)
    if len(word) > 0:
        break
    else:
        print("Please do not input an empty string.(retry)")

def chng_char(input_string, index, char):
    return input_string[0:index] + char + input_string[index+1:]

bitmap =         ["....................................................................",
                  "   **************   *  *** **  *      ******************************",
                  "  ********************* ** ** *  * ****************************** * ",
                  " **      *****************       ******************************     ",
                  "          *************          **  * **** ** ************** *     ",
                  "           *********            *******   **************** * *      ",
                  "            ********           ***************************  *       ",
                  "   *        * **** ***         *************** ******  ** *         ",
                  "                 ******         *************    **   **  *         ",
                  "               ****  *         ***************   *** ***  *         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********         ********          * *** ****      ",
                  "                  *********         ******  *        **** ** * **   ",
                  "                  *********         ****** * *           *** *   *  ",
                  "                    ******          ***** **             *****   *  ",
                  "                    *****            **** *            ********     ",
                  "                   *****             ****              *********    ",
                  "                   ****              **                 *******   * ",
                  "                   ****              **                 *******   * ",
                  "                   ***                                       *    * ",
                  "                   ***                                       *    * ",
                  "...................................................................."]

bitmap_example = ["....................................................................",
                  "   **************   *  *** **  *      ******************************",
                  "  ********************* ** ** *  * ****************************** * ",
                  " **      *****************       ******************************     ",
                  "          *************          **  * **** ** ************** *     ",
                  "           *********            *******   **************** * *      ",
                  "            ********           ***************************  *       ",
                  "   *        * **** ***         *************** ******  ** *         ",
                  "                 ******         *************    **   **  *         ",
                  "               ****  *         ***************   *** ***  *         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********        *************    *  ** ***         ",
                  "                 ********         ********          * *** ****      ",
                  "                  *********         ******  *        **** ** * **   ",
                  "                  *********         ****** * *           *** *   *  ",
                  "                    ******          ***** **             *****   *  ",
                  "                    *****            **** *            ********     ",
                  "                   *****             ****              *********    ",
                  "                   ****              **                 *******   * ",
                  "                   ****              **                 *******   * ",
                  "                   ***                                       *    * ",
                  "                   ***                                       *    * ",
                  "...................................................................."]
line = ""
word_count = 0
for i in range(0, len(bitmap_example[0])):
    line = line + word[word_count]
    word_count += 1
    if word_count == len(word):
        word_count = 0

for i in range(0, len(bitmap_example)):
    bitmap[i] = line

for j in range(0, len(bitmap_example)):
    for k in range(0, len(bitmap_example[0])):
        if bitmap_example[j][k] == " ":
            if bitmap[j][k] != " ":
                bitmap[j] = chng_char(bitmap[j], k, " ")


print()
print("Done here is your bitmap!")
print()
for i in range(0, len(bitmap_example)):
    print(bitmap[i])
print()
print()
print("Thanks for using (bluedrummer at github)")
