sentence = 'Anti Tracks is a complete solution to protect your privacy and enhance your PC' \
           ' performance. With a simple click Anti Tracks securely erase your internet tracks, ' \
           'computer activities and programs history information stored in many hidden files on your ' \
           'computer.Anti Tracks support Internet Explorer, AOL, Netscape/Mozilla and Opera browsers.' \
           ' It also include more than 85 free plug-ins to extend erasing features to support popular' \
           ' programs such as ACDSee, Acrobat Reader, KaZaA, PowerDVD, WinZip, iMesh, Winamp and much ' \
           'more. Also you can easily schedule erasing tasks at specific time intervals or at Windows' \
           ' stat-up/ shutdown.To ensure maximum privacy protection Anti Tracks implements the US' \
           ' Department of Defense DOD 5220.22-M, Gutmann and NSA secure erasing methods, ' \
           'making any erased files unrecoverable even when using advanced recovery tools'
for ch in ",.?!":
    sentence = sentence.replace(ch, ' ')
print(sentence)
words = sentence.split()
print(words)
words_dic = {}
for word in words:
    if word in words_dic:
        words_dic[word] += 1
    else:
        words_dic[word] = 1
print(words_dic)