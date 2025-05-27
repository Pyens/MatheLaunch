#Defines Characters
define e = Character(_('Emma') , color="#cb7eff")
define pov = Character(_('[inputname]') , color="#69ff7f")
define u = Character(_('???') , color="#cb7eff")

#Transitions (To be moved to a separate file)
define flashbulb = Fade(0.2, 0.0, 0.8, color='#ffffff')

#Game Proper
label start:
    scene bg black
    with fade

    #Name input
    $ inputname = renpy.input("My name is...")

    "{i}All my life, I've always had a dream.{/i}"
    "{i}To make a game.{/i}"
    "{i}I've always played video games. From Tetris, to Mario, to Call of Duty, to Genshin Impact, I've played all sorts of games.{/i}"
    "{i}And someday, I want to make a game of my own.{/i}"
    u "So why not just do it?"
    
    scene bg restaurant
    show emma normal

    pov "Huh?"
    e "You heard me. Why not just do it?"
    "Emma's a friend of mine. She takes BS Mathematics, and she's honestly a genius.
    She's always helped me out with everything, and she's a confident go getter who always pushes me to do my best. But still..."
    pov "What do you mean? I don't know anything about making games!"
    e "Maybe... but I do. I played around modding for a while."
    e "And I can teach you everything I know."
    e "I mean, you can be taught right?"

    #Choice1
    menu:
        "Sure!":
            jump willing
        "No thanks.": 
            jump unwilling
    
    label willing:
        show emma happy

        e "Great! This'll be fun! Let's get started!"
        pov "Huh? Wait, now?"
        e "Heck yeah! Early bird gets the worm and allat."
        e "What's with that worried look you got? Don't worry, we'll start with something simple."
        e "How about a mobile game? Something simple too like pong. Just so you can get used to it first."
        pov "Pong? Uhh... Sure, why not?"

        scene bg bedroom
        show emma thinking

        e "So, first things first. You cool with math?"
        e "I mean, this kinda thing kinda involves a lot of it."

        menu:
            "Yup!":
                jump nochoice
            "No way!": 
                jump nochoice

    label nochoice:
        pov "Umm... I-"

        show emma happy
        e "I mean we're here now so I guess you're fine with it!"
        e "So, let's get started!"

        show emma thinking
        e "Okay, so first things first. You have a computer right?"
        e "I mean, you can't really make a game without one."
        e "You do?"
        e "Then... well, before we get started, let's set up a timeline."
        e "How about... one week? I mean, it's just pong ya know? Shouldn't take too long."
        e "You can add some flair too with that time!"
        show emma normal
        e "Speaking of which, what do you want to add?"
        e "A story? Characters? Dark mode? Anything you want really."
        e "Just make sure to keep it simple. I mean, it's your first game after all."
        e "I mean, we only have a week. If it's too much, it may be too much to handle."
        e "So we should brainstorm a bit first."
        pov "Uhh... I want..."
        with flashbulb

        scene bg bedroom
        show emma tired
        e "Well... that was a lot."
        e "We've got a bunch of plans here now, but it's up to you to decide what you want."
        e "Prepare a timeline for us. Keep in mind though, we only have {color=#B30000}one week{/color}."

    label m1w:
        scene bg black
        "Together, we brainstormed many possible additions to the game."
        "Then, Emma estimated the amount of time it would take to add those additions."
        "We thought of {b}'Programming Pong'{/b}, which would take {b}1.5 days.{/b}"
        "{b}'Adding power-ups'{/b}, which would take {b}1 day.{/b}"
        "{b}'Drawing themes'{/b}, which I wanted, which would take {b}2.5 days{/b}."
        "{b}'Drawing the base art'{/b}, which would take {b}half a day{/b}."
        "{b}'Adding a Story and Characters'{/b}, which would take {b}6 days{/b}."
        "{b}'Adding Music'{/b}, which would take {b}2.8 days{/b}."
        "{b}'Adding Microtransactions'{/b}, which would take {b}three fifths of a day{/b}."
        "And {b}'Adding a Tutorial'{/b}, which would take {b}half a day{/b}."
        "We also thought of a bunch of other things, but those were the main ones."
        "We wanted to {b}maximise the amount of time we used{/b}, and we needed the {b}base art{/b} and {b}programming done at least{/b}."
        "There was only one configuration of options which would allow for this to work, which is Programming Pong, Drawing the base art, Drawing themes, and adding:"
        menu:
            "Music":
                "Wrong answer. Try again."
                jump m1w
            "Tutorial":
                "Wrong answer. Try again."
                jump m1w
            "Power-ups": 
                jump m1r
            "Microtransactions":
                "Wrong answer. Try again."
                jump m1w

    label m1r:
        "Right! Power-ups!"

        scene bg bedroom
        with fade
        show emma tired        
        
        e "So this is what you came up with?"
        e "Are you sure? Really, really sure?"
        e "Well, alright then. It's your game after all."
        e "It's already getting late though, so let's call it a night for now."
        e "Bye!"

        scene bg black
        with fade
        "{i}Suddenly, me and Emma were working together on a game.{/i}"
        "{i}It was a dream come true. I have to do my best with this game.{/i}"
        "{i}I hope I can finish it in time. I mean, it's only pong right?{/i}"
        "..."
        "{b}DAY 1 - 7 DAYS LEFT{/b}"

    #Day 1
        scene bg restaurant
        show emma greet
        e "Morning, [inputname]!"
        e "Had a good night's sleep?"
        show emma normal
        e "So, you're ready to get started now, right?"
        e "We have a lot to do after all."
        show emma thinking
        e "Well, yesterday, you said you wanted to add a bunch of flair."
        e "But before we can get started with that, you need to program the actual game first."
        e "So, let's start with that."
        e "I know you're not much of a programmer, I know how your Com Sci grades are."
        e "So maybe you could use a change in perspective."
        e "How about seeing programming as an making arguments with mathematical logic?"
        e "After all, programming is just a bunch of logic."
        pov "Uhh... I guess?"
        e "So, you know what mathematical logic is right?"
        e "You take Math 10 right?"
        
        menu:
            "Yup!":
                jump notmoron
            "I don't know...": 
                jump moron

    label moron:
        show emma disbelief
        e "..."
        e "Really?"
        e "You academic atrocity."
        e "Finee, I guess I can teach you."
        show emma thinking
        e "So, let's start with the basics."
        e "Let's say S and P are sets."
        e "Like students, Math 10 professors, Chowking employees, and so on."
        e "A categorical proposition expresses the relationship between two of these sets."
        e "There's all S are P, meaning, obviously that all S are P."
        e "For example, all gasses are fluids. All UPLB students are students."
        e "Then there's no S are P, meaning that no S are P."
        e "For example, no murderers are innocent. No cars are professors."
        e "Easy, right?"
        e "There's also some S are P, meaning some, possibly not all S are P."
        e "An example is, some fries are potatoes. Some cars are red."
        e "And finally, some S are not P, meaning some, possibly not all S are not P."
        e "Some fries are not potatoes. Some cars are not red."
        e "Get it?"
        e "Good."
        e "Then there's the compound propositions, made out of more than one simple propositions."
        e "They're connected by logical connectors, of which there are five."
        e "One is 'negation' which negates a proposition, marked by a squiggly (~) or 'not'."
        e "For example, ~p, where p is 'All Roses are Red' reads; 'Not All Roses are Red."
        e "Another is 'Conjunction' which is true if both propositions are true. It is denoted by 'p∧q' or 'p and q'"
        e "For example, p∧q, where p is 'All Roses are Red' and q is 'All Violets are Blue' reads; 'All Roses are Red and All Violets are Blue'."
        e "The third is 'Disjunction' which is true if either or both propositions are true. It is denoted by 'p∨q' or 'p or q'"
        e "For example, p∧q, where p is 'All Roses are Red' and q is 'All Violets are Blue' reads; 'All Roses are Red or All Violets are Blue'."
        e "The fourth is 'Implication' which is true unless the antecedent is true and the consequent is false."
        e "The antecedent is the first proposition, and the consequent is the second proposition."
        e "For example in the compound proposition 'If p then q', p is the antecedent and q is the consequent."
        e "It is denoted by 'p→q' or 'if p then q'"
        e "For example, p→q, where p is 'All Roses are Red' and q is 'All Violets are Blue' reads; 'If All Roses are Red then All Violets are Blue'."
        e "And finally, the fifth is 'Biconditional' which is true if both propositions are either true or false."
        e "It is denoted by 'p↔q' or 'p if and only if q'."
        e "For example, p↔q, where p is 'All Roses are Red' and q is 'All Violets are Blue' reads; 'All Roses are Red if and only if All Violets are Blue'."
        show emma normal
        e "So, you get it now?"
       
    label notmoron:  
        show emma happy
        e "Good. Let's go to your place and get started then."
        e "Don't worry too much, it's just pong."

        "She lied. It was so much harder than I thought."
        "'After all, programming is just a bunch of logic' she said, but it was so much harder than that."
        "But understanding the logic did help."
        "It was like a piece of a puzzle, you could see that it was a piece of a puzzle, but you couldn't see the whole picture."
        "It was there in the code, but code was a different monster all together."
        "It showed the right places to go at times though, so it was worth learning all that, I suppose."
        "It took three days to get the game to work."
        "Two days of fumbling, half a day at stack Exchange, and another half a day staring blankly at the screen."
        "But it was done."

        scene bg bedroom
        show emma tired
        e "That took a while, but see? Progress! Just a bit left we can leave for tomorrow."
        show emma greet
        e "I'm going now, good night!"
        e "Rest well!"
        
        scene bg black
        with fade
        "{i}With that, the coding was finished.{/i}"
        "{i}I was so tired, it took days to get the game to work, but I was so happy.{/i}"
        "{i}There was progress. Slowly, but surely, my dream was coming true.{/i}"
        "{b}DAY 4 - 4 DAYS LEFT{/b}"

    #Day 4
        scene bg exhibit
        with fade
        show emma greet
        e "Yo! [inputname]!"
        pov "Hey Emma! Why did you ask to meet me here?"
        show emma thinking
        e "I thought we could take a break from the game for a bit."
        e "You've worked hard to learn how to code these past few days, and you even got the game working."
        e "So, why not take a break and look at some art?"
        e "Also, you wanted to add some 'flair' to the game right?"
        e "What better place than an art exhibit? You can get some inspirations here for the flair!"
        e "You wanted themes right? Well, here you go!"
        show emma happy
        e "Let's go look around!"

        with flashbulb

        show emma thinking
        "Together, we saw many different paintings and artworks."
        "In the exhibit, we found a painting of a pyramid, of lightning, a lettuce, and planets."
        e "Look at this one! It's so pretty!"
        e "The composition looks weirdly amazing for how random these elements are."
        e "You know, there's actually a lot of math in geometry."
        e "Those planets? Spherical."
        e "You can put a line, and a point not on said line, and if you put a line through that point, they would meet!"
        e "It's not like the stuff you usually think about when you hear geometry, right?."
        e "The stuff you usually hear from there is Euclidean Geometry like that pyramid, where if you do the same thing I said earlier, the lines won't intersect!"
        e "There's also Hyperbolic Geometry, like that lettuce over there!"
        e "If you put a line through that point, all lines would intersect with that line! Pretty cool right?"
        e "And then there's Fractal Geometry, which is like that lightning over there."
        e "If you notice, the artist uses perspective, that's also geometry, Projective Geometry."
        e "It's cool that art has a lot of math hidden in it right? Though I'm not much of an art person."
        
        with flashbulb

        scene bg exhibit
        show emma happy
        e "That was fun!"
        e "Did you have fun too?"

        menu:
            "Yeah!":
                jump fun
            "Not really...": 
                jump unfun

    label unfun:
        show emma sad
        e "Aww... really?"
        e "Sorry for dragging you along then."
        e "I just thought it would be fun to look at some art together."
        e "But at least you got some ideas for the game right?"
        jump cont

    label fun:
        show emma happy
        e "Yay! I had fun too!"
        e "Today was great!"
        e "And look! You got some ideas for the game too!"
        jump cont

    label cont:
        show emma normal
        e "Well, it's getting late now."
        show emma tired
        e "We should head back home."
        e "Bye, [inputname]! See you tomorrow!"

        scene bg black
        with fade
        "{i}With that, the rest day ended.{/i}"
        "{i}With some inspiration, We could get started with the art tomorrow.{/i}"
        "DAY 5 - 3 DAYS LEFT"

        scene bg cafe
        with fade
        show emma greet
        e "Ey, [inputname]!"
        pov "Hi Emma! Why are we in a cafe?"
        show emma thinking
        e "Well, I thought we could use a change of scenery for a bit."
        e "It's somewhat cozier here than at home right?"
        pov "I guess? It's not the cheapest place though."
        show emma happy
        e "Don't worry about it!"
        e "It's on me!"
        show emma normal
        e "Anyways, we gotta get started on the assets for the game."
        e "You know, the graphics and stuff for your 'flair'."
        e "We only got a couple of days left, so let's lock in, and get started!"

    #jump mini3

    label amini3:
        scene bg cafe
        with fade
        show emma tired
        e "I am so not an artist."
        e "But hey, we got it!"
        e "The game looks great! Just some small things to take care of, and we're done!"
        pov "What things?"
        show emma thinking
        e "Just where to release the game."
        e "I mean, you want to release it right?"
        pov "But who would play it? I mean, it's just pong."
        e "Well, you never know. You could get lucky."
        e "Why not release it? We've worked hard on it after all."
        e "Might as well, right?"
        e "It's getting late now though, so let's call it a night."
        show emma greet
        e "Bye, [inputname]!"

        scene bg black
        with fade
        "{i}With that, the game was finished.{/i}"
        "{i}Just one last step, and my dream was coming true.{/i}"
        "{b}DAY 7 - FINAL DAY{/b}"

        scene bg restaurant
        with fade
        show emma happy
        e "Finally, we're done!"
        e "Just gotta release the thing!"
        show emma thinking
        e "So, we gotta decide where and when to release it, and how to market it."
        pov "Market it?"
        show emma normal
        e "Yeah! Maybe an ad or something."
        e "Why not? I mean, you want people to play it right?"
        pov "Sure."
        e "I already did a lot of research yesterday, did an all nighter and all."
        e "So, you just gotta look at what I found here."

        label m4w:
        e "{b}MobilePlay{/b} is a good place to release it."
        e "Games there are usually free, and they have a lot of players."
        e "A website called WeirdStatPresentations.com shows that the amount of players games there have is represented by the function {b}y=x/500^2+x.{/b}"
        e "{b}Aploded{/b} also exists."
        e "Games there are usually trash, lots of kids though."
        e "WeirdStatPresentations.com shows that the amount of players games there have is represented by the function {b}y=2(x-2){/b}."
        e "Weird stat presentations right? All verified though, pretty cool if you ask me."
        e "In the {b}long term{/b}, which one would get us more players?"

        menu:
            "MobilePlay":
                e "Are you sure? I don't know..."
                menu:
                    "Yes!":
                        e "Right!"
                        jump m4r
                    "No...":
                        e "All right, I'll say it again."
                        jump m4w
            "Aploded":
                e "Are you sure? I don't know..."
                menu:
                    "Yes!":
                        e "Really?"
                        e "Think about it."
                        jump m4w
                    "No...":
                        e "All right, I'll say it again."
                        jump m4w

        label m4r:
        show emma happy
        e "And that's that!"
        e "Pretty quick right? Thanks to my amazing research skills."
        e "Anyway, we're done now!"
        e "When we release the game, let's celebrate!"

        scene bg black
        with fade
        "{i}A FEW DAYS LATER.{/i}"

        scene bg bedroom
        with fade
        "THREE!"
        "TWO!"
        "ONE!"
        "..."
        show emma veryhappy
        e "And it's out!"
        pov "I can't believe we actually did it!"
        e "Yeah! We did it!"
        e "We made a game together!"
        e "Thank you so much for working with me on this! It was so much fun!"

        menu:
            "Thank you too!":
                jump thank
            "I did most of the work though.":
                jump brag

    label brag:
        e "Hah! Sure you did!"

    label thank:
        e "Couldn't have done this without you!"
        e "That's that!"
        e "Now, let's make another game together!"
        pov "...Sure."
        pov "Not right now though."
        e "Of course not!"
        e "Now eat! This is a celebration after all!"
        e "That food cost a lot of money, so you better eat a ton!"

        scene bg black
        with fade
        "{i}And with that, my dream came true.{/i}"
        "{i}Together with Emma, I'll go even further.{/i}"
        "{i}We'll make games that shake the world!{/i}"
        #include scene if bg celebrate finished
        #scene bg celebrate
        #"{i}Beginning with pong, we'll make great games together, as comrades.{/i}"
        "{b}END{/b}"

        return

    label unwilling:
        show emma sad
        
        e "Damn man, your loss."
        e "Anyways, I gotta go. See ya later."

        scene bg black
        with fade

        "And with that, I never really got started on my game."
        "Emma never brought it up again, and life just went on as normal."
        "I got my degree, got a job, and honestly..."
        "I wish that I had taken her up on that offer."
        "My dream was right there, but... it's too late now. Oh well."
        "{b}Regretful Ending{/b}"

        return