class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(self.lyrics)
        
        
a = Song("Hello, it's me, I'm a kinda beautiful, You like just me to find")
a.sing_me_a_song()
