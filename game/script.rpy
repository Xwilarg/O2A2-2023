# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    voice "voice/part1/1.mp3"
    e "There he is - wow, he looks dapper! Why on earth is he in a suit and tie? I didn’t think they were going to break ground at the construction site this early."
    
    voice "voice/part1/2.mp3"
    e "Where is he going? Is he meeting someone?"
    
    voice "voice/part1/3.mp3"
    e "Another... woman?"

    e "I’m rooted to the ground, frozen on the street across from his workplace. I watch as he strides purposefully away from me."

    e "I woke up this morning and reached across the bed, hopeful. I am quickly disappointed, like I have been every morning for the past year."

    e "I shuffled from the bedroom to the kitchen. There, I’m greeted by the only men in my life: Mr. Coffee and good old cuppa Joe."

    e "Joe always comes with me to my office. He sits with me through endless online meetings with checkerboards of faces - colleagues that I barely know."

    e "I usually have my video turned off at these meetings. That way I don’t embarrass myself while I daydream about our luscious CEO."

    e "It’s not like I’m getting any at home. I would never go so far as to do anything about it, though."

    e "Is he cheating on me?"

    e "I couldn’t stand being lonely in the apartment any more. I envied his job. He can go out and talk to people every day."

    e "Hear voices unfiltered through speakers. See people in the flesh. Smell the musk and moisture of other living beings."

    e "Feel the heat rising from another warm body."

    e "I decided to surprise him at work with lunch. I was in a hurry when I left the apartment. I almost forgot my backpack - I never go anywhere without it."

    e "Now I see that surprising him was a terrible idea. He has gone so far down the street that I almost lose sight of him."

label choice_a:

    e "I sprint across to keep him in view, then slow and follow him from a distance."

    e "The city is unfamiliar to me. He picks up his pace, as if in a hurry. I start jogging to keep up."

    e "He stops abruptly outside a nondescript building, then disappears inside. I quickly follow, scanning the sign above the entrance."

    e "A funeral home?"

    e "No one’s in the lobby. A glass door swings shut to my right. I cautiously peek in."

    e "He takes a front row seat. A few strangers are scattered around the room."

    e "The woman’s portrait beside the casket startles me."

    e "It’s my picture. I gasp, loud enough that everyone turns to look at me, including him."

    e "He stares blankly but politely at me. I step in towards him."

    e "What’s going on?"

    e "Are you here for my wife’s wake, he asks."

    e "What cruel joke are you playing on me? I’m your wife!"

    e "He jerks backwards from me, brows furrowing in anger. Get away from me, he screams."

    e "The fear in his voice is palpable. I am frantic."

    e "It’s her, he yells at the others."

    e "Yes, it’s me! Your wife!"

    e "He ignores me. It’s her, the evil parasite, he continues yelling."

    e "A robed man rushes at me, shouting."

    e "You’ve taken this woman’s life, spirit! What more do you want? Leave now, leave this family alone, he warns."

    e "He waves a book at me menacingly. Pain splits my head. I fish my wallet out of my backpack and hurl it at them."

    e "Look! It’s me! I’m your wife!"

    e "All I hear is more shouting at me. Leave, parasite, leave, the voices scream."

    e "No, no! It’s my life! Mine!"

    e "This life is mine!"

label choice_b:

    e "I yell his name."

    e "He doesn’t stop or turn back."

    e "He’s too far ahead!"

    e "I sprint across the street, still calling after him."

    e "He must have his music on."

    e "I’m close enough now to reach out. I lay my hand on his shoulder."

    e "Babe..."

    e "Startled, he comes to an abrupt halt, but he doesn’t turn around. He covers my hand on his shoulder with his and squeezes."

    e "I’ve been calling you! Where are you going?"

    e "His hand falls from mine. He doesn’t respond. In fact, he starts walking again, completely ignoring me."

    e "Babe!"

    e "He picks up his pace as I run after him. He waves at someone I can’t see ahead of him."

    e "Then, he stops. I catch up to him."

    e "The hell, babe? Why are you running from me?"

    e "Confused, I walk around to face him."

    e "He is beaming, but he isn’t looking at me. He’s looking right through me."

    e "I hear a feminine voice call, sweetheart."

    e "Before I can turn around, a buzz goes through my body. I’m suddenly wracked by visions of twisted sheets and lusty moans in my brain."

    e "I step back away from him, shocked, and watch a pair of arms that aren’t mine circle his neck."

    e "She asks, is it done, and he nods."

    e "They cannot see me! What the hell is going on?"

    e "I scream in frustration as I watch them turn around and walk away. No one else on the street pays me any heed."

    e "My whole body feels heavy. My backpack weighs me down like an anchor."

    e "I can’t let him get away with whatever the hell is happening."

    e "I chase after them. I call him again. This time I’m no longer surprised he doesn’t hear me."

    e "When I catch up to them, I snake both my arms around his neck from behind and pull myself up."

    e "I wrap my legs around his waist. His gait slows a little and his shoulders hunch but he keeps on walking."

    e "I grip him tightly, pulling my face to the back of his neck. I sniff his scent and lick the fuzz just above his collar."

    e "I will be right here with you."


    # This ends the game.

    return
