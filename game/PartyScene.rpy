##Groups: (Kamal, Boris, Flower Kid)= Hanging out near a garden display
##(Ronbo, Parsley, Dallas)= Sharing jokes near the snack table,
##(Gillis, Randy, Putunia)= Flexing by the rubber duck pool,
##(Millie and TimTam)= Sneaking around, waiting to pour salt in the punch bowl,
##(Trevor and Nat) Hanging out near some flowers, with Nat trying to ignore Trevor,
##(Borbra, Questionette, Jerafina, Lulia and Tiff) At the Karaoke stand and Tiff at the DJ booth. Wallus and Trencil = hanging out under the vine patio cover.
##Gerry attending the prize table which is attached to the snack table were
##Jimothan is attending.
##Marv is fishing out of a small, implantable kiddie pool full of rubber duckies and goldfish.
##Mirphy is standing away from the crowds, trying to get a picture with everyone in the frame

##Puzzle:

##With Boris, his puppet has gone missing,
##Kamal: He has bad breath and is really self conscious about it.
##Jerafina lost her lipstick.
##Parsley is starving
##Mirphy can't find any really inspiring to photograph.

##And as you go around and talk to everyone, the player figures out how to solve the problems.

##They find Jerafina's lipstick in the punchbowl (or order a drink from Jim who pours it in your cup wo noticing).
##You give Parsley some pizza from Jim.
##Ask Trencil who gives you some gum in exchange for a flower. You give the gum to Kamal.
##And you find out Gerry was given the puppet by Timtam after they said 'it was too weird' you have to bargain with Gerry to get it back from him.
##May play goldfishing minigame to gain a coin to exchange with but still need to work out code
##Then return Pabit to Boris.

label kamalsparty:
    if kamalscakescene == 6:
        jump kamalspartyend
    else:
        "Everyone seems to be enjoying the party. I guess I should try talking to some of these people."
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
        tren "Hmm?"
        menu:
            "Hey Trencil, may I have a stick of gum?" if trencilrequest == True:
                jump asktrencilrequest
            "Nevermind, sorry.":
                tren "I hope you enjoy the festivities, then."
                jump kamalsparty

label asktrencilrequest:
    if trenask4flower == True:
        tren "Have you retreived a flower for me?"
    else:
        mc "Actually, I wanted to ask you if I may have some gum."
        tren "Hmm? Worried about bad breath, are you? I suppose I could spare one."
        tren "But not for free though."
        mc "Then what do you want?"
        tren "I would like… A flower."
        mc "But… We’re surrounded by flowers, why don’t you just pick one yourself?"
        tren "It’s not the flower itself, I am interested in. But I would like something in exchange for my gum."
        mc "Okay, I’ll see what I can find."
        $ trenask4flower = True
        jump kamalsparty
menu flower4trencilmenu:
    "I don't have the flower for you yet.":
        tren "Then I leave you to your search."
        jump kamalsparty
    "I found a flower for you!" if flower4tren ==True:
        tren "Splendid!"
label flower4trencil:
    $ gum4kamal = True
    mc "Here you go. May I have the gum now?"
    tren "Why thank-you. Here is your gum, as promised."
    wa "Hey, can I have one too?"
    tren "I thought I already gave you one."
    wa "I, uh…. Accidentally swallowed it."
    tren "And you thought I’d do it by accident."
    wa "It was tasty though."
    $ kamalscakescene += 1
    $ gotgumfromtren = True
    $ trencilrequest = False

    jump kamalsparty

    ##Player can click on the background and they will find a highlighted section of a flower patch.
    ##They have the option to pick 3 different kinds of flowers. Each one will tell Trencil something about their personality. After they pick one, they can talk to Trencil again.
    ##Trencil will have a different reaction depending on which flower you give him. But regardless if which one you give him, he will give you a stick of gum to give to Kamal.
    ##Return to interacting with party screen.
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
    tren "Ah, I think this flower suits me. I may have to grow some at home."
    wa "Y'know, I like to do some gardening at home too."
    tren "Truly? What is it you grow?"
    wa "Mostly moss."
    tren "Interesting. Perhaps, if you have time, you could invite me to see your garden sometime."
    wa "I'd love to!"
    jump kamalsparty

##Mirphy
label partymirphy:
    if miprhyintro == False:
        mi "Oi! Get out of the shot! I’m trying to capture the vibes in this party!"
        mi "Oh, it’s you again! What’s up? Ya having fun here?"
        menu:
            "Not really. It’s kinda boring.":
                mi "Well why don’t you try the rubber duck game Boris set up, or singing some Karaoke? I’ll take some pictures of you while you’re at it."
                jump mirphypictures
            "It’s better now that I’m talking to you.":
                mi "Are you trying to flirt with me!?"
                mi "Well, I’ll tell you right now that it ain’t going to work."
                mi "You’ll have to do better than than that pick-up line."
                mc "You’d like me to try harder?"
                mi "Well, I uh…"
                mi "Look, I got some pictures to take. Why don’t you go talk to the other cobbers here. Or go get yerself a cold one."
                mc "What kind of pictures are you taking?"
                jump mirphypictures
            "I’ve been having fun so far. What about you?":
                mi "This party’s pretty good so far. I’d love to try my voice at Karaoke singing but the girls keep hogging the mic. But more importantly, I’d wish something interesting would happen at this party."
                mc "Interesting how?"
                jump mirphypictures

    if miprhyintro == True:
        jump mirphyafterintro
label mirphypictures:
mi "Oh, I don’t know. I’m waiting for a spectacle to happen. One that no one sees coming. If anything, I can at least take a picture of Kamal’s face when he blows out the candles. That outta be nice."
mc "When do we get the cake?"
mi "Boris says he’s waiting until everything’s perfect before he brings it out. Whatever that means."
mi "It better not involve Martha or anything to do with teeth again! Otherwise I'm kicking him in the head!"
mc "His head's pretty high up."
mi "I've got the reach."
$ miprhyintro = True

jump kamalsparty

##If you talk to her again
label mirphyafterintro:
    mi "Don’t mean to be rude to Kamal’s guest, but could ya mosey along? I got some pictures to take here. Why don’t you talk to the others or go get yerself a some pizza?"
    mi "Hmmm... Maybe I can get Tim Tam to do something for me..."
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
    ji "Well hello there! You must be Flower Kid’s friend. Nice to meet ya. The name’s Jimothan. Need a drink? A snack?"
    menu:
        "I’d like some punch, please!"if jimdrink == False:
            ji "One Punch, coming right up! Haha, just kidding. Here’s your drink, kid."
            $ jimdrink = True
            "You take a sip just notice something in your cup."
            "You've found a deep purple Cosmo-Lala lipstick."
            $ jeralipstick = True
            jump kamalsparty
        "I’d like a pizza, please!" if jimpizza == False:
            ji "Here you go. You get one slice. Doesn’t look as good as my pizza, though."
            $ jimpizza = True
            jump kamalsparty
        "I’m good. I just came to say ‘Hi’.":
            ji "Ah, well that’s nice of ya. Hello to you too! Why don’t ya go say hi to my son, Parsley? He doesn’t get out much and it’d be nice if he made more friends."
            jump kamalsparty
        "I was wondering if you're ever going to give Gerry some water for his glued shoes." if gerryintro == True:
            "I will... Eventually."
            "After he stops trying to scam people."
            jump kamalsparty
##Jimothan convo end



##Gerry convo

label partygerry:
    if gerryintro == False:
        ger "Hey there, the name’s Gerry, You want some of these prizes? I can sell ‘em to ya."
        mc "Sell them? I thought you said they were prizes. As in I’d win them."
        ger "You can win them! By having lotsa money!"
        ger "I can give ya anything on this table for, let’s say, ka-billion bucks?"
        mc ".... No."
        "You try to walk away but your feet suddenly feel stuck."
        ##The player tries to move but their shoes are glued in the spot.
        mc "What the-!?"
        ger "Heheh, going somewhere? I can sell you something to help get rid of that glue."
        ger "Or, if you’d like, I can offer ya an extra special prize."
        mc "What special prize?"
        ##Gerry pulls out Pabit.
        ger "How’s about this little guy?"
        mc "Hey, that’s looks like Boris."
        ger "Really? Well Tim Tam gave it to me for some extra pizza. Said it had a 'weird vibe' to it. But I’ll let ya have it for, let’s say… 1 tripilion."
        mc "I don’t have that kind of money."
        ger "Whelp, too bads for you then. You can’ts walk away from this deal. Ya could always work out a loanz."
        "A splash of water hits your shoes."
        "You look up and see Jimothan has thrown some near your feet to set you free."
        ji "Gerry, no scamming people."
        ger "Awwww, come on. It’s not a scam if it’s a fair deal."
        mc "Hardly fair."
        ##Jimothan looks at player.
        ji "Better move along before he tries to staple your shoes next."
        ji "As for you, I think you need to take a break from this before you try to scam anyone else."
        ger "... I can’t move. I accidentally glued my feet to the ground too."
        ji "*sigh* I’ll get some more water."
        $ gerryintro = True
        jump kamalsparty
        ##Gerry convo end.
    else:
        jump gerryafterintro


##Return after convo.
label gerryafterintro:
    if gerrytraded == False:
        ger "Ugh, my feet are still stuck. I hopes Jimz come back with the waters."
        ger "Oh, it's youz again. Ya lookin' for some freebeez?"
        menu:
            "Not right now, thanks.":
                ger "Well then, Scrams! I'm busy right nows."
                ger "Maybe I can get Jerafina to spill her drink this ways."
                jump kamalsparty
            "Actually, I would like that puppet, but-" if whereispabit == True:
                ger "Stupendous! That’ll be twelve billion, please!"
                mc "*But*, I’m not paying for it with money. I’ll trade ya for it."
                ger "Oh? Ya got my interest. What’s ya got for tradin’?"
                jump gerrytrade
            "I'm looking to trade, actually." if goldfish4gerry == True:
                ger "Oh? Ya got my interest. What’s ya got for tradin’?"
                jump gerrytrade
    if gerrytraded == True:
        jump gerryhasgoldfish
menu gerrytrade:
    "I have a goldfish." if goldfish4gerry == True:
        ger "Wait, you have gold?"
        mc "Well, it’s a goldf-"
        ger "Sold! Here, the puppet is yours."
        $ goldfish4gerry = False
        $ pabit = True
        ger "With this gold I can buy more glue to get more customers to stick around! Heheh."
        $ gerrytraded = True
        jump kamalsparty
    "I, uh… Shoot, I have nothing." if goldfish4gerry == False:
        ger "Well, that’s too bad. Comes back when ya gots a milly-on dollarz."
        jump kamalsparty
    "On second thought, I'll hold off on the trade for a bit":
        ger "Oh come on! Don't leave me hanging!"
        ger "Or stuck in glue in thiz case."
        jump kamalsparty

label gerryhasgoldfish:
    ger "Oh man, with this gold, I'm gunna make so much moneyz!"
    ger "What will I buy with it first."
    ji "I'd recommend a book on basic math, for starters."
    jump kamalsparty
##end gerry convo

##Borbra and Questionette BG observation only
label borbraandqsing:
    if jerahaslipstick == True:
        "Borbra and Questionette are taking a rest by the food stand. Laughing with Jim over some punch."
        jump kamalsparty
    if jerahaslipstick == False:
        "The two women you met at the park are singing their hearts out on the karaoke stage. Borbra has a booming voice that sounds off pitch, but she seems to be having fun."
        "And Questionette looks like she’s having fun too but you can’t seem to understand her lyrics."
jump kamalsparty
label djtiff:
##Tiff BG observation only
"A fashionable woman with round sunglasses is occupying the DJ booth. Best not to disturb her from her concentration."
jump kamalsparty

label partytrevorandnat:
##Trevor and Nat
trev "So if your Dad’s a vampire and  you're half vampire, it would mean you'd have half of his powers, right?"
nat "Yeah. And your point is?"
trev "So have you got, like, super strength and speed? Can you turn into a bat?"
nat "Are you going to interrogate me all night with these dumb questions?"
trev "This information is important! I am conducting a research into supernatural creatures that’ll reshape the world as we know it! Everyone must know the truth!"
nat "Yeah, I’ll believe that as soon as you turn into a real werewolf."
nat "Oh good, someone else to talk to. Who are you?"
mc "I’m [player_name]. Nice to meet you."
nat "Oh, you’re Flower Kid’s friend, right? They mentioned something about a new friend showing up."
trev "Ah yes, the Flower Kid’s mysterious benefactor. Here to ‘help’ everyone with their ‘problems’."
nat "Ugh, Trevor, not everyone is in league with the so-called ‘Orthodominati’."
trev "Then who do you really work for!? Who are your conspirators!?"
nat "I’m going to walk away if you keep on like that."
trev "Oh, eh, um… Okay I’ll stop."
jump kamalsparty

##End of Trevor and Nat convo

label partygillputandrandy:

##Gillis, Randy and Putunia
pu "WE SHOULD ARM WRESTLE! I’LL BET I CAN BEAT YOU!"
gil "You’re on!"
##They wrestle and Gillis feigns a humiliating defeat.
gil "AAAARGH! I’ve been defeated by a small child!"
pu "HAHAHAAA! MY SUPER STRENGTH IS UNMATCHED!"
gil "Owww, the pain! The pain! I’ll never arm wrestle again!"
ran "Oh my dear, sweaty Gillis. So ruthlessly tromped and trampled by the great, heroic Putunia The Punisher! Allow me to plant a sweet kiss to soothe thy ailments, my gentile giant~"
gil "Heheheh, thanks Randy. I feel better now."
pu "EW, YOU GUYS ARE GROSS!"
jump kamalsparty
##End of Gillis, Randy and Putunia convo.
##Ronbo, Parsley, and Dallas
label partyparsronanddal:
    if afterpartyprdintro == True:
        jump partyprdafterintro
    else:
        ron "And I says to the guy; ‘Wearing shoes like these is no small feat, buddy!’"
        pb "BWUAHAHAHA!"
        dal "Eeehheheheheh… I don’t get it."
        pb "Oh heeeey, it’s you! How’s going, cheesy calzone!"
        ron "Calzone?"
        pb "Sorry, *hic*, I’m just really hungry right now. I could go for just about anything."
        menu:
            "I can probably find you something to eat.":
                pb "Aw, you will? I’d appreciate it, pal."
                ron "I’d appreciate it too buddy, he’s giving my rubber nose some funny looks."
                $ afterpartyprdintro = True
                jump kamalsparty
            "Understandable. I’m kinda hungry too.":
                pb"Where can I get some food around here."
                dal "Don’t be looking at me, dude. You ate three of my paintbrushes and still owe me for that."
                pb "I said I was sorry!"
                $ afterpartyprdintro = True
                jump kamalsparty
            "I have some pizza right here if you want it." if jimpizza == True:
                pb "Oh man, really! Can I have it?"
                mc "Sure!"
                pb "Aww, thanks buddy! You’re, *hic* you’re my new bestfriend."
                "He devours the pizza in one bite."
                ron "Don’t take it personally kid. He says that to everyone that feeds him."
                dal "But wait… He said I was his bestfriend too after I gave my my paintbrush… Aw man…"
                $ kamalscakescene += 1
                $ parsisfed = True
                $ afterpartyprdintro = True
                jump kamalsparty

label partyprdafterintro:
    if parsisfed == True:
        jump parsleyisfed
    if parsisfed == False:
        pb "Have ya *hic* Have ya found something to snack on yet?"
        menu:
            "I found some pizza for you!" if jimpizza == True:
                pb "Oh man, really! Can I have it?"
                mc "Sure!"
                pb "Aww, thanks buddy! You’re, *hic* you’re my new bestfriend."
                "He devours the pizza in one bite."
                ron "Don’t take it personally kid. He says that to everyone that feeds him."
                dal "But wait… He said I was his bestfriend too after I gave my my paintbrush… Aw man…"
                $ parsisfed = True
                jump kamalsparty
            "Nothing yet, bud. I'm still looking.":
                dal "Please hurry. He gets 'chewy' when he's like this."
                pb "Liiike what, exactly?"
                dal "Nothing, buddy. Cheers!"
                pb "Cheers! To good friends, and good..."
                pb "Something."
                jump kamalsparty
label parsleyisfed:
    pb "*BUUURRRP* Oooh~ I don't feel so good."
    dal "Dude, did you get into my paints again?"
    pb "No... I think my Dad put anchovies on this pizza."
    pb "I hate anchovies."
    "It might be best to stay out of this convo."
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
        jump jeraandluliasingparty
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
    lu "It looks like the girls are finally done singing. Let's get up there!"
    j " Right behind you, honey!"
    $ kamalscakescene += 1
    $ jerahaslipstick = True
    jump kamalsparty


label jeraandluliasingparty:
    "It looks Jerafina and Lulia are now on stage while Borbra and Questionette are having a rest. They look like they're having a lot of fun singing together."
    jump kamalsparty


##End of Lulia and Jerafina convo


##Boris, Kamal and FK
label partyboriskamandFK:
    if boriskamalfkintro == False:
        bh "I'm getting worried. I couldn't find my puppet anywhere downstairs. I hope he hasn't… Gone anywhere."
        k "Don't worry, I'm sure he'll turn up somewhere."
        bh "I hope so. Also, why are you covering your mouth?"
        k " Oh, I had some fish tacos for lunch today and, uh… I didn’t have time to brush my teeth before I came here. They used a lot of fish sauce in it, apparently."
        bh "Oh dear."
        k "It's okay… So long as no one can smell my breath I'm fine."
        fk "But you can't keep your mouth covered for the whole party… Oh! Hey it's [player_name]! How are you enjoying the party?"
        menu:
            "You guys seem to be having some trouble with something.":
                fk "You… Could say that… More just inconveniences than actual problems."
            "Why's Kamal covering his mouth?":
                k "I, uh… Don’t want anyone to smell what I ate for lunch."
            "Boris looks kinda stressed.":
                bh "I, uh… I seemed to have misplaced my puppet."
        mc "Anything I can do to help you guys out?"
        fk "Well, we’d hate to make you do any work while you’re trying to enjoy yourself, bud. However, if you find something that can help brighten Kamal or Boris’ mood, let us know."
        mc "I’ll keep an eye out."
        fk "Thanks, [player_name]"
        fk "And don’t sweat it if you don’t find them. No one’s gonna hold you accountable if their problems don’t get solved. And if you need to call it a night, let me know."
        mc "I’ll keep that in mind, thanks!"
        $ boriskamalfkintro = True
        jump kamalsparty
    if boriskamalfkintro == True:
        jump afterboriskamalfkintro

label afterboriskamalfkintro:
    if borisandkamalpartypts == 2:
        jump kamalandborishappyatparty
    else:
        fk "Hey bud, what’s up? Have you found anything yet? Or are you looking to head home early?"
        menu:
            "I haven’t found anything yet. I’m still looking.":
                fk "Ah, no worries then, bud. Take your time. Enjoy some of the pizza while your here."
                k "Thanksfully, Boris remembered not to accept Jim's invitation to cook for everyone and ordered delivery instead."
                jump kamalsparty
            "I'm thinking I might head home early, actually.":
                fk "Alright. You sure about it?"
                jump leavepartyearly
            "I found minty gum for Kamal." if gum4kamal == True:
                fk "You did? That’s great! Hey Kamal!"
                jump kamalsgum
            "I found Boris’ puppet." if pabit == True:
                fk "Really? That’s great! Where did you find it?"
                mc "Gerry had it."
                fk "Oh, I might have to have a word with him about taking Boris’ stuff without asking. But thanks for finding it! Hey Boris!"
                jump reuniteborispabitparty

label kamalsgum:
    k "Eh?"
    fk "[player_name] brought some gum. Maybe that can help you with your problem!"
    k "It’s worth a shot."
    "Kamal takes the gum and takes a moment to chew on it."
    k "Mmm! This is pretty good gum. How does my breath smell?"
    fk "Much better now."
    k "What a relief! Thanks a ton, [player_name] I owe you one!"
    mc "I’m glad I could help."
    $ kamalscakescene += 1
    $ borisandkamalpartypts += 1
    $ gum4kamal = False
    jump kamalsparty

label reuniteborispabitparty:
    bh "Huh?"
    fk "We found Pabit! He’s safe and sound!"
    bh "Oh thanks goodness!"
    "Boris takes Pabit."
    bh "Oh, my sweet little boy! I’m so glad to see you’re okay! Don’t you wonder off again!"
    bh "Thank-you so much, [player_name]! And Pabit thanks you too!"
    mc "It was no problem."
    bh "I hope you enjoy the rest of the party!"
    mc "One of the others mentioned the puppet had a ‘weird vibe’ to it."
    bh "Aha, I know, the resemblance between him and I can be uncanny sometimes."
    bh "Why don’t you go enjoy yourself some ‘snacks’ and drinks? Jimothan loves talking to new guests! And thanks again for all your help!"
    $ kamalscakescene += 2
    $ borisandkamalpartypts += 1
    $ pabit = False
    jump kamalsparty

label kamalandborishappyatparty:
    bh "Pabit, where have you been you little trouble-maker? I was worried sick about you!"
    pa "Eye didn't gooo any wearz! A smale childde grabbed me when 1 was nt luuking!"
    fk "Ha ha! You always do such a cute voice for him, Boris!"
    k "Heheh, yeaah. He sure does."
    jump kamalsparty



##leave convo

menu leavepartyearly:
    "Yeah":
        fk "Alright"
        fk "Boris! [player_name] and I are heading home now! Thanks for hosting the party."
        bh "Already? We haven’t even brought out the cake yet. Oh well, I hope you both have a good night then. Thank-you so much for coming!"
        fk "Thanks for having us, Boris! You guys have fun!"
        k "Hey, thanks for coming guys. And it was good to meet you, [player_name]!"
        mc "You too, guys! Thanks for having me here! Good night!"
        "You and Flower Kid leave the party and make your way through the town to your apartment."
        jump routeselect
    "No, actualy I think I’ll stay a little longer.":
        fk "Alright, enjoy yourself!"
        jump kamalsparty


##If player has helped enough people, they trigger the Birthday Cake scene.

##Birthday cake scene.

label kamalspartyend:
    bh "I think now is a good time, Flower Kid."
    fk "Alright, I’ll go get Wallus!"
    k "Huh, what’s going on?"
    bh "It’s a surprise! ;- )"
    "Boris leaves you, Kamal and heads for the stairs into the shop. Flower Kid then goes to speak with Wallus who nods and excuses himself from Trencil before he goes to get an extra chair and table from Jimothan. Flower Kid then heads for the stage and gestures for Lulia and Jerafina to finish their song."
    "When they stepped off the stage, Flower Kid stepped into their place and took hold of the mic."
    fk "Ahem, attention everyone! It's time to bring out the cake. Gather around!"
    "As they speak Wallus brings the table and chair to the stage and sets up some utensils and plates."
    fk "Kamal, may we ask that you come have a seat?"
    k "Oh, uh-... O-ok."
    "He looks nervous but he complies and takes a seat after Flower Kid pulls it out for him."
    fk "Tonight, we're also going to have a special guest tonight; A visitor from another world!"
    k "Wait, what-?"
    fk "Iwashi-Kan! You are clear for landing!"
    "Off to the outskirts of the crowd Tiff begins playing some space synths on her keyboard."
    k "What is even going-"
    k "...."
##Kamal looks like he's about to burst out laughing
    k "Oh my god…"
    bh "Greetings, Earthlings!"
    "Boris comes walking out of the shadows. Dressed in what looks like a cosplay of a robot made of cardboard."
    bh "I come in peace!"
##Kamal is trying really hard not to laugh.
    k "Boris!?"
    bh "I do not know who this ‘Boris’ is, Earthling. But what I do know is that it is someone’s VERY special day today!"
    bh "Activating… Cake Delivery Mode!"
    "He makes a series of stiff, robotic movements towards Kamal. Vocalizing a bunch of ‘beeps’, ’boops’ and buzzing sounds. He then opens the secret cardboard compartment in his costume’s chest to reveal an beautifully prepared cake for Kamal."
    "Kamal laughs and claps his hands."
    k "Oh my gosh, Boris! This is too much!"
    "Boris then uses a lighter that extends out of one of his robot arms and starts to sing Happy Birthday to Kamal. Soon everyone, including you, start to sing along and recite the words by heart. Near the end, Kamal's entire face could barely contain his smile as he tried to hide his blushing."
    "When the song concluded, everyone cheered and clapped as they gathered around Kamal; Eagerly awaiting for him to blow out the candles."
    bh "Happy Birthday, my Kamal~ Think of a wish before you blow out the candles!"
    "Kamal paused, gazing over everyone with an unfiltered smile still plastered on his face. You both briefly make eye contact before he gazes at the candles."
    "He takes a deep breath in and blows out the candles."
    "Everyone claps and cheers as Boris removes his helmet and prepares to cut the cake."
    bh "Alright, everyone! Line up for cake!"
    "Before Boris's knife could touch it however, the cake moved. Boris paused, thinking someone had knocked on the table, but then saw the cake jolt. The icing on it’s top layer jiggling at the movement."
    bh "What the-?"
    tt "Chaos Reigns."
    "The cake then explodes and an opossum emerges, screaming and covered in icing and sprinkles."
    "Everyone else lets out a shriek at the sight and a wave of panic and shocked reactions ensues."
    mi "Now this makes it a great party!!"
    jump routeselect
##Show CG of the opossum erupting from cake, everyone reacting to it while TimTam eats cake off the ground and Mirphy takes a picture of everything while she gives a peace sign from the bottom corner of the frame.
