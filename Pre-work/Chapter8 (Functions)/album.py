def make_album(first_name, album_title, last_name='', tracks=''):
    """Return a dictionary of information about an artist."""
    artist = {'first': first_name, 'last': last_name, 'album' : album_title}
    if last_name:
        artist['last'] = last_name
    if tracks:
        artist['tracks'] = tracks
    return artist


while True:
    print("\nPlease tell me the artis's name, album, and number of tracks:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    a_name = input("Album name: ")
    if a_name == 'q':
        break
    track_count = input("Number of tracks: ")
    if track_count == 'q':
        break

    musician = make_album(f_name, a_name, l_name, track_count)
    print(musician)
    
    
    
musician = make_album('kanye', 'My Beautiful Dark Twisted Fantasy', last_name='west', tracks = 13)
print(musician)