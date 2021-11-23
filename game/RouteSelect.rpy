label routeselect:
    $ inbox_mail = []
    scene emailbg
    $ Add_Email("Boris Habit", Boris_Email, "Hab_B@PedalMail.cob", "Borisrouteintro") ##Habit
    $ Add_Email("Kamal Bora", Kamal_Email, "bunnies66@WYSU.mountain", "Kamal_Email") ##Kamal
    $ Add_Email("Parsley Botch", Parsley_Email, "parsleybotch@lawyerup.now", "Parsley_Email") ##Parsley
    $ Add_Email("Mirphy Fotoparat", Mirphy_Email, "mirphyfotos@flashmail.zoom", "Mirphy_Email") ##Mirphy
    $ Add_Email("Pabit", Pabit_Email, "puppetmaster@PedalMail.cob", "Pabit_Email") ##Pabit
    $ Add_Email("Jerafina Tabouli", Jerafina_Email, "jlt@h.k12.wy.us", "Jerafina_Email") ##Jera
    show screen Inbox
    show screen Current_Email
    call screen Current_Email


#########
#HABIT
#########
label Borisrouteintro:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[1]
        $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Helo again [player_name]! :-)) If you hab tyme too-morrow Id like 4 U 2 com-e to the shoope 2 help me with some tasks. We need 2 promote the shop's flowurs but my friend, F..K., is busy. If u can stop bye 2 Lend A Hand, I wood GREATLY appreciated it! -B{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptHabitRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Flowers, bords and smilies. ~ Boris : -){/color}", ["Reply and Accept", "Not yet"], ["AcceptHabitRoute", "routeselect"])
        call screen EmailOptions


label AcceptHabitRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281}[player_name]{/color}", MC_Email, "{color=# 8412281}Sure! I got time tomorrow to help you out.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Boris Habit{/color}", Boris_Email, "{color=# 8412281}Womderful! I wIll c u tomrrow then! ;;-){/color}", [], [])
    jump Habit_Route

 #######
 #KAMAL
 ######
label Kamal_Email:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[2]
        $ current_conversation.Add_Message("{color=# 8412281} Kamal Bora{/color}", Kamal_Email, "{color=# 8412281} Heya, [player_name]! This is Kamal! I think a package of mine somehow got accidentally mailed to the wrong address.{/color}", [], [])
        $ current_conversation.Add_Message("{color=# 8412281} Kamal Bora{/color}", Kamal_Email, "{color=# 8412281} How does stuff like that even happen!? It's crazy! lol.{/color}", [], [])
        $ current_conversation.Add_Message("{color=# 8412281} Kamal Bora{/color}", Kamal_Email, "{color=# 8412281} Anyways, I heard you were helping around town and was wondering if you would be able to bring the package to my workplace.{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptKamalRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Kamal Bora{/color}", Kamal_Email, "{color=# 8412281}What do ya say?{/color}", ["Reply and Accept", "Not yet"], ["AcceptKamalRoute", "routeselect"])
        call screen EmailOptions


label AcceptKamalRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281}[player_name]{/color}", MC_Email, "{color=# 8412281}Sure! I got time tomorrow to help you out.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Kamal Bora{/color}", Kamal_Email, "{color=# 8412281}Great! See you tomorrow!{/color}", [], [])
    jump Kamal_Route

#########
#PARSLEY
########
label Parsley_Email:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[3]
        $ current_conversation.Add_Message("{color=# 8412281} Parsley Botch{/color}", Parsley_Email, "{color=# 8412281}I heard you were helping around town and was wondering if you would be able to bring the lunch to my workplace.{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptParsleyRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Parsley Botch{/color}", Parsley_Email, "{color=# 8412281}What do ya say?{/color}", ["Reply and Accept", "Not Yet"], ["AcceptParsleyRoute", "routeselect"])
        call screen EmailOptions


label AcceptParsleyRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281}[player_name]{/color}", MC_Email, "{color=# 8412281}Sure! I got time tomorrow to help you out.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Parsley Botch{/color}", Parsley_Email, "{color=# 8412281}Great! See you tomorrow!{/color}", [], [])
    jump Parsley_Route

#########
#JERA
########

label Jerafina_Email:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[4]
        $ current_conversation.Add_Message("{color=# 8412281} Jerafina Tabouli{/color}", Jerafina_Email, "{color=# 8412281}I heard you were helping around town and was wondering if you would be able to come to school to help make decorations.{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptJerafinaRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Jerafina Tabouli{/color}", Jerafina_Email, "{color=# 8412281}What do ya say?{/color}", ["Reply and Accept", "Not yet"], ["AcceptJerafinaRoute", "routeselect"])
        call screen EmailOptions


label AcceptJerafinaRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281}[player_name]{/color}", MC_Email, "{color=# 8412281}Sure! I got time tomorrow to help you out.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Jerafina Tabouli{/color}", Jerafina_Email, "{color=# 8412281}Great! See you tomorrow!{/color}", [], [])
    jump Jerafina_Route


#########
#PABIT
#########

## Points or Flower Quest for Pabit's route
label Pabit_Email:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[5]
        $ current_conversation.Add_Message("{color=# 8412281} Pabit{/color}", Pabit_Email, "{color=# 8412281}Helo again [player_name] u mey naut know me, butt I know u!{/color}", [], [])
        $ current_conversation.Add_Message("{color=# 8412281} Pabit{/color}", Pabit_Email, "{color=# 8412281}U r beryyy kind u know? I wached u help Ebery1 ther!{/color}", [], [])
        $ current_conversation.Add_Message("{color=# 8412281} Pabit{/color}", Pabit_Email, "{color=# 8412281}Any whoo, I hav believed we hab met before, but i wanna ask u soemting, would u liek to be mah Fwiend?{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptPabitRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Pabit{/color}", Pabit_Email, "{color=# 8412281}PLease?  -P{/color}", ["Reply and Accept", "Not yet"], ["AcceptPabitRoute", "routeselect"])
        call screen EmailOptions

label AcceptPabitRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281} Pabit{/color}", Pabit_Email, "{color=# 8412281}Thank you <3  -P{/color}", [], [])
    jump Pabit_Route


#########
#MIRPHY
#########


label Mirphy_Email:
    if RouteSelected == False:
        show screen Current_Email
        $ current_conversation = conversations[6]
        $ current_conversation.Add_Message("{color=# 8412281} Mirphy Fotoparat{/color}", Mirphy_Email, "{color=# 8412281}I heard you were helping around town and was wondering if you would be able to come to school to help make decorations.{/color}", [], [])
        $ email_options = {"Reply and Accept":"AcceptMirphyRoute", "Not yet":"routeselect"}
        $ current_conversation.Add_Message("{color=# 8412281} Mirphy Fotoparat{/color}", Mirphy_Email, "{color=# 8412281}What do ya say?{/color}", ["Reply and Accept", "Not yet"], ["AcceptMirphyRoute", "routeselect"])
        call screen EmailOptions


label AcceptMirphyRoute:
    $ RouteSelected = True
    $ current_conversation.Add_Message("{color=# 8412281}[player_name]{/color}", MC_Email, "{color=# 8412281}Sure! I got time tomorrow to help you out.{/color}", [], [])
    $ current_conversation.Add_Message("{color=# 8412281} Mirphy Fotoparat{/color}", Mirphy_Email, "{color=# 8412281} Great! See you tomorrow!{/color}", [], [])
    jump Mirphy_Route
