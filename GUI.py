import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.money_made = tk.Label(self, text="Christmas Twitter Bot Controller")

        # how many total retweets to process
        self.retweets = tk.Label(self, text='Number of ReTweets?')
        self.Er = tk.Entry(self)

        # how long will the computer be running the bot
        self.time_period = tk.Label(self, text='Time Period?')
        self.Et = tk.Entry(self)

        # what word or phrase should the bot be looking for
        self.query = tk.Label(self, text='What word should the bot look for in tweets')
        self.Eq = tk.Entry(self)

        # what should the bot direct message certain users
        self.direct_message = tk.Label(self, text='What should the direct message be?')
        self.Ed = tk.Entry(self)

        # the button that sets bot to run
        self.run = tk.Button(self, text='Run Bot', command=self.on_click)

        self.money_made.pack()

        self.retweets.pack()
        self.Er.pack()

        self.time_period.pack()
        self.Et.pack()

        self.query.pack()
        self.Eq.pack()

        self.direct_message.pack()
        self.Ed.pack()

        self.run.pack()

    def on_click(self):
        print('Bot is running')
        if self.Et.get() == '0':
            print('nice')
        else:
            self.destroy()

    def say_hi(self):
        print("hi there, everyone!")

def run():
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    run()