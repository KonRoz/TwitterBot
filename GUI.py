from tkinter import *
import Bot


newWindow = Tk()

# header of window

money_made = Label(newWindow, text="Christmas Twitter Bot Controller")

# how many total retweets to process
retweets = Label(newWindow, text='Number of ReTweets?')
Er = Entry(newWindow)

# how long will the computer be running the bot
time_period = Label(newWindow, text='Time Period?')
Et = Entry(newWindow)

# what word or phrase should the bot be looking for
query = Label(newWindow, text='What word should the bot look for in tweets')
Eq = Entry(newWindow)

# what should the bot direct message certain users
direct_message = Label(newWindow, text='What should the direct message be?')
Ed = Entry(newWindow)


# will result in a change of screen showing the progress of the bot
def on_click():
    print('Bot is running')
    newWindow.destroy()


# the button that sets bot to run
run = Button(newWindow, text='Run Bot', command=on_click)

# adding each field to the window
money_made.pack()

retweets.pack()
Er.pack()

time_period.pack()
Et.pack()

query.pack()
Eq.pack()

direct_message.pack()
Ed.pack()

run.pack()

# Running the window
newWindow.mainloop()

