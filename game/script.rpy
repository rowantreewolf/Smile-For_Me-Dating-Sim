# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Kamal_Email = "bunnies66@WYSU.mountain" ## We should define the emails as strings so we dont suffer
define Boris_Email = "Hab_B@PedalMail.cob"
define Petal_Mail = "PetalMail.Staff@PetalMail.com"
define Parsley_Email = "parsleybotch@lawyerup.now"
define Mirphy_Email = "mirphyfotos@flashmail.zoom"
define Jera_Email = "jlt@h.k12.wy.us" # I think this is her but I'm not sure ;w;
define Pabit_Email = "puppetmaster@PedalMail.cob"

## Character Definitions
##Main Characters
define mc = Character("[player_name]")
define bh = Character("Boris") ## I'm using Habits inital for his speaking cue, since we're gonna need b for Borbra.
define k = Character("Kamal")
define fk = Character("Flower Kid")
define mi = Character("Mirphy")
define pb = Character("Parsley")
define j = Character("Jerafina")
define pa = Character("Pabit")

##Side Characters
define pet = Character("[pet_name]")
define q = Character("Questionette")
define b = Character("Borbra")
define pu = Character("Putunina")
define tt = Character("Tim-Tam")
define trev = Character("Trevor")
define tren = Character("Trencil")
define ron = Character("Ronbo")
define mil = Character("Millie")
define wa = Character("Wallus")
define ma = Character("Marv")
define ger = Character("Gerry")
define ji = Character("Jimothan")
define nat = Character("Nat")
define gil = Character("Gillis")
define ran = Character("Randy")
define dal = Character("Dallas")
define lu = Character("Lulia")


##Minor Characters
define ch = Character("Child")
define tpar = Character("The Parent")
define ks = Character("Kasmall")
define everyone = Character("Everyone")


##Fishing Mini-Game##
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

# time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out

########
##Points and secret choices##
######
init:
    ###conversation statements
    $ dog = False
    $ cat = False
    $ pabit = False
    $ kamal_spoiledbd = False
    $ ask4gumtren = False
    $ kamalstinkybreath = False
    $ whereispabit = False
    $ jimafterintro = False
    $ wallusandtrenintro = False
    $ trenask4flower = False
    $ jimdrink = False
    $ jimpizza = False
    $ gerrywantprize = False
    $ goldfish4gerry = False
    $ jeralipstick = False
    $ flower4tren = False
    $ trencilrequest = False
    $ miprhyintro = False
    $ marvintro = False
    $ marvfishingfirstaskstat = False
    $ gerryintro = False
    $ jeraandluliaintro = False
    $ boriskamalfkintro = False
    $ gum4kamal = False
    $ nomoregoldfish = False
    $ gotgumfromtren = False
    $ jerahaslipstick = False
    $ parsisfed = False
    $ gerrytraded = False
    $ afterpartyprdintro = False

    ###points
    $ kamalscakescene = 0
    $ borisandkamalpartypts = 0

    ##RouteTracker
    $ RouteSelected = "None"

## {color=#8412281} {/color}
# The game starts here.
label start:
    scene emailbg
    $ NewEmail = False
    ## Adding the email to the inbox
    $ Add_Email("PetalMail", "PetalMail.Staff@PetalMail.com", "Welcome To PetalMail!", "PetalMail") ## PetalMail = conversations[0]
    $ Add_Email("Boris Habit", Boris_Email, "Hab_B@PedalMail.cob", "Boris_Emails")
    show screen Inbox

label PetalMail:
    $ current_conversation = conversations[0]
    show screen Current_Email
    $ current_conversation.Add_Message("{color=# 8412281} PetalMail", "PetalMail.Staff@PetalMail.com{/color}", "{color=# 8412281} Hello! Your email software has been updated!{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} PetalMail", "PetalMail.Staff@PetalMail.com{/color}", "{color=# 8412281} Thank-you for choosing PetalMail!{/color}", [], []) ## Add Message to the current conversation
    call screen Current_Email ## At the end of the conversation, call the screen again, this stops it from moving onto the next label.


label Boris_Emails:
    show screen Current_Email
    $ current_conversation = conversations[1]
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Deere 'You',{/color}", [],[])##"You" needs to be replaced with mc's name.
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Heyllo! I am Boris Habit, beautiful, glowing 'Florest!!' You do not know me, but mye friend F.K. knows you! : -){/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Flower delivery season is starting and we will soon be verry busy sharing flowers and bouquets of smiles with everyone in our littel town. F.K. tells me you are a fast runner and love to spread habbieness. Well, we need some-one like that very much these days!!{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Let me know soone whether you want to come share in our flower-y task. (F.K. has not said it, but I thinke they may be missinge you.{/color}", [], [])
    $ email_options = {"Reject Job":"BackToMenu", "Accept Job":"Name_change"}
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Flowers and smilies. ~ Boris : -){/color}", ["Accept Job", "Decline"], ["Name_change", "BackToMenu"])
    call screen EmailOptions

label Name_change:
    $ current_conversation.Add_Message("{color=# 8412281}Boris Habit{/color}", Boris_Email, "{color=# 8412281}Wondurrfle! Eye Looke foreward 2 C ing U!{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Oh!, buy the waye.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Our furend tells me That you may habe goone throuughe a Name Change. Could you tell m3e whot it ise??{/color}", [], [])
    $ player_name = ""
    $ player_name = renpy.input("Choose your name.")
    $ player_name = player_name.strip()
    if player_name == "":
        $player_name="Newby"
$ current_conversation.Add_Message("{color=# 8412281}Boris Habit{/color}", Boris_Email, "{color=# 8412281}Whoate a nicce name! :-){/color}", [], [])
$ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}I'will Seei U later, [player_name]!{/color}", [], [])


jump Begin_Game

label Begin_Game:
    hide screen Current_Email
    hide screen Inbox with fade
    show black
    ##Scene starts with an overview of the town
    show town with fade
    "It was Spring in Ruizville; the town you will be calling home for now on. This small town was nestled in a mountain region where it was surrounded by beautiful, wild nature."
    "This place was ideally a nice getaway from the hustle and bustle of the city with many friendly folks to befriend."
    "That was how your friend, nicknamed The Flower Kid, described their home to you. When you shared news that you were looking for a new home, they seemed ecstatic to hear that you were moving in."
    "You received the email from Boris Boris offering me a job at his Flower Shop. You were on your way there now."
    hide town with fade
    show black
    ##Shift scene to Flower Shop exterior
    show flowershopex with fade
    "It was located in a quaint looking area in downtown called Rose Street, and the smell in the air matched the name. You spotted the Flower Shop and made your way towards it. You were looking forward to meeting your old friend and the man himself."

    ##Scene shifts to inside the Flower Shop
    ##Flower Kid sprite appears.
    show fkh1
    fk "Ahhhhh! [player_name], you're here! You finally made it!" ## I took out the [mcs name] to prevent an error.
    mc "Hey, Kid! It's good to see you again too! It's been a while."
    hide fkh1
    show fkde1
    fk "Yeah it has! I haven't seen you since the carnival on the coast. It's been what, a year?"
    mc "It feels longer than that. But I'm happy to say that I've managed to land a place here. Say, is Mr. Boris around? He sent me an email that you guys were looking for help."
    hide fkde1
    show fkn3
    fk "He's just tending to some flowers, follow me!"
    hide fkn3
    hide flowershopex with fade
    show black
    ##You and fk climb up a set of stairs to the garden patio on the roof.
    show roofgarden with fade
    show fkde4
    fk "Boris! [player_name] is here!"
    bh "Oh, good! I'll be just a moment."
    hide fkde4
    ##Cut to CG of the first sighting of Boris. He is tending to the shop's garden and is carrying a massive bundle of flowers of
    ##all sorts in his arms that are ready to be turned into bouquets. He is smiling at the mc in a friendly manner while holding a pair of
    ##pruning shears. The patio itself is overwhelmed with an abundance of flowers and plant-life with the sun shining brightly from above.

    bh "Hello there! I'm so happy you could make it. I hope the move wasn't too difficult."
    mc "It wasn't too bad. It's a pleasure to finally meet you, Mr. Boris."
    mc "What a beautiful garden you have!"
    bh "Why thank-you! But please, call me Boris."
    bh "Please, just call me Boris."
    show habit shy:
        xalign 0.1
    show fke1 at right
    mc "So I hear you have a job offer for me?"
    show habit neutral2
    bh "Ah yes! I do indeed! As I've said in the letter, things are about to get very busy for us. We could use the extra help."
    show habit neutral1
    bh "My friend and I pride ourselves in spreading smiles in the town and making people happy in any way we can. We aren't just a flower delivery service!"
    show habit neutral2
    bh "But sometimes there are people whose unhappiness requires a more personal approach to fix."
    hide fke1
    show fke3 at right
    fk "We sometimes offer help to those who need an extra hand or an outsider to come in to help sort things out. That's where we come in."
    mc "What do you mean by personal approach?"
    hide fke3
    show fke1 at right
    show habit happy2
    bh "Talk to them, get to know them. Be the friend they need in their time. But other than that we usually, as they say, play by ears."
    mc "I thought we were just delivering flowers. What else is there?"
    hide fke1
    show fkn2 at right
    fk "Well, Boris and I had this idea."
    fk "After we’ve been talking about how we can make more people happy. Sometimes flowers just aren’t enough."
    hide fkn2
    show fkn1 at right
    fk "So we decided to provide a semi- secret service where we offer to help people around town with a variety of problems they may face."
    show habit neutral2
    bh "Except for illegal ones. Just, uh, needed to clarify that."
    hide fkn1
    show fkn4 at right
    fk "Don't worry about it, I'll walk you through your first day of the job and introduce you to some friends of mine."
    show habit excited
    bh "Tonight, we are throwing a birthday party for a very special friend of ours. We need your help making sure everyone is able to attend tonight."
    mc "Who's your friend?"
    hide fkn4
    show fke5 at right
    fk "His name is Kamal. You'll get to meet him today while we're out."
    show habit happy2
    bh "I've written down a list of names and what we need from them. When you're done, you come back to the shop then you can go home so you can get ready for the party."
    mc "Wait, I'm going to?"
    bh "Of course! We wouldn't want you to feel left out."
    show habit excited
    bh "But enough dilly-dally! I won't keep you for any longer. Better skip along like a daisy! Toodles!"
    hide habit excited with moveoutleft
    hide fke5 with moveoutright
    hide roofgarden with fade
    show flowershopex with fade
    ##Boris waves goodbye as you and fk walk out to the exterior of the Flower Shop.
    show fkn3
    fk "Okay, so let's check out the list and see who we need to see."

    ##Cut to a list of names including sketches done by Boris of the people left to check on Kamal's party list: Mirphy, Parsley, Jerafina and Kamal himself.
    hide fkn3
    fk "Let's go see Mirphy first. I called her earlier and she said she'll be at the park taking pictures."
    mc "She is a photographer?"
    fk "Yeah, a real artist with the camera. Follow me, I know which park she's at."
    hide flowershopex with fade

label Park_MirphyIntro:
    show park with fade
    ##scene cuts to where they head for the park and start searching for Mirphy. They make it to a more secluded area where there are more trees. fk and the mc spot Borbra and Questionette doing poses while birds are perched on their arms.
    mc "Huh, what are those two doing with all those birds?"
    show fkn5
    fk "Oh hey! I know those two! Borbra! Questionette!"
    hide fkn5
##fk runs towards them before a tall woman steps into view from the bushes to stop them.
    show mirphy camera angry1 with moveinright:
        xalign 0.9
        yalign 0.9
    mi "Oi! Stop right there! You're gonna ruin my shot!"

##Cut to a CG where the birds are frightened and fly up to the tree branches, startling both Borbra and Questionette.

    b "My babies! Don't be scared come back!"
    q "Borbra, made eye soup sticks wick rick time?"
    b "Ya, some sticks might help."
    show fkn4 at left
    fk "Ah, I'm so sorry guys! I didn't mean to ruin the shot."
    show mirphy camera discomfort2
    mi "Oh, hey Flower Kid. It's alright, we'll get the birds back down eventually."
    show mirphy camera neutral1
    extend " But what brings you out here? And who's this?"
    hide fkn4
    show fke3 at left
    fk "Oh, this is my new partner in crime! [player_name]. [player_name], this is Mirphy!"
    mc "Nice to meet you, Mirphy"
    show mirphy smirk1
    mi "Nice to meet ya too. Kid told me they were having a friend move into town. You're a lot shorter than I expected."
    hide fke3
    show bn1 at left
    b "When you're taller than everyone else, everyone is shorter than you expected, Mirphy."
    show mirphy smile1
    mi "Aha! True."
    menu:
        "Tall and beautiful!":
            show mirphy angry1
            mi "Don’t be thinking you can be smooth with me that quick, mate."
        "Tall and talented!":
            show mirphy blush2
            mi "Why thank-you! I know I am."
    hide bn1
    show fkn1 at left
    fk "So Mirphy, we just wanted to check in and make sure you'll be ready for the party tonight."
    show mirphy smile1
    mi "Don't worry kid, I'll be ready with my camera."
    show mirphy smirk1
    mi "I can't wait to snap the look on Kamal's face when we surprise him. He's so easy to spook."
    hide fkn1
    show fke4 at left
    fk "Well we don't want to scare him too much. The last thing we want is for him to have another anxiety attack."
    show mirphy neutral2
    mi "On his birthday, no less. No worries, Kid, I gotcha. Just be sure to tell Trencil that if he decides to show up. That spook should tie some bells to his shoes or something so we can at least hear him coming."
    hide fke4
    show fke5 at left
    fk "Will do, okay see you later Mirphy!"
    show mirphy smile1
    mi "See ya, Kid. Nice meeting ya [player_name]!"
    mc "Nice meeting you too!"
    fk "Bye Borbra, bye Q!"
    hide fke5
    b "Later, kid!"
    show qn2 at left
    q "Au revoir, Flour"
    hide qn2 with moveoutleft
    hide mirphy smile with moveoutright

label Courtroom_ParsleyIntro:
    ##You leave the group as they all wave back at fk and you are pulled aside to speak to them again.
    show fkn3
    fk "Alright, next on the list is Parsley."
    mc "Wait, Parsley? Are we getting groceries too?"
    hide fkn3
    show fke2
    fk "Oh, no. His name is Parsley. But it's also spelt like the herb. He works as a businessman and also a lawyer and a few other jobs on the side too."
    mc "Sounds like a busy man. Where are we gonna find him?"
    hide fke2
    show fke1
    fk "He'll be at the town's courthouse today and will meet us for lunch there. Follow me, I know that way!"
    hide fke1
    hide park with fade
    ##Cut to the exterior of the courthouse and fk and the mc are awaiting to see if Parsley will arrive.
    show courty with fade
    mc "Hmmm… Are we early, Kid?"
    show fke3
    fk "I don’t think so. I think Parsley might be running late again."
    mc "Again?"
    hide fke3
    show fke2
    fk "Yeah, he’s almost always has errands to run; things to do, people to meet, etc."
    mc "How many jobs did you say he had again?"
    fk "Um…"
    hide fke2
    pb "Flower Kid!"

    ##cut to a CG of Parsley running towards the mc and fk while clutching onto a pile of papers, a briefcase and few envelopes and business cards.
    show parsley tired1:
        xalign 0.9
        ypos 400
    show fkde2 at left
    fk "Parsley! You made it!"
    show parsley tired2
    pb "Hey, Kid. Sorry I’m late. I was getting things ready for an important case. Now… What was it you wanted to see me about again?"
    show parsley sweaty1
    pb  "And who’s this?"
    hide fkde2
    show fke2 at left
    fk "This is [player_name], they're my friend that I told you about. They're gunna be working at the flower shop with Boris and I."
    show parsley neutral2
    pb "Oh right, yeah, you said that in your email. It's good to meet you, [player_name]."
    "He reaches forward and shakes the your hand. Very formal-like."
    mc "Nice to meet you too."
    hide fke2
    show fke3 at left
    fk "So Parsley, you think you'll be able to make it to the party tonight?"
    show parsley neutral1
    pb "Wait... what party?"
    hide fke3
    show fke4 at left
    fk "The, uh... The Birthday Party for Kamal. The one I talked to you about in the email?"
    show parsley sweaty1
    pb "Oh shoot! I forgot! Oh my god, that's tonight!?"
    hide fke4
    show fke3 at left
    fk "Oh no... So you're not going to make it?"
    show parsley sweaty2
    pb "Oh no no! It's okay, I can still make it. I, uh, I'll just have to skip our lunch today, however. It's just I got some work I'll need to get done before tonight."
    mc "Oh, that's a shame. I was looking forward to getting to know you."
    show parsley blush
    pb "Heheh, well maybe we'll get a chance later at the party."
    hide fke3
    menu:
        "That's okay, maybe we can talk later.":
            show parsley happy
            pb "Yeah! For sure."
        "Say nothing.":
            show fke5 at left
            fk "It's no big deal, Parsley. So long as you can make it."
            show parsley happy
            pb "Oh yeah, no worries. I wouldn't want to miss seeing everyone again."
            hide fke5
    show parsley neutral3
    pb "Anyways, I better get going. These files won't sort themselves out. See ya, Kid! And it was nice meeting you, [player_name]."
    show fkde4 at left
    fk "Bye!"
    hide parsley neutral3 with moveoutright
    mc "Well, that was brief. I guess we move on then."
    hide fkde4
    show fke4
    fk "Yeah, sorry about that. Parsley is always on a tight schedule."
    mc "I see that."
    fk "Heheh, yeah. Anyways, let's go see Jerafina. Hopefully she's less busy right now. She'll be at the school right now."
    mc "She's in school?"
    hide fke4
    show fke3
    fk "Yeah, she works as a teacher. She's really nice and smart. She should be teaching class with some friends of mine right now. Let's go!"
    hide fke3
    hide courty with fade

label School_JerafinaIntro:
    show schoolex with fade
    ##Scene cuts to them traveling to the school.
    show fkn3
    fk "Alright, we're here. It's almost the end of the second period so she should be free to talk soon. Just follow me, I know where her room is."
    hide fkn3
    hide schoolex with fade
    show schoolin with fade

    ##Cut to the inside of the school building as you both make it to the room where class is taking place and watch from the outside window.
    show fkn5
    fk "There she is. We'll wait out here until she's done."
    mc "Okay."
    hide fkn5
    ##mc watches Jerafina as she teaches the class and you can hear on what's she's saying.

    j "Alright class, who can tell me 3 times 24?"
    tt "It’s possum."
    j "That’s er, I’m sorry what did you say Tim Tam?"
    pu "Tim Tam put a rat in your desk again!"
    j "..."

    ##She looks concerned before she opens her desk and pulls out a rat by the tail. It squeaks as the other kids scream.

    j "Tim Tam, we talked about this. No bringing rats to school."

    ##She goes to the window and casually opens it while the rat flails in her hand. She leans over and lets it go free before returning to class.

    ## Cut to cg of Jerafina going back to teaching the class. She has multiplication math written on the board and all the kids are seated at their desks
    ## with TimTam close to the front. Jerafina is looking at her with pride as she readies her chalk to write the answer while the other kids are cheering
    ## for her. A shy smile on Tim Tam’s face. Also, the rat is trying to sneak back into the classroom through the open window, but it’s far to the side
    ## so that only people who pay close attention will notice.

    j "Tim Tam, I know you know the real answer to this one. Will you try for me?"
    tt "....."
    pu "You can do it Tim Tam!"
    j "We believe in you."

    ## The other kids cheer as well. Before going quiet to hear their answer.

    tt "....!"
    tt "....."
    tt "......72."
    j"That's right! Very good, Tim Tam."

    ##She writes the answer on the board while the kids cheer her on.

    tt "....... :)"

    ##the bell rings, signifying the end of class.

    j "Alright, children, enjoy your lunch break! See you all in half an hour!"

    ##Everyone rushes out and Putunia and Tim Tam come running out towards Flower Kid.

    pu "It's the Flower Hero!"
    tt "Crime accomplice..."
    pu "What are you talking about!? Flower Kid stands for good!"
    j "No shouting in the halls, please."
    pu "Sorry, Miss Tabouli."

    ##Jerafina shows up and greets the two.

    j "Well, if it isn't the Flower Hero themselves. It's good to see you again. And you brought a friend along with you today?"
    pu "FK, come play with us on the jungle gym before everyone else gets there!"
    fk "Sorry, Putunia, I can't today. I have work to do."
    pu "Oh, okay... Tim Tam let's go!"
    tt "We should put butter on the monkey bars again."

    ##They both run off

    j "Now who is this new friend of yours, FK?"
    show fkn2
    fk "This is [player_name], they just moved into town today and I'm helping them get acquainted with everyone."
    j "Well, this certainly a pleasant surprise. I offer a warm welcome kiss on the cheek if you want it."
    menu:
        "I can have one?":
            j "Coming right up!"
            j "Mmmmmmwah!"
            ##She kisses the player on the cheek.
            j "That one is on the house."
            ## she winks
        "No thanks, I’m good.":
            j "Alright then. If you say so."
    hide fkn2
    show fke3
    fk "Anyways, Jerafina, we wanted to check in with you to see if you’ll be able to make it to Kamal’s birthday tonight to help with decorations."
    j "Ooooh? It was tonight? Oh dear, I forgot about it. I had plans for a test tomorrow for the children but…"
    j "Will Lulia be there?"
    hide fke3
    show fkn3
    fk "She’s already agreed to come. Apparently she and Tiff are singing a duet together."
    j "Then I can move the test to another date!"
    mc "Who’s Lulia?"
    j "A Dazzling Star, darling. The Queen of the Stage~."
    hide fkn3
    show fke1
    fk "She and Jerafina go way back. You’ll meet her at the party."
    hide fke1
    show fkn5
    fk "Speaking of which, we need to go see Kamal next. We better get going."
    j "Going so soon? Ah well. I’ll see you later then. And [player_name], you and I will have a date at the Karaoke Stage."
    menu:
        "I don’t sing.":
            j "Oh, you oughta try it though. It's fun to just let loose and sing your heart out."
        "You’re on!":
            j "Hehehe~ I gotta warn you though, I've only been out sung once on the mic."
    j "See youuuu~"
    hide fkn5
    ##Jerafina walks back into the classroom to take care of some work.
    mc "We’re off to see the birthday boy himself?"
    show fke2
    fk "Yup. He works at the Ugly Duckling Dental Clinic in town. Let’s head out to meet him."
    hide fke2
    hide schoolin with fade
    show dentalex with fade
    ##Cuts to the outside of the GDDC and Fk stops the player before they enter.
    show fke2
    fk "Alright, I need to talk to you real quick before we enter."
    mc "Sure, what is it?"
    hide fke2
    show fke3
    fk "Don’t say anything about the party to Kamal, okay? It’s supposed to be a surprise for him so we don’t want to spoil it. We’ll need to avoid talking about it. You think you can do that?"
    hide fke3
    mc "Sure, I can do that."
    show fke1
    fk "Great. Let’s go see him then."
    hide fke1
    hide dentalex with fade
    ##Player and FK enter the clinic and look around and notice Kamal talking to a little kid before their dental appointment. The kid is crying their eyes out and Kamal is knelt down to try to help them feel better.
    show dentalin with fade
    k "Hey buddy, there’s nothing to be scared about, you’re going to be fine"
    ch "I don’t wanna go in here. The dentist is scary! I don’t want them to take my teeth!"
    tpar "I’m sorry, sir. He always gets like this."
    k "No, it’s okay, lots of kids get nervous on their appointments."
    k "Say, would you like to meet a friend of mine? He can help make you feel better."
    ch "Wh-who's your friend."
    k "Why… It's me! The friendly neighbourhood puppet assistant, Kasmall!"

    ##cg of Kamal holding Kasmall to cheer up the kid.

    ks "Hey buddy, it's going to be okay. I know it seems scary but nothing bad's going to happen. We just need to give your teeth a cleaning. Do you brush your teeth at home?"
    ch "Yeah, I do!"
    ks "Very good! Keeping your teeth healthy is very important! And my friends here in the clinic are going to help to make sure your teeth stay white and strong!"
    ks "They’ll take good care of you and your teeth, little buddy! So there’s nothing to be afraid of."
    ch "Mmm… Okay."
    ks "You’ll be okay, buddy. I promise. How about a hug?"
    ch "Okay!"

    ##The puppet and the kid hug and the kid is ushered away to their appointment.

    ##Kamal puts away the puppet before Flower Kid greets them.
    show fkn5
    fk "Hey Kamal! Another busy day here?"
    k "Ah, it’s normal around here. Teeth cleanings are a daily thing here. But hey, I always got time for a visit from you! It’s good to see you, little buddy!"
    k "And who’s this?"
    hide fkn5
    show fkn2
    fk "This is [player_name]! We met while I went away traveling a few months ago and they decided to move into town! So I’m showing them around town to get acquainted with some people."
    k "Well, it’s nice to be acquainted with ya, [player_name]. A friend of Flower Kid is a friend of mine!"
    hide fkn2
    menu:
        "It’s nice to meet you too.":
            jump nospoilkamalsbd
        "Did you make that puppet yourself?":
            k "Heh, thanks. But, eh, no. I asked a friend of mine to make one for me. It helps to cheer up the kids."
            jump nospoilkamalsbd
        "You know, there's a big birthday surprise being set up for you.":
            k "Eh?"
            show fks
            fk"[player_name]!"
            hide fks
            jump spoilkamalsbd

label spoilkamalsbd:
    ##player spoils secret
    show fkn4
    fk "*sigh* I'm sorry Kamal… It was supposed to be a surprise party for you."
    k "Well, to be fair, Boris is always trying to do something extra special for my birthdays. So I kinda saw this coming anyway. It's not your fault."
    hide fkn4
    show fkd
    fk "So this wouldn't have been much of a surprise to begin with… bummer."
    hide fkd
    $ kamal_spoiledbd = True
    jump prologuekamalconvocont
## jump to convo cont

label nospoilkamalsbd:
    ##Player keeps secret
    show fkn3
    fk "Habit says that he’s got something to show on at the flower shop after you’re done work today. Do you think you can come over?"
    k "Don’t tell me it’s another bucket trick he’s come up with."
    hide fkn3
    show fkn4
    fk "Oh no! Nothing like that. He just wants to hang out with you for a while on the roof garden. I'm just checking on his behalf that you remember."
    hide fkn4
    jump prologuekamalconvocont

label prologuekamalconvocont:
    ##convo continue
    show fkn2
    fk "Well, anyways, will you be able to make it to the shop tonight?"
    k "Oh yeah He sent an email about that. Don't worry, I already told him I'll be able to make it. But thanks for stopping by though."
    hide fkn2
    show fkn1
    fk "No problem. Hope the rest of your shift goes well."
    k "Thanks. And hey, it was nice meeting you [player_name]."
    mc "It was nice seeing you too! Later!"
    hide fkn1
    hide dentalin with fade
    show dentalex with fade
    ##You both leave the dental clinic and start making your way back to the flower shop.
    show fkn5
    fk"Alright. That's everyone on the list. Let's head back to the shop and tell Habit we're done."
    mc "Alright then."
    hide fkn5
    ##You both start making your way back when the player notices some noises coming from a alleyway.

    mc "Hey, hold up. Do you hear that."

    ##You and FK pause as you both stop to listen and after a moment they hear the sound of a sad, mewling kitten and a whining pup.
    show fke3
    fk "It sounds like a cat... And a dog? It sounds like something's wrong."
    mc "I heard it over there, let's go check it out."
    hide fke3
    ##The scene cuts to the alleyway where you both heard the sounds and you look around the place to find the animals.

    mc "I swear I heard them here somewhere."
    show fks
    fk "Oh! Sssh! I see them over there."
    hide fks
    ##They point to behind the dumpster and you both move quietly to see a dog and a cat curled up together near the trash.

    mc "Oh my gosh! Who left these poor babies here!?"
    fk "It looks like they were just recently abandoned. Or ran away from home."
    mc "I don't see any collars."
    mc "What do we do?"
    fk "Well... We can't just leave them here, that's for sure."
    fk "Let me think."

    ##You both take a moment to ponder what to do next.
    menu:
        "Try speaking to them.":
            "The dog's ears perk up your voice. It leans closer to try to catch your scent."
        "Hold out your hand for them to sniff.":
            "The cat looks at your hand curiously before it cautiously approaches. It gives it a sniff before it rubs it's head against your fingers and let out a spft purr."

    mc "Well, they seem tame enough."
    show fkn3
    fk "You know... I have been talking to my parents about getting a pet."
    fk "Do you think you can take one home?"
    mc "What? Me? You just said you wanted a pet though."
    hide fkn3
    show fkn2
    fk "Yeah, but I'd only have enough room at home for one. And since you have your own pet-friendly apartment, maybe you can take one home? At least long enough until they can get some help."
    mc "Well..."
    hide fkn2
    menu:
        "I guess I can take the dog.":
            ##player takes dog
            $ dog = True
            show fkn5
            fk "Okay I'll take the cat then."
        "I guess I can take the cat.":
            ##player takes cat
            $ cat = True
            show fkn5
            fk "Okay, I'll take the dog home then."

    ##You get a CG where you take either the cat or the Dog home. Enter description of mc accepting
    hide fkn5
    show fkn3
    fk "You know, if you want to head home, I can go speak with Boris instead. You outta take the little furball home asap!"
    mc "Wouldn't it make me look bad not to show attendance to Boris, though?"
    hide fkn3
    show fkn1
    fk "Don't worry, I'll explain the pet situation to him. It was my idea to begin with anyway. Besides,  you'll be coming to the party tonight. You'll get another chance to speak to him before the day ends."
    mc "Okay, if you're certain. I'll meet you back at the shop later then."
    fk "Later!"
    hide fkn1
    hide dentalex with fade
    show apartmentin with fade

    ##You carry the cat/dog back to your apartment. Stopping by a pet shop to grab some supplies and called a vet to schedule an appointment the next day.
    ##Scene opens to the mc back at their apartment and they share a moment with their new pet as it gets settled in their new home.

    mc "Okay, got you some food, some blankets and bowls. I can get toys tomorrow."

label firstpettalk:
    if dog == True:
        "The dog lets out a little bark of approval."
    if cat == True:
        "The cat doesn't seem to pay attention and looks around the apartment."
    menu:
        "Offer to pet them.":
            if dog == True:
                "The dog starts to pant and smile while you pet it's ears. It looks delighted."
            if cat == True:
                "The cat closes it's eyes briefly and purrs softly as you stroked it's soft fur."
        "Give them some space.":
            "You decide to give them space to get used to their new home."

    mc "I suppose I'll have to come up with a name for you then. What should I call you..."

    ##Naming mechanic appears to give the pet whatever name the mc wants.
    $ pet_name = ""
    $ pet_name = renpy.input("Choose your new friend's name.")
    $ pet_name = pet_name.strip()
    if pet_name == "":
           $pet_name="Fluffy"
    mc "[pet_name]. What do you think of that one?"
    if dog == True:
        "[pet_name] barks happily."
    if cat == True:
        "[pet_name] let out a soft trill."


    mc "Yeah? You like that name?"

    if dog == True:
        "[pet_name] reaches up and licks your face."
    if cat == True:
        "[pet_name] rubs their head against your leg before walking away."

    mc "Aww~ Okay, [pet_name] it is then. Now let's get you cleaned up and fed before I gotta go back, okay?"

    ##cat: "Meow~!"
    ##dog: "Bark!"
    ##The scene cuts to later when the sun has setted and you are getting ready for Kamal's birthday party.

    mc "Okay. Ready to go... Man, this party thing is making me anxious. I barely know any of these people and I have to go hang out with them at a party the same day I just met them. Well, at least Flower Kid will be there. I can always talk to them to feel less out of place."
    mc "I better head out now. It's starting soon. Take care, [pet_name], I'll be back later okay? Try not to make a mess."
    "[pet_name] doesn't seem to hear you as they're happily taking a nap in their new bed."
    hide apartmentin with fade
    show flowershopex with fade

    ##scene cuts to the outside of the Flower Shop. Some lights are on and you see Flower Kid and Habit waiting for you outside.
    show partyhabit happy at right
    show fkpe1 at left
    bh "[player_name]! I'm so happy you made it! How is your new pet? Flower told me all about what happened."
    mc "Oh, they're fine. Thanks for asking!"
    hide fkpe1
    show fkpe2 at left
    fk "So did you pick a name for them?"
    mc "I went with [pet_name]."
    hide fkpe2
    show fkpe1 at left
    fk "Nice."
    hide partyhabit happy
    show partyhabit neutral1 at right
    bh "Alright, you two are the last ones to go inside, I'll wait out here for Kamal to arrive. Now remember, this is supposed to be a surprise party. Wait with the others in the garden until he walks up, alrighty?"
    mc "Okay, I'll see you upstairs then."
    hide partyhabit neutral1
    show partyhabit excited at right
    bh " Hurry! Hurry! He'll be here any minute!"
    hide partyhabit excited
    hide fkpe1
    hide flowershopex with fade
    ##You and fk enter the shop and climb the stares.
    ##Scene cuts to black

    "..........."
    trev "Uh, excuse me… I gotta use the bathroom. How long do we have to wait?"
    mi "You can go after Kamal shows up. Should be any minute now."
    ron "Actually, uh, I gotta use the washroom too. Any chance we can just sneak off?"
    tren "Oh for pity’s sake."
    mil "SSSHHH! Everyone can it! I hear him coming."

    ##Everyone goes quiet while they can hear voices coming closer.

    bh "We’re almost there. Just a few more steps."
    k "Boris, is it really necessary to cover my eyes like this?"
    bh "Don’t worry about it, it’ll be worth it!"

    ##Cut to rooftop garden in party mode. However, if they did, they just get Kamal calmly reacting to the situation, explaining he was told this would happen and Habit’s disappointed expression.
    show Kamalspartybg with fade
    ##Disappointed
    if kamal_spoiledbd == True:
        everyone "Surprise! Happy Birthday Kamal!"
        k "Oh, wow guys! This is so sweet of you all! Thank-you!"
        bh "... You don’t sound as surprised as I thought you would be."
        k "Well, uh… I kinda already knew you guys were planning this. Sorry."
        bh "What!? So the surprise was ruined!?" ##sad face
        k "Oh-no no! It’s not ruined! A birthday party is still a birthday party, Boris! This place looks awesome!"
        k "Look, let’s not worry about the surprise part and just go eat some cake, okay?"
        bh "Okay…"

    ##Cut to bg where the mc can now interact with characters.

    ##Kamal is surprised
    else:
        everyone "Surprise! Happy Birthday Kamal!"
        k "Oh my gosh! What is all this!?"
        bh "It’s a surprise party for YOU, Kamal!"
        fk " We all wanted to throw a big party for you so we all worked together to get everything ready for you!"
        k "Oh my gosh, this is…"

    ##He starts to tear up, but in a happy way

    k "This is so amazing guys… Thank-you so much!"
    fk "Oh, Kamal~"
    bh " Don’t cry."

    ##They both hug him.

    fk "Alright, everyone! Let’s eat some cake!"
    hide Kamalspartybg with fade
    hide black
    jump kamalsparty

    label BackToMenu:
        return
