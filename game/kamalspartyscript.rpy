##Dialogue starts
label kamalpartyintro:
    show Kamalspartybg with fade
"Everyone seems to be enjoying the party. I guess I should try talking to some of these people."
label kamalsparty:
    if kamalscakescene == 6:
        jump kamalspartyend
    else:
        call screen kamalsparty

##########
##Wallus and Trencil
##########

label partywallusandtrencil:
    if wallusandtrenintro == True:
        jump wallusandtrenafterintro
    else:
        jump partywallusandtrencilintro
label partywallusandtrencilintro:
    $ wallusandtrenintro = True
    $ trencilrequest = True
    show wae at left
    show trensad at right
    wa "Um…. Is that…?"
    tren "*Sighs* No, it’s not blood. It’s that ‘fruit punch’ that Jimothan is serving."
    wa "I was gunna ask if it has alcohol in it."
    tren "As far as I can tell, no. Plus there are children here and I doubt Jimothan would be that irresponsible."
    wa "True, true. But should you be drinking and chewing gum at the same time? Won’t you accidentally swallow it?"
    tren "I can do both at the same time. It keeps my breath fresh."
    hide wae at left
    show was at left
    hide trensad at right
    show trenst at right
    wa "But-... Hmm, who might you be? A new friend of Kamals?"
    tren "The Flower Child mentioned a new friend coming to town. This must be them."
    mc -"Yup, that’d be me!"
    wa "It’s nice to meet you! I’m Wallus. This is Trencil."
    tren "Pleasure."
    menu:
        "Are those fangs I see?":
            hide was at left
            hide trenst at right
            show trensad
            tren "Well, you’re observant, aren’t you?"
            hide trensad
        "I’m guessing you two are the ‘wallflowers’ of the party.":
            hide was at left
            hide trenst at right
            show wae
            wa "Yeah, I guess you could say that."
            hide wae
show trensad
tren "But I’m sure conversing with us will only bore you. Why don’t you go speak with everyone else, they seem curious to meet you."
hide trensad
jump kamalsparty

label wallusandtrenafterintro:
    if gotgumfromtren == True:
        jump aftergumfromtren
    else:
        show trenst
        tren "Hmm? Do you need something?"
        hide trenst
        menu:
            "Hey Trencil, may I have a stick of gum?" if trencilrequest == True:
                jump asktrencilrequest
            "Nevermind, sorry.":
                show trensad
                tren "I hope you enjoy the festivities, then."
                hide trensad
                jump kamalsparty

label asktrencilrequest:
    if trenask4flower == True:
        show trenst
        tren "Have you retreived a flower for me?"
        hide trenst
    else:
        show trensad
        mc "Actually, I wanted to ask you if I may have some gum."
        hide trensad
        show trens
        tren "Hmm? Worried about bad breath, are you? I suppose I could spare one."
        hide trens
        show trensad
        tren "But not for free though."
        mc "Then what do you want?"
        tren "I would like… A flower."
        mc "But… We’re surrounded by flowers, why don’t you just pick one yourself?"
        hide trensad
        show trens
        tren "I would like something in exchange for my gum."
        mc "Okay, I’ll see what I can find."
        hide trens
        $ trenask4flower = True
        jump kamalsparty
menu flower4trencilmenu:
    "I don't have the flower for you yet.":
        show trensad
        tren "Then I leave you to your search."
        hide trensad
        jump kamalsparty
    "I found a flower for you!" if flower4tren ==True:
        show trens
        tren "Splendid!"
        hide trens
label flower4trencil:
    $ gum4kamal = True
    show trens
    mc "Here you go. May I have the gum now?"
    tren "Why thank-you. Here is your gum, as promised."
    hide trens
    show trensad at right
    show wae at left
    wa "Hey, can I have one too?"
    tren "I thought I already gave you one."
    hide wae
    show was at left
    wa "I, uh…. Accidentally swallowed it."
    tren "And you thought I’d do it by accident."
    wa "It was tasty though."
    hide was
    hide trensad
    $ kamalscakescene += 1
    $ gotgumfromtren = True
    $ trencilrequest = False

    jump kamalsparty


label kamalpartyflowerbed:
    if trenask4flower == True:
        mc "Now I need to pick a flower for Trencil."
        $ flower4tren = True
        mc "This should do."
        jump kamalsparty
    else:
        mc "These are some really lovely flowers. I shouldn't disturb them."
        jump kamalsparty
label aftergumfromtren:
    ##TRencil's flower changes depending on what you pick
    show trens at right
    show wan at left
    tren "Ah, I think this flower suits me. I may have to grow some at home."
    hide wan
    show wae at left
    wa "Y'know, I like to do some gardening at home too."
    hide trens
    show trenside at right
    tren "Truly? What is it you grow?"
    hide wae
    show was at left
    wa "Mostly moss."
    hide trenside
    show trens at right
    tren "Interesting. Perhaps, if you have time, you could invite me to see your garden sometime."
    wa "I'd love to!"
    hide was
    hide trens
    jump kamalsparty

##Mirphy
label partymirphy:
    if miprhyintro == False:
        $ kamalscakescene += 1
        show pmirphyangry1c
        mi "Oi! Get out of the shot! I’m trying to capture the vibes in this party!"
        hide pmirphyangry1c
        show pmirphyneutral2c
        mi "Oh, it’s you again! What’s up? Ya having fun here?"
        hide pmirphyneutral2c
        menu:
            "Not really. It’s kinda boring.":
                show pmirphysmile1c
                mi "Well why don’t you try the rubber duck game Boris set up, or singing some Karaoke? I’ll take some pictures of you while you’re at it."
                hide pmirphysmile1c
                jump kamalsparty
            "It’s better now that I’m talking to you.":
                show pmirphyangry2nc
                mi "Are you trying to flirt with me!?"
                mi "Well, I’ll tell you right now that it ain’t going to work."
                hide pmirphyangry2nc
                show pmirphysmile2nc
                mi "You’ll have to do better than than that pick-up line."
                mc "You’d like me to try harder?"
                hide pmirphysmile2nc
                show pmirphydiscomfort2nc
                mi "Well, I uh…"
                hide pmirphydiscomfort2nc
                show pmirphyneutral2nc
                mi "Look, I got some pictures to take. Why don’t you go talk to the other cobbers here. Or go get yerself a cold one."
                mc "What kind of pictures are you taking?"
                hide pmirphyneutral2nc
                jump mirphypictures
            "I’ve been having fun so far. What about you?":
                show pmirphysmile1nc
                mi "This party’s pretty good so far. I’d love to try my voice at Karaoke singing but the girls keep hogging the mic. But more importantly, I’d wish something interesting would happen at this party."
                mc "Interesting how?"
                hide pmirphysmile1nc
                jump mirphypictures

    if miprhyintro == True:
        jump mirphyafterintro
label mirphypictures:
show pmirphydiscomfort1nc
mi "Oh, I don’t know. I’m waiting for a spectacle to happen. One that no one sees coming. If anything, I can at least take a picture of Kamal’s face when he blows out the candles. That outta be nice."
mc "When do we get the cake?"
hide pmirphydiscomfort1nc
show pmirphyneutral1nc
mi "Boris says he’s waiting until everything’s perfect before he brings it out. Whatever that means."
hide pmirphyneutral1nc
show pmirphyangry2nc
mi "It better not involve Martha or anything to do with teeth again! Otherwise I'm kicking him in the head!"
mc "His head's pretty high up."
hide pmirphyangry1nc
show pmirphysmirk2nc
mi "I've got the reach."
hide pmirphysmirk2nc
$ miprhyintro = True

jump kamalsparty

##If you talk to her again
label mirphyafterintro:
    show pmirphyneutral2c
    mi "Don’t mean to be rude to Kamal’s guest, but could ya mosey along? I got some pictures to take here. Why don’t you talk to the others or go get yerself a some pizza?"
    hide pmirphyneutral2c
    show pmirphydiscomfort2c
    mi "Hmmm... Maybe I can get Tim Tam to do something for me..."
    hide pmirphydiscomfort2c
    jump kamalsparty
##Mirphy end convo


##Marv convo
label partymarv:
    if marvfishingfirstaskstat == True:
        jump marvfishingfirstask
    else:
        label marvintro:
            ma "*Sighs* I wish Gillis and his friends would flex their muscles elsewhere. They’re making the fish nervous."
            ma "Hey, you! Make no sudden movements! You’ll scare the fish."
            menu:
                "Sorry, I'll try to be careful.":
                    ma "Thank-you. Not many folks know how to respect a fish's personal space."
                "I don't think the fish really care.":
                    ma "Shows what you know about fish!"
            mc "What's with the kiddie pool full of goldfish, anyway?"
            ma "I’ve been put in charge of the ‘fishing game’. Though this is hardly what I call fishing."
            ma "Real fishing isn't giving you a rubber bowl of water full of pet fish and using a plastic fishing rod to catch 'em with!"
            ma "It's a shame we couldn't have just set this party up by a lake er something."
            ma "Anyways..."
            jump marvfishingfirstask

label marvfishingfirstask:
    if nomoregoldfish == True:
        jump nomorefishmarv
    if nomoregoldfish == False:
        ma "You wanna try yer hand at fishing?"
        $ marvfishingfirstaskstat = True
        jump marvfishingaskmenu

label marvfishingsecask:
    ma "Looks like yer catch got away. That's life sometimes. You want to try again?"
    jump marvfishingaskmenu

menu marvfishingaskmenu:
    "Sure!":
        ma "Alrighty then!"
        ma "But let me give ya some tips before ya start."
        ma "You gotta wait for the fish to take the bait first."
        ma "Then when ya feel a bite, REEL IT IN as fast as you can!"
        ma "If you're too slow, your catch will get away."
        ma "You got all that? Good."
        ma "3..."
        ma "2..."
        ma ".....1! Go!"
        jump fishingwait
    "I think I'll pass.":
        ma "Well, if you change yer mind, you know where to find me."
        jump kamalsparty

label fishingwait:
    $ fishingwait_count = renpy.random.randint(1, 6)
    if fishingwait_count == 1:
        "........"
        jump fishingwait
    elif fishingwait_count == 2:
        "........."
        jump fishingwait
    elif fishingwait_count == 6:
        "......"
        jump fishingwait
    elif fishingwait_count == 3:
        "........"
        jump fishingwait
    elif fishingwait_count == 4:
        "........."
        jump fishingwait
    elif fishingwait_count == 5:
        "..........!!!{nw}"
        jump fishingtimedmenu


label fishingtimedmenu:
    "You got a bite!"
    pause .5
    jump fishingmenu1



label fishingmenu1:
    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'fishingmenu1_slow'
    show screen countdown
    menu:
        "Reel!":
            hide screen countdown
            jump fishingmenu2
        "Wait.":
            hide screen countdown
            jump fishingmenu1_slow
        "Wait.":
            hide screen countdown
            jump fishingmenu1_slow
        "Wait.":
            hide screen countdown
            jump fishingmenu1_slow
label fishingmenu2:
        $ time = 1
        $ timer_range = 1
        $ timer_jump = 'fishingmenu1_slow'
        show screen countdown
        menu:
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow
            "Reel!":
                hide screen countdown
                jump fishingmenu3
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow
label fishingmenu3:
        $ time = 1
        $ timer_range = 1
        $ timer_jump = 'fishingmenu1_slow'
        show screen countdown
        menu:
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow
            "Reel!":
                hide screen countdown
                jump fishingmenu1_end
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow
            "Wait.":
                hide screen countdown
                jump fishingmenu1_slow

label fishingmenu1_slow:
    ma "The goldfish got away."
    jump marvfishingsecask

label fishingmenu1_end:
    ma "You got it! Good catch!"
    ma "Here's yer prize!"
    $ goldfish4gerry = True
    "You won a goldfish in a bag."
    mc "Uh... That's great and all but, what am I supposed to do with the fish? I already have a pet at home."
    ma "Well you can barbeque it, try making sushi, feed it to your pet."
    ma "Or you could try talking to that Gerry feller over at the prize table."
    ma "He sees anything that shines as a valuable."
    $ nomoregoldfish = True
    jump kamalsparty

label nomorefishmarv:
    ma "The fishing game is closed for now. It's dinner time for the little guys."
    "He sprinkles some fishfood into the pool and watches from the side with a delighted smile as the goldfish eat."
    jump kamalsparty

##Jimothan Convo
label partyjim:
    show jin1
    ji "Well hello there! You must be Flower Kid’s friend. Nice to meet ya. The name’s Jimothan. Need a drink? A snack?"
    hide jin1
    menu:
        "I’d like some punch, please!"if jimdrink == False:
            show jiw
            ji "One Punch, coming right up! Haha, just kidding. Here’s your drink, kid."
            hide jiw
            $ jimdrink = True
            "You take a sip just notice something in your cup."
            "You've found a deep purple Cosmo-Lala lipstick."
            $ jeralipstick = True
            jump kamalsparty
        "I’d like a pizza, please!" if jimpizza == False:
            show jin2
            ji "Here you go. You get one slice. Doesn’t look as good as my pizza, though."
            hide jin2
            $ jimpizza = True
            jump kamalsparty
        "I’m good. I just came to say ‘Hi’.":
            show jiw
            ji "Ah, well that’s nice of ya. Hello to you too! Why don’t ya go say hi to my son, Parsley? He doesn’t get out much and it’d be nice if he made more friends."
            hide jiw
            jump kamalsparty
        "I was wondering if you're ever going to give Gerry some water for his glued shoes." if gerryintro == True:
            show jii
            "I will... Eventually."
            "After he stops trying to scam people."
            hide jii
            jump kamalsparty
##Jimothan convo end



##Gerry convo

label partygerry:
    if gerryintro == False:
        show gerw
        ger "Hey there, the name’s Gerry, You want some of these prizes? I can sell ‘em to ya."
        mc "Sell them? I thought you said they were prizes. As in I’d win them."
        hide gerw
        show gers
        ger "You can win them! By having lotsa money!"
        ger "I can give ya anything on this table for, let’s say, ka-billion bucks?"
        mc ".... No."
        "You try to walk away but your feet suddenly feel stuck."
        mc "What the-!?"
        hide gers
        show gere2
        ger "Heheh, going somewhere? I can sell you something to help get rid of that glue."
        ger "Or, if you’d like, I can offer ya an extra special prize."
        mc "What special prize?"
        ##Gerry pulls out Pabit.
        ger "How’s about this little guy?"
        mc "Hey, that’s looks like Boris."
        hide gere2
        show gere1
        ger "Really? Well Tim Tam gave it to me for some extra pizza. Said it had a 'weird vibe' to it. But I’ll let ya have it for, let’s say… 1 tripilion."
        mc "I don’t have that kind of money."
        hide gere1
        show gere2
        ger "Whelp, too bads for you then. You can’ts walk away from this deal. Ya could always work out a loanz."
        hide gere2
        "A splash of water hits your shoes."
        "You look up and see Jimothan has thrown some near your feet to set you free."
        show gerdi1 at left
        show jii at right
        ji "Gerry, no scamming people."
        ger "Awwww, come on. It’s not a scam if it’s a fair deal."
        mc "Hardly fair."
        hide jii
        show jin2 at right
        ji "Better move along before he tries to staple your shoes next."
        hide jin2 at right
        show jii at right
        ji "As for you, Gerry, I think you need to take a break from this before you try to scam anyone else."
        ger "..."
        hide gerdi1
        show gerdi2 at left
        ger "I can’t move. I accidentally glued my feet to the ground too."
        hide jii
        show jis at right
        ji "*sigh* I’ll get some more water."
        hide gerdi2
        hide jis
        $ gerryintro = True
        jump kamalsparty
        ##Gerry convo end.
    else:
        jump gerryafterintro


##Return after convo.
label gerryafterintro:
    if gerrytraded == False:
        show gerdi1
        ger "Ugh, my feet are still stuck. I hopes Jimz come back with the waters."
        hide gerdi1
        show gerdi2
        ger "Oh, it's youz again. Ya lookin' for some freebeez?"
        hide gerdi2
        menu:
            "Not right now, thanks.":
                show gerdi2
                ger "Well then, Scrams! I'm busy right nows."
                ger "Maybe I can get Jerafina to spill her drink this ways."
                hide gerdi2
                jump kamalsparty
            "Actually, I would like that puppet, but-" if whereispabit == True:
                show gere2
                ger "Stupendous! That’ll be twelve billion, please!"
                mc "*But*, I’m not paying for it with money. I’ll trade ya for it."
                hide gere2
                show gere1
                ger "Oh? Ya got my interest. What’s ya got for tradin’?"
                hide gere1
                jump gerrytrade
            "I'm looking to trade, actually." if goldfish4gerry == True:
                show gere1
                ger "Oh? Ya got my interest. What’s ya got for tradin’?"
                hide gere1
                jump gerrytrade
    if gerrytraded == True:
        jump gerryhasgoldfish
menu gerrytrade:
    "I have a goldfish." if goldfish4gerry == True:
        show gere1
        ger "Wait, you have gold?"
        mc "Well, it’s a goldf-"
        hide gere1
        show gere2
        ger "Sold! Here, the puppet is yours."
        hide gere2
        $ goldfish4gerry = False
        $ pabit = True
        show gere2
        ger "With this gold I can buy more glue to get more customers to stick around! Heheh."
        hide gere2
        $ gerrytraded = True
        jump kamalsparty
    "I, uh… Shoot, I have nothing." if goldfish4gerry == False:
        show gere1
        ger "Well, that’s too bad. Comes back when ya gots a milly-on dollarz."
        hide gere1
        jump kamalsparty
    "On second thought, I'll hold off on the trade for a bit":
        show gerdi1
        ger "Oh come on! Don't leave me hanging!"
        ger "Or stuck in glue in thiz case."
        hide gerdi1
        jump kamalsparty

label gerryhasgoldfish:
    show gers
    ger "Oh man, with this gold, I'm gunna make so much moneyz!"
    ger "What will I buy with it first."
    hide gers
    show jii
    ji "I'd recommend a book on basic math, for starters."
    hide jii
    jump kamalsparty
##end gerry convo


label borbraandqsing:
    "The two women you met at the park are singing their hearts out on the karaoke stage. Borbra has a booming voice that sounds off pitch, but she seems to be having fun."
    "And Questionette looks like she’s having fun too but you can’t seem to understand her lyrics."
    jump kamalsparty
label djtiff:
"A fashionable woman with round sunglasses is occupying the DJ booth. Best not to disturb her from her concentration."
jump kamalsparty

label partytrevorandnat:
##Trevor and Nat
show trevorn2 at right
show natbored at left
trev "So if your Dad’s a vampire and  you're half vampire, it would mean you'd have half of his powers, right?"
nat "Yeah. And your point is?"
trev "So have you got, like, super strength and speed? Can you turn into a bat?"
nat "Are you going to interrogate me all night with these dumb questions?"
trev "This information is important! I am conducting a research into supernatural creatures that’ll reshape the world as we know it! Everyone must know the truth!"
nat "Yeah, I’ll believe that as soon as you turn into a real werewolf."
hide natbored
hide trevorn2
show natneutral1 at left
show trevorn1 at right
nat "Oh good, someone else to talk to. Who are you?"
mc "I’m [player_name]. Nice to meet you."
nat "Oh, you’re Flower Kid’s friend, right? They mentioned something about a new friend showing up."
hide trevorn1
show trevorsus at right
trev "Ah yes, the Flower Kid’s mysterious benefactor. Here to ‘help’ everyone with their ‘problems’."
hide natneutral1
show natneutral2 at left
nat "Ugh, Trevor, not everyone is in league with the so-called ‘Orthodominati’."
trev "Then who do you really work for!? Who are your conspirators!?"
hide natneutral2
show natbored at left
nat "I’m going to walk away if you keep on like that."
hide trevorsus
show trevorn2
trev "Oh, eh, um… Okay I’ll stop."
hide natbored
hide trevorn2
jump kamalsparty

##End of Trevor and Nat convo

label partygillputandrandy:

##Gillis, Randy and Putunia
show puth at right
show gillf at left
pu "WE SHOULD ARM WRESTLE! I’LL BET I CAN BEAT YOU!"
gil "You’re on!"
"They wrestle and Gillis feigns a humiliating defeat."
hide puth
hide gillf
show puts at right
show gillh at left
gil "AAAARGH! I’ve been defeated by a small child!"
pu "HAHAHAAA! MY SUPER STRENGTH IS UNMATCHED!"
hide gillh
show gilln2 at left
gil "Owww, the pain! The pain! I’ll never arm wrestle again!"
hide puts
show rans at right
ran "Oh my dear, sweaty Gillis. So ruthlessly tromped and trampled by the great, heroic Putunia The Punisher! Allow me to plant a sweet kiss to soothe thy ailments, my gentile giant~"
hide gilln2
show gillh at left
gil "Heheheh, thanks Randy. I feel better now."
show putn at center
pu "EW, YOU GUYS ARE GROSS!"
hide rans
hide gillh
hide putn
jump kamalsparty
##End of Gillis, Randy and Putunia convo.

##Ronbo, Parsley, and Dallas
label partyparsronanddal:
    if afterpartyprdintro == True:
        jump partyprdafterintro
    else:
        show ronbolaugh at left
        ron "And I says to the guy; ‘Wearing shoes like these is no small feat, buddy!’"
        show parsley drunk1 at center
        pb "BWUAHAHAHA!"
        show dalc at right
        dal "Eeehheheheheh… I don’t get it."
        pb "Oh heeeey, it’s you! How’s going, cheesy calzone!"
        hide ronbolaugh
        hide dalc
        show dals2 at right
        show ronbosmile at left
        ron "Calzone?"
        pb "Sorry, *hic*, I’m just really hungry right now. I could go for just about anything."
        hide parsley drunk1
        hide ronbosmile
        hide dals
        menu:
            "I can probably find you something to eat.":
                show parsley drunk1 at center
                pb "Aw, you will? I’d appreciate it, pal."
                show ronboneutral2 at left
                ron "I’d appreciate it too buddy, he’s giving my rubber nose some funny looks."
                hide parsley drunk1
                hide ronboneutral2
                $ afterpartyprdintro = True
                jump kamalsparty
            "Understandable. I’m kinda hungry too.":
                show parsley drunk2 at center
                show dalc at right
                pb "Where can I get some food around here."
                dal "Don’t be looking at me, dude. You ate three of my paintbrushes and still owe me for that."
                pb "I said I was sorry!"
                hide parsley drunk2
                hide dalc
                $ afterpartyprdintro = True
                jump kamalsparty
            "I have some pizza right here if you want it." if jimpizza == True:
                show parsley drunk1 at center
                pb "Oh man, really! Can I have it?"
                mc "Sure!"
                pb "Aww, thanks buddy! You’re, *hic* you’re my new bestfriend."
                hide parsley drunk1
                "He devours the pizza in one bite."
                show ronboneutral1 at left
                ron "Don’t take it personally kid. He says that to everyone that feeds him."
                show daln at right
                dal "But wait… He said I was his bestfriend too after I gave him my paintbrush… Aw man…"
                hide ronboneutral1
                hide daln
                $ kamalscakescene += 1
                $ parsisfed = True
                $ afterpartyprdintro = True
                jump kamalsparty

label partyprdafterintro:
    if parsisfed == True:
        jump parsleyisfed
    if parsisfed == False:
        show parsley drunk1
        pb "Have ya *hic* Have ya found something to snack on yet?"
        hide parsley drunk1
        menu:
            "I found some pizza for you!" if jimpizza == True:
                show parsley drunk1 at center
                pb "Oh man, really! Can I have it?"
                mc "Sure!"
                pb "Aww, thanks buddy! You’re, *hic* you’re my new bestfriend."
                hide parsley drunk1
                "He devours the pizza in one bite."
                show ronboneutral1 at left
                ron "Don’t take it personally kid. He says that to everyone that feeds him."
                show daln at right
                dal "But wait… He said I was his bestfriend too after I gave him my paintbrush… Aw man…"
                hide ronboneutral1
                hide daln
                $ parsisfed = True
                jump kamalsparty
            "Nothing yet, bud. I'm still looking.":
                show dalc at right
                dal "Please hurry. He gets 'chewy' when he's like this."
                show parsley drunk2 at center
                pb "Liiike what, exactly?"
                hide dalc
                show dals2 at right
                dal "Nothing, buddy. Cheers!"
                hide parsley drunk2
                show parsley drunk1 at center
                pb "Cheers! To good friends, and good..."
                hide parsley drunk1
                show parsley drunk2 at center
                pb "Something."
                hide parsley drunk2
                hide dals2
                jump kamalsparty
label parsleyisfed:
    show parsley drunk2 at center
    pb "*BUUURRRP* Oooh~ I don't feel so good."
    show daln at right
    dal "Dude, did you get into my paints again?"
    pb "No... I think my Dad put anchovies on this pizza."
    pb "I hate anchovies."
    "It might be best to stay out of this convo."
    hide parsley drunk2
    hide daln
    jump kamalsparty

##Jerafina and Lulia
label partyjeraandlu:
    if jeraandluliaintro == True:
        jump jeraluliaafterintro
    else:
        $ jeraandluliaintro = True
        j "Hhhhheyy! Look who showed up to the paaaarrrtyyyy!"
        j "Luuuiilia, this is Flower’s Kid’s new friend. Theeeeey just moved into town."
        lu "Ah, [player_name] right? It’s so nice to meet you. Fina and was just talking about you."
menu:
    "What did she say?":
        lu "Don’t worry, she only had nice things to say."
    "It’s nice to meet you too.":
        lu "Pleasure to meet you as well, dear."
        j "You should hear Lulia siiiiing~ She’s… She’s got the most beautiful voice!"
        lu "Finaaaa~ Enough with the flattery! You’re making me blush!"
        j "What if I gave ya a biiiiig kiss right now?"
        lu "Stop it!"
        mc "Uh, should I leave?"
        j "Oh no no! Don’t go! We were just about to get on stage!"
mc "Are you girls going to sing?"
lu "We’re waiting for Que and Borbra to finish up."
j "I can’t wait to sing with you Lulia, let me just…"
"She reaches inside her purse to look for something but can’t seem to find it."
j "Oh, uh… Uh-oh."
lu "What’s wrong, sweetheart?"
j "My lipstick… I can’t find my lipstick… Oh no… W-Where could it have gone!?"
lu "Now calm down, Fina, I’m sure it couldn’t have gone far. I saw it in your hand when you went to get our drinks. Maybe you dropped it somewhere."
j "Oh no, Lulia, I need to find it. Oh no, I am the worst! You got me the Cosmo-Lala lipstick for my birthday and I go ahead and lose it! Why am I so clumsy!?"
lu "Sweetie, calm down, it’ll be okay. [player_name], would you be a dear and help us find her lipstick?"

menu:
    "Sure, I’ll be on the look out for it.":
        lu "Thank-you, [player_name], having an extra pair of eyes will help."
        jump kamalsparty
    "Actually, I found it already." if jeralipstick == True:
        jump lipstickfound

jump kamalsparty

label jeraluliaafterintro:
    if jerahaslipstick == True:
        jump jeraandluliadancing
    else:
        lu "Have you seen it anywhere yet?"
        menu:
            "No, not yet. Sorry.":
                j "Ooooh nooooo, where could it be?"
                jump kamalsparty
            "I found your lipstick!" if jeralipstick == True:
                jump lipstickfound

label lipstickfound:
    j "What!? You did?"
    "You hand it over to her. She looks overjoyed."
    j "You. Are. Myyyyy Heerrrooooo, darling!"
    "She leans over and kisses you on the cheek."
    j "Thaaaank- you so much, dear. Now I can stop worrying and enjoy the party."
    lu "It looks like the girls are never gunna finish singing. Let's just dance here together!"
    j "I'm with you on that, honey!"
    $ kamalscakescene += 1
    $ jerahaslipstick = True
    jump kamalsparty


label jeraandluliadancing:
    "Jerafina and Lulia are dancing together and seemed to be wrapped up in their own fun."
    jump kamalsparty


##End of Lulia and Jerafina convo


##Boris, Kamal and FK
label partyboriskamandFK:
    if boriskamalfkintro == False:
        show partyhabit worry at left
        bh "I'm getting worried. I couldn't find my puppet anywhere downstairs. I hope he hasn't… Gone anywhere."
        show pokamalworry at right
        k "Don't worry, I'm sure he'll turn up somewhere."
        hide partyhabitworry
        show partyhabit neutral2 at left
        bh "I hope so. Also, why do you keep checking your breath?"
        k "Oh, I had some fish tacos for lunch today and, uh… I didn’t have time to brush my teeth before I came here. They used a lot of fish sauce in it, apparently."
        hide partyhabit neutral2
        show partyhabit worry at left
        bh "Oh dear."
        k "It's okay… So long as no one can smell my breath I'm fine."
        show fkpd at center
        fk "But you can't keep away from everyone for the whole party… Oh! Hey it's [player_name]! How are you enjoying the party?"
        hide partyhabit worry
        hide pkamalworry
        hide fkpd
        menu:
            "You guys seem to be having some trouble with something.":
                show fkpd
                fk "You… Could say that… More just inconveniences than actual problems."
                hide fkpd
            "Kamal looks anxious.":
                show pkamalworry
                k "I, uh… Don’t want anyone to smell what I ate for lunch."
                hide pkamalworry
            "Boris looks kinda stressed.":
                show partyhabit neutral2
                bh "I, uh… I seemed to have misplaced my puppet."
                hide partyhabit neutral2
        mc "Anything I can do to help you guys out?"
        show fkpe2
        fk "Well, we’d hate to make you do any work while you’re trying to enjoy yourself, bud. However, if you find something that can help brighten Kamal or Boris’ mood, let us know."
        mc "I’ll keep an eye out."
        hide fkpe2
        fk "Thanks, [player_name]"
        show fkpe1
        fk "And don’t sweat it if you don’t find them. No one’s gonna hold you accountable if their problems don’t get solved. And if you need to call it a night, let me know."
        mc "I’ll keep that in mind, thanks!"
        hide fkpe1
        $ boriskamalfkintro = True
        jump kamalsparty
    if boriskamalfkintro == True:
        jump afterboriskamalfkintro

label afterboriskamalfkintro:
    if borisandkamalpartypts == 2:
        jump kamalandborishappyatparty
    else:
        show fkpe1
        fk "Hey bud, what’s up? Have you found anything yet? Or are you looking to head home early?"
        hide fkpe1
        menu:
            "I haven’t found anything yet. I’m still looking.":
                show fkpe1 at left
                fk "Ah, no worries then, bud. Take your time. Enjoy some of the pizza while your here."
                show pkamalneutral2
                k "Thankfully, Boris remembered not to accept Jim's invitation to cook for everyone and ordered delivery instead."
                hide fkpe1
                hide pkamalneutral2
                jump kamalsparty
            "I'm thinking I might head home early, actually.":
                show fkpe2
                fk "Alright. You sure about it?"
                hide fkpe2
                jump leavepartyearly
            "I found minty gum for Kamal." if gum4kamal == True:
                show fkpe1
                fk "You did? That’s great! Hey Kamal!"
                hide fkpe1
                jump kamalsgum
            "I found Boris’ puppet." if pabit == True:
                show fkpe2
                fk "Really? That’s great! Where did you find it?"
                mc "Gerry had it."
                hide fkpe2
                show fkpd
                fk "Oh, I might have to have a word with him about taking Boris’ stuff without asking. But thanks for finding it! Hey Boris!"
                hide fkpd
                jump reuniteborispabitparty

label kamalsgum:
    show pkamalneutral2 at right
    k "Eh?"
    show fkpe1 at left
    fk "[player_name] brought some gum. Maybe that can help you with your problem!"
    k "It’s worth a shot."
    hide fkpe1
    hide pkamalneutral2
    "Kamal takes the gum and takes a moment to chew on it."
    show pkamaldelight at right
    k "Mmm! This is pretty good gum. How does my breath smell?"
    show fke2 at left
    fk "Much better now."
    k "What a relief! Thanks a ton, [player_name] I owe you one!"
    mc "I’m glad I could help."
    hide pkamaldelight
    hide fkpe2
    $ kamalscakescene += 1
    $ borisandkamalpartypts += 1
    $ gum4kamal = False
    jump kamalsparty

label reuniteborispabitparty:
    show partyhabit worry at left
    bh "Huh?"
    show fkpe1 at right
    fk "We found Pabit! He’s safe and sound!"
    hide partyhabit worry
    show partyhabit excited at left
    bh "Oh thanks goodness!"
    hide partyhabit excited
    "Boris takes Pabit."
    show partyhabit happy
    bh "Oh, my sweet little boy! I’m so glad to see you’re okay! Don’t you wonder off again!"
    bh "Thank-you so much, [player_name]! And Pabit thanks you too!"
    mc "It was no problem."
    bh "I hope you enjoy the rest of the party!"
    mc "One of the others mentioned the puppet had a ‘weird vibe’ to it."
    hide partyhabit happy
    show partyhabit neutral2
    bh "Aha, I know, the resemblance between him and I can be uncanny sometimes."
    hide partyhabit neutral2
    show partyhabit happy
    bh "Why don’t you go enjoy yourself some ‘snacks’ and drinks? Jimothan loves talking to new guests! And thanks again for all your help!"
    hide partyhabit happy
    $ kamalscakescene += 1
    $ borisandkamalpartypts += 1
    $ pabit = False
    jump kamalsparty

label kamalandborishappyatparty:
    show partyhabit neutral2 at left
    bh "Pabit, where have you been you little trouble-maker? I was worried sick about you!"
    pa "Eye didn't gooo any wearz! A smale childde grabbed me when 1 wasnt luuking!"
    show fkpe1 at right
    fk "Ha ha! You always do such a cute voice for him, Boris!"
    hide partyhabit neutral
    show partyhabit happy at left
    k "Heheh, yeaah. He sure does."
    hide partyhabit happy
    hide fkpe1
    jump kamalsparty



##leave convo

menu leavepartyearly:
    "Yeah":
        show kfpe3
        fk "Alright"
        hide fkpe3
        show fkpe2 at right
        fk "Boris! [player_name] and I are heading home now! Thanks for hosting the party."
        show partyhabit worry at left
        bh "Already? We haven’t even brought out the cake yet. Oh well, I hope you both have a good night then. Thank-you so much for coming!"
        fk "Thanks for having us, Boris! You guys have fun!"
        hide partyhabit
        show pkamalhappy at left
        k "Hey, thanks for coming guys. And it was good to meet you, [player_name]!"
        mc "You too, guys! Thanks for having me here! Good night!"
        "You and Flower Kid leave the party and make your way through the town to your apartment."
        hide pkamalhappy
        hide fkpe2
        jump routeselect
    "No, actualy I think I’ll stay a little longer.":
        show fkpe1
        fk "Alright, enjoy yourself!"
        hide fkpe1
        jump kamalsparty


##Birthday cake scene.

label kamalspartyend:
    show partyhabit happy at right
    bh "I think now is a good time, Flower Kid."
    show fkpe1 at left
    fk "Alright, I’ll go get Wallus!"
    show pkamalneutral2 at center
    k "Huh, what’s going on?"
    bh "It’s a surprise! ;- )"
    hide partyhabit happy
    hide fkpe1
    hide pkamalneutral2
    "Boris leaves you, Kamal and heads for the stairs into the shop. Flower Kid then goes to speak with Wallus who nods and excuses himself from Trencil before he goes to get an extra chair and table from Jimothan. Flower Kid then heads for the stage and gestures for Lulia and Jerafina to finish their song."
    "When they stepped off the stage, Flower Kid stepped into their place and took hold of the mic."
    show fkpe2
    fk "Ahem, attention everyone! It's time to bring out the cake. Gather around!"
    "As they speak Wallus brings the table and chair to the stage and sets up some utensils and plates."
    fk "Kamal, may we ask that you come have a seat?"
    hide fkpe2
    show pkamalneutral1
    k "Oh, uh-... O-ok."
    hide pkamalneutral1
    "He looks nervous but he complies and takes a seat after Flower Kid pulls it out for him."
    show fkpe2
    fk "Tonight, we're also going to have a special guest tonight; A visitor from another world!"
    hide fkpe2
    show pkamalconfused
    k "Wait, what-?"
    hide pkamalconfused
    show fkph
    fk "Iwashi-Kan! You are clear for landing!"
    hide fkph
    "Off to the outskirts of the crowd Tiff begins playing some space synths on her keyboard."
    show pkamalneutral2
    k "What is even going-"
    hide pkamalneutral2
    show pkamalconfused
    k "...."
##Kamal looks like he's about to burst out laughing
    hide pkamalconfused
    show pkamalsurprise
    k "Oh my god…"
    hide pkamalsurprise
    bh "Greetings, Earthlings!"
    "Boris comes walking out of the shadows. Dressed in what looks like a cosplay of a robot made of cardboard."
    bh "I come in peace!"
##Kamal is trying really hard not to laugh.
    show pkamalsurprise at right
    k "Boris!?"
    bh "I do not know who this ‘Boris’ is, Earthling. But what I do know is that it is someone’s VERY special day today!"
    bh "Activating… Cake Delivery Mode!"
    "He makes a series of stiff, robotic movements towards Kamal. Vocalizing a bunch of ‘beeps’, ’boops’ and buzzing sounds. He then opens the secret cardboard compartment in his costume’s chest to reveal an beautifully prepared cake for Kamal."
    "Kamal laughs and claps his hands."
    hide pkamalsurprise
    show pkamalstim at right
    k "Oh my gosh, Boris! This is too much!"
    hide pkamalstim
    "Boris then uses a lighter that extends out of one of his robot arms and starts to sing Happy Birthday to Kamal. Soon everyone, including you, start to sing along and recite the words by heart. Near the end, Kamal's entire face could barely contain his smile as he tried to hide his blushing."
    "When the song concluded, everyone cheered and clapped as they gathered around Kamal; Eagerly awaiting for him to blow out the candles."
    bh "Happy Birthday, my Kamal~ Think of a wish before you blow out the candles!"
    "Kamal paused, gazing over everyone with an unfiltered smile still plastered on his face. You both briefly make eye contact before he gazes at the candles."
    "He takes a deep breath in and blows out the candles."
    "Everyone claps and cheers as Boris removes his helmet and prepares to cut the cake."
    bh "Alright, everyone! Line up for cake!"
    "Before Boris's knife could touch it however, the cake moved. Boris paused, thinking someone had knocked on the table, but then saw the cake jolt. The icing on it’s top layer jiggling at the movement."
    bh "What the-?"
    show ttsh
    tt "Chaos Reigns."
    "The cake then explodes and an opossum emerges, screaming and covered in icing and sprinkles."
    "Everyone else lets out a shriek at the sight and a wave of panic and shocked reactions ensues."
    mi "Now this makes it a great party!!"

##Show CG of the opossum erupting from cake, everyone reacting to it while TimTam eats cake off the ground and Mirphy takes a picture of everything while she gives a peace sign from the bottom corner of the frame.

jump routeselect
