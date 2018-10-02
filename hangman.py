# Hangman Game with GUI
# Icons made by Webalys Freebies from www.flaticon.com is licensed by CC 3.0 BY

# -------------------- IMPORTS --------------------
import pygame
import random
import time
import math
import sys
import os
import glob

# -------------------- CATEGORY WORDS --------------------
category_objects = ['lamp', 'jug', 'microwave', 'pencil', 'shirt', 'bagpipe', 'cylinder', 'glove', 'brush', 'drop', 'umbrella', 'ivory', 'card', 'clover', 'board', 'jukebox', 'light', 'tissue', 'xylophone', 'painting']  # List of words relating to objects
category_animals = ['camel', 'badger', 'lizard', 'sphinx', 'shark', 'jellyfish', 'penguin', 'ocelot', 'monkey', 'dragon', 'dog', 'aardvark', 'wombat', 'sloth', 'elephant', 'rhinoceros', 'vixen', 'tarantula', 'iguana', 'glowworm']  # List of words relating to animals
category_ist = ['ergonomic', 'aesthestics', 'database', 'elements', 'hardware', 'application', 'data', 'file', 'processor', 'linux', 'computer', 'keyboard', 'mouse', 'design', 'pseudocode', 'algorithm', 'flowchart', 'documentation', 'functionality', 'software']  # List of words relating to IST
category_food = ['cookie', 'rhubarb', 'kiwifruit', 'pizza', 'chocolate', 'chicken', 'sandwich', 'salad', 'pie', 'cherry', 'salmon', 'jelly', 'peanut', 'jawbreaker', 'tomato', 'egg', 'cereal', 'vodka', 'carrot', 'celery']  # List of words relating to food
category_science = ['acceleration', 'velocity', 'glucose', 'chemistry', 'valency', 'chromosome', 'diffusion', 'enzyme', 'energy', 'mitochondria', 'reaction', 'dissolve', 'solubility', 'absorb', 'exothermic', 'endothermic', 'temperature', 'covalent', 'ionisation', 'ionic']  # List of words relating to science

# -------------------- PYGAME VARIABLE SETUP --------------------
FPS = 60
window_width = 640
window_height = 480

# -------------------- COLOURS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHT_BLUE = (45, 69, 170)
BRIGHT_BLUE_HIGHLIGHTED = (62, 92, 212)
BRIGHT_BLUE_GRAYED = (182, 190, 223)

# -------------------- HINT DICTIONARY --------------------
get_hint = {
    # Objects Words
    'lamp': 'A device for giving light.',
    'jug': 'A cylindrical container with a handle and a lip, used for holding and pouring liquids.',
    'microwave': 'An oven that uses microwaves to cook or heat food.',
    'pencil': 'An instrument for writing or drawing.',
    'shirt': 'A garment for the upper body.',
    'bagpipe': 'A musical instrument with reed pipes.',
    'cylinder': 'A solid geometrical figure with straight parallel sides and a circular or oval cross section.',
    'glove': 'A covering for the hand worn for protection.',
    'brush': 'An implement with a handle and a block of bristles, hair, or wire.',
    'drop': 'A small round or pear-shaped portion of liquid that hangs or falls or adheres to a surface.',
    'umbrella': 'A device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain.',
    'ivory': 'A hard creamy-white substance composing the main part of the tusks of an elephant, walrus, or narwhal.',
    'card': 'A piece of thick, stiff paper or thin pasteboard.',
    'clover': 'A plant with leaves which are typically three-lobed.',
    'board': 'A long, thin, flat piece of wood or other hard material.',
    'jukebox': 'A machine that automatically plays a selected musical recording when a coin is inserted.',
    'light': 'The natural agent that stimulates sight and makes things visible.',
    'tissue': 'A disposable piece of absorbent paper.',
    'xylophone': 'A musical instrument played by striking a row of wooden bars of graduated length with one or more small wooden or plastic beaters.',
    'painting': 'A painted picture.',

    # Animals Words
    'camel': 'A large, long-necked ungulate mammal of arid country, with long slender legs, broad cushioned feet, and either one or two humps on the back.',
    'badger': 'A heavily built omnivorous nocturnal mammal of the weasel family, typically having a grey and black coat.',
    'lizard': 'A reptile that typically has a long body and tail, four legs, movable eyelids, and a rough, scaly, or spiny skin.',
    'sphinx': 'A winged monster of Thebes, having a woman\'s head and a lion\'s body.',
    'shark': 'A long-bodied chiefly marine fish with a cartilaginous skeleton, a prominent dorsal fin, and tooth-like scales.',
    'jellyfish': 'A free-swimming marine coelenterate with a jelly-like bell or saucer-shaped body that is typically transparent and has stinging tentacles around the edge.',
    'penguin': 'A large flightless seabird of the southern hemisphere, with black upper parts and white underparts and wings developed into flippers for swimming under water.',
    'ocelot': 'A medium-sized wild cat that has an orange-yellow coat marked with black stripes and spots, native to South and Central America.',
    'monkey': 'A small to medium-sized primate that typically has a long tail, most kinds of which live in trees in tropical countries.',
    'dragon': 'A mythical monster like a giant reptile.',
    'dog': 'A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractile claws, and a barking, howling, or whining voice.',
    'aardvark': 'A nocturnal badger-sized burrowing mammal of Africa, with long ears, a tubular snout, and a long extensible tongue, feeding on ants and termites.',
    'wombat': 'A burrowing plant-eating Australian marsupial which resembles a small bear with short legs.',
    'sloth': 'A slow-moving tropical American mammal that hangs upside down from the branches of trees using its long limbs and hooked claws.',
    'elephant': 'A very large plant-eating mammal with a prehensile trunk, long curved ivory tusks, and large ears, native to Africa and southern Asia.',
    'rhinoceros': 'A large, heavily built plant-eating mammal with one or two horns on the nose and thick folded skin, native to Africa and southern Asia.',
    'vixen': 'A female fox.',
    'tarantula': 'A very large hairy spider found chiefly in tropical and subtropical America, some kinds of which are able to catch small lizards, frogs, and birds.',
    'iguana': 'A large arboreal tropical American lizard with a spiny crest along the back and greenish coloration.',
    'glowworm': 'A soft-bodied beetle with luminescent organs in the abdomen.',

    # IST Words
    'ergonomic': 'Relating to or designed for efficiency and comfort in the working environment.',
    'aesthetics': 'A set of principles concerned with the nature and appreciation of beauty.',
    'database': 'A structured set of data held in a computer.',
    'elements': 'The rudiments of a subject.',
    'hardware': 'The machines, wiring, and other physical components of a computer or other electronic system.',
    'application': 'A program or piece of software designed to fulfil a particular purpose.',
    'data': 'Facts and statistics collected together for reference or analysis.',
    'file': 'A collection of data, programs, etc. stored in a computer\'s memory or on a storage device under a single identifying name.',
    'processor': 'The part of a computer in which operations are controlled and executed.',
    'linux': 'An open-source operating system modelled on UNIX.',
    'computer': 'An electronic device which is capable of receiving information.',
    'keyboard': 'A panel of keys that operate a computer or typewriter.',
    'mouse': 'A small handheld device which is moved across a mat or flat surface to move the cursor on a computer screen.',
    'design': 'The art or action of conceiving of and producing a plan or drawing of something before it is made.',
    'pseudocode': 'A notation resembling a simplified programming language.',
    'algorithm': 'A process or set of rules to be followed in calculations or other problem-solving operations.',
    'flowchart': 'A graphical representation of a computer program in relation to its sequence of functions.',
    'documentation': 'Material that provides official information or evidence or that serves as a record.',
    'functionality': 'The range of operations that can be run on a computer or other electronic system.',
    'software': 'The programs and other operating information used by a computer.',

    # Food Words
    'cookie': 'A sweet biscuit.',
    'rhubarb': 'The thick reddish or green leaf stalks of a cultivated plant of the dock.',
    'kiwifruit': 'A fruit with a thin hairy skin, green flesh, and black seeds.',
    'pizza': 'A dish consting a flat round base of dough baked with a topping of tomatoes and cheese, typically with added meat, fish, or vegetables.',
    'chocolate': 'A food in the form of a paste or solid block made from roasted and ground cacao seeds.',
    'chicken': 'Meat from a chicken.',
    'sandwich': 'An item of food consisting of two pieces of bread with a filling between them.',
    'salad': 'A cold dish of various mixtures of raw or cooked vegetables.',
    'pie': 'A baked dish of fruit, or meat and vegetables, typically with a top and base of pastry.',
    'cherry': 'A small, soft round stone fruit that is typically bright or dark red.',
    'salmon': 'A large edible fish that is a popular sporting fish, much prized for its pink flesh.',
    'jelly': 'A small sweet made with gelatin.',
    'peanut': 'The oval seed of a tropical South American plant.',
    'jawbreaker': 'A large, hard, spherical sweet.',
    'tomato': 'A glossy red, or occasionally yellow, pulpy edible fruit which is eaten as a vegetable or in salad.',
    'egg': 'An oval or round object laid by a female bird, reptile, fish, or invertebrate.',
    'cereal': 'A breakfast food made from roasted grain, typically eaten with milk.',
    'vodka': 'An alcoholic spirit of Russian origin.',
    'carrot': 'A tapering orange-coloured root eaten as a vegetable.',
    'celery': 'A cultivated plant of the parsley family, with closely packed succulent leaf stalks which are used as a salad or cooked vegetable.',

    # Science Words
    'acceleration': 'The rate of change of velocity per unit of time.',
    'velocity': 'The speed of something in a given direction.',
    'glucose': 'A simple sugar which is an important energy source in living organisms and is a component of many carbohydrates.',
    'chemistry': 'The branch of science concerned with the substances of which matter is composed, the investigation of their properties and reactions, and the use of such reactions to form new substances.',
    'valency': 'The combining power of an element.',
    'chromosome': 'A thread-like structure of nucleic acids and protein found in the nucleus of most living cells, carrying genetic information in the form of genes.',
    'diffusion': 'The intermingling of substances by the natural movement of their particles.',
    'enzyme': 'A substance produced by a living organism which acts as a catalyst to bring about a specific biochemical reaction.',
    'energy': 'The property of matter and radiation which is manifest as a capacity to perform work.',
    'mitochondria': 'An organelle found in large numbers in most cells, in which the biochemical processes of respiration and energy production occur.',
    'reaction': 'A force exerted in opposition to an applied force.',
    'dissolve': 'Become or cause to become incorporated into a liquid so as to form a solution.',
    'solubility': 'Able to be dissolved.',
    'absorb': 'Take in or soak up by chemical or physical action.',
    'exothermic': 'A reaction or process accompanied by the release of heat.',
    'endothermic': 'A reaction or process accompanied by or requiring the absorption of heat.',
    'temperature': 'The degree or intensity of heat present in a substance or object.',
    'covalent': 'Relating to or denoting chemical bonds formed by the sharing of electrons between atoms.',
    'ionisation': 'Convert (an atom, molecule, or substance) into an ion or ions, typically by removing one or more electrons.',
    'ionic': 'A chemical bond formed by the electrostatic attraction of oppositely charged ions.'
}

# -------------------- SCENE BASE --------------------


class SceneBase:  # Base template for all scenes
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):  # This method will receive all the events that happened since the last frame
        print("uh-oh, you didn't override this in the child class")

    def Update(self):  # Put your game logic in here for the scene
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):  # Put your render code here. It will receive the main screen Surface as input
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):  # Function to switch to another scene
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

# -------------------- ANIMATION FUNCTIONS --------------------


class LogoSprite(pygame.sprite.Sprite):  # Image animation for LOGO
    def __init__(self):
        super(LogoSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'logo'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in logo/

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(195, 70, 250, 250)  # Create a shape 250px x 250px at x195 y70

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 9:  # Once counter reaches 9
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


class ObjectsSprite(pygame.sprite.Sprite):  # Image animation for OBJECTS CATEGORY BAR
    def __init__(self):
        super(ObjectsSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'category_pics/objects'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in category_pics/objects

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(40, 70, 560, 60)  # Create a shape 560px x 60px at x40 y70

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 3:  # Once counter reaches 3
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


class AnimalsSprite(pygame.sprite.Sprite):  # Image animation for ANIMALS CATEGORY BAR
    def __init__(self):
        super(AnimalsSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'category_pics/animals'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in category_pics/animals

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(40, 155, 560, 60)  # Create a shape 560px x 60px at x40 y155

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 3:  # Once counter reaches 3
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


class ISTSprite(pygame.sprite.Sprite):  # Image animation for IST CATEGORY BAR
    def __init__(self):
        super(ISTSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'category_pics/ist'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in category_pics/ist

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(40, 240, 560, 60)  # Create a shape 560px x 60px at x40 y240

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 3:  # Once counter reaches 3
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


class FoodSprite(pygame.sprite.Sprite):  # Image animation for FOOD CATEGORY BAR
    def __init__(self):
        super(FoodSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'category_pics/food'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in category_pics/food

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(40, 325, 560, 60)  # Create a shape 560px x 60px at x40 y325

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 3:  # Once counter reaches 3
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


class ScienceSprite(pygame.sprite.Sprite):  # Image animation for SCIENCE CATEGORY BAR
    def __init__(self):
        super(ScienceSprite, self).__init__()
        self.counter, self.index, self.images = 0, 0, []
        self.directory = 'category_pics/science'  # Directory to the folder containing the images
        [self.images.append(pygame.image.load(self.directory + '/0' + str(i) + '.png')) if len(str(i)) == 1 else self.images.append(pygame.image.load(self.directory + '/' + str(i) + '.png')) for i in range(len(glob.glob(os.path.join(self.directory, '*'))))]  # Create a list of pygame image.load for each image in category_pics/science

        self.image = self.images[self.index]  # Current image
        self.rect = pygame.Rect(40, 410, 560, 60)  # Create a shape 560px x 60px at x40 y410

    def update(self):
        self.counter += 1  # Counter for updating frame
        if self.counter == 3:  # Once counter reaches 3
            self.index += 1  # Increment image index
            if self.index >= len(self.images):  # If the image index is the last one
                self.index = 0  # Reset image index
            self.image = self.images[self.index]  # Set the current image
            self.counter = 0  # Reset counter


animation_logo = pygame.sprite.Group(LogoSprite())  # Animate the individual logo images
animation_objects = pygame.sprite.Group(ObjectsSprite())  # Animate the individual objects category bar images
animation_animals = pygame.sprite.Group(AnimalsSprite())  # Animate the individual animals category bar images
animation_ist = pygame.sprite.Group(ISTSprite())  # Animate the individual IST category bar images
animation_food = pygame.sprite.Group(FoodSprite())  # Animate the individual food category bar images
animation_science = pygame.sprite.Group(ScienceSprite())  # Animate the individual science category bar images

# -------------------- FUNCTIONS --------------------


def blit_text(surface, text, pos, font, max_width, max_height):  # Function to display text within set area
    words = [word.split(' ') for word in text.splitlines()]  # Array where each row is a list of words
    space = font.size(' ')[0]  # The width of a space
    x, y = pos  # Split coordinates to x and y
    for line in words:
        for word in line:
            word_surface = font.render(word, True, BLACK)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x
                y += word_height  # Start on new row
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x
        y += word_height  # Start on new row

# -------------------- MAIN CODE --------------------


def run_game(width, height, fps, starting_scene):  # Function to start and prepare everything
    global mono_font, hint_font, paragraph_font, credits_font, credits_title_font, credits_paragraph_font, font, box, highlight_box, start_title, play_text, credits_text  # Globalise the fonts for use in the other classes
    pygame.init()  # Initialise Pygame
    pygame.display.set_caption('Hangman')  # Set the window title to 'Hangman'

    mono_font = pygame.font.Font('fonts/PTMono.ttc', 26)  # Monospace Font - PTMono 26
    hint_font = pygame.font.Font('fonts/Arial.ttf', 14)  # Hint Font - Arial 14
    paragraph_font = pygame.font.Font('fonts/Arial.ttf', 24)  # Paragraph Font - Arial 24
    credits_font = pygame.font.Font('fonts/TektonPro-Bold.otf', 20)  # Credits Font - TektonPro Bold 20
    credits_title_font = pygame.font.Font('fonts/TektonPro-Bold.otf', 24)  # Credits Title Font - TektonPro Bold 24
    credits_paragraph_font = pygame.font.Font('fonts/Arial.ttf', 18)  # Credits Paragraph Font - Arial 18
    font = pygame.font.Font('fonts/TektonPro-Bold.otf', 26)  # Default font - TektonPro Bold 26

    box = pygame.Surface((170, 38))  # Creates a box 170px x 38px
    box.set_alpha(153)  # Set the alpha to 153/255
    box.fill(BLACK)  # Fill the box black

    highlight_box = pygame.Surface((560, 60))  # Creates a box 560px x 60px
    highlight_box.set_alpha(38)  # Set the alpha to 38
    highlight_box.fill(WHITE)  # Fill the box white

    # As the starting scene is the title scene, these variables need to be placed here
    start_title = font.render('Hangman Game', True, BLACK)  # Render 'Hangman Game' text black with font 'font'.
    play_text = font.render('Play', True, WHITE)  # Render 'Play' text white with font 'font'.
    credits_text = credits_font.render('Credits', True, WHITE)  # Render 'Credits' text white with font 'credits font'

    pygame.mixer.music.load('Happy Ukulele.mp3')  # Load and play the music 'Happy Ukulele'
    pygame.mixer.music.set_volume(0.5)  # Set the volume to 0.5/1
    pygame.mixer.music.play(-1)  # Set the music to loop infinitely

    screen = pygame.display.set_mode((width, height))  # Set the screen dimensions
    clock = pygame.time.Clock()  # Clock for frame speed

    active_scene = starting_scene

    while active_scene is not None:  # While there is a scene that's active
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:  # If user clicks 'X' button
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:  # If user has a key pressed down
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]  # Left 'ALT' or Right 'ALT' key
                if event.key == pygame.K_ESCAPE:  # If user pressed 'ESCAPE' key
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)

# -------------------- SCENES --------------------


class TitleScene(SceneBase):  # Home screen
    def __init__(self):
        SceneBase.__init__(self)
        self.play_hover = 0  # Hovering status for play button
        self.credits_hover = 0  # Hovering status for credit button
        self.music_status = True  # Music status for music button

        self.title_background = pygame.image.load('screens/title_screen.png')  # Image of background
        self.music_icon = pygame.image.load('music.png')  # Image of music icon
        self.music_mute_icon = pygame.image.load('music_mute.png')  # Image of music mute icon

        self.play_button = pygame.Rect(245, 370, 150, 50)  # Location and size for play button
        self.music_button = pygame.Rect(587, 5, 48, 48)  # Location and size for music button
        self.credits_button = pygame.Rect(530, 445, 100, 25)  # Location and size for credits button

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # If user pressed 'RETURN' or 'ENTER' key
                self.SwitchToScene(InstructionScene())  # Switch to instructions scene

            if self.play_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over play button
                self.play_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked play button
                    self.SwitchToScene(InstructionScene())  # Switch to instructions scene
            else:  # If mouse isn't hovering over play button
                self.play_hover = 0

            if self.credits_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over credits button
                self.credits_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked credits button
                    self.SwitchToScene(CreditsScene())  # Switch to credits scene
            else:
                self.credits_hover = 0

            if self.music_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over music button
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked on music button
                    if self.music_status:  # If music is currently playing
                        self.music_status = False
                        pygame.mixer.music.set_volume(0)  # Set the volume of the music to 0
                    else:  # If music isn't currently playing
                        self.music_status = True
                        pygame.mixer.music.set_volume(0.5)  # Set the volume of the music to 0.5/1

    def Update(self):  # Game logic goes in here.
        pass

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        screen.blit(self.title_background, (0, 0))  # Display background
        screen.blit(start_title, (320 - start_title.get_width() // 2, 40 - start_title.get_height() // 2))  # Display 'Hangman Game' title
        animation_logo.update()  # Update logo image
        animation_logo.draw(screen)  # Display updated logo image

        if self.music_status:  # If music is currently playing
            screen.blit(self.music_icon, (587, 5))  # Display music icon
        else:  # If music isn't currently playing
            screen.blit(self.music_mute_icon, (587, 5))  # Display muted music icon

        if self.play_hover == 0:  # If mouse isn't hovering over play button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.play_button)  # Display normal play button
        else:  # If mouse is hovering over play button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.play_button)  # Display highlighted play button

        if self.credits_hover == 0:  # If mouse isn't hovering over credits button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.credits_button)  # Display normal credits button
        else:  # If mouse is hovering over credits button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.credits_button)  # Display highlighted credits button

        screen.blit(play_text, (320 - play_text.get_width() // 2, 398 - play_text.get_height() // 2))  # Display 'Play' text
        screen.blit(credits_text, (580 - credits_text.get_width() // 2, 460 - credits_text.get_height() // 2))  # Display 'Credits' text


class CreditsScene(SceneBase):  # Credits screen
    def __init__(self):
        SceneBase.__init__(self)
        self.next_hover = 0  # Hovering status for next button
        self.prev_hover = 0  # Hovering status for prev button
        self.back_hover = 0  # Hovering status for back button
        self.page_number = 0   # Current page number

        self.credits_background = pygame.image.load('screens/credits_screen.png')  # Image of background

        self.next_button = pygame.Rect(371, 376, 145, 38)  # Location and size for next button
        self.prev_button = pygame.Rect(131, 376, 145, 38)  # Location and size for prev button
        self.back_button = pygame.Rect(530, 445, 100, 25)  # Location and size for back button

        self.credits_title = font.render('Credits', True, BLACK)  # Render 'Credits' text black with font 'font'
        self.next_text = font.render('Next', True, WHITE)  # Render 'Next' text white with font 'font'
        self.prev_text = font.render('Prev', True, WHITE)  # Render 'Prev' text white with font' 'font'
        self.back_text = credits_font.render('Back', True, WHITE)  # Render 'Back' text white with font 'credits font'

        self.game_designer = credits_title_font.render('Game Designer', True, BLACK)  # Render 'Game Designer' text black with font 'credits title font'
        self.producers = credits_title_font.render('Producers', True, BLACK)  # Render 'Producers' text black with font 'credits title font'
        self.artists = credits_title_font.render('Artists', True, BLACK)  # Render 'Artists' text black with font 'credits title font'
        self.audio = credits_title_font.render('Audio', True, BLACK)  # Render 'Audio' text black with font 'credits title font'
        self.special_thanks = credits_title_font.render('Special Thanks', True, BLACK)  # Render 'Special Thanks' text black with font 'credits title font'

        self.game_designer_list = credits_paragraph_font.render('Oliver Lin', True, BLACK)  # Render 'Oliver Lin' text black with font 'credits paragraph font'
        self.producers_list = credits_paragraph_font.render('Oliver Lin   Nerd Paradise', True, BLACK)  # Render text 'Oliver Lin   Nerd Paradise' text black with font 'credits paragraph font'
        self.artists_list = credits_paragraph_font.render('Oliver Lin   www.flaticon.com   Freepik', True, BLACK)  # Render text 'Oliver Lin   www.flaticon.com   Freepik' text black with font 'credits paragraph font'
        self.audio_list = credits_paragraph_font.render('AudioMicro', True, BLACK)  # Render text 'AudioMicro' text black with font 'credits paragraph font'
        self.special_thanks_list = 'Michael Chen, Wing Tim Choi, Xavier Hinton, Patrick Lin, Mrinnank Sinha'  # String of names

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if self.page_number == 0:  # If current page number is 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # If user pressed 'RIGHT ARROW' key
                    self.page_number = 1

                if self.next_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over next button
                    self.next_hover = 1
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked next button
                        self.page_number = 1
                else:  # If mouse isn't hovering over next button
                    self.next_hover = 0

            if self.page_number == 1:  # If current page number is 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:  # If user pressed 'LEFT ARROW' key
                    self.page_number = 0

                if self.prev_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over prev button
                    self.prev_hover = 1
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked on prev button
                        self.page_number = 0
                else:  # If mouse isn't hovering over prev button
                    self.prev_hover = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:  # If user pressed 'BACKSPACE' or 'DELETE' key
                self.SwitchToScene(TitleScene())  # Switch to title scene

            if self.back_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over back button
                self.back_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked on back button
                    self.SwitchToScene(TitleScene())  # Switch to title scene
            else:  # If mouse isn't hovering over back button
                self.back_hover = 0

    def Update(self):  # Game logic goes in here.
        pass

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        screen.blit(self.credits_background, (0, 0))  # Display background
        screen.blit(self.credits_title, (320 - self.credits_title.get_width() // 2, 40 - self.credits_title.get_height() // 2))  # Display 'Credits' title

        if self.page_number == 0:  # If current page number is 0
            pygame.draw.rect(screen, BRIGHT_BLUE_GRAYED, self.prev_button)  # Gray out prev button
            if self.next_hover == 0:  # If mouse isn't hovering over next button
                pygame.draw.rect(screen, BRIGHT_BLUE, self.next_button)  # Display normal button
            else:  # If mouse is hovering over next button
                pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.next_button)  # Display highlighted button

            screen.blit(self.game_designer, (320 - self.game_designer.get_width() // 2, 100 - self.game_designer.get_height() // 2))  # Display 'Game Designer' text
            screen.blit(self.producers, (320 - self.producers.get_width() // 2, 170 - self.producers.get_height() // 2))  # Display 'Producers' text
            screen.blit(self.artists, (320 - self.artists.get_width() // 2, 240 - self.artists.get_height() // 2))  # Display 'Artists' text
            screen.blit(self.audio, (320 - self.audio.get_width() // 2, 310 - self.audio.get_height() // 2))  # Display 'Audio' text

            screen.blit(self.game_designer_list, (320 - self.game_designer_list.get_width() // 2, 125 - self.game_designer.get_height() // 2))  # Display 'Oliver Lin' text
            screen.blit(self.producers_list, (320 - self.producers_list.get_width() // 2, 195 - self.producers_list.get_height() // 2))  # Display ' Oliver Lin   Nerd Paradise' text
            screen.blit(self.artists_list, (320 - self.artists_list.get_width() // 2, 265 - self.artists_list.get_height() // 2))  # Display 'Oliver Lin   www.flaticon.com   Freepik' text
            screen.blit(self.audio_list, (320 - self.audio_list.get_width() // 2, 325 - self.artists_list.get_height() // 2))  # Display 'AudioMicro' text

        if self.page_number == 1:  # If current page number is 1
            pygame.draw.rect(screen, BRIGHT_BLUE_GRAYED, self.next_button)  # Gray out next button
            if self.prev_hover == 0:  # If mouse isn't hovering over prev button
                pygame.draw.rect(screen, BRIGHT_BLUE, self.prev_button)  # Display normal prev button
            else:  # If mouse is hovering over prev button
                pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.prev_button)  # Display highlighted prev button

            screen.blit(self.special_thanks, (320 - self.special_thanks.get_width() // 2, 100 - self.special_thanks.get_height() // 2))  # Display 'Special Thanks' text
            blit_text(screen, self.special_thanks_list, (30, 125), credits_paragraph_font, 610, window_height)  # Render 'Michael Chen, Michael Chen 2, Wing Tim Choi, Xavier Hinton, Patrick Lin, Mrinnank Sinha' black with font 'credits paragraph font'

        if self.back_hover == 0:  # If mouse isn't hovering over back button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.back_button)  # Display normal back button
        else:  # If mouse is hovering over back button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.back_button)  # Display highlighted back button

        screen.blit(self.next_text, (443 - self.next_text.get_width() // 2, 398 - self.next_text.get_height() // 2))  # Display 'Next' text
        screen.blit(self.prev_text, (203 - self.prev_text.get_width() // 2, 398 - self.prev_text.get_height() // 2))  # Display 'Prev' text
        screen.blit(self.back_text, (580 - self.back_text.get_width() // 2, 460 - self.back_text.get_height() // 2))  # Dispaly 'back' text


class InstructionScene(SceneBase):  # Instructions screen
    def __init__(self):
        SceneBase.__init__(self)
        self.continue_hover = 0  # Hovering status for continue button

        self.instruction_background = pygame.image.load('screens/instructions_screen.png')  # Image of background

        self.continue_button = pygame.Rect(40, 370, 560, 50)  # Location and size for continue button

        self.instruction_title = font.render('Instructions', True, BLACK)  # Render 'Instructions' text black with font 'font'
        self.continue_text = font.render('Continue...', True, WHITE)  # Render 'Continue...' text white with font 'font'
        self.instructions = 'Hangman is a quick and easy game for at least two players. One player makes up a secret word, while the other player(s) tries to guess the word by asking what letters it contains. However, every wrong guess brings you one step closer to losing.'  # String of game instructions

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # If user pressed 'RETURN' or 'ENTER'
                self.SwitchToScene(CategoryScene())  # Switch to category scene

            if self.continue_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over continue button
                self.continue_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked continue button
                    self.SwitchToScene(CategoryScene())  # Switch to category scene
            else:  # If mouse isn't hovering over continue button
                self.continue_hover = 0

    def Update(self):  # Game logic goes in here.
        pass

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.  # Render code goes here. It will receive the main screen Surface as input.
        screen.blit(self.instruction_background, (0, 0))  # Display background
        screen.blit(self.instruction_title, (320 - self.instruction_title.get_width() // 2, 40 - self.instruction_title.get_height() // 2))  # Display 'Instructions' title

        if self.continue_hover == 0:  # If mouse isn't hovering over continue button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.continue_button)  # Display normal continue button
        else:  # If mouse is hovering over continue button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.continue_button)  # Display highlighted continue button

        blit_text(screen, self.instructions, (30, 100), paragraph_font, window_width, window_height)  # Render instructions text black with font 'paragraph font'
        screen.blit(self.continue_text, (320 - self.continue_text.get_width() // 2, 398 - self.continue_text.get_height() // 2))  # Display 'Continue...' text


class CategoryScene(SceneBase):  # Category selection screen
    def __init__(self):
        SceneBase.__init__(self)
        self.objects_hover = 0  # Hovering status for objects category bar
        self.animals_hover = 0  # Hovering status for animals category bar
        self.ist_hover = 0  # Hovering status for IST category bar
        self.food_hover = 0  # Hovering status for food category bar
        self.science_hover = 0  # Hovering status for science category bar
        self.category_selected = 0  # Current selected category

        self.category_background = pygame.image.load('screens/category_screen.png')  # Image of background
        self.objects_image = pygame.image.load('category_pics/objects/00.png')  # Image of objects category bar
        self.animals_image = pygame.image.load('category_pics/animals/00.png')  # Image of animals category bar
        self.ist_image = pygame.image.load('category_pics/ist/00.png')  # Image of IST category bar
        self.food_image = pygame.image.load('category_pics/food/00.png')  # Image of food category bar
        self.science_image = pygame.image.load('category_pics/science/00.png')  # Image of science category bar

        self.objects_button = pygame.Rect(40, 70, 560, 60)  # Location and size for objects category bar
        self.animals_button = pygame.Rect(40, 155, 560, 60)  # Location and size for animals category bar
        self.ist_button = pygame.Rect(40, 240, 560, 60)  # Location and size for IST category bar
        self.food_button = pygame.Rect(40, 325, 560, 60)  # Location and size for food category bar
        self.science_button = pygame.Rect(40, 410, 560, 60)  # Location and size for science category bar

        self.category_title = font.render('Select a Category', True, BLACK)  # Render 'Select a Category' text black with font 'font'
        self.objects_text = font.render('Objects', True, WHITE)  # Render 'Objects' text white with font 'font'
        self.animals_text = font.render('Animals', True, WHITE)  # Render 'Animals' text white with font 'font'
        self.ist_text = font.render('IST', True, WHITE)  # Render 'IST' text white with font 'font'
        self.food_text = font.render('Food', True, WHITE)  # Render 'Food' text white with font 'font'
        self.science_text = font.render('Science', True, WHITE)  # Render 'Science' text white with font 'font'

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if self.objects_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over objects category bar
                self.objects_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked objects category bar
                    self.category_selected = 1
                    self.SwitchToScene(GameScene())  # Switch to game scene
            else:  # If mouse isn't hovering over objects category bar
                self.objects_hover = 0

            if self.animals_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over animals category bar
                self.animals_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked animals category bar
                    self.category_selected = 2
                    self.SwitchToScene(GameScene())  # Switch to game scene
            else:  # If mouse isn't hovering over animals category bar
                self.animals_hover = 0

            if self.ist_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over IST category bar
                self.ist_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked IST category bar
                    self.category_selected = 3
                    self.SwitchToScene(GameScene())  # Switch to game scene
            else:  # If mouse isn't hovering over IST category bar
                self.ist_hover = 0

            if self.food_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over food category bar
                self.food_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked food category bar
                    self.category_selected = 4
                    self.SwitchToScene(GameScene())  # Switch to game scene
            else:  # If mouse isn't hovering over food category bar
                self.food_hover = 0

            if self.science_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over science category bar
                self.science_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked science category bar
                    self.category_selected = 5
                    self.SwitchToScene(GameScene())  # Switch to game scene
            else:  # If mouse isn't hovering over science category bar
                self.science_hover = 0

    def Update(self):  # Game logic goes in here.
        global secret, category_number  # Globalise these two variables for use in game scene

        if self.category_selected == 1:  # If selected category is objects
            secret = list(random.choice(category_objects))  # Choose a random word from the objects category
            print('Secret word is: ' + ''.join(secret))  # Print out the secret word in console log
        elif self.category_selected == 2:  # If selected category is animals
            secret = list(random.choice(category_animals))  # Choose a random word from the animals category
            print('Secret word is: ' + ''.join(secret))  # Print out the secret word in console log
        elif self.category_selected == 3:  # If selected category is IST
            secret = list(random.choice(category_ist))  # Choose a random word from the IST category
            print('Secret word is: ' + ''.join(secret))  # Print out the secret word in console log
        elif self.category_selected == 4:  # If selected category is food
            secret = list(random.choice(category_food))  # Choose a random word from the food category
            print('Secret word is: ' + ''.join(secret))  # Print out the secret word in console log
        elif self.category_selected == 5:  # If selected category is science
            secret = list(random.choice(category_science))  # Choose a random word from the science category
            print('Secret word is: ' + ''.join(secret))  # Print out the secret word in console log

        category_number = self.category_selected

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        screen.blit(self.category_background, (0, 0))  # Display background
        screen.blit(self.category_title, (320 - self.category_title.get_width() // 2, 40 - self.category_title.get_height() // 2))  # Display 'Select a Category' title

        if self.objects_hover == 0:  # If mouse isn't hovering over objects category bar
            screen.blit(self.objects_image, (40, 70))  # Display the still image of objects category bar
        else:  # If mouse is hovering over objects category bar
            animation_objects.update()  # Update animation to next frame
            animation_objects.draw(screen)  # Display frame
            screen.blit(highlight_box, (40, 70))  # Display a highlighted box over objects category bar

        if self.animals_hover == 0:  # If mouse isn't hovering over animals category bar
            screen.blit(self.animals_image, (40, 155))  # Display the still image of animals category bar
        else:  # If mouse is hovering over animals category bar
            animation_animals.update()  # Update animation to next frame
            animation_animals.draw(screen)  # Display frame
            screen.blit(highlight_box, (40, 70))  # Display a highlighted box over animals category bar

        if self.ist_hover == 0:  # If mouse isn't hovering over IST category bar
            screen.blit(self.ist_image, (40, 240))  # Display the still image of IST category bar
        else:  # If mouse is hovering over IST category bar
            animation_ist.update()  # Update animation to next frame
            animation_ist.draw(screen)  # Display frame
            screen.blit(highlight_box, (40, 240))  # Display a highlighted box over IST category bar

        if self.food_hover == 0:  # If mouse isn't hovering over food category bar
            screen.blit(self.food_image, (40, 325))  # Display the still image of food category bar
        else:  # If mouse is hovering over food category bar
            animation_food.update()  # Update animation to next frame
            animation_food.draw(screen)  # Display frame
            screen.blit(highlight_box, (40, 325))  # Display a highlighted box over food category bar

        if self.science_hover == 0:  # If mouse isn't hovering over science category bar
            screen.blit(self.science_image, (40, 410))  # Display the still image of science category bar
        else:  # If mouse is hovering over science category bar
            animation_science.update()  # Update animation to next frame
            animation_science.draw(screen)  # Display frame
            screen.blit(highlight_box, (40, 410))  # Display a highlighted box over science category bar

        screen.blit(box, (235, 81))  # Display a black box over objects bar
        screen.blit(box, (235, 166))  # Display a black box over animals bar
        screen.blit(box, (235, 251))  # Display a black box over IST bar
        screen.blit(box, (235, 336))  # Display a black box over food bar
        screen.blit(box, (235, 421))  # Display a black box over science bar

        screen.blit(self.objects_text, (320 - self.objects_text.get_width() // 2, 105 - self.objects_text.get_height() // 2))  # Display 'Objects' text
        screen.blit(self.animals_text, (320 - self.animals_text.get_width() // 2, 190 - self.animals_text.get_height() // 2))  # Display 'Animals' text
        screen.blit(self.ist_text, (320 - self.ist_text.get_width() // 2, 275 - self.ist_text.get_height() // 2))  # Display 'IST' text
        screen.blit(self.food_text, (320 - self.food_text.get_width() // 2, 360 - self.food_text.get_height() // 2))  # Display 'Food' text
        screen.blit(self.science_text, (320 - self.science_text.get_width() // 2, 445 - self.science_text.get_height() // 2))  # Display 'Science' text


class GameScene(SceneBase):  # Hangman game screen
    def __init__(self):
        SceneBase.__init__(self)
        self.hangman_pic = 0  # Current hangman pic status
        self.counter = 0  # One time counter variable
        self.hint_hover = 0  # Hovering status for hint button
        self.asked_hint = 0  # Whether user has asked for a hint
        self.win = 0  # Whether the user has won
        self.lose = 0  # Whether the user has lost
        self.selected_letter = ''  # Current selected letter
        self.secret_list = []  # List of secret word split between each letter obfuscated to '_'
        self.used_letters = []  # List of already guessed letters

        self.objects_background = pygame.image.load('screens/game_screen_objects.png')  # Image of objects background
        self.animals_background = pygame.image.load('screens/game_screen_animals.png')  # Image of animals background
        self.ist_background = pygame.image.load('screens/game_screen_ist.png')  # Image of IST background
        self.food_background = pygame.image.load('screens/game_screen_food.png')  # Image of food background
        self.science_background = pygame.image.load('screens/game_screen_science.png')  # Image of science background

        self.hint_button = pygame.Rect(468, 415, 152, 50)  # Location and size for hint button

        self.game_title = font.render('Hangman', True, BLACK)  # Render 'Hangman' text black with font 'font'
        self.used_letters_title = font.render('Used Letters', True, BLACK)  # Render 'Used Letters' text black with font 'font'
        self.hint_text = font.render('Hint', True, WHITE)  # Render 'Hint' text white with font 'font'
        self.display_message = font.render('', True, BLACK)  # Render '' text black with font 'font'

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if event.type == pygame.KEYDOWN:  # If key is pressed down
                self.selected_letter = event.unicode

            if self.hint_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over hint button
                self.hint_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked hint button
                    self.asked_hint = 1
            else:  # If mouse isn't hovering over hint button
                self.hint_hover = 0

            if self.win == 1 or self.lose == 1:  # If user has won or lost
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # If user pressed 'RETURN' or 'ENTER' key
                    self.SwitchToScene(ScoreScene())  # Switch to score scene

    def Update(self):  # Game logic goes in here.
        global final_hangman_status, final_hint_status  # Globalise these two variables for use in score scene

        if self.win == 1:  # If user has won
            self.display_message = font.render('You win! Press enter to continue.', True, BLACK)  # Render 'You win! Press enter to continue' text black with font 'font'
            self.SECRET_WORD = mono_font.render(''.join(self.secret_list), True, BLACK)  # Render combined string of secret list text black with font 'mono font'
        elif self.lose == 1:  # If user has lost
            self.hangman_status = pygame.image.load('hangman_pics/9.png')  # Set current hangman status image to 9
            self.display_message = font.render('Game over! Press enter to continue', True, BLACK)  # Render 'Game over! Press enter to continue' text black with font 'font'
            self.SECRET_WORD = mono_font.render(''.join(self.secret_list), True, BLACK)  # Render combined string of secret list text black with font 'mono font'

        if self.secret_list == secret:  # If user guessed the word
            self.win = 1
        elif self.hangman_pic != 9:  # If the current hangman pic number is not 9
            if self.counter == 0:  # If counter is 0
                [self.secret_list.append('_') for i in range(len(secret))]  # List compression for appending '_' to secret list for each letter in secret
                self.counter = 1

            self.hangman_status = pygame.image.load('hangman_pics/' + str(self.hangman_pic) + '.png')  # Image of current hangman status 
            self.SECRET_WORD = mono_font.render(''.join(self.secret_list), True, BLACK)  # Render combined string of secret list text black with font 'mono font'

            if self.selected_letter in self.used_letters:  # If selected letter is already used
                self.display_message = font.render('You\'ve already chosen that letter!', True, BLACK)  # Render 'You've already chosen that letter!' text black with font 'font'
            elif self.selected_letter == '':  # If selected letter is blank
                pass
            elif not self.selected_letter.isalpha():  # If selected letter is not a letter
                self.display_message = font.render('That\'s not a letter!', True, BLACK)  # Render 'That's not a letter!' text black with font 'font'
            else:  # If selected letter isn't already used and is a letter
                self.used_letters.append(self.selected_letter)  # Append selected letter to used letters list
                if self.selected_letter in secret:  # If selected letter is in secret
                    self.display_message = font.render('You got a letter!', True, BLACK)  # Render 'You got a letter!' text black with font 'font'
                    user_guess = [i for i, x in enumerate(secret) if x == self.selected_letter]  # List compression for finding list location for selected letter in secret word

                    for i in range(len(user_guess)):  # For each i in user guess list
                        self.secret_list[user_guess[i]] = self.selected_letter  # Replace '_' in secret list with selected letter
                else:  # If selected letter isn't in secret
                    self.display_message = font.render('Try again', True, BLACK)  # Render 'Try again' text black with font 'font'
                    self.hangman_pic += 1
            self.selected_letter = ''
        else:  # If user hasn't guessed the word and the current pic number is 9
            self.lose = 1

        final_hangman_status = self.hangman_pic
        final_hint_status = self.asked_hint

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        if category_number == 1:  # If selected category is 1 (i.e. objects)
            screen.blit(self.objects_background, (0, 0))  # Display objects background
        elif category_number == 2:  # If selected category is 2 (i.e. animals)
            screen.blit(self.animals_background, (0, 0))  # Display animals background
        elif category_number == 3:  # If selected category is 3 (i.e. IST)
            screen.blit(self.ist_background, (0, 0))  # Display IST background
        elif category_number == 4:  # If selected category is 4 (i.e. food)
            screen.blit(self.food_background, (0, 0))  # Display food background
        elif category_number == 5:  # If selected category is 5 (i.e. science)
            screen.blit(self.science_background, (0, 0))  # Display science background
        pygame.draw.line(screen, BLACK, (448, 0), (448, 480), 5)  # Draw a stright black line from (448,0) to (448,480) with a thickness of 5
        pygame.draw.line(screen, BLACK, (0, 400), (448, 400), 5)  # Draw a stright black line from (0,400) to (448,400) with a thickness of 5
        screen.blit(self.game_title, (224 - self.game_title.get_width() // 2, 40 - self.game_title.get_height() // 2))  # Display 'Hangman' title

        if self.hint_hover == 0:  # If user hasn't asked for a hint
            pygame.draw.rect(screen, BRIGHT_BLUE, self.hint_button)  # 
        else:
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.hint_button)

        if self.asked_hint == 1:  # If user has asked for a hint
            blit_text(screen, get_hint[''.join(secret)], (10, 410), hint_font, 438, 480)  # Display hint for secret word text
            pygame.draw.rect(screen, BRIGHT_BLUE_GRAYED, self.hint_button)

        screen.blit(self.used_letters_title, (544 - self.used_letters_title.get_width() // 2, 40 - self.used_letters_title.get_height() // 2)) # Display 'Used Letters' text
        screen.blit(self.hangman_status, (99, 70))  # Display image of current hangman status
        screen.blit(self.display_message, (224 - self.display_message.get_width() // 2, 330 - self.display_message.get_height() // 2))  # Display '' text
        screen.blit(self.SECRET_WORD, (224 - self.SECRET_WORD.get_width() // 2, 360 - self.SECRET_WORD.get_height() // 2))  # Display '_' obfuscated secret word text
        blit_text(screen, ' '.join(self.used_letters), (478, 70), font, window_width, window_height)  # Display used letters text
        screen.blit(self.hint_text, (544 - self.hint_text.get_width() // 2, 442 - self.hint_text.get_height() // 2))  # Display hint text


class ScoreScene(SceneBase):  # Score screen
    def __init__(self):
        SceneBase.__init__(self)
        self.score = 0  # Current score
        self.continue_hover = 0  # Hovering status for continue button

        self.score_background = pygame.image.load('screens/score_screen.png')  # Image of background
        self.score_background_lost = pygame.image.load('screens/score_screen_lost.png')  # Image of background if user lost

        self.continue_button = pygame.Rect(40, 410, 560, 50)  # Location and size for continue button

        self.score_title = font.render('Your final score', True, BLACK)  # Render 'Your final score' text black with font 'font'
        self.continue_text = font.render('Continue', True, WHITE)  # Render 'Continue' text white with font 'font'
        self.answer = font.render('The word was:', True, BLACK)  # Render 'The word was:' text black with font 'font'

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # If user pressed 'RETURN' or 'ENTER' key
                self.SwitchToScene(PlayAgainScene())  # Switch to play again scene

            if self.continue_button.collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over continue button
                self.continue_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked continue button
                    self.SwitchToScene(PlayAgainScene())  # Switch to play again scene
            else:  # If mouse isn't hovering over continue button
                self.continue_hover = 0

    def Update(self):  # Game logic goes in here.
        self.score = font.render(str((int(math.ceil(((15 - len(secret))*(10 - final_hangman_status)) if final_hangman_status != 9 else 0)/((0.5 if final_hangman_status == 0 else 1) if final_hint_status == 0 else 2)))), True, BLACK)  # Render score text black with font 'font' || Score calculation: (15 - length of word)*(10 - final hangman status) IF YOU WIN, OTHERWISE 0  / (0.5 IF NO WRONG GUESSES, OTHERWISE 2)
        self.secret_word = font.render(''.join(secret), True, BLACK)  # Render secret word text black with font 'font'

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        if final_hangman_status == 9:  # If user lost
            screen.blit(self.score_background_lost, (0, 0))  # Display lost background
        else:
            screen.blit(self.score_background, (0, 0))  # Display background
        screen.blit(self.score_title, (320 - self.score_title.get_width() // 2, 40 - self.score_title.get_height() // 2))  # Display 'Your final score' title

        if final_hangman_status == 9:  # If user lost
            screen.blit(self.answer, (320 - self.answer.get_width() // 2, 200 - self.answer.get_height() // 2))  # Display 'The word was:' text
            screen.blit(self.secret_word, (320 - self.secret_word.get_width() // 2, 230 - self.secret_word.get_height() // 2))  # Display secret word text

        if self.continue_hover == 0:  # If user isn't hovering over continue button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.continue_button)  # Display normal continue button
        else:  # If user is hovering over continue button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.continue_button)  # Display highlighted continue button

        screen.blit(self.score, (320 - self.score.get_width() // 2, 108 - self.score.get_height() // 2))  # Display score text
        screen.blit(self.continue_text, (320 - self.continue_text.get_width() // 2, 438 - self.continue_text.get_height() // 2))  # Display 'Continue' text


class PlayAgainScene(SceneBase):  # Play again screen
    def __init__(self):
        SceneBase.__init__(self)
        self.no_hover = 0  # Hovering status for no button
        self.yes_hover = 0  # Hovering status for yes button

        self.play_again_background = pygame.image.load('screens/playagain_screen.png')  # Image of background
        self.smile = pygame.image.load('smile.png')  # Image of smiley face

        self.yes_button = pygame.Rect(40, 300, 560, 50)  # Location and size for yes button
        self.no_button = pygame.Rect(40, 370, 560, 50)   # Location and size for no button

        self.play_again_title = font.render('Play Again?', True, BLACK)  # Render 'Play Again?' text black with font 'font'
        self.yes_text = font.render('Yes', True, WHITE)  # Render 'Yes' text white with font 'font'
        self.no_text = font.render('No', True, WHITE)  # Render 'No' text white with font 'font'

    def ProcessInput(self, events, pressed_keys):  # Receives all the events that happened since the last frame.
        for event in events:
            if pygame.Rect(40, 370, 560, 50).collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over no button
                self.no_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked no button
                    self.SwitchToScene(TitleScene())  # Switch to title scene
            else:  # If mouse isn't hovering over no button
                self.no_hover = 0

            if pygame.Rect(40, 300, 560, 50).collidepoint(pygame.mouse.get_pos()):  # If mouse is hovering over yes button
                self.yes_hover = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If user left clicked yes button
                    self.SwitchToScene(CategoryScene())  # Switch to category scene
            else:  # If mouse isn't hovering over yes button
                self.yes_hover = 0

    def Update(self):  # Game logic goes in here.
        pass

    def Render(self, screen):  # Render code goes here. It will receive the main screen Surface as input.
        screen.blit(self.play_again_background, (0, 0))  # Display background
        screen.blit(self.play_again_title, (320 - self.play_again_title.get_width() // 2, 40 - self.play_again_title.get_height() // 2))  # Display 'Play Again?' text

        screen.blit(self.smile, (320 - self.smile.get_width() // 2, 175 - self.smile.get_height() // 2))  # Display smiley image

        if self.yes_hover == 0:  # If user isn't hovering over yes button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.yes_button)  # Display normal yes button
        else:  # If user is hovering over yes button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.yes_button)  # Display highlighted yes button

        if self.no_hover == 0:  # If user isn't hovering over no button
            pygame.draw.rect(screen, BRIGHT_BLUE, self.no_button)  # Display normal no button
        else:  # If user is hovering over no button
            pygame.draw.rect(screen, BRIGHT_BLUE_HIGHLIGHTED, self.no_button)  # Display highlighted no button

        screen.blit(self.no_text, (320 - self.no_text.get_width() // 2, 398 - self.no_text.get_height() // 2))  # Display 'No' text
        screen.blit(self.yes_text, (320 - self.yes_text.get_width() // 2, 328 - self.yes_text.get_height() // 2))  # Display 'Yes' text

run_game(window_width, window_height, FPS, TitleScene())  # Function call to start game
pygame.quit()  # Quit Pygame
sys.exit()  # Quit application
