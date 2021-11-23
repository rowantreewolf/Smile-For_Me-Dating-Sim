label Habit_Route:
##Start of Habit's route

"You decided to take up Boris' request to help him around the shop. As you make your way across town towards the flower shop, you wonder what sort of job he has in store for you."
"It would be your first time working with him."
"You arrive at the shop and can see Boris through the store front window. He seems to be moving some things around and is rushing from one end of the store to the other, tending to as many plants as possible. Is he working all by himself today?"
##Play the sound of the shop bell ringing as the player enters.
##Scene opens at the flower shop interior with Boris greeting the player.
bh "Sorry, the shop’s not quite open yet, please- Oh, It’s you!"
##He looks happy to see you.
bh "Thank you for coming by, [player_name]. How are you this morning?"
mc "I’m doing fine. It looks like you’re quite busy."
bh "Aha, you could say that I am. But it’s nothing to worry about."
bh "I have a special job for us today! It is a very exciting time to work at a flower shop! Or… At least it should be."
mc "What do you mean?"
bh "Well… Take a look around the shop. What do you notice is different?"
"You look around the small interior of the shop. You see all the freshly cut flowers on display, as well as the wrapping paper and cards on display near the front of the shop. You can hear the low hum of the flower fridge at the back."
mc "Um, nothing, really. Everything looks the same, as far as I can tell."
bh "Exactly!"
"He lets out a sigh."
bh "Barely anything has sold for a couple of weeks now. And, because it’s spring, it is supposed to be one of the busiest times of the year! But hardly anyone has come to visit the store ever since Flower’s parents let me take over."
##He gives the player a determined look.
bh "Since you are new in town, having you around should give us a fresh, ‘outsider’s’ perspective on things! Give us a new perspective on things!"
menu:
    "That’s… encouraging.":
        bh "Really? I’m happy to hear that!"
    "Well… Okay, then. I’m happy to help...?":
        bh "Wonderful!"

bh "I have a plan to bring more customers back to the shop! You and I are going to do…"
bh "A marketing campaign!"
menu:
    "Cool!":
        bh "I have an idea about what we can do first. We’re going to make posters together and display them all around town."
    "Cool…":
        bh "I have an idea about what we can do first. We’re going to make posters together and display them all around town."
bh "I have an idea about what we can do first. We’re going to make posters together and display them all around town."
mc "You think posters are going to be enough?"
bh "Well, er… Maybe?"
bh "It could be that people are so busy with life right now that they have forgotten that this shop exists. Perhaps a small reminder that we’re here is all we need to start reeling in customers again."
menu:
    "I’m not much of an artist but I’ll try to help out.":
        bh "They’ll be going about their day, walking down the street. Feeling glum and sad that they have to go back to a colorless, plantless home."
    "That sounds really fun! Let’s get started!":
        bh "They’ll be going about their day, walking down the street. Feeling glum and sad that they have to go back to a colorless, plantless home."
bh "They’ll be going about their day, walking down the street. Feeling glum and sad that they have to go back to a colorless, plantless home."
bh "And then- An explosion of color appears before them as they see a poster of Doc-eh!...  Boris’ Flower Shop!"
label habitthemechoice:
bh "It shall fill them with a sense of...of…"
##Depending on the style picked, it will unlock an interaction at the conflict conclusion with a certain character helping Boris. Mystery = Trencil, Abstract = Dallas, Party = Tiff.
menu:
    "Mystery!":
        ##This allows Trencil to help Boris at climax
        bh "Exactly! Wonderful idea, [player_name]!"
        bh "Let's get to drawing!"
        jump habitmysterchoice
    "Abstract wonder!":
        ##This allows Dallas and Margo to help Boris
        bh "Exactly! Wonderful idea, [player_name]!"
        bh "Let's get to drawing!"
        jump habitmysterchoice
    "Party vibes!":
        ##This allows Tiff to help Boris
        bh "Exactly! Wonderful idea, [player_name]!"
        bh "Let's get to drawing!"
        jump habitmysterchoice

label habitmysterchoice:
    bh "This poster looks great! What do you think, [player_name]?"
    menu:
        "Yeah, I'm happy with it!":
            bh "Wonderful!"
            jump habitthemechoicemade
        "Hmm, let's try something else.":
            bh"Oh, well if you're not happy with it..."
            jump habitthemechoice
label habitthemechoicemade:
    bh "Alright, we have our poster! Let us go out and remind the world that this shop exists!"
##Leave the shop and player can choose what place they want to visit next.
bh "Alright, we'll need to visit a place with lots of people to hand these out to."
bh "I'm thinking we should go to the park. What do you think?"
bh "And don't worry if you're nervous with strangers. Let me do the talking *wink*."
menu:
    "Ok, thanks.":
        bh "Excellent! Now with that out of the way, let's get to work!"
    "I don't mind talking to people.":
        bh "No, no, don't worry. I'll do the talking. Okay?"
        mc "Uhh, okay."
##Scene transitions to the park
##In this scene, depending on what you picked for the poster; Lulia, Dallas or Trencil will be there. Plus Owen (by Bear) and Li Lee (by Lilli) Will be there as cameos and for humor.
bh "Okay, we need to find a place where there will be lots of people. Where do you think we should start?"
menu:
    "Let's try the pond.":
        bh "Okay, let's head there!"
        jump pondscene
    "Let's try the flowerbeds.":
        bh "Okay, let's head there!"
        jump Lileescene
    "Let's wait along the path.":
        bh "Okay, let's head there!"
        jump Pathscene

label pondscene:
##Boris and the player encounter Owen while he is feeding ducks.
bh "Ah, the Duck Pond. All those cute little quacks ought to draw lots of people over."
##He notices Owen feeding some of the ducks.
bh "Oh look! There’s someone already here! Let’s go talk with them!"
##Owen shows up.
bh "Hello, my plaid wearing friend! Do you have a moment?"
owen "Er, s-sure. I guess."
bh "I see that you're having a good time feeding the duckies bread."
owen "I am…"
bh "I should tell you that bread is actually very bad for ducks."
owen "Why?"
bh "A friend of mine once gave me an earful for feeding bread to pigeons. She said they were not healthy for them at all."
owen " R-really? But everyone feeds them bread."
bh "I know! It's such a tragedy! So many people around the world are still feeding birds bread and don’t know the consequences! The little birdies think they are full from eating it and then they neglect to eat more nutritious food. Then their feathers start to fall out, they lose the ability to fly, and then they get eaten by dogs and cats."
bh "Oh, I apologize, I went off on a ramble."
bh "May I interest you in our flyer for our Flower Shop? It details what we have to offer!"
owen "Starts sniffling"
bh "... It can also be used as a tissue."
##Takes the flyers and blows his nose and wipes his tears, walking away still crying.
##Accomplishment chime plays.
mc "...."
bh "...."
mc "...."
bh "....Well, one down! Let’s find the next future customer!"
##Jump back to flyer choice screen.
label Lileescene:
bh "Ah, excellent place to look! We’ll find someone who’s already interested in flowers here! We’ll practically let the flyer do the talking!"
bh "Oh look! There’s someone here already!"
##They approach Li Lee.
bh "Hello, young person! It’s a fine day today to be sniffing the flowers, is it not?"
lilee "........"
bh "..... U-uh, ahem."
bh "While you’re enjoying the flowers, do you have a moment to talk about the flower shop in town?"
lilee "......."
bh "..."
lilee "....." ##Li Lee stare intensifies.
bh "I’ll, uh just leave this with you."
##He hands the flyer to Li Lee
lilee "....." ##They look at the flyer then to you and then walk away.
mc "That was kinda weird."
bh "Maybe I intimidated them into silence. I tend to do that sometimes."
"He tries to laugh it off."
bh "Come on, let's try somewhere else."
##Jump back to flyer choice screen.

label Pathscene:
##Dallas, Trencil and Tiff. Encounters are dependent on the type of flyer you picked.
##If Abstract, you get Dallas
##If Mysterious, you get Trencil
##If Beautiful, you get Tiff.
##You and Boris stand by the path as you wait for the next person to walk by.
bh "Hum, de-hum-hum-hum~ Sooo, [player_name], may I ask you something?"
mc "Oh, yeah, sure. What is it?"
bh "What made you want to move to this town?"
mc "F.K. didn’t tell you?"
bh "All they said was that you were looking for a job. But why this place in particular? You could have found a job anywhere, really. And you came a long way to move to this town, if I understand correctly."
menu:
    "I wanted to get out and see the world a little.":
        bh "Ah, so you have  a bit of an adventurous sense to you, do you? Well… This town is pretty small if you’re looking for excitement but some of the natural landscape is quite a sight to see."
    "I didn’t like the place I lived before.":
        bh "Oh, I am sorry to hear that. But I hope this town turns out better for you."
    "I wanted to see my old friend again, and maybe make new ones.":
        bh "F.K. has told me all about your adventures together when they were travelling. Ah, how fun it must be to travel around with a friend!"
        mc "You should try it out sometime, it’s a lot of fun."
        bh "Oh, I would love to. But the flower shop needs me."
    "I wasn’t happy with my last job.":
        bh "Oh, I am sorry to hear that. But I hope this job turns out better for you."
        bh "You are… Happy with the job, yes?"
        menu:
            "Yeah.":
                bh "Oh good! I’m so happy to hear that!"
            "Um…":
                bh "Uh, p-perhaps we can discuss it later."
            "I’ve only worked one day.":
                bh "Eh-heh-heh, that is true."
            "I’d rather not say yet.":
                bh "Ah, I understand, I won’t press for details."
##convo cont
bh "Oh look, here comes someone now!"

##Trencil
bh "Hello there, my friend, do you have a moment!"
tren "Hmm? Oh, it’s you again. Taking a day off from the shop, are you? It’s nice to see you out in the shade for once."
bh "Ah yes, that’s me. Always busy, busy, busy!"
bh "Anyways, we’re looking to invite more customers to shop at our store. We have a flyer if you want to take a look."
tren "Habit, you know I was just there the other day. Or has your memory been wilting recently? And another observation I’ve noted is that it seems like I am one of the few customers who still visits your store."
bh "...Oh."
tren "But I’ll take the flyer, regardless. Perhaps my daughter could make use of it and pay you a visit. She has been taking up gardening more often."
bh "Oh… S-sure, here you go."
tren "Hope you have a lovely day as well, Habit."
bh "You, as well, Trencil."

##Dallas
bh "Why, if it isn't Dallas! How are you today, my friend?"
dal"Yooooo, Habit! Long time no see man, what's up?"
bh "My new assistant and I are handing out flyers to help promote our shop! Would you care to take a look?"
dal "Wait, I thought you already had an assistant. Kamal, right?"
bh "Oh, not anymore. We both work different jobs now. [player_name] and I work together at the flower shop now."
dal "Eeeh! I remember you! You were at Kamal’s party."
dal "And that is so cool, Boris! I'd love to have a flyer!"
bh "Wonderful, here you are then."
##You hand Dallas a flyer
dal "Woah! Did you guys, like, draw this yourselves?"
"Yeah, we did."
dal "DUDES! This is so groovy, man! I love your style! You should totally think about selling art like this. That’d be so rad!"
bh "That’s so nice of you to say! Thank you!"
dal "I’ll totally stop by the store sometime. Catch ya later, dudes!"
mc "Bye!"
##He leaves the scene.
bh "Well, that went well!"
mc "I think so too."
bh "Let’s see who else we can find."
##They hand out flyers for the rest of the day.

##Tiff ##She may have her albums on display at the renovated store. May also have a party theme.
bh "Hello, Miss! Do you have a moment to-... Oh! Hello, Tiff, it’s you."
tiff "Oh, hello Habit! How have you been?"
bh "Oh, u-um, I'm doing fine. Thank-you. How have you been?"
tiff "I've been doing great actually. I've started a record deal and my music is gaining a lot of fans!. What are you and your friend up to?"
bh "My friend and I are handing out flyers for our shop. If you want to look."
tiff "FK’s Shop? You’re looking to hire some people or something?"
bh "Oh, no, no, no! It’s not about that! We’re just looking to draw more customers in."
tiff "Oh, okay! Well, I wish you luck with that."
bh "Thank you."
tiff "..."
tiff ".....Um, are you going to hand me a flyer?"
bh "O-Oh! Of course. Here you go."
tiff "Thanks. You have a good day, Boris."
Boris "You too, Tiff."
##Tiff leaves the scene.
bh "Well that went well. But we still have more flyers to hand out. Let’s go."
"You and Boris spend the rest of the afternoon handing out flyers until you eventually run out."
"Boris lets out a sigh after a long afternoon of talking with strangers."
bh "Oh boy, what a day."
mc "I know! I’m starving."
bh "I saw a hotdog stand near the flowerbeds earlier. Why don’t we eat there? It’ll be my treat!"
mc "Sounds good, thank you!"
bh "Aw, it’s the least I can do for your help today."
"You both walk over to the hotdog stand, place your orders, and wait for your food."
bh "Why don’t we sit on the bench over there?"
mc "Sure."
"Your food is ready and you both head to the bench."
"You both talk casually as you eat until Boris notices something."
bh "Oh no! Look at these poor dears!"
mc "What, what happened?"
"You watch him set his drink down. He moves over to a patch of flowers near the bench. They look like they’ve been stepped on."
bh "Oh you poor things. Someone stepped on you, didn’t they?"
bh "It’s okay, Doctor Habit is here to help."
bh "[player_name], would you like to help?"
menu:
    "Er,  I’d rather finish my lunch before it gets cold.":
        jump habitskiphelpwithflowers
    "Sure, I’ll help.":
        jump habithelpwithflowers
label habithelpwithflowers:
    bh "Thank you! Just hold these stems in place while I make some supports for them."
    "You hold the flowers up one at a time as Boris takes a few nearby twigs from the ground, as well as some twist ties from his pocket. After carefully aligning the flower’s stems straight, he attaches them to the twigs with the twist ties so they’re no longer tipped over."
    bh "There, all better! Oh… But these poor darlings couldn’t be helped."
    "He holds a small cluster of flowers with stems too damaged to recover."
    bh "It would be a shame to let these go to waste. I bet they could make someone happy."
    "You really love flowers, huh?"
    bh "I do!"
    "You should keep them!"
    bh "You think so?"
    "Yeah, they would be going to a good home."
    bh "Aww, that’s so sweet of you."
    "They’re just plants."
    bh "Plants that love."
    bh "Flowers always give and they’re always kind. I hope to be as kind as they are, one day."
    menu:
        "What makes you say that?":
            bh "Flowers have always been special to me. They make the world a better and more beautiful place just by being themselves. They can bring happiness to other people’s lives, even if it’s only in small ways."
            bh "Even during times when I didn’t see it that way."

        "I think you’re a pretty kind person, already.":
            bh "... Aha." ##He blushes


"..."

bh "I’d like you to have these flowers."
##He presents the bouquet to the player.

mc "What really?"


bh "Yeah. I think they would be going to a good home."

"Your hands briefly touch as he passes the flowers to you."

mc "Aw, thank you Boris. That’s sweet of you."

bh "No, thank you. The flowers can be used to brighten up your new home."

"He checks the time."

bh "It is starting to get late. We’d better clean up and head back to the shop."

mc "Okay."

bh "Thanks again for coming down to help me today, [player_name]"

menu:
    "No problem.":
        jump habitafterparkflowerhelp

    "Anytime.":
        jump habitafterparkflowerhelp

label habitskiphelpwithflowers:
    bh "Good point. We don't want that."
    "You both eat your lunch and watch the world go by as you sit comfortably in silence toether."
label habitafterparkflowerhelp:

bh "Ah, it feels like it’s been such a long day. Cannot wait for dinner."

mc "What are you having tonight?"

bh "I’m thinking of spaghetti without the sauce."

mc "...Isn’t that just cooked noodles?"

bh "Say, [player_name], I’ve been thinking. I’ve been meaning to spend more time with the people I’m close to, since I’d like to make more friends. So, if it’s alright with you… Would you like to go out for coffee sometime?"
menu:
    "Yeah, sure!":
        bh "Wonderful! I know this great cafe I like to visit. I’ll show you where it is sometime."
    "If I have time in the future.":
        bh "Ah, I understand."

"You both arrive at the shop."

bh "Oh look! A letter arrived today."

"You both see a letter stuck inside the mail slot of the shop’s door."

bh "I didn’t expect any letters or bills today. I wonder who it is from."

"He picks up the letter and turns it over to look at the address. He looks flustered after reading the name."

mc "What is it?"

bh "It’s… from my Uncle."

mc "Uncle?"

bh "Yes… But I haven’t seen him since I was just a small child… How on earth did he find me? Is this a trick?"
mc "Well let’s read the letter and find out."

"Boris reluctantly opens the envelope and pulls the letter out. It all looks handwritten in Russian."

bh "Oh my god… He… He wants to come visit me."

bh "He and my cousins have been looking for me and they found out I was living here. How did they know?"

bh "...And it says they want to come see me. They left me their email address."

mc "You sound uncertain."
bh"I haven’t seen them in many many years."
menu:
    "Did you know them very well?":
        bh"I… Sort of?"
    "How do you think they found you?":
        bh"I don’t know… Maybe they used the internet and found my name somewhere."

bh "My memories of them are so foggy, but…"

bh "I do remember my uncle being very kind though. And the twins loved to play pranks."

bh "...I-I'm sorry."

bh "I think I need some time to reread this and think this over. This… feels like a lot to take in."

mc "Okay, Boris, I understand."

bh "Thank you. I hope you have a good night."

mc "You too, we’ll be in touch."

bh "Thank you."

"You walk home as Boris stays at the shop with a troubled look on his face."


"....."
"About two weeks went by since the conversation."

##The scene opens up at the player’s apartment, the computer is flashing to indicate there’s an email. GIF background? The player can click on the computer or their pet at this time. When the player clicks on the computer, it brings them to the email.
##If Computer system gets too complicated to code, use phone call conversation instead.

##Boris Email

"Hell-o again! I am sorry I didnot email YOU sooner. I habve been busy!"

"I Hab decideded 2 invite my Uncle and couzins for a ‘visite' and we hav beene having funn catchy-ing up with each othere. My uncle tells me he es verie proud I B-came a florist."

"Bumt eye’m still have-ing troublee getting custum-ers 2 com to the shoppe. I Have a New Plan we kan trye a nd I’d lyke to ask yoU to comee meet me at my houze b4 we put thee plan in-2 action."

"PS I hope youu have been doing well, and I still woulb likey to go 4 aure coffee. -]"

"PSS I thinky you’are neat."

##Boris Habit

"PSSS DON'T truste the twinz. They will de-C-ieve U!"

mc "Reply to Boris and go to his house."
"Hang out a little while longer."
##mc goes back to the room and the scene will repeat if they click on the computer again."

##Reply

"I can come down to your place, today Boris. I’ll meet you there in an hour and a half."

"Boris Womberful! I Will look fore-ward 2 B seeing U! Ta-ta 4 now! <3"

"You log off and get yourself ready to head out."

"You travel across town and locate Boris’ house with the address he gave you. It’s located in a small, quiet and green neighbourhood with few other houses around."

"You walk up to the front door and ring the bell."

"..."

"You hear some voices and then some heavy footsteps on the other side of the door."

##Door opening sound.
bh "[player_name]! It’s so good to see you! Come in, come in! We were just having some tea!"

##You enter the house and meet the rest of the family in the kitchen.

gh "Ah, so this is your new friend you’ve been telling me about."

bh "Grigory, I’d like to introduce you to [player_name]. They’re assisting me with the flower shop."

gh "Доброе утро, it’s a pleasure to meet you."

mc "It’s a pleasure to meet you too!"

gh "I hear you and Boris will be off promoting the shop today. I’ve been wanting to see the place myself, but Boris has yet to arrange that."

bh "Oh, don’t worry about that, Дядя. You’ll get to see it soon, promise!"

ba "Boris’ little friend is here!"

fo "How interesting~"

##The Twins appear.

bh "Oh, [player_name], these are my cousins, Bahd and Fortzaw."

twins "Bahd and Fortzaw Habit, at your service."

fo "We’ve heard good things about you."

ba "Yes, many good things."

fo "Boris is quite generous in his compliments about you."

bh "Fortzaw, не надо так говорить!"

bh "Don’t mind them, they like to tell silly jokes."
menu:
    "Compliments?":
        fo "Oh yes! He’s been showering you in praises."
        ba "He won’t shut up about you."
        fo "We’ve only just recently reunited."
        twins "But we would say that he-"
        bh "That’s enough you two!"
        bh "Please ignore them! They are pathological liars!"
        twins "Heheheheh~"
    "You guys like jokes? I love jokes!":
        twins "Oh yes, we *love* jokes~" ##>;3
        fo "Oh, what’s that behind your ear?"
        ##He reaches out and pulls a coin out of your ear.
        fo "Oh! Look at that, you’re 5 rubles richer."
        "He gives you the coin."
        ba "Oh what’s that in your other ear?"
        "He reaches to your other ear and pulls out a 5 dollar bill."
        ba "You’re five dollars richer now too."
        fo "Wait, what’s this?"
        "He seems to pluck something from the top of your head."
        "It looks like a tiny paper wad until he unfolds it and shows that it’s a ticket receipt."
        fo "Oh dear, it seems you have a ticket for unlawfully stashing coins in your ears. The money you have should suffice."
        "Both Fortzaw and Bahd take back the money they gave you."
        ba "Now hold on, there’s something in your nose. Hold still."
        "He steps up and holds your nose with one hand while he starts to pull an endless stream of ties tied together out of your nose. Fortzaw looks astonished as he gathers the piling material."
        fo "My goodness! You could open a tie shop with these!"
        "The ties all eventually come out as one big pile in Fortzaw’s arms."
        menu:
            "uuuh…":
                fo "Sorry, were we being too *nosy*?"
                ba "*Snirk*"
            "*laugh*":
                ba "Heheh, such a delightful laugh you have!"
            "I’ve seen those tricks a million times before.":
                ba "Oh? You have, have you?"
                fo "We got more tricks up our sleeve."

bh "Ah, [player_name] will need to get going soon. Perhaps another time."
ba "Aww, fine. Maybe later then."
twins "Perhaps later then." ##;)
"Didn’t you have another plan for promoting the shop, Boris?"
bh "Ah yes! I did say that!"

##convo cont

bh "[player_name], would you meet me in the garden for a moment?"

mc "Uh, sure."

"You notice the Twins and Grigory giving each other curious looks as you and Boris walk out the sliding door to the garden out back."
##Scene Habit’s back garden

bh "Okay, I have to confess, [player_name]. Our last attempt to promote the shop wasn’t as successful as I had hoped. I think even less people have come to the shop since the last time we spoke."
menu:
    "Oh, I’m really sorry to hear that, Boris.":
        bh "It’s all okay. I have another idea that could help us."
    "Does your family know you’re struggling?":
        bh "No… And I prefer they didn’t know."
        bh "I only just reunited with them. I don’t want them to see how much I’m failing already."
    "Do you have another idea on what we can do?":
        bh" Yes, actually, I do!"

bh "If handing out flyers didn’t grab people’s attention, we may need something that will surely grab everyone’s attention. So I spent all of last night making flower wreaths and flower crowns!"
menu:
    "So that’s why you look tired.":
        bh "Ah, I’ll be fine. Don’t worry about me. I’m sort of a ‘nightowl’ anyway."
    "Aren’t we supposed to be saving those flowers to, y’know, sell them?":
        bh "W-Well, I figured if flyers didn’t work, perhaps people needed something that actually shows what we have to offer."
mc "What are we going to do with them?"
bh "Today we’ll be heading to the mall and handing these out to everyone we come across. If they see how beautiful our flowers look, surely they will come to the shop for a visit!"
bh "They have to."
bh "So, are you ready?"
mc "Uh, sure, I’m ready when you are."
bh "Alrighty! Let’s head out for another day full of adventure!"
"You both head back inside."
bh "Grigory, Bahd, Forzaw! My friend and I are heading out to the mall! We’ll be back later this afternoon! Take care of the house while I’m gone."
twins "Have fun you two!"
gh "Safe travels, племянник!"
##Cut to mall interior and you and Boris prepare to hand out the gifts. The list of people interacting are Meadi, Parsley, and Mirphy

bh "Ah-ha! Perfect, the mall looks busy today! Surely we’ll find a few potential customers."

##Choice screen of mall


##Enter Parsley
##Include Ronbo mention
bh "Why if it isn’t Parsley! Hello friend! How are you?"

pb "Oh, hello, Dr. Habit."

bh "Oh, you don’t have to call me that anymore. Just Habit is fine."

pb "Right…"

pb"Listen, bud, I don’t feel entirely comfortable talking to you. After, y’know, the whole attempted teeth stealing thing."

bh "Oh… I understand."

bh "I, uh, I’ll be on my way then. I’m sorry to have bothered you."

##Parsley leaves.

mc "You know him very well?"
bh "He was once a client of mine when I was still a doctor."
bh "The ‘teeth incident’... Was a complicated affair. I would rather not talk about it."

mc "Okay, I understand."
"We’ll have better luck with the next person."
bh "Yeah… I hope so."

##Millie, Putunia and TimTam.

mi "Hey look! It’s the walking cringe compilation!"

pu "AHHH! THE GREEN MENACE RETURNS!"

bh "Er, hello children. Would you like some flower crowns from our shop?"

pu "Are you good now?"

bh "Yes! I promise I am a good doctor AND florist now!"

pu "Hmmmm… Okay! You can give me a crown now."

bh "Haha! Alright, here you go."

"Putunia accepts a flower crown and puts it on her head."

"She looks delighted by it."

mi "Hey, I’ll take one too!"

bh "Of course, here you go!"

"Boris hands her one and she examines it."

"Then she tosses it in the air and whacks it with her golf club, creating an explosion of fluttering petals as the barren stems fly through the air."

"They then smack into the face of a poor, unsuspecting clown that was talking to Parsley."

mi "Ha! Bullseye!"

pu "Nice shot, Millie!"

bh "My beautiful flowers!"

mi "Geez, old man, don’t cry about it! They’re just stupid flowers."
mi "Come on! Let’s go find other stuff to hit."

"Millie runs off laughing. But Putunia pauses as she looks up at Boris."
pu "Sorry, Mr. Habit."

"She runs off to join her friend."

"Boris looks down at the ruined flower petals on the ground."

bh "..."

menu:
    "That was so rude of her!":
        bh "It’s okay. They’re just flowers."
    "They’re just kids, don’t take it personally, Boris.":
        bh "Yeah, I know."
    "Let’s move on.":
        bh "Yeah, we still have flower crowns to give out."

##After handing out all the flower crowns.

mc "Thank you! Be sure to visit the shop!"

bh "Well, that’s the last of the flower crowns. Finally, we’re done."

mc "I know, right? Today was tough."
bh "Hopefully today’s work will help the shop."
mc"You sound exhausted."
bh "I’ll be alright, don’t worry about me."

##Move on to cafe date choice.

bh "We should head back now. I’ll need to get ready to reopen the shop tomorrow."

mc"Hold on. Why don’t we go have coffee together?"

bh "Coffee?... Oh right! I did mention before that we should go out for coffee sometime, didn’t I?"

mc "Why don’t I treat you this time? You deserve it."

bh "Oh really? Why, thank you! That’s so kind of you."

mc "My pleasure, Boris."

##Cut to coffee date.
##Scene is your POV sitting across from Boris in an arts and crafts cafe.
label habitcoffeedate:
    bh "Ahhh, this is so nice. Nothing like a refreshing cup of coffee at…"
    "He checks the clock."
    bh "3 in the afternoon."
    menu:
        "I prefer it in the morning.":
            bh "A perfect start up to the day!"
        "I like to drink it at night, actually.":
            bh "I would hope that doesn’t make you lose sleep, though."
        "Same here!":
            bh "Cheers then!"
"You both take a sip of coffee."
mc "So, what is this cafe? It looks a bit unusual."
bh "It’s an Arts and Crafts Cafe! Dallas showed it to me once before. I like to come here when I need something to distract me after… A rather long day."
menu:
    "Hey, it wasn’t your fault.":
        bh "..."

    "Those people just don’t know how to appreciate flowers.":
        bh "..."

    "You tried your best.":
        bh "..."


bh "Oh, there’s no need to worry about me. I’m fine. Just being a silly man is all."
menu:
    "I don’t think you’re silly.":
        bh "Well, I’m happy you don’t think so."
    "You’re a sweet and wonderful person!":
        bh "... Aww haha! You’re such a sweet person."

"Despite your words, Boris still seems to be having a hard time cheering up. You look at the art materials before you and consider what might cheer him up."
mc "Why don’t we draw a picture together, Boris?"
bh "Drawing?"
mc "Yeah, since we’re here, let’s have some fun drawing together."
bh "Oh, sure, I’d actually love that! Let’s set up the materials."
##Scene changes to the table top with paper and markers, pencil crayons and other art materials around.
bh "What would you like to draw, [player_name]?"
menu:
    "Let’s draw some flowers.":
        bh "I’d love to!"
        jump habitcoffeedatedrawflowers
    "Let’s draw some animals.":
        bh "Oh, how cute! Let’s do that!"
        jump habitcoffeedatedrawanimals
    "I’ll let you choose.":
        bh "Hmmm... Let's draw some teeth!"
        mc  "Teeth?"
        bh "No, wait, not a good idea."
        bh "Umm, let's draw flowers instead."
        jump habitcoffeedatedrawflowers

label habitcoffeedatedrawflowers:
    bh "What kind of flower are you going to draw?"
    mc "Hmmm…"
    ##They draw the flower they picked for Trencil at the party.
    bh "Oooh! How pretty!"
    mc "Thanks! I saw a flower like this in your rooftop garden at Kamal's party."
    ##Rose
    bh "Ah yes, the Rosa damascena. Also called the Damask Rose. The most fragrant of all roses and a prized ingredient in perfumes."
    bh "Did you know that roses are related to apples?"
    mc "Really?"
    bh "Oh yes! And Almonds, raspberries, pears, plums, peaches and rosehips!"
    mc "That’s so cool!"
    bh "Ah yes, Gerbera jamesonii, or just Gerbera Daisies, the smaller relatives of the sunflower."
    mc "Oh really? I guess I can see the resemblance."
    bh "And if you ever have trouble sleeping, try placing a vase of them on your nightstand. They’re efficient at exchanging CO2 and O2 even after the stems have been cut. This provides (or gives)  as you sleep, which helps you get better rest."
    bh "Ah yes, Tulipa gesneriana, the iconic flower of spring! Did you know that in Holland during the 17th century, Tulips were more valuable than gold?  They were actually used as currency for a time."
    mc "Wow, really?"
    bh "Oh, yes! *Sighs* Imagine a world where instead of coins and paper bills, you could exchange a bouquet of flowers for everything you need."
    mc "Would that make you a florist, still, or a banker?"
    bh "Maybe both!" ##He laughs.
    ##Flower continue
    mc "Okay, your turn, Boris."
    bh "Hmmm…."
    ##He draws a Toothlily.
    mc "Oh! What a beautiful flower!"
    bh "And a very special friend of mine. It’s called the Tooth Lily and is my most precious flower."
    menu:
        "What’s the scientific name for it?":
            bh "Hmm… That would be Palicourea dente. It’s native to the jungles of South America and renowned for its unusual method of blooming."
            bh "It was widely believed to promote happiness to those who have it."
            bh "Oddly enough, it’s technically not a true lily. Though I still consider it a lily."
        "Why is this flower so special to you?":
            bh "Well… I’d rather not get into too many details. But let’s just say my Lily has been with me through many years and has comforted me during bad times. It is a dear friend of mine."
            jump habitcoffeedateconvocont

label habitcoffeedatedrawanimals:
    bh "What are you thinking of drawing?"
    mc "Hmmmm."
    ##The mc will either draw their cat or their dog.
    bh "Aww, what a cute (doggy, kitty.)"
    mc "Actually, this is one of the abandoned pets Flower Kid and I adopted."
    bh "Oh yes, I remember them mentioning that! Flower Kid finally picked a name for theirs, did they tell you?"
    mc "No they didn't, what is it?"
    bh "Violet."
    mc "That's a beautiful name!"
    bh "I know, right! Just like the flower!"
    mc "Alright, your turn to draw an animal."
    bh "Hmmm…"
    ##He draws some white dogs that once invaded the Habitat(for artist reference).
    mc "Aw, cute! Do you have dogs like these?"
    bh "Oh no, there’s actually a funny story behind these dogs."
    mc "Oh?"
    bh "Back when I was running HabiUh- A mental health retreat, everyone was feeling rather glum. So to try and cheer them up, I brought in a pack of little white dogs to make everyone’s day happier."
    bh "It was a disaster. They ate one of my paper assistants, broke into the lounge, and Mirphy was so distraught she sat in the carnival and curled up into a ball while all the dogs surrounded her and begged her to play with them."
    menu:
        "That sounds hilarious!":
            bh "It was, but I soon began to feel bad for her. We eventually herded the dogs out of the place."
            jump habitcoffeedateconvocont
        "That sounds awful!":
            bh "Perhaps it was a little mean to laugh at her. But we eventually herded the dogs out of the place, so it was alright."
            jump habitcoffeedateconvocont
        "Have you ever had any pets?":
            bh "Never any animals. I’ve always stuck with keeping flowers. Or little bugs."
            jump habitcoffeedateconvocont

label habitcoffeedateconvocont:
    bh "But let’s not dwell on that, let’s draw more pictures!"

##Time passes and it's time to head home or stay at Boris' place for the night.
label habitaftercoffeedate:
    bh "Oh my gosh! Look at the time! I hadn't realized we were here for so long!"
    mc "Time flies when you're having fun."
    bh"It certainly does!"
    mc"I was just thinking it was time we headed back home."
    bh "I’m sorry I took up so much of your time."
    bh "But before you go, I just had an idea. Would you like to come to my house for dinner tonight?"
    bh "My uncle is a wonderful cook! And we may even play a game afterward."
    bh "What do you think?"
    menu:
        "I would love to!":
            jump habitacceptdinner
        "Maybe another time.":
            jump habitrefusedinner


label habitrefusedinner:
    bh "Alright, another time then."
    bh "You take care, [player_name]."
    mc "Later Boris! I'll see you around!"
    jump habitskippeddinner


label habitskippeddinner:
    ##Cut to mc's apartment at night.
    "That was quite a day. I better get some rest."
    ##player has option to interact with pet, the computer or go to sleep.
    ##Image map for room.


## Midnight poker night and dinner.
label habitacceptdinner:
bh "Wonderful! Let’s head back together! Grigory should be starting dinner at this time. He’s been insisting on cooking for all of us ever since he arrived."
bh "His borscht is the best thing ever made!"


"You and Boris make it back to his house as the sunsets in the horizon. As you enter his home, there's a waft of smells in the air as dinner was being prepared."

gh "That’s wonderful that you’re staying over! I’ll have to make a little extra tonight. Bahd, Forzaw, would you mind grabbing an extra chair and tableware for [player_name]?"
twins "Of course!"
bh "Would you like our help making dinner tonight? Or would you rather set up the table with Bahd and Forzaw?"
menu:
    "I'll help with dinner!":
        bh "Okay! Let's get cooking then!"
        jump habithelpingwithcooking
    "I'll help set up the table!":
        bh "Alrighty then! Let me know if you need anything!"
        jump habithelpingwiththetable

label habithelpingwiththetable:
    "You decide to help the twins set up the table and approach the twins."
    mc "Hey you two, need me to grab anything for you?"
    ba "Just need spoons from the drawers."
    "You find the spoons and bring five over to the table and set them down."
    mc "I’ll go grab the knives and forks next."
    fo "No need to."
    "They make a hand gesture over their nose, as if pinching it, and they reach up with their other hand. They then squint as they start to wiggle a fork from their nose. After they pull it out they make another hand gesture with their hand before they fan out the utensils and reveal five forks and five knives."
    menu:
        "You clap, impressed by the trick.":
            fo "Hehehe, we learned that one while we did magic shows for a while."
            ba "We can teach it to you if you’d like."
            mc "That would be cool! Thanks!"
            "Bahd and Forzaw showed you how the trick was done. They both seemed enthusiastic to have someone to teach their secret to."
        "You shrug. I’ve seen it before.":
            fo "Really? Bahd, did you hear that?"
            ba "I thought we were the only ones who knew that trick."
            fo "Ah well, perhaps [player_name] is just playing ‘Hard to impress.’"
            ba "Then we shall play ‘Hard to conform to peer pressure."
            fo "Let us forget their comment and finish setting the table."
        "That was gross.":
            fo "It is only a trick. I didn’t actually have a fork up my nose."
            ba "We can show you how the trick is done, if you’d like."
            menu:
                "No thanks, let’s keep it a mystery.":
                    fo "Suit yourself."

                "Sure, I’d like that!":
                    "Bahd and Forzaw showed you how the trick was done. They both seemed enthusiastic to have someone to teach their secret to."

    "Before long, Boris announced that dinner was going to be ready soon and needed the three of you to finish setting up the table."
    "As you and the twins placed the remainder of the tableware down, they both leaned down and spoke to you so only you would hear them."
    fo "You know, Boris seems a lot happier now than he did this morning."
    ba "Whatever you did today, it's good to see our cousin looking better."
    "Those words stuck to you as preparations were finished and you all began to dig in."



label habithelpingwithcooking:
    mc "So what are we cooking tonight?"
    gh "We're having Golubsty with Borscht!"
    mc "Yum! Those sound great!"
    bh "Oh yes! They will be! My uncle is a master chef!"
    gh "Oh, please. You flatter me needlessly!"
    menu:
        "Are either of them vegan friendly?":
            gh "We usually use meat for Golubsty, but I can create meatless ones for you. And Borscht is made purely of vegetables, so you will not have to worry about it."
            mc "Thank you."
            gh "It is my pleasure to feed a guest! Please tell me what you think of my food when we're finished! I appreciate feedback."
        "I’ve heard of Borscht, but not the other one.":
            gh "Ah, Golubsty is a type of cabbage roll with ground meat, chopped vegetables and a seasoned tomato sauce poured on top. It is one of my favorite dishes to make!"
            bh "Last time we had them I ate 12 rolls."
            gh "I hope you'll at least share with your friend tonight."
            bh "Hahaha, don't worry, I can share."
"Anything you need me to do?"
gh "You can chop vegetables for us or stir the sauce while it heats up."
menu:
    "I'll stir the sauce.":
        gh "Alright, here's the spoon. Thank-you for offering to help."
        "As you stir the sauce, Grigory and Boris are helping each other to prepare the rest of the meal. Grigory began to teach Boris how to wrap the cabbage leaves with filling as Boris complained that his fingers were too large."
        "But after some gentle encouragement from both you and Grigory, he managed to make a few rolls with ease. He has a small but very pleased smile on his face."
    "I'll help with the vegetables.":
        gh "Alright, the vegetables and cutting board are set up and ready to go. Let me know if you need anything."
        "As you chop the vegetables, Grigory and Boris are helping each other to prepare the rest of the meal. Grigory began to teach Boris how to wrap the cabbage leaves with filling as Boris complained that his fingers were too large."
        "But after some gentle encouragement from both you and Grigory, he managed to make a few rolls with ease. He has a small but very pleased smile on his face."
gh "Oh! Boris, would you go into the pantry and grab another can of tomato sauce for me?"
bh "Alright!"
"Boris leaves the room and Grigory moves closer to you to speak with you."
gh "You know, I'm really glad you're helping Boris with the shop. He's been so worried about it since we arrived. I was starting to worry about him."
gh "I'm glad he has a good friend like you to support him."
"Those words stuck to you as preparations were finished and you all began to dig in."

##After Dinner and beginning of Midnight Poker


bh "Ahhhh~ That was delicious."
twins "Mmm-hmm~"
mc "Yeah, I’m stuffed!"
gh "I’m happy you all liked it. I’ve had that recipe for over 20 years now."
fo "Well now that the table’s cleared…"
ba "We can finally play some Midnight Poker."
bh "That is, if you still want to. If you want to call it a night I can give you a ride home."
menu:
    "Nah, I’m good to play.":
        jump habitacceptpokernight
    "Actually, I think I’m ready to head home now.":
        jump habitskippokernight


label habitacceptpokernight:
    bh "Alright then. This’ll be fun, I know it!"
    jump habitpokernight

label habitskippokernight:
    ba "Aww, come on. Stay and play at least one round!"
    bh "They’re tired, Bahd. Let them go home."
    fo "Fine. But next time you’ll have to play a round with us!"
    gh "Thank you for the visit. It’s been wonderful to get to know you."
    mc "You too. Good night, everyone!"
    twins "Good night!"
    gh "Приятных сновидений."
    jump habitafterdinner

##Cut to outside the player’s apartment.
label habitafterdinner:
    bh "Thanks for staying for dinner, [player_name]. I hope my family didn’t weird you out."
    menu:
        "I’m used to weird families.":
            bh "Heheh, you and me both."
        "I love your family. They seem really nice!":
            bh "I think they’re really nice too."
            bh "Anyways, have good night. We’ll go out for coffee again sometime."
    "He leans down and gives you a gentle, warm hug."
    menu:
        "Hug him back.":
            "He flashes one more, toothy smile before he heads back to your car and you head back to your apartment for the night."
        "Kiss his cheek.":
            "His cheeks flush a dark color as he freezes for a second. He then giggles and holds you closer to return the kiss."
            bh "Muah! Hehehe!" ##His smile was large and delightful.
    bh "I’ll see you soon. Sleep well!"
    mc "You too!"
    "You watched him as Boris walked back to his car, giving you one last lingering look while his smile still plastered on his face."
    "You then went back to your apartment feeling a warm glow in your chest."
    jump habitdayafter_afterdinner

label habitafterpokernight:
    "Hours passed by as the poker game went on. Eventually, exhaustion began to settle on everyone."
    gh "That was a good game! I haven’t played a game that long in ages."
    bh "I haven’t had that much fun in ages!"
    ba "Next time we should try Uno."
    gh "But my goodness, look how late it is. And you have to work tomorrow, right Boris?"
    bh "I do, but I can stay up late and still work, don’t worry."
    bh "But what about you, [player_name]? You must be exhausted."
    menu:
        "I’m ready to drop at any moment.":
            bh "Then we better get you settled then. You can use the couch to sleep on. Let me go grab some pillows and sheets for you."
        "I’m hardly tired. I’m like a night owl.":
            bh "Same with me. Some nights I rarely sleep. Though we should probably prepare a spot for you to sleep in. The couch will work. Let me go grab some pillows and sheets for you."

"You and the Habits get ready for sleep. Boris set up the couch for you to sleep on while Grigory prepares tea for everyone. After the tea was made Grigory and the Twins retreated to their rooms for the night. You and Boris were the last ones awake."
"You settled into the cushions as Boris handed you a cup of tea."
bh "Here you go."
mc "Thanks, Boris. This tea smells great."
bh "Thank-you, I grew in my garden in the backyard."
"He lets you take a sip before he continues."
bh "So, [player_name], I'd like to thank you for coming tonight. I hope you had fun."
menu:
    "I had a ton of fun.":
        bh "Me too! I hadn’t had a fun gathering like that at home in a long time!"
    "It was great! Your cousins and uncle are cool!":
        bh "I know, aren’t they? They’re just as kind as I remember them."
    "I think I might abstain from playing poker again any time soon.":
        bh "Haha, I don’t blame you. It can feel rather one sided when the Twins are playing."

bh "Listen… I’m really happy you decided to stay and spend time with us. I feel that it wouldn’t have been as fun without you."
menu:
    "Aw, thanks Boris.":
        bh "I'm really glad you decided to stay for the night. It wouldn't have been as fun without you."
        mc "I'm glad I did."
    "It was more fun because you were here.":
        bh "Ahah, such a flatterer."


bh "Anyways, I wish you a good night. Sleep well."
menu:
    "Good night, Boris.":
        "He smiles at you warmly. Then he stands up and heads to his room for the night."
        "You finish your tea and drift off to a peaceful sleep on the soft, cozy couch."
    "Go for a kiss.":
        mc "Boris, wait."
        bh "Hmm?"
        "You prompt him to lean down closer to you."
        "When he kneels down you lean in close and give him a kiss on his cheek."
        "When you withdraw his cheeks are blushing red as he looks at you with a surprised look."
        bh "U-Um… Why thank-you."
        mc "Heheh, I thought it’d be nice to kiss you good night."
        bh "Oh, heheh, well I appreciate the gesture."
        bh "Let me return it."
        "He says softly before he leans forward and kisses your forehead."
        "Good night, [player_name]."
        "Good night, Boris."
        "He smiles at you before he stands up and walks down the hall. He turns to wave you good night before he disappears around the corner."
        "You settle down on the couch and finish your tea before you drift off to a peaceful sleep."
    "Go for a hug.":
        mc "Wait..."
        "You prompt him to lean down closer to you."
        "When he kneels down you lean in close and pull him into a warm hug."
        "He seems to stiffen a little before he melts into your arms and hugs you back."
        "His embrace feels warm and it engulfs you."
        "He lets out a content sigh and you both hold each other for a moment before you both withdraw."

bh "You have a good night, [player_name]."
mc "Good night, Boris."
"He smiles at you before he stands up and walks down the hall. He turns to wave to you good night before he disappears around the corner."
"You settle down on the couch and finish your tea before you drift off to a peaceful sleep."
jump habitdayafter_afterpokernight



##The Next day at Boris house
label habitdayafter_afterpokernight:

"The morning light shines on your face as you wake up. You shift around on the couch until you were awake enough to get up."
"As you sit up and rub your eyes you get the feeling that something is off."
"You then see Grigory walk into the living room with a coffee in hand."
gh "Good morning, [player_name]."
mc "Good morning, Grig."
gh "Did you sleep well?"
mc "I did thanks. And you?"
gh "I did too. Though I have to ask you."
gh "Did you see Boris before he left?"
mc "I didn’t actually. I just woke up now."
gh "Hmmm…"
"He looked troubled."
mc "Is something wrong?"
gh "Boris doesn’t normally leave this early. He stays long enough to have coffee and have a talk with us."
gh "I may just be fretting over him too much but I feel that there is something wrong."
menu:
    "That does seem off.":
        gh "It does, doesn't it?"

    "It’s probably nothing to worry about.":
        gh "Perhap… But still…"

mc "He should be at the flower shop right now. I could stop by and see how he’s doing."
gh "Why don’t we go together? I’ve been meaning to go visit his shop since I got here."
gh "But every time I brought it up, Boris insisted on staying away until things were ‘perfect’."
gh "I wasn’t sure what he meant by that."
mc "We can go there now and ask him."
gh "Alright. Let me wash up and we’ll go there together."

##Cut to outside the shop.

mc "Here we are."
gh "So this is the shop."
gh "I’ll be honest, it looks a little unkempt."
mc "Let’s try to get inside."
"You both approach the door and attempt to open it but find that it’s locked."
gh "I don’t suppose you have the key, do you?"
mc "No. But I think F.K. may have it. Let me call them."
"You pull out your cellphone and call F.K."
##Ringing sound effect.

"...."
"...."
fk "Hello?"
mc "Hey F.K! It’s me. I’m outside the shop, do you have the keys to get inside?"
fk "Oh *yawns*. Yeah I do. Did Boris lock himself inside again?"
mc "I’m not sure. I haven't seen him all morning and we think he might be in the shop."
fk "Oh, okay, I’ll meet you down there right away. And who’s ‘we’?"
mc "Boris’ uncle is here too."
fk "Oh cool! I’ll finally get to meet him! Alright, I’ll be down there soon. Later!"
"They hang up and you and Grigory wait outside the shop until F.K. arrives on their bicycle."
fk "*pantspants* Hey guys! Made it!"
fk "And you must be Boris’ uncle, right?"
gh "I am! The name is Grigory. It’s a pleasure to meet you, F.K. Boris has said many great things about you."
fk "Hehe, well I’m quite flattered! He and I have been friends for a couple years now. We’re also coworkers! And as his coworker…"
"He pulls out a ring of keys."
fk "I also got the keys to his shop. Let’s get it open."

"F.K. unlocks the door and you all enter the empty flower shop interior."

jump habitconfrontation


##The Next day at player’s apartment.
label habitdayafter_afterdinner:

"The morning light shines on your face as you wake up. You shift around on the bed until you were awake enough to get up."
"As you sit up and rub your eyes you get the feeling that something is off."
"A few minutes after you woke up, your cellphone rings."
##Cellphone ring sound effect
"...."
mc "Hello?"
fk "Good morning, sleepy!"
mc "Hey F.K. What’s up?"
fk "Have you heard from Boris recently?"
mc "I saw him last night."
fk "Oh…"
mc "For family dinner."
fk "Oh."
fk "Well, the reason I'm asking is because he was supposed to pick me up for work today but he never showed up. I hoped you saw him."
mc "He didn't mention any change in plans."
fk "I was going to head down to the shop to see if he's there."
fk "I'd like you to come down to the shop too. I have a funny feeling about this and I'd feel better if I had another friend with me."
mc "Sure thing, bud. I'll meet you down there."
fk "Thanks, [player_name]. See you soon."
"You hang up and get yourself ready to head to the flower shop."

##Cut to flower shop exterior.

fk "Sorry to wake you up so early. But I appreciate that you came."
mc "Not a problem, bud. Let's see if we can find Boris."
mc "Hang on, is that…?"

##Grig sprite appears

mc "Grigory? What are you doing here?"
gh "Ah, [player_name], it's good to see you."
gh "Boris didn't seem like himself this morning so I came to the shop to see how he was doing."
gh "But it's locked. Is the store closed today?"
fk "No, we're supposed to be open today."
fk "Erm, sorry. I'm F.K. Boris' friend. I work here too."
gh "Good to meet you. I'm Grigory, his uncle."
fk "Like I said, it’s supposed to be open today. But luckily for us, I have the key to the store."
fk "Let’s see if he’s here."

"F.K. unlocks the door and you all enter the empty flower shop interior."
jump habitconfrontation

label habitconfrontation:

fk "Woah!"
gh "Does it… Normally look this empty?"
fk "No, it’s not supposed to look like this at all! What happened here?"
mc "I don’t know. Boris said he was struggling to get customers in but he never mentioned what he was doing with the shop."
fk "Well, let’s head upstairs to the garden. I think he may be up there."

##stair walking sounds

"You, F.K. and Grigory make it up to the Roof Garden and find Boris kneeling by a bed of flowers."
"He is gripping some wilted flowers in his hands and it looks like he has been crying recently."
bh "Oh, hello, everyone. I didn’t expect you all to find me."
mc "Boris… What’s wrong?"
fk "Yeah bud. The shop looks nearly empty down there. What happened?"
bh  "I…"
##He starts to tear up.
bh "I’m sorry."
bh "I tried to make this shop successful."
bh "I even gave everything I have away in hopes of bringing people in."
bh "But nothing works."
bh "I don’t know what to do."

##He covers his face with his hands and slumps down.
menu:
    "Hug him.":
        jump Habithughim
label Habithughim:
mc "Hug him and tell him everything’s going to be okay."
"He raises his head and looks at you with a surprised expression as you hold him."
mc "It’s gunna be okay, Boris. It’ll be alright."
"He seems to hesitate for a moment before he leans down and holds you back, burying his face into your shoulder."
"Soon, F.K. approached and held Boris as well. And then Grigory."
"And for a while you all held the florist, comforting him until his tears subsided."
fk "Boris, just talk to us, we’re here to help."
"Boris sniffled, burying his face in his hands. Grigory approached him and gently placed a hand on his nephew’s shoulder."
"Boris gazed up at him and seemed to calm down. He wiped his face before standing up."
bh "Okay…"
fk "We’re willing to help you with whatever you need. We’re friends, buddy,"
gh "We can talk in private if you wish orp"
bh "No… I’ll tell you. I’ll tell you all the truth. I cannot hide it anymore."
bh "F.K., when your parents left me in charge of the shop, I wanted to make them proud and help the shop thrive. Especially after all the kindness and generosity your family has given me. Ever since… The teeth incident, you have always been so kind to me. A true friend. I wanted to repay you all after all the mistakes I have made."
bh "You helped me find purpose in my life again."
fk "Boris…"
bh "But, even with this wonderful opportunity being handed to me, I still mess it all up. I can’t bring a single new customer in. Everyone I talk to just thinks I’m weird, or I scare them away."
bh "If I can’t get any new customers in, the shop is merely an empty greenhouse collecting cobwebs. Nothing I do works."
bh "Even after all this time, I’m still a failure."
menu:
    "You’re not a failure, Boris!":
        bh "You saw how the people reacted when I tried promoting the shop. None of them even showed up to window shop."
    "Then let us help you!":
        bh "Help me? But how?"
    "You tried your best.":
        bh "My best was never enough."

gh "Boris, why didn’t you tell us you were struggling?"
bh "..."
bh "I didn’t want to disappoint my family."
bh "I wanted to prove that I could do this on my own without burdening the people I care about."
gh " Boris…"
gh "You could never disappoint me. You’re pursuing a life that makes you happy. You have friends that care about you. And you grew up to be a kind-hearted man, despite all the hardships you faced."
gh "I couldn’t be more proud of you."
bh ".... R-really?"
gh "конечно. I love you, Boris, you’re family. And I’ll do whatever I can to support my family."
fk "And Boris, we never expected you to run everything by yourself! Even my parents needed extra help every now and then. Putting all that pressure on yourself does nothing to help."
fk "We’re friends Boris, you can always ask me for help."
bh "..." ##He smiles
bh "Thank you F.K. Спасибо дядя."
fk "Anytime, anywhere, Boris."
gh "Все для моей семьи, мой дорогой племянник."
bh "[player_name], you’ve already done so much for me. I feel selfish asking for more."
bh "But… Would you be willing to help me with the flower shop one last time?"
menu:
    "Sure I will, Boris, that’s what friends are for.":
        bh "And what a wonderful friend you are."
    "I’m here for you, for as long as it takes.":
        bh "... Thank-you, [player_name]. You’re so sweet." ##blushes

fk "Okay then, everyone, I vote that we order some coffee and breakfast and get a group meeting together. I’ll call up some friends too for help."
gh "I’ll call Forzaw and Bahd to come down to the shop, as well. They may have a few helpful ideas."
bh "Okay. I’ll clear some space for everyone."

label habitbeginrenovation:
    gh "Your cousins have arrived to help us out, Boris."
fo "We may not be gardeners…"
ba "But we can still lend a green thumb to help out."
twins "Heheheheh~"
bh "Heheheh. Thanks, you two."
fk "And I made some calls to a few friends of mine, so they should be on their way. While we wait, we should brainstorm."
gh "Let’s start with what’s been troubling you, Boris. What do you find is causing you the most difficulty with the shop?"
bh "Well… I feel that it’s hard to connect with customers. I don’t know what to do to entice them to come visit the shop. For one reason or another, they never seem to show up. I can’t figure out what I’m doing wrong."
menu:
    "Well, you are kind of a weirdo.":
        bh "So I’ve been told."
    "You just need to try a different approach.":
        bh "Like what?"
    "I don’t think there’s anything wrong with what you tried.":
        bh "Thank you, [player_name]"

gh "Perhaps I can help with that."
bh "You can?"
gh "When I worked as a mortician, I learned to effectively address the emotional needs of my living clients."
gh "Perhaps my knowledge and experience can be used to help you connect with your customers."
bh "Thanks, Uncle."
gh "Anything for family."
ba "And we have some resources we can pull from too."
fo "Yes. With our insect friends!"
bh "Insects?"
ba "As entomologists, we have access to a wide variety of species. Some of which can be helpful in a home garden."
fo "If we had the space for it, we could set up a terrarium or two for some of our insects."
ba "We've got ladybugs, worms, butterflies…"
fo "Lacewings, praying mantises, and, of course, bees."
bh "It sounds like they would make a wonderful addition to the shop! But how will I find the space for all of them?"

##The shop bell rings.

fk "I know someone who may help with that."

label habitrenovationchoice:

##Enter Trencil, Dallas or Tiff.


##Mystery Choice

bh "Trencil!?"
tren "Hello. I’ve been informed you require assistance in rejuvenating the flower shop."
FK "Thanks for coming, Trencil. We were just talking about the changes we might make to the place. You had some really good ideas in our phone conversation, if you’d like to share them."
tren "Of course."
tren "Boris, as you know, I am an avid gardener myself and have been for many, many years."
bh "I remember us talking about flowers when you came to buy seeds a month ago."
tren "Yes, but I also have intimate knowledge with flowers that expand farther than what you have available here. Centuries of gardening allows for plenty of learning opportunities."
tren "If you would like, I can share some of my knowledge with you and share secrets of flowers that have been lost to the ages. I also have some rare seeds in my collection I may be willing to part with. An expanded variety of flowers may benefit your shop greatly."
bh "That all sounds wonderful, Trencil! I would be happy to garden with you if you’re willing to teach me about these rare flowers! Thank you so much!"
tren "It’s my pleasure to pass on the joy of gardening to another."

##Party Choice

bh "Tiff!?"
tiff "Hiya, Boris. F.K. gave me a call, saying the shop needs a fresh new look. My friend and I are here to help."
##Mike "Hey there, I’m Mike! I’m the host of a local radio station here. I got a call from Tiff that you could use a shout out on my channel."
##Mike "Luckily for you guys, I owe her a favor."
bh "A favor?"
tiff "It’s a long story."
tiff "Anyways, I’ve known F.K.’s family for years. I met them when they hired me to sing for F.K.’s birthday. They were so supportive of my music career when I was just starting out."
tiff "I want to show my support for their store."
bh "Even if I’m working here?"
tiff "If they trust you with their family business, they must see something very special in you."
bh "...Thank you, Tiff."

##Abstract Choice

bh "Dallas!?"
dal "Hey, my dude! How’s it going? F.K. gave me the details of what was happening and you called the right people to help give this place a fresh look!"
dal "I remember seeing your poster and hearing how you were having trouble with the shop. I thought, ‘Man, it would be such a bummer if this place went down in the dumps’. So I figured I could give a hand with renovations."
dal "And my sister tagged along to help out!"
##Margo "I’m Margo, it is a pleasure to mee you! My little brother showed me the poster you made and I thought it looked wonderful! I felt such a spark of inspiration from it, but had no idea what to do about it."
##Margo "But when I heard you needed help, I figured repainting these walls would be the perfect outlet I need."
dal "Same here, Boris! We’d love to give this place a new paint job. Whaddya say?"
bh "You… Why… I would love to have your help, Dallas! And you too, Margo!"
bh "Let your artistic spirits shine!"


##FK intervenes and renovation starts

fk "Alright, we’ve got everyone here now. Let’s finish breakfast and start the renovation!"

##Depending on what poster theme was picked at the beginning, the renovation will take different looks and have different characters involved.

"You, Boris and everyone else began work on renovating the flower shop. The flowers were restocked and revitalized, the walls repainted, and new items were brought into the store for sale and decoration."

##Trencil/Mystery

"Trencil spent a few evenings showing Boris his greenhouse of rare and exotic plants. He taught Boris some of the secrets of gardening that he had accumulated over the centuries."

"Boris eagerly absorbed his knowledge and was excited to grow more friends for his garden"

##If romance points are high enough.
"On some nights, both you and Boris were able to work in the greenhouse together. He passed on what he learned from Trencil to you. You two passed the time by sharing stories, laughs, and private conversations. Hours would stretch on into the night. Your dirt-covered hands would linger against each other as you nurtured your new flowers together."


##Margo&Dallas/Abstract
"The artistic siblings went to work giving the entire shop a new paint job on just about every surface they could reach. They worked tirelessly, driven by the spark of creativity. However, they left one wall alone, and encouraged the members of the staff to add their own artistic touches to it."
##If romance points are high enough.
"You and Boris had fun together painting flowers (and each other) on the wall. As you painted, you shared ideas about the shop’s future and how you might run it together. As you both excitedly conversed about a future filled with flowers, Boris filled the wall with many smiles and hearts surrounding an image of the two of you holding hands."


##Tiff&Mike/Party

"Tiff and Mike kept their word that they would promote the shop and, within a week, word spread for miles and miles about the flower shop’s reopening. You and Boris were even given a chance for an interview to talk about Ruizville’s long-running and wondrous flower shop."

##If romance points are high enough.

"You and Boris shared the story of your journey to bring life back to the flower shop. All the while, Boris would take nearly every opportunity to shower you in compliments. He said that you were the real star of the show. Any time you would get embarrassed or feel nervous during the interview, he would reach out to hold your hand and give you a squeeze to let you know he was there by your side."


label habitrenovationreopening:
"Two weeks have passed during the renovations."
"On the morning of the reopening, Boris paced nervously around the shop. He made rounds again and again to ensure everything was in place."
bh "Have the plants been watered? Have we got enough stock? Does everyone have-!?"
gh "Boris! Boris, you need to relax. We have everything we need."
bh "I’m sorry, I’m just nervous."
bh "What if no one shows up, what if-"
gh "Boris, take a look outside."
"Boris reluctantly complies and looks out the display window of the shop. He looks shocked at the sight of a huge line waiting outside. The line included all the people you both spoke to before, and new faces as well."
bh "I’ve… Never seen so many people waiting to come into the shop before."
mc "They’re here because of what we accomplished."
"They’re here because of all your hard work, Boris."
"He smiles warmly at you."
bh "I couldn’t have done it without you, [player_name]."
fk "It’s opening time, everyone! Let’s rock this joint!"
"Flower Kid opened the shop doors and allowed a flood of customers to enter the shop."
"You, Boris, Grig, the Twins and Flower Kid were busy the entire day of the grand reopening of the flower shop. It was one of the biggest booms in sales and customers Boris had seen in a long time."
"It almost seemed like the entire town was eager to try their hands at gardening."
"The renovation for the flower shop was a huge success."

label habitrenosuccessstart:
##Fade to the renovated flower shop interior during a party.
"One week later."
"Boris taps lightly at the microphone."
bh "Is this on?"
FK "Yup, you’re good to go, Boris."
bh "Alright…"
"He coughs behind his hand to gather everyone's attention."
bh "Before we start the party, I would like to thank everyone for coming."
bh "I also want to thank everyone who helped make the renovation so successful. Thanks to all of your hard work, the flower shop is now back in business."
bh "It couldn’t have been done without you."
"He looks straight at you as he says this."
bh "And… That is all I have to say, eheheh."
bh "A toast to everyone here! I hope you enjoy the cake!"
"Everyone cheered and raised their drinks. After the toast, Boris stepped away from the microphone and walked towards you."
bh "When you have a moment, I’d like to talk to you in private on the rooftop garden."
mc "Alright, I shouldn’t be here long."
bh "Take your time. This party is more for you than it is for me. Come find me when you’re ready."
bh "And the cake is really good! Do try some."
mc "Alright, will do."

label habitrenosuccess:
##Cut to image map of Flower Shop Success Party. Grig, The Twins, FK and the people who helped (Trencil, Margo&Dallas, or Tiff&Mike) are available to talk to.
##Grig
##First intro
gh "Ah, [player_name]! What a week it has been. Are you enjoying yourself this evening?"
mc "I am, thanks! How are you?"
gh "I’m doing great! I’m glad Boris decided to throw this party. We needed this."
menu:
    "I’m just glad all that work has paid off.":
        gh "I didn’t have much doubt in our success. Boris is fortunate to have so many friends willing to help him. I feel that he just needed his confidence back."
    "So what are your plans now that the shop is done?":
        gh "I think I will stay here and help Boris with the shop for a while. I want to spend as much time as I can with my nephew before I return to retirement. And I’ve grown to take a liking to this town. It’s very quaint and the people are very pleasant here."


##The Twins
fo "Well, hello again!"
ba "Enjoying the cake? I personally would have preferred chocolate."
fo "Chocolate!? Strawberry is way better."
menu:
    "Strawberry is better.":
        fo "Ha! See even [player_name] agrees!"
        ba "Bah! Whatever!"
    "Chocolate is better.":
        ba "See? Chocolate is a classic!"
        fo "Tch! You’re missing out on strawberry."
    "Are you two enjoying the party so far?":
        ba "It’s nice enough."
        fo "It’s missing a karaoke stand, though."
    "What do you guys plan to do now that the shop is done?":
        fo "We’ll actually be heading back to our university soon."
        ba "Our vacation is drawing to a close. But we intend on keeping in touch with Boris."
        fo "Gotta make sure he’s taking care of our insect friends!"

##FK

fk "Hey buddy! Good to see you! Man, what a busy week it’s been, huh?"
mc "Yeah, you can say that again."
fk "Man, what a busy week it’s been, huh?"
mc "Ha ha, very funny."
fk "Heheheh!"
mc "So, are you enjoying the party?"
fk "Of course! If there’s free cake involved, it’s hard to call it a bad party."
mc "So what are your plans now that the renovation is done?"
fk "I’ll still be helping Boris around the shop. Nothing has changed except now the shop looks way cooler than it did before!"
##As you try to leave the conversation.
fk "Oh, before you go, I just wanna say something."
fk "Thanks for being there and helping Boris out. I was really worried about him for a while. I’m glad you both got through this."

##TRencil
tren "Well, hello, [player_name]. I trust that you’re enjoying yourself this evening?"
mc "I am, thanks. How about you?"
tren "I keep getting a sense of deja vu here. Other than that, I am quite enjoying myself. I am glad the renovation was a success."
mc "What are your plans now that the shop is done?"
tren "I will return to my home and attend to my own flowers again. However, I did enjoy my time teaching you and Boris. I may offer lessons to customers here in the future. But for now, I’ve had enough of crowds."
tren "Now if you’ll excuse me, I was enjoying my corner of solitude."

##Dallas and Margo
##Margo "Well hello, if it isn’t the aspiring artist!"
dal "Hey dude! How’s it going?"
mc "I’m doing good, thanks!"
mc "How are you two enjoying the party?"
##Margo "Wonderfully! The festivities and fruit punch are exquisite
dal "Ya, the party's totally rocking! Everyone seems to love the new look! Toooootally adds, like, new life to the place!"
##Margo "It is most fortunate you had my help, Dallas."
dal "Heeey, we, like, worked as a team! It wasn't all you!"
##Margo: "Hahaha! I'm only teasing you, Dallas~"
mc "What are your plans now that the renovation is done?"
dal "Well, I'm going to be continuing what I always do. Making art where ever inspirations strikes me."
dal "I'll also be getting back to offering art lessons if you ever wanna, like, just come by to check it out!"
##Margo "I might join in on Dallas' lessons. See what he's learned since we last met."
##Margo "Other than that, I'll be heading back to my own studio and continuing my works."


##Tiff (Mike left the party)

tiff "Hey you! Good to see you! How’s it going kid?"
mc "I’m doing good, thanks!"
menu:
    "Where’s Mike?":
        tiff "Oh, he left early to get ready for work tomorrow. He’s got a comedy show he needs to get ready for tomorrow."
    "Thanks for all your help, Tiff.":
        tiff "It’s nothing. The flower shop is an important part of this community. I was glad to be of help."
    "What are your plans now that the shop is reopened?":
        tiff "Well, I gotta head back to my studio tomorrow. I need to get to work on my upcoming album."
        tiff "Boris said he would be happy to set up a display for my records here in the store."
        tiff "I’m also considering asking Boris if I can host an album signing for my fans."


bh "Are you ready to go up to the garden?"
menu:
    "Yeah, I’m ready now.":
        bh "All right, watch your step."
        ##Confession scene
    "Not yet.":
        bh "Don’t worry, take your time."
        ##Jump back to party


##Rooftop confession

"You and Boris leave the party and enter the rooftop garden."
"You glance up at the clear, night sky as the sound of crickets and the smell of fresh flowers fills your senses."
bh "What a beautiful night we have tonight."
"The florist breathes in deep before letting out a long sigh."
bh "I… Wanted to thank you for everything you’ve done. I was having so much doubt that I could make the shop a success. I was at my wit’s end. But you were always there to help cheer me up and give me hope."

##Friendship
bh "You’ve been a good friend to me, [player_name]. When things quiet down in the shop, would you like to come hang out with Kamal and I sometime?"
mc "I would love to, Boris."
bh "I’m glad you decided to move here. I’m lucky to get to know someone as kind as you."
bh "Now let’s head back before F.K. eats all the cake."
"You both headed back downstairs and had fun together at the party for the rest of the evening."

##Move to friendship ending


##Romance
bh "I don’t know how else I can thank you."
bh "..."
bh "I, uh… We’ve gotten close in the past couple of weeks, haven’t we? You’ve only moved here recently, but it feels like I’ve known you longer than that."
bh "I… Really like you, [player_name]. When things settle down at the shop, would you like to go on a ‘date’ sometime?"
##choose friendship
mc "Let’s call it a friend date."
bh "Ah, I understand. Just a friend date it is then."
bh "...."
bh "Thanks for listening to me ramble. I hope this doesn’t make things awkward for us."
mc "It’s alright, I still value you as a friend."
bh "Thank you."
"You both go back downstairs and have fun together at the party for the rest of the evening."


##accept romance
"It’s a date!"
bh "R-really!? That’s great!"
bh "I'm… just so happy I could-"

##blushes.
bh "Um, if it's alright, may I kiss you?"
mc "Yes!"
"Boris leans down and carefully places his hands on your shoulders. You both close your eyes as he gently kisses you on the lips. It was short, sweet and almost playful."
"Actually, can we hug instead?"
"Boris leaned down and carefully wrapped his arms around you as you returned the gesture. The big man easily encapsulated you in his warm embrace. Some of his hair brushed against your face as you breathed in his smell, which was mingled with the scent of earth and flowers."

##convo con
"He pulled back slowly. His face was warm with a loving smile, and his cheeks were tinted with a pink blush."
bh "Heheh, thanks for that."
mc "Thank you. That was nice."
bh "Hehehe, yeah. I think that was nice too."
bh "Do you think we should head back downstairs? Before they start wondering where we went?"
mc "Nah, let's stay here longer."
bh "Alright. I like that plan better."
"You both moved to the couch under the ivy-covered canopy and looked at the stars together. You held each other's hands as he night went on."
"I think we should before everyone eats the rest of the cake."
bh "Haha, good plan!"
"He reached out to hold your hand as you both went down stairs. You enjoyed the rest of the party together as the night went on."

##Friendship Ending

"3 Months Later."
##The scene opens at the part
Fk "Alright! We’re almost done! Just a few more dozen to go."

gh "Phew, I’m going to need to lie down for a few days after this. My back isn’t used to bending over this much."

k "Same here. I might have to see a chiropractor after this."

bh "Oh it’s not so bad, you two! My back feels great!"

mc "My back is actually killing me too."
k "I can recommend the clinic I go to if you’d like."
"I’d appreciate it"
"I could plant flowers all day."
bh "That’s the spirit!"

gh "I think it would be best to take a short break, however."

fk "Why don’t we head up the hill to take a look at our progress?"

bh "Alright!"

"You all headed up the hill to see the progress of your day’s work."

##CG of a field full of ‘flower portraits’.

k "Oh wow! It’s really coming together!"

fk "Yup, just one person left to fill."

mc "And who would that be?"

bh "You, silly!"

mc "Aww, really!?"

fk "Yeah, but with a big clown nose and giant googly eyes."

mc "F.K.!"

"You all had a good laugh as you enjoyed your break on the grass with your friends."


##Romance Ending

##OPens at either the apartment or mall.

"You're going on a dinner date with Boris tonight and you want to get him a gift."
"What gift are you going to get Boris?"
menu:
    "A rare new flower.":
        "You pick the flower."

    "A cute stationery card.":
        "You pick put a card with smiling faces and cute animals on it."

    "New scrunchies for his hair.":
        "You pick a pink scrunchie with glitter on it."

##Scene fades to shop interior.

"You pass by a leaving customer as you enter the shop."

bh "Thanks for stopping by! Tell me how gardening goes!"

bh "Oh! [player_name]! Good to see you!"

mc "Hey Boris! Are you ready for our date?"

bh "Almost, I just have to close up shop for tonight."

gh "I can do that for you, Boris."

bh "Really? You're sure?"

gh "Yeah, don't worry about it. You two have a good time."

bh "Aww, cпасибо дядя!"

gh "Повеселись!"

##Move to exterior

mc "One of these days you'll have to teach me Russian so I can actually understand what you two are talking about."

bh "Haha! I would be happy to!"

bh "But let’s go to my house! I have a surprise for you!"

bh "Oh right. Let’s go!"

##Scene change to Lounge2 interior

"You and Boris are enjoying spaghetti together."

bh "Ahh, this place’s spaghetti without cheese or sauce is superb! My compliments to the chef!"

"You both take a bite out of the pasta and as you both pull back, you realize you ended up with one end of the same noodle in your mouths."


mc "Bite closer"
"He blushes but then giggles and takes a bite closer, as well."

"Wait and see what he does."
bh "He blinks, looking at you before he seems to smirk and bites closer towards you."

"Then you both bite closer."

"And closer."

"Closer."

"Both your noses booped together as you both finished the last piece and Boris snuck a quick kiss onto you."

"You both laughed and leaned back into your seats."

bh "Oh! Before I forget, I got you a present!"

mc "Actually, so did I!"

bh "Haha! What a coincidence! You go first, then."

mc "Nah, you first."

bh "No, no, no, please! I insist!"

mc "Okay, fine."

"You bring out your gift and place it on the table."

##gift reactions
##A rare flower
bh "Oh my goodness! Is that… A Desert Rose?!"
bh "It’s so beautiful!"
mc "I’m glad you like it. I wanted to get you a flower that was hard to come by."
bh "Aww, that’s so thoughtful of you!"
bh "Thank-you so much, [player_name]."



##Boris’ turn

bh "Okay! My turn! But first, close your eyes."
"You do so and hear some rustling on Boris’ side of the table before something is placed down."

bh "Okay, now open!"

"You open your eyes and see what looks like a Tooth Lily. But it's a brilliant gold color and lets off a soft glow."

mc "Oh my gosh!"

bh "This is the Golden Tooth Lily."

bh "For many months now I have been working on the first hybridization of the original Tooth Lily. Because the species is so rare I wanted to find more ways of preserving them. This flower is one of the first successful blooms."

bh "And I want you to have it."

mc "Oh my gosh, Boris, I…"
##menu:
"I would be honored to care for it."
"I will cherish it always."

bh "Thank-you, [player_name]. I know I can count on you to care for it."

bh "...."

"He reaches out and takes your hand in his and looks lovingly into your eyes."

bh "I love you."

"You squeeze his hand back."

mc "I love you too, Boris."
