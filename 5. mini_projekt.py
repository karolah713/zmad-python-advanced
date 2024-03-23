#Zadanie 5. Napisz klasę Playlist, która będzie reprezentować listę odtwarzania utworów muzycznych. Klasa powinna
# zawierać metody magiczne __add__, __radd__, __getitem__ oraz __setitem__, aby umożliwić łączenie dwóch list odtwarzania,
# dodawanie utworu do listy odtwarzania, uzyskiwanie utworów z listy odtwarzania oraz ustawianie wartości utworów na liście odtwarzania.

class Playlist:

    def __init__(self, playlist):
        if playlist is None:
            self.playlist = []
        else:
            self.playlist = playlist

    def __str__(self):
        return " | ".join(self.playlist)

    def __add__(self, other):
        if isinstance(other, Playlist):
            return Playlist(self.playlist + other.playlist)
        elif isinstance(other, list):
            return Playlist(self.playlist + other)
        elif isinstance(other, str):
            return Playlist(self.playlist + [other])
        else:
            raise TypeError("You are trying to add non-Playlist object.")

    def __radd__(self, other):
        return self.__add__(other)

    def __getitem__(self, index):
        if index < len(self.playlist):
            return self.playlist[index]
        else:
            raise IndexError('This index is out of range')

    def __setitem__(self, index, val):
        self.playlist[index] = val

    def add_song(self, song):
        self.playlist.append(song)


p1 = Playlist(['Bon Jovi-Its my life','Volbeat-Still Counting','Maneskin-Gossip','Sam Ryder-More'])
print(f'Playlist 1:  {p1.playlist}')
p2 = Playlist(['Iron Maiden-Fear of the dark','Nothing But Thieves-Amsterdam'])
print(f'Playlist 2:  {p2.playlist}')

# print both lists together
print(p1 + p2)

print(p1 + ['Track 5'])    # add new song as list
print(p1 + 'Track 6')   # add new song as string

print(['Track 7'] + p2)  # add new song as list
print('Track 8' + p2)   # add new song as string

# get track by index
print(p1[3])

# set another value - track at specified string
print(p2)
p2[1] = 'Song10'
print(p2)

# adding song to playlist
p2.add_song('Author AB-SongXY')
print(p2)
