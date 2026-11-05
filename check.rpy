# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
$ persistent.check = False
label check:
    if persistent.check:
        jump d1_engl
    else:
        jump d1

label d1_engl:
    $ yesno = renpy.input("Do you understand what I'm talking about?", length=3)
    $ yesno = yesno.strip()
    if yesno == "Yes":
        n "Really?.."
    elif yesno == "yes":
        n "Please write with a capital letter - you ruin the narrative!"
        jump d1_engl
    elif yesno == "YES":
        n "There is no need for screaming..."
        jump d1_engl
    elif yesno == "No":
        n "Well, I'm not very surprised."
    elif yesno == "no":
        n "Please write with a capital letter - you ruin the narrative!"
        jump d1_engl
    elif yesno == "NO":
        n "There is no need for screaming..."
        jump d1_engl
    else:
        n "I will be honest with you, and I expect the same from you. Please."
        jump d1_engl
    return
