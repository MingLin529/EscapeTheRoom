# Course: CS 30
# Period: 1
# Date created: 20/01/08
# Date last modified: 20/01/08
# Name: Mingyuan Lin
# Description: print out the plot of the story


class Story:
    def __str__(self):
        return self.plots


class StartingPlot(Story):
    def __init__(self):
        self.plots = """
        You are John Anderson, an university student. You, who was supposed to
        return home to enjoy the summer vacation, were somehow trapped in this
        room. When a person wakes up and finds that the surrounding environment
        is strange, this is a very scary thing. As a senior YouTuber, you have
        seen animation since childhood and you with rich imagination have
        decided to face this problem alone. After some thoughts, you decide:
        """


class WatchYoutube(Story):
    def __init__(self):
        self.plots = """
        It is indeed you, what a wise choice! You pulled out your phone, opened
        the YouTube client, and watched the video you downloaded the previous
        two days. Since there is no earphone, you can only put it outlaud. Your
        voice is so noisy that it attracts someone who shouldn't.
        """


class SearchForWiFi(Story):
    def __init__(self):
        self.plots = """
        It is indeed you that you decide to pull out your phone first and
        search for WiFi here. Unfortunately, there's no WiFi and not even a
        sign of signals here. Your phone has only 2% of battery left, also
        there are 83 missed calls. You open the call log. Most of these 83
        missed calls are from your mother. The last call was at 8:07 last
        night. In other words, after 8:07 last night, you entered the no-signal
        zone. And the person kidnapped you didn't confiscate your phone. As a
        very important communication tool, mobile phones need to be handled
        properly. So you decide:
        """


class TurnOnLowBatteryMode(Story):
    def __init__(self):
        self.plots = """
        It is indeed you! You have decided to turn on your phone in
        energy-saving mode, so that if your phone enters the signal area,
        you can receive calls as soon as possible. You put your phone in your
        pocket.
        """


class TurnOffThePhone(Story):
    def __init__(self):
        self.plots = """
        It is indeed you that you decided to turn off your phone to save power.
        You are very worried that 2% of your battery will not last long. After
        you turned off your phone, you put it in your pocket.
        """


class Transition1(Story):
    def __init__(self):
        self.plots = """
        And pay attention to the pattern on the wall. You have imagined a lot
        of scenes that will only appear in the game. If it's the same as in the
        game, then this is a magic circle. Dense and complex text is written at
        the bottom of the array. On the ground in front of the array, an
        incense burner and two dishes are placed. White hair and black hair are
        separately placed on the left and right dishes. After some
        consideration, you decide:
        """


class LeaveTheHair(Story):
    def __init__(self):
        self.plots = """
        It is indeed you, your keen thinking immediately made you judge. This
        array faintly reveals an unknown atmosphere, it's better not to touch
        it. You naturally took a few steps back.
        """


class Transition2(Story):
    def __init__(self):
        self.plots = """
        Just then suddenly footsteps came from outside the door. You got
        closer, the footsteps were laid back, probably from the owner of the
        house. The steps became clearer and clearer, and it was clearly moving
        towards your room. What to do?
        """


class LayBackToBed1(Story):
    def __init__(self):
        self.plots = """
        It is indeed you, you quickly figured out a way. We can pretend to
        sleep until she leaves, then we will have another chance to act. Was
        she the one who kidnapped me? It was incredible that she was a
        white-haired old woman. Just as then, you seem to smell a strange
        smell It was that incense! She has lit the three-pillar incense. Then
        you lost your awareness.
        """

        "After waking up, you find that you are lying in the hospital. Was "
        "everything just a dream? Your mother told you that you were in a "
        "coma due to anemia. When the police found you, you layed in an "
        "unnoticeable corner of a station. In short, your body has no big "
        "deal, but there is a bloody-red mole on your face."


class TakeTheBlackHair(Story):
    def __init__(self):
        self.plots = "It is indeed you, your keen thinking immediately made "
        "you judge, this black hair must be the key to ruining this array. "
        "In this way, no matter what kind of magic this magic array is going "
        "to cast, it can be regarded as destroying one of the conditions. "
        "You are thinking so."


class LayBackToBed2(Story):
    def __init__(self):
        self.plots = "It is indeed you, you quickly figured out a way. We "
        "can pretend to sleep until she leaves, then we will have another "
        "chance to act. Was she the one who kidnapped me? It was incredible "
        "that she was a white-haired old woman. Just as then, you suddently "
        "remembered you have taken the black hair. Then I pretend to sleep..."


class LockTheDoor(Story):
    def __init__(self):
        self.plots = "It is indeed you who came up with such a bold action "
        "in such a short period of time. Yes, who said you can't lock the "
        "door of someone else's house. This can delay time as well as delay "
        "time. The door was locked, but where can I leave without leaving "
        "through the door? Your eyes moved to the window, and a bold idea "
        "came into being:"


class JumpDownTheWindow(Story):
    def __init__(self):
        self.plots = "This is an old-fashioned window, common in the last "
        "century. Unexpectedly, you start to wonder if you have actually "
        "been abducted. As wanting to trap me in the house, why not lock the "
        "windows and door? Anyways, no time to care that much. I have to "
        "say, it is indeed you! The use of curtains as an elevator, this "
        "high-end technique, has only been seen on TV before, it is still "
        "difficult to operate in practice. Fortunately, this bungalow is not "
        "high, and there are cluttered and soft lawns on the ground. It may "
        "not be too painful to fall. Just then, a dog howling at you "
        "fiercely and ran towards you. Before you landed, you are bitten."
