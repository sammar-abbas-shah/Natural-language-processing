import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
from collections import defaultdict

class EmotionDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Detector")
        self.root.geometry("850x800")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(True, True)

        # Extended emotion lexicon with weighted scores
        self.emotion_lexicon = {
            'happy': {
                'happy': 2, 'joy': 2, 'joyful': 2, 'glad': 1.5, 'delighted': 2,
                'cheerful': 1.5, 'elated': 2, 'ecstatic': 2.5, 'wonderful': 2,
                'amazing': 2, 'awesome': 2, 'fantastic': 2, 'great': 1.5,
                'excellent': 1.5, 'perfect': 1.5, 'lovely': 1.5, 'beautiful': 1.5,
                'brilliant': 1.5, 'fabulous': 2, 'incredible': 2, 'marvelous': 2,
                'pleased': 1.5, 'satisfied': 1.5, 'content': 1, 'blessed': 2, 'lucky': 1.5,
                'grateful': 1.5, 'thankful': 1.5, 'proud': 1.5, 'confident': 1,
                'optimistic': 1, 'hopeful': 1, 'laugh': 1.5, 'laughter': 1.5,
                'smile': 1.5, 'smiling': 1.5, 'fun': 1.5, 'funny': 1, 'hilarious': 2,
                'good': 1, 'nice': 1, 'pleasant': 1, 'superb': 2, 'terrific': 2,
                'outstanding': 2, 'magnificent': 2, 'bliss': 2, 'blissful': 2,
                'euphoric': 2.5, 'overjoyed': 2.5, 'celebrate': 1.5, 'celebration': 1.5,
                'win': 1.5, 'winning': 1.5, 'success': 1.5, 'victory': 2,
                'achieve': 1, 'accomplished': 1.5, 'cheer': 1.5, 'upbeat': 1.5,
                'jolly': 1.5, 'merry': 1.5, 'radiant': 1.5, 'sunny': 1,
                'thrilled': 2, 'exhilarated': 2, 'jubilant': 2, 'gleeful': 1.5,
                'chipper': 1, 'peppy': 1, 'bubbly': 1.5, 'perky': 1,
                'fortunate': 1.5, 'privileged': 1, 'rewarded': 1.5, 'fulfilled': 1.5
            },
            'sad': {
                'sad': 2, 'sadness': 2, 'unhappy': 2, 'miserable': 2.5, 'depressed': 2.5,
                'depression': 2.5, 'melancholy': 2, 'gloomy': 1.5, 'dismal': 1.5,
                'sorrow': 2, 'sorrowful': 2, 'grief': 2.5, 'grieving': 2.5, 'mourn': 2,
                'mourning': 2, 'cry': 2, 'crying': 2, 'tears': 1.5, 'tearful': 1.5,
                'lonely': 2, 'alone': 1.5, 'isolated': 1.5, 'abandoned': 2, 'rejected': 1.5,
                'hurt': 1.5, 'pain': 1.5, 'painful': 1.5, 'ache': 1.5, 'aching': 1.5,
                'heartbroken': 2.5, 'broken': 1.5, 'devastated': 2.5, 'crushed': 2,
                'disappointed': 1.5, 'let down': 1.5, 'regret': 1.5, 'regretful': 1.5,
                'sorry': 1, 'miss': 1.5, 'missing': 1.5, 'nostalgic': 1,
                'empty': 1.5, 'hollow': 1.5, 'numb': 1.5, 'despair': 2.5, 'hopeless': 2,
                'helpless': 1.5, 'worthless': 2, 'failure': 1.5, 'fail': 1.5,
                'lost': 1.5, 'defeated': 1.5, 'brokenhearted': 2.5, 'weep': 2, 'weeping': 2,
                'somber': 1.5, 'grim': 1.5, 'bleak': 1.5, 'dark': 1, 'darkness': 1,
                'down': 1.5, 'downcast': 1.5, 'dejected': 1.5, 'despondent': 2,
                'forlorn': 2, 'woeful': 2, 'wretched': 2, 'doleful': 1.5,
                'lugubrious': 1.5, 'morose': 1.5, 'glum': 1.5, 'sullen': 1.5,
                'blue': 1, 'low': 1, 'downhearted': 1.5, 'discouraged': 1.5,
                'disheartened': 1.5, 'crestfallen': 1.5, 'heavyhearted': 1.5,
                'tear': 1.5, 'sob': 2, 'sobbing': 2, 'whimper': 1.5, 'whimpering': 1.5
            },
            'angry': {
                'angry': 2, 'anger': 2, 'mad': 2, 'furious': 2.5, 'rage': 2.5,
                'enraged': 2.5, 'irritated': 1.5, 'irritating': 1.5, 'annoyed': 1.5,
                'annoying': 1.5, 'frustrated': 1.5, 'frustrating': 1.5, 'agitated': 1.5,
                'aggravated': 1.5, 'outraged': 2.5, 'livid': 2.5, 'fuming': 2,
                'seething': 2, 'hostile': 2, 'aggressive': 1.5, 'hate': 2.5, 'hated': 2,
                'hatred': 2.5, 'disgust': 2, 'disgusted': 2, 'disgusting': 2,
                'revolting': 2, 'repulsive': 2, 'contempt': 2, 'despise': 2.5,
                'loathe': 2.5, 'abhor': 2.5, 'detest': 2.5, 'resent': 2, 'resentful': 2,
                'bitter': 1.5, 'spiteful': 2, 'vengeful': 2, 'revenge': 2,
                'jealous': 1.5, 'envy': 1.5, 'envious': 1.5, 'irritable': 1.5,
                'temper': 1.5, 'tantrum': 2, 'explode': 1.5, 'exploding': 1.5,
                'storm': 1, 'storming': 1.5, 'fierce': 1, 'violent': 2,
                'attack': 1.5, 'attacking': 1.5, 'fight': 1.5, 'fighting': 1.5,
                'argue': 1.5, 'argument': 1.5, 'conflict': 1.5, 'war': 2,
                'destroy': 2, 'destroying': 2, 'damage': 1.5, 'damaging': 1.5,
                'ruin': 1.5, 'ruined': 1.5, 'terrible': 1.5, 'horrible': 1.5,
                'awful': 1.5, 'atrocious': 2, 'appalling': 2, 'dreadful': 2,
                'irate': 2, 'incensed': 2, 'infuriated': 2.5, 'wrath': 2.5,
                'wrathful': 2.5, 'indignant': 2, 'exasperated': 1.5, 'fed up': 2,
                'pissed': 2, 'pissed off': 2.5, 'ballistic': 2, 'berserk': 2.5,
                'raging': 2, 'stormy': 1.5, 'thunderous': 1.5, 'menacing': 2,
                'hostility': 2, 'antagonistic': 1.5, 'belligerent': 2, 'combative': 1.5
            },
            'fearful': {
                'afraid': 2, 'fear': 2, 'scared': 2, 'terrified': 2.5, 'frightened': 2,
                'frightening': 2, 'horror': 2.5, 'horrified': 2.5,
                'panic': 2.5, 'panicked': 2.5, 'panicking': 2.5, 'anxious': 1.5,
                'anxiety': 1.5, 'worried': 1.5, 'worry': 1.5, 'worrisome': 1.5,
                'nervous': 1.5, 'tense': 1.5, 'stressed': 1.5, 'stress': 1.5,
                'overwhelmed': 1.5, 'threatened': 2, 'threatening': 2, 'danger': 2,
                'dangerous': 2, 'risk': 1.5, 'risky': 1.5, 'unsafe': 1.5, 'insecure': 1.5,
                'vulnerable': 1.5, 'exposed': 1.5, 'paranoid': 2, 'suspicious': 1.5,
                'doubt': 1, 'doubtful': 1, 'uncertain': 1, 'unsure': 1,
                'hesitant': 1, 'reluctant': 1, 'cautious': 1, 'careful': 0.5,
                'alarm': 1.5, 'alarmed': 1.5, 'shock': 1.5, 'shocked': 1.5,
                'trauma': 2, 'traumatic': 2, 'nightmare': 2, 'dread': 2,
                'petrified': 2.5, 'petrifying': 2.5, 'spooked': 1.5, 'haunted': 1.5,
                'timid': 1, 'shy': 0.5, 'coward': 1.5, 'cowardly': 1.5,
                'weak': 1, 'powerless': 1.5, 'helpless': 1.5,
                'apprehensive': 1.5, 'uneasy': 1.5, 'restless': 1, 'jittery': 1.5,
                'trembling': 1.5, 'shaking': 1.5, 'quivering': 1.5, 'quaking': 1.5,
                'cowering': 1.5, 'cringing': 1.5, 'wincing': 1, 'flinching': 1,
                'alarmed': 1.5, 'startled': 1.5, 'jumpy': 1.5, 'skittish': 1.5,
                'fretful': 1.5, 'troubled': 1, 'distressed': 1.5, 'tormented': 2
            },
            'surprised': {
                'surprised': 2, 'surprise': 2, 'shocked': 2, 'shocking': 2,
                'amazed': 2, 'amazing': 1.5, 'astonished': 2.5, 'astonishing': 2,
                'stunned': 2, 'stunning': 1.5, 'staggered': 2, 'startled': 2,
                'bewildered': 1.5, 'bewildering': 1.5, 'confused': 1, 'confusing': 1,
                'perplexed': 1.5, 'puzzled': 1, 'disoriented': 1,
                'unexpected': 1.5, 'unbelievable': 2, 'incredible': 1.5,
                'wow': 2, 'whoa': 1.5, 'omg': 1.5, 'unreal': 1.5,
                'sudden': 1, 'suddenly': 1, 'abrupt': 1,
                'speechless': 2, 'dumbfounded': 2.5, 'flabbergasted': 2.5,
                'awestruck': 2, 'awe': 1.5, 'wonder': 1, 'wonderstruck': 2,
                'miracle': 1.5, 'miraculous': 1.5, 'phenomenal': 1.5,
                'jolted': 1.5, 'jarred': 1.5, 'taken aback': 2, 'caught off guard': 2,
                'thunderstruck': 2.5, 'dazed': 1.5, 'dazzled': 1.5, 'mesmerized': 1.5,
                'spellbound': 1.5, 'breathless': 1.5, 'gobsmacked': 2, 'aghast': 2
            },
            'love': {
                'love': 2.5, 'loving': 2, 'adore': 2.5, 'adoring': 2.5, 'cherish': 2,
                'cherished': 2, 'affection': 2, 'affectionate': 2, 'fond': 1.5,
                'fondness': 1.5, 'devoted': 2, 'devotion': 2, 'passion': 2,
                'passionate': 2, 'romantic': 1.5, 'romance': 1.5, 'intimate': 1.5,
                'tender': 1.5, 'tenderness': 1.5, 'caring': 1.5, 'care': 1,
                'compassion': 1.5, 'compassionate': 1.5, 'empathy': 1.5, 'empathetic': 1.5,
                'warm': 1, 'warmth': 1, 'gentle': 1, 'kind': 1, 'kindness': 1,
                'sweet': 1, 'cute': 1, 'darling': 1.5, 'dear': 1, 'beloved': 2,
                'precious': 1.5, 'treasure': 1.5, 'treasured': 1.5, 'heart': 1,
                'soulmate': 2, 'partner': 0.5, 'together': 0.5, 'united': 1,
                'bond': 1, 'bonded': 1, 'connected': 1, 'attachment': 1.5,
                'infatuated': 1.5, 'infatuation': 1.5, 'enamored': 2, 'captivated': 1.5,
                'enchanted': 1.5, 'charmed': 1.5, 'besotted': 2, 'smitten': 2,
                'head over heels': 2, 'crazy about': 2, 'wild about': 2,
                'yearning': 1.5, 'longing': 1.5, 'desire': 1.5, 'desiring': 1.5,
                'attracted': 1, 'attraction': 1, 'crush': 1.5, 'flirt': 1,
                'hug': 1, 'hugging': 1, 'kiss': 1.5, 'kissing': 1.5, 'cuddle': 1.5,
                'snuggle': 1.5, 'embrace': 1.5, 'hold': 0.5, 'holding': 0.5,
                'marriage': 1, 'married': 1, 'wedding': 1.5, 'anniversary': 1,
                'forever': 1, 'eternal': 1.5, 'endless': 1, 'unconditional': 2
            },
            'excitement': {
                'excited': 2, 'exciting': 2, 'thrill': 2, 'thrilling': 2, 'thrilled': 2,
                'exhilarated': 2, 'exhilarating': 2, 'energized': 1.5, 'energetic': 1.5,
                'enthusiastic': 2, 'enthusiasm': 2, 'eager': 1.5, 'eagerly': 1.5,
                'keen': 1.5, 'animated': 1.5, 'lively': 1.5, 'spirited': 1.5,
                'vibrant': 1.5, 'dynamic': 1, 'electrified': 2, 'electrifying': 2,
                'pumped': 1.5, 'amped': 1.5, 'fired up': 2, 'hyped': 1.5,
                'stoked': 1.5, 'psyched': 1.5, 'jazzed': 1.5, 'buzzing': 1.5,
                'restless': 1, 'antsy': 1, 'itching': 1, 'yearning': 1.5,
                'longing': 1.5, 'craving': 1.5, 'dying to': 1.5, 'cant wait': 2,
                'looking forward': 2, 'anticipating': 1.5, 'expectant': 1.5,
                'buoyant': 1.5, 'effervescent': 1.5, 'ebullient': 1.5, 'exuberant': 1.5,
                'vivacious': 1.5, 'zealous': 1.5, 'ardent': 1.5, 'fervent': 1.5,
                'feverish': 1.5, 'frantic': 1, 'frenzied': 1.5, 'wild': 1,
                'adventure': 1.5, 'adventurous': 1.5, 'quest': 1, 'journey': 0.5,
                'explore': 1, 'exploring': 1, 'discover': 1, 'discovering': 1,
                'novelty': 1, 'new': 0.5, 'fresh': 0.5, 'unusual': 0.5
            },
            'boredom': {
                'bored': 2, 'boring': 2, 'boredom': 2, 'dull': 2, 'dullness': 2,
                'tedious': 2, 'tedium': 2, 'monotonous': 2, 'monotony': 2,
                'repetitive': 1.5, 'repetition': 1.5, 'routine': 1, 'routinely': 1,
                'mundane': 1.5, 'ordinary': 1, 'plain': 1, 'uninteresting': 2,
                'unexciting': 1.5, 'uninspiring': 1.5, 'unstimulating': 1.5,
                'lifeless': 1.5, 'spiritless': 1.5, 'listless': 1.5, 'lethargic': 1.5,
                'sluggish': 1.5, 'lazy': 1, 'idle': 1, 'inactive': 1,
                'indifferent': 1.5, 'apathetic': 1.5, 'unconcerned': 1,
                'disinterested': 1.5, 'uninvolved': 1, 'detached': 1,
                'weary': 1.5, 'weariness': 1.5, 'tired': 1, 'exhausted': 1,
                'drained': 1, 'spent': 1, 'burned out': 1.5, 'fatigued': 1,
                'yawn': 1.5, 'yawning': 1.5, 'drowsy': 1, 'sleepy': 1,
                'blah': 1.5, 'meh': 1.5, 'whatever': 1, 'same old': 1.5,
                'nothing new': 1.5, 'stuck': 1, 'trapped': 1, 'stagnant': 1.5,
                'stale': 1.5, 'flat': 1, 'blank': 1, 'empty': 1, 'void': 1.5
            },
            'confusion': {
                'confused': 2, 'confusing': 2, 'confusion': 2, 'puzzled': 1.5,
                'puzzling': 1.5, 'perplexed': 1.5, 'perplexing': 1.5, 'baffled': 2,
                'baffling': 2, 'bewildered': 1.5, 'bewildering': 1.5, 'mystified': 1.5,
                'mystifying': 1.5, 'disoriented': 1.5, 'lost': 1.5, 'adrift': 1.5,
                'unclear': 1.5, 'ambiguous': 1.5, 'vague': 1, 'uncertain': 1.5,
                'unsure': 1.5, 'doubtful': 1.5, 'questioning': 1, 'wondering': 1,
                'curious': 0.5, 'inquisitive': 0.5, 'searching': 0.5, 'seeking': 0.5,
                'muddled': 1.5, 'jumbled': 1.5, 'chaotic': 1.5, 'chaos': 1.5,
                'disarray': 1.5, 'tangled': 1, 'knotty': 1, 'complicated': 1.5,
                'complex': 1, 'intricate': 1, 'convoluted': 1.5, 'elaborate': 0.5,
                'cryptic': 1.5, 'enigmatic': 1.5, 'incomprehensible': 2,
                'unintelligible': 1.5, 'garbled': 1.5, 'nonsensical': 1.5,
                'absurd': 1, 'ridiculous': 1, 'preposterous': 1, 'ludicrous': 1,
                'what': 1, 'huh': 1, 'umm': 0.5, 'uhh': 0.5, 'dunno': 1,
                'no idea': 1.5, 'clueless': 1.5, 'at a loss': 1.5, 'stumped': 1.5
            },
            'curiosity': {
                'curious': 2, 'curiosity': 2, 'inquisitive': 1.5, 'inquisitiveness': 1.5,
                'interested': 1.5, 'interesting': 1.5, 'fascinated': 2, 'fascinating': 2,
                'fascination': 2, 'intrigued': 1.5, 'intriguing': 1.5, 'engrossed': 1.5,
                'absorbed': 1, 'captivated': 1.5, 'mesmerized': 1.5, 'spellbound': 1.5,
                'enthralled': 1.5, 'riveted': 1.5, 'hooked': 1.5, 'drawn': 1,
                'attracted': 1, 'tempted': 1, 'tantalized': 1.5, 'allured': 1.5,
                'enticed': 1.5, 'seduced': 1, 'lured': 1, 'beguiled': 1.5,
                'wonder': 1.5, 'wondering': 1.5, 'marvel': 1.5, 'marveling': 1.5,
                'question': 1, 'questioning': 1, 'query': 1, 'inquiry': 1,
                'probe': 1, 'probing': 1, 'explore': 1.5, 'exploring': 1.5,
                'investigate': 1.5, 'investigating': 1.5, 'research': 1,
                'study': 1, 'learn': 1, 'learning': 1, 'discover': 1.5,
                'discovery': 1.5, 'uncover': 1.5, 'reveal': 1, 'revealing': 1,
                'mystery': 1.5, 'mysterious': 1.5, 'secret': 1, 'secrets': 1,
                'unknown': 1, 'unexplored': 1.5, 'uncharted': 1.5, 'novel': 1,
                'new': 0.5, 'fresh': 0.5, 'different': 0.5, 'unique': 0.5,
                'peculiar': 1, 'odd': 0.5, 'strange': 0.5, 'weird': 0.5,
                'bizarre': 1, 'uncanny': 1, 'eerie': 0.5
            },
            'relief': {
                'relief': 2, 'relieved': 2, 'reassured': 1.5, 'reassuring': 1.5,
                'comforted': 1.5, 'comforting': 1.5, 'soothed': 1.5, 'soothing': 1.5,
                'calmed': 1.5, 'calming': 1.5, 'eased': 1.5, 'easing': 1.5,
                'alleviated': 1.5, 'alleviation': 1.5, 'mitigated': 1,
                'lessened': 1, 'reduced': 0.5, 'decreased': 0.5, 'subsided': 1,
                'faded': 0.5, 'dissipated': 1, 'evaporated': 0.5, 'lifted': 1,
                'released': 1, 'liberated': 1.5, 'freed': 1.5, 'free': 1,
                'unburdened': 1.5, 'lightened': 1.5, 'weightless': 1,
                'breathing easy': 1.5, 'sigh of relief': 2, 'whew': 1.5,
                'thank goodness': 1.5, 'thank god': 1.5, 'phew': 1.5,
                'safe': 1, 'safer': 1, 'secure': 1, 'protected': 1,
                'out of danger': 1.5, 'out of the woods': 1.5, 'in the clear': 1.5,
                'home free': 1.5, 'scot free': 1.5, 'spared': 1.5,
                'rescued': 1.5, 'saved': 1.5, 'recovered': 1, 'healed': 1,
                'mended': 1, 'fixed': 0.5, 'resolved': 1, 'settled': 1,
                'at peace': 1.5, 'tranquil': 1, 'serene': 1, 'peaceful': 1,
                'rested': 1, 'refreshed': 1, 'renewed': 1, 'rejuvenated': 1
            },
            'guilt': {
                'guilt': 2, 'guilty': 2, 'ashamed': 2, 'shame': 2, 'shameful': 2,
                'remorse': 2, 'remorseful': 2, 'regret': 1.5, 'regretful': 1.5,
                'repentant': 2, 'contrite': 2, 'apologetic': 1.5, 'sorry': 1.5,
                'self-blame': 2, 'blame myself': 2, 'my fault': 2, 'i fault': 2,
                'responsible': 0.5, 'accountable': 0.5, 'liable': 0.5,
                'wrong': 1, 'bad': 1, 'sin': 1.5, 'sinful': 1.5, 'sinner': 1.5,
                'wicked': 1.5, 'evil': 1.5, 'immoral': 1.5, 'unethical': 1,
                'dishonorable': 1.5, 'disgraceful': 1.5, 'ignoble': 1.5,
                'humiliated': 1.5, 'mortified': 1.5, 'embarrassed': 1,
                'embarrassing': 1, 'cringe': 1.5, 'cringeworthy': 1.5,
                'unworthy': 1.5, 'undeserving': 1.5, 'inadequate': 1,
                'unforgivable': 2, 'unpardonable': 2, 'inexcusable': 1.5,
                'should have': 1, 'could have': 1, 'would have': 1,
                'if only': 1.5, 'what if': 1, 'second thoughts': 1,
                'doubting': 1, 'second guessing': 1.5, 'racked': 1.5,
                'tormented': 1.5, 'haunted': 1.5, 'plagued': 1.5,
                'conscience': 1, 'guilty conscience': 2, 'weighed down': 1.5,
                'burdened': 1.5, 'heavy heart': 1.5
            },
            'shame': {
                'shame': 2, 'ashamed': 2, 'shameful': 2, 'humiliated': 2,
                'humiliation': 2, 'mortified': 2, 'mortifying': 2, 'embarrassed': 2,
                'embarrassing': 2, 'embarrassment': 2, 'abashed': 1.5,
                'disgraced': 2, 'disgrace': 2, 'disgraceful': 1.5,
                'dishonored': 2, 'degraded': 2, 'demeaned': 1.5, 'belittled': 1.5,
                'insulted': 1, 'offended': 1, 'affronted': 1, 'slighted': 1,
                'snubbed': 1, 'rejected': 1.5, 'spurned': 1.5, 'scorned': 1.5,
                'derided': 1.5, 'mocked': 1.5, 'ridiculed': 1.5, 'laughed at': 1.5,
                'pointed at': 1, 'stared at': 0.5, 'whispered about': 1,
                'gossip': 1, 'gossiped': 1, 'rumor': 1, 'scandal': 1.5,
                'exposed': 1.5, 'uncovered': 1, 'revealed': 0.5, 'found out': 1.5,
                'caught': 1, 'caught red-handed': 1.5, 'busted': 1,
                'naked': 0.5, 'vulnerable': 1, 'defenseless': 1,
                'small': 0.5, 'insignificant': 1, 'worthless': 1.5,
                'inadequate': 1, 'inferior': 1, 'less than': 1, 'not enough': 1,
                'flawed': 1, 'imperfect': 0.5, 'defective': 1, 'broken': 1,
                'tainted': 1.5, 'stained': 1, 'soiled': 1, 'dirty': 0.5,
                'unclean': 0.5, 'impure': 1, 'contaminated': 1
            },
            'jealousy': {
                'jealous': 2, 'jealousy': 2, 'envy': 2, 'envious': 2, 'covet': 2,
                'covetous': 2, 'coveting': 2, 'resent': 1.5, 'resentful': 1.5,
                'resentment': 1.5, 'bitter': 1.5, 'bitterness': 1.5,
                'green with envy': 2, 'green-eyed': 2, 'jaundiced': 1.5,
                'possessive': 1.5, 'clingy': 1, 'controlling': 1,
                'insecure': 1.5, 'threatened': 1.5, 'competitive': 0.5,
                'rival': 1, 'rivalry': 1, 'competitor': 0.5, 'opponent': 0.5,
                'comparison': 1, 'comparing': 1, 'measure up': 1,
                'not good enough': 1.5, 'second best': 1.5, 'inferior': 1,
                'less than': 1, 'inadequate': 1, 'lacking': 1, 'missing out': 1.5,
                'fomo': 1.5, 'left out': 1.5, 'excluded': 1, 'outsider': 1,
                'unwanted': 1, 'unloved': 1, 'neglected': 1, 'ignored': 1,
                'overlooked': 1, 'passed over': 1, 'replaced': 1.5,
                'usurped': 1.5, 'displaced': 1, 'dethroned': 1.5,
                'betrayed': 1.5, 'cheated': 1.5, 'deceived': 1, 'two-timed': 1.5,
                'stolen': 1, 'taken': 0.5, 'robbed': 1, 'deprived': 1
            },
            'pride': {
                'proud': 2, 'pride': 2, 'accomplished': 1.5, 'achievement': 1.5,
                'achieved': 1.5, 'success': 1.5, 'successful': 1.5, 'triumph': 2,
                'triumphant': 2, 'victory': 2, 'victorious': 2, 'win': 1.5,
                'winning': 1.5, 'champion': 1.5, 'championship': 1.5,
                'best': 1, 'top': 1, 'first': 1, 'number one': 1.5,
                'superior': 1.5, 'excellent': 1, 'outstanding': 1.5,
                'remarkable': 1, 'extraordinary': 1.5, 'exceptional': 1.5,
                'distinguished': 1.5, 'eminent': 1, 'renowned': 1.5,
                'famous': 0.5, 'celebrated': 1, 'honored': 1.5, 'prestigious': 1,
                'dignity': 1.5, 'self-respect': 1.5, 'self-esteem': 1.5,
                'confident': 1, 'confidence': 1, 'assured': 1, 'self-assured': 1.5,
                'poised': 1, 'composed': 0.5, 'graceful': 0.5, 'elegant': 0.5,
                'noble': 1, 'honorable': 1, 'worthy': 1, 'deserving': 1,
                'merit': 1, 'meritorious': 1.5, 'commendable': 1.5,
                'laudable': 1.5, 'praiseworthy': 1.5, 'admirable': 1.5,
                'respectable': 1, 'estimable': 1, 'august': 1, 'grand': 0.5,
                'majestic': 1, 'magnificent': 1, 'splendid': 1, 'glorious': 1.5,
                'heroic': 1.5, 'gallant': 1, 'valiant': 1.5, 'courageous': 1,
                'brave': 1, 'bold': 0.5, 'fearless': 1, 'undaunted': 1.5
            },
            'trust': {
                'trust': 2, 'trusting': 2, 'trusted': 2, 'trustworthy': 2,
                'reliable': 1.5, 'rely': 1.5, 'dependable': 1.5, 'depend': 1,
                'faith': 1.5, 'faithful': 1.5, 'faithfulness': 1.5, 'loyal': 1.5,
                'loyalty': 1.5, 'devoted': 1.5, 'devotion': 1.5, 'committed': 1,
                'dedicated': 1, 'steadfast': 1.5, 'steadfastness': 1.5,
                'constant': 1, 'consistent': 1, 'true': 1, 'truthful': 1.5,
                'honest': 1.5, 'honesty': 1.5, 'sincere': 1.5, 'sincerity': 1.5,
                'genuine': 1, 'authentic': 1, 'real': 0.5, 'credible': 1,
                'believable': 1, 'convincing': 0.5, 'assured': 1, 'certain': 0.5,
                'sure': 0.5, 'confident': 0.5, 'secure': 1, 'safe': 1,
                'protected': 1, 'shielded': 1, 'guarded': 1, 'defended': 1,
                'supported': 1, 'supportive': 1, 'backed': 0.5, 'validated': 1,
                'confirmed': 0.5, 'verified': 0.5, 'proven': 1, 'tested': 0.5,
                'tried': 0.5, 'true blue': 1.5, 'rock solid': 1.5,
                'solid as a rock': 1.5, 'unwavering': 1.5, 'unfaltering': 1.5,
                'unshakeable': 1.5, 'resolute': 1, 'determined': 0.5,
                'bond': 1, 'bonded': 1, 'close': 0.5, 'intimate': 0.5,
                'familiar': 0.5, 'known': 0.5, 'understood': 0.5, 'accepted': 0.5
            },
            'anticipation': {
                'anticipate': 2, 'anticipation': 2, 'expect': 1.5, 'expectation': 1.5,
                'expected': 1, 'await': 1.5, 'awaiting': 1.5, 'waiting': 1,
                'wait': 1, 'hope': 1.5, 'hoping': 1.5, 'hopeful': 1.5,
                'look forward': 2, 'looking forward': 2, 'eager': 1.5,
                'eagerly': 1.5, 'excited': 1, 'excitement': 1, 'thrill': 1,
                'thrilled': 1, 'counting down': 1.5, 'almost there': 1,
                'coming soon': 1, 'upcoming': 1, 'approaching': 1,
                'imminent': 1.5, 'impending': 1.5, 'looming': 0.5,
                'nearing': 1, 'close': 0.5, 'near': 0.5, 'around corner': 1.5,
                'on horizon': 1.5, 'in sight': 1, 'within reach': 1,
                'preparing': 1, 'preparation': 1, 'ready': 1, 'readiness': 1,
                'gearing up': 1, 'warming up': 0.5, 'priming': 0.5,
                'foresee': 1, 'foreseeable': 1, 'predict': 0.5, 'predictable': 0.5,
                'forecast': 0.5, 'outlook': 0.5, 'prospect': 1, 'prospects': 1,
                'future': 0.5, 'tomorrow': 0.5, 'next': 0.5, 'soon': 0.5,
                'shortly': 0.5, 'before long': 0.5, 'any moment': 1,
                'any day': 1, 'any time': 0.5, 'eventually': 0.5, 'finally': 0.5,
                'at last': 0.5, 'culmination': 1, 'climax': 1, 'peak': 0.5,
                'pinnacle': 1, 'zenith': 1, 'summit': 0.5, 'apex': 0.5
            },
            'calmness': {
                'calm': 2, 'calmness': 2, 'peaceful': 2, 'peace': 2, 'serene': 2,
                'serenity': 2, 'tranquil': 2, 'tranquility': 2, 'quiet': 1.5,
                'quietness': 1.5, 'still': 1.5, 'stillness': 1.5, 'silent': 1,
                'silence': 1, 'hushed': 1.5, 'muted': 1, 'soft': 0.5,
                'gentle': 1, 'gentleness': 1, 'mild': 1, 'mildness': 1,
                'subdued': 1, 'restrained': 1, 'controlled': 0.5, 'composed': 1.5,
                'collected': 1.5, 'poised': 1.5, 'balanced': 1.5, 'centered': 1.5,
                'grounded': 1.5, 'anchored': 1.5, 'settled': 1.5, 'stable': 1,
                'stability': 1, 'steady': 1, 'steadiness': 1, 'even': 0.5,
                'smooth': 0.5, 'placid': 1.5, 'undisturbed': 1.5, 'untroubled': 1.5,
                'unruffled': 1.5, 'unperturbed': 1.5, 'unflappable': 1.5,
                'imperturbable': 1.5, 'stoic': 1, 'stoical': 1, 'philosophical': 0.5,
                'detached': 0.5, 'disengaged': 0.5, 'removed': 0.5, 'aloof': 0.5,
                'distant': 0.5, 'reserved': 0.5, 'reticent': 0.5, 'withdrawn': 0.5,
                'meditative': 1, 'contemplative': 1, 'reflective': 0.5,
                'mindful': 1, 'aware': 0.5, 'present': 0.5, 'grounded': 1,
                'relaxed': 1.5, 'relaxation': 1.5, 'at ease': 1.5, 'comfortable': 1,
                'cozy': 0.5, 'snug': 0.5, 'content': 1, 'contented': 1,
                'satisfied': 0.5, 'fulfilled': 0.5, 'complete': 0.5, 'whole': 0.5
            },
            'disgust': {
                'disgust': 2, 'disgusted': 2, 'disgusting': 2, 'repulsed': 2,
                'repulsive': 2, 'revulsion': 2, 'revolted': 2, 'revolting': 2,
                'nausea': 2, 'nauseous': 2, 'nauseating': 2, 'sick': 1.5,
                'sickened': 1.5, 'sickening': 1.5, 'ill': 1, 'queasy': 1.5,
                'gross': 2, 'grossed out': 2, 'yuck': 2, 'yucky': 2,
                'eww': 2, 'ew': 2, 'ick': 1.5, 'icky': 1.5, 'ugh': 1.5,
                'vomit': 2, 'vomiting': 2, 'puke': 2, 'puking': 2, 'retch': 2,
                'gag': 1.5, 'gagging': 1.5, 'churn': 1, 'stomach turning': 1.5,
                'filthy': 2, 'filth': 2, 'dirty': 1.5, 'dirt': 1, 'unclean': 1.5,
                'squalid': 2, 'sordid': 1.5, 'squalor': 2, 'foul': 2,
                'foulness': 2, 'putrid': 2, 'rotten': 1.5, 'decayed': 1.5,
                'rancid': 2, 'stale': 1, 'stinking': 2, 'stench': 2, 'odor': 1,
                'smell': 0.5, 'reek': 1.5, 'reeking': 1.5, 'fetid': 2,
                'contaminated': 1.5, 'tainted': 1.5, 'polluted': 1.5,
                'defiled': 2, 'desecrated': 2, 'violated': 1.5, 'profaned': 1.5,
                'abhorrent': 2, 'detestable': 2, 'loathsome': 2, 'odious': 2,
                'abominable': 2, 'heinous': 2, 'atrocious': 1.5, 'vile': 2,
                'wicked': 1.5, 'evil': 1, 'corrupt': 1.5, 'depraved': 1.5,
                'degenerate': 1.5, 'perverted': 1.5, 'sickening': 1.5,
                'distasteful': 1.5, 'unpalatable': 1.5, 'unsavory': 1.5,
                'offensive': 1.5, 'objectionable': 1.5, 'obnoxious': 1.5,
                'repugnant': 2, 'antipathy': 1.5, 'aversion': 1.5, 'distaste': 1.5
            }
        }

        self.negation_words = ['not', 'no', 'never', 'none', 'nobody', 'nothing', 'neither',
                               'nowhere', 'hardly', 'scarcely', 'barely', "don't", "doesn't",
                               "didn't", "wasn't", "weren't", "won't", "wouldn't", "can't",
                               "cannot", "couldn't", "shouldn't", "isn't", "aren't", "aint"]

        self.intensifiers = {
            'very': 1.5, 'extremely': 2, 'incredibly': 2, 'absolutely': 2,
            'completely': 1.5, 'totally': 1.5, 'utterly': 2, 'really': 1.5,
            'so': 1.5, 'too': 1.3, 'quite': 1.3, 'rather': 1.2,
            'pretty': 1.2, 'fairly': 1.1, 'highly': 1.5, 'deeply': 1.5,
            'strongly': 1.5, 'intensely': 2, 'exceptionally': 1.8,
            'remarkably': 1.5, 'extraordinarily': 2, 'unusually': 1.3
        }

        self.diminishers = {
            'slightly': 0.5, 'somewhat': 0.6, 'kinda': 0.6, 'kind': 0.6, 'of': 0.6,
            'barely': 0.4, 'hardly': 0.4, 'scarcely': 0.4, 'partially': 0.6,
            'mildly': 0.5, 'faintly': 0.4, 'vaguely': 0.5, 'relatively': 0.7,
            'reasonably': 0.8
        }

        self.emotion_emojis = {
            'happy': '😊', 'sad': '😢', 'angry': '😠', 'fearful': '😨',
            'surprised': '😲', 'neutral': '😐', 'mixed': '😕', 'love': '❤️',
            'excitement': '🤩', 'boredom': '😴', 'confusion': '😵',
            'curiosity': '🤔', 'relief': '😌', 'guilt': '😓', 'shame': '😳',
            'jealousy': '😒', 'pride': '🦁', 'trust': '🤝', 'anticipation': '👀',
            'calmness': '🧘', 'disgust': '🤢'
        }

        self.emotion_colors = {
            'happy': '#f39c12', 'sad': '#3498db', 'angry': '#e74c3c',
            'fearful': '#34495e', 'surprised': '#9b59b6', 'neutral': '#95a5a6',
            'mixed': '#1abc9c', 'love': '#e91e63', 'excitement': '#ff5722',
            'boredom': '#607d8b', 'confusion': '#795548', 'curiosity': '#00bcd4',
            'relief': '#8bc34a', 'guilt': '#6d4c41', 'shame': '#ff8a80',
            'jealousy': '#827717', 'pride': '#ffd700', 'trust': '#4caf50',
            'anticipation': '#ff9800', 'calmness': '#81d4fa', 'disgust': '#558b2f'
        }

        self.emotion_names = {
            'happy': 'happiness', 'sad': 'sadness', 'angry': 'anger',
            'fearful': 'fear', 'surprised': 'surprise', 'neutral': 'neutrality',
            'mixed': 'mixed feelings', 'love': 'love/affection',
            'excitement': 'excitement', 'boredom': 'boredom',
            'confusion': 'confusion', 'curiosity': 'curiosity',
            'relief': 'relief', 'guilt': 'guilt', 'shame': 'shame',
            'jealousy': 'jealousy', 'pride': 'pride', 'trust': 'trust',
            'anticipation': 'anticipation', 'calmness': 'calmness',
            'disgust': 'disgust'
        }

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#667eea", padx=20, pady=15)
        title_frame.pack(fill=tk.X)

        tk.Label(title_frame, text="Emotion Detector", font=("Helvetica", 24, "bold"),
                bg="#667eea", fg="white").pack()
        tk.Label(title_frame, text="Detects 20 emotions from text using advanced keyword analysis",
                font=("Helvetica", 11), bg="#667eea", fg="#e0e0e0").pack()

        # Main content frame with scrollbar
        main_canvas = tk.Canvas(self.root, bg="#f0f2f5", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = tk.Frame(main_canvas, bg="#f0f2f5")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )

        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=830)
        main_canvas.configure(yscrollcommand=scrollbar.set)

        main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Enable mousewheel scrolling
        def on_mousewheel(event):
            main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        main_canvas.bind_all("<MouseWheel>", on_mousewheel)

        # Input section
        input_frame = tk.LabelFrame(scrollable_frame, text="Your Text", font=("Helvetica", 12, "bold"),
                                   bg="#f0f2f5", fg="#333", padx=10, pady=10)
        input_frame.pack(fill=tk.X, pady=(10, 15), padx=20)

        self.text_input = scrolledtext.ScrolledText(input_frame, height=5, font=("Helvetica", 12),
                                                   wrap=tk.WORD, bd=2, relief=tk.GROOVE)
        self.text_input.pack(fill=tk.X, pady=5)
        self.text_input.insert(tk.END, "I am so happy and excited today! It's wonderful!")

        btn_frame = tk.Frame(input_frame, bg="#f0f2f5")
        btn_frame.pack(fill=tk.X, pady=(5, 0))

        tk.Button(btn_frame, text="Analyze Emotion", font=("Helvetica", 12, "bold"),
                 bg="#667eea", fg="white", padx=20, pady=8, cursor="hand2",
                 command=self.analyze_emotion).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(btn_frame, text="Clear", font=("Helvetica", 11),
                 bg="#e0e0e0", fg="#333", padx=15, pady=8, cursor="hand2",
                 command=self.clear_text).pack(side=tk.LEFT)

        # Results section
        self.results_frame = tk.LabelFrame(scrollable_frame, text="Analysis Results",
                                          font=("Helvetica", 12, "bold"),
                                          bg="#f0f2f5", fg="#333", padx=10, pady=10)
        self.results_frame.pack(fill=tk.X, pady=(0, 15), padx=20)

        # Main emotion display
        self.main_emotion_frame = tk.Frame(self.results_frame, bg="#f8f9fa", bd=2, relief=tk.RIDGE)
        self.main_emotion_frame.pack(fill=tk.X, pady=(0, 15), ipady=10)

        self.emoji_label = tk.Label(self.main_emotion_frame, text="😊", font=("Helvetica", 60),
                                   bg="#f8f9fa")
        self.emoji_label.pack()

        self.emotion_name_label = tk.Label(self.main_emotion_frame, text="Happy",
                                          font=("Helvetica", 20, "bold"), bg="#f8f9fa", fg="#f39c12")
        self.emotion_name_label.pack()

        self.confidence_label = tk.Label(self.main_emotion_frame, text="Confidence: 85%",
                                        font=("Helvetica", 11), bg="#f8f9fa", fg="#666")
        self.confidence_label.pack()

        # Emotion bars - 2 columns for 20 emotions
        self.bars_frame = tk.Frame(self.results_frame, bg="#f0f2f5")
        self.bars_frame.pack(fill=tk.X, pady=(0, 10))

        self.bar_widgets = {}
        emotions = ['Happy', 'Sad', 'Angry', 'Fearful', 'Surprised', 'Love', 'Excitement',
                   'Boredom', 'Confusion', 'Curiosity', 'Relief', 'Guilt', 'Shame',
                   'Jealousy', 'Pride', 'Trust', 'Anticipation', 'Calmness', 'Disgust', 'Neutral']

        left_col = tk.Frame(self.bars_frame, bg="#f0f2f5")
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        right_col = tk.Frame(self.bars_frame, bg="#f0f2f5")
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for idx, emotion in enumerate(emotions):
            parent = left_col if idx < 10 else right_col
            row = tk.Frame(parent, bg="#f0f2f5")
            row.pack(fill=tk.X, pady=2)

            tk.Label(row, text=emotion, font=("Helvetica", 10, "bold"),
                    bg="#f0f2f5", fg="#555", width=12, anchor="w").pack(side=tk.LEFT)

            bar_container = tk.Frame(row, bg="#e0e0e0", height=22, width=200)
            bar_container.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            bar_container.pack_propagate(False)

            bar_fill = tk.Frame(bar_container, bg=self.emotion_colors[emotion.lower()],
                               height=22, width=0)
            bar_fill.place(x=0, y=0)

            pct_label = tk.Label(row, text="0%", font=("Helvetica", 10, "bold"),
                                bg="#f0f2f5", fg="#333", width=5)
            pct_label.pack(side=tk.RIGHT)

            self.bar_widgets[emotion.lower()] = (bar_fill, pct_label, bar_container)

        # Details section
        self.details_frame = tk.LabelFrame(self.results_frame, text="Details",
                                          font=("Helvetica", 11, "bold"),
                                          bg="#f8f9fa", fg="#555", padx=10, pady=10)
        self.details_frame.pack(fill=tk.X, pady=(10, 0))

        self.details_text = tk.Label(self.details_frame,
                                    text="Enter text and click Analyze to see emotion details.",
                                    font=("Helvetica", 11), bg="#f8f9fa", fg="#555",
                                    wraplength=700, justify=tk.LEFT)
        self.details_text.pack(anchor="w")

        # Examples section
        examples_frame = tk.LabelFrame(scrollable_frame, text="Quick Examples (20 Emotions)",
                                      font=("Helvetica", 11, "bold"),
                                      bg="#f0f2f5", fg="#555", padx=10, pady=10)
        examples_frame.pack(fill=tk.X, pady=(0, 10), padx=20)

        examples = [
            ("Happy", "I am so happy and joyful today!"),
            ("Sad", "I feel so sad and lonely right now."),
            ("Angry", "I am furious and angry about this!"),
            ("Fearful", "I am scared and terrified of what might happen."),
            ("Surprised", "I am shocked and surprised by the news!"),
            ("Love", "I love you so much, you mean everything to me."),
            ("Excitement", "I am so excited and thrilled for the concert!"),
            ("Boredom", "This is so boring and dull, nothing interesting happens."),
            ("Confusion", "I am confused and puzzled by what you said."),
            ("Curiosity", "I am curious and fascinated by this mystery."),
            ("Relief", "I am so relieved that the danger is over."),
            ("Guilt", "I feel guilty and ashamed of what I did."),
            ("Shame", "I am humiliated and embarrassed by my mistake."),
            ("Jealousy", "I am jealous and envious of their success."),
            ("Pride", "I am proud of my achievements and victory."),
            ("Trust", "I trust you completely, you are reliable."),
            ("Anticipation", "I am eagerly anticipating the big event tomorrow."),
            ("Calmness", "I feel calm and peaceful in this quiet place."),
            ("Disgust", "That is disgusting and revolting, I feel sick."),
            ("Neutral", "The weather is normal today."),
        ]

        for label, text in examples:
            btn = tk.Button(examples_frame, text=label, font=("Helvetica", 9),
                          bg="white", fg="#667eea", bd=1, relief=tk.SOLID,
                          cursor="hand2", padx=8, pady=3,
                          command=lambda t=text: self.set_text(t))
            btn.pack(side=tk.LEFT, padx=3, pady=2)

    def set_text(self, text):
        self.text_input.delete(1.0, tk.END)
        self.text_input.insert(tk.END, text)
        self.analyze_emotion()

    def clear_text(self):
        self.text_input.delete(1.0, tk.END)
        for emotion, (bar, pct, container) in self.bar_widgets.items():
            bar.config(width=0)
            pct.config(text="0%")
        self.emoji_label.config(text="😐")
        self.emotion_name_label.config(text="Neutral", fg="#95a5a6")
        self.confidence_label.config(text="Confidence: 0%")
        self.details_text.config(text="Enter text and click Analyze to see emotion details.")

    def analyze_emotion(self):
        text = self.text_input.get(1.0, tk.END).strip()

        if not text:
            messagebox.showwarning("Empty Input", "Please enter some text to analyze!")
            return

        result = self.detect_emotion(text)
        self.display_results(result)

    def detect_emotion(self, text):
        lower_text = text.lower()
        words = re.findall(r'\b\w+\b', lower_text)
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

        scores = defaultdict(float)
        detected_words = defaultdict(list)

        # Check multi-word phrases
        for emotion, lexicon in self.emotion_lexicon.items():
            for phrase, weight in lexicon.items():
                if ' ' in phrase:
                    matches = re.findall(re.escape(phrase), lower_text)
                    if matches:
                        scores[emotion] += weight * len(matches)
                        detected_words[emotion].extend(matches)

        # Process word by word
        for i, word in enumerate(words):
            negation_multiplier = 1
            intensifier_multiplier = 1

            # Check context in previous 3 words
            for j in range(max(0, i - 3), i):
                prev_word = words[j]
                if prev_word in self.negation_words:
                    negation_multiplier = -1
                if prev_word in self.intensifiers:
                    intensifier_multiplier = self.intensifiers[prev_word]

                # Check for two-word diminishers
                if j < i - 1:
                    two_word = prev_word + ' ' + words[j + 1]
                    if two_word in self.diminishers:
                        intensifier_multiplier = self.diminishers[two_word]

            for emotion, lexicon in self.emotion_lexicon.items():
                if word in lexicon and ' ' not in word:
                    base_score = lexicon[word]
                    final_score = base_score * intensifier_multiplier

                    if negation_multiplier == -1:
                        # Handle negation with emotion-specific flips
                        flip_map = {
                            'happy': 'sad', 'sad': 'happy', 'love': 'hate',
                            'excitement': 'boredom', 'calmness': 'fearful',
                            'trust': 'fearful', 'relief': 'fearful',
                            'pride': 'shame', 'anticipation': 'boredom'
                        }
                        if emotion in flip_map:
                            target = flip_map[emotion]
                            scores[target] += abs(final_score) * 0.7
                            detected_words[target].append('not ' + word)
                        else:
                            final_score *= 0.3
                            scores[emotion] += final_score
                            detected_words[emotion].append('not ' + word)
                    else:
                        scores[emotion] += final_score
                        detected_words[emotion].append(word)

        # Check for mixed emotion patterns
        mixed_score = 0
        mixed_patterns = [
            r'but\s+also', r'happy\s+but', r'sad\s+but', r'angry\s+but',
            r'mixed\s+feelings', r'conflicted', r'bittersweet',
            r'part\s+happy', r'part\s+sad', r'both\s+happy', r'both\s+sad',
            r'while.*also', r'although.*still'
        ]

        for pattern in mixed_patterns:
            if re.search(pattern, lower_text):
                mixed_score += 2

        # Detect contradictory emotions
        has_emotions = {e: scores[e] > 0 for e in ['happy', 'sad', 'angry', 'fearful', 'love', 'excitement']}
        emotion_count = sum(has_emotions.values())

        if (has_emotions['happy'] and has_emotions['sad']) or \
           (has_emotions['happy'] and has_emotions['angry']) or \
           (has_emotions['sad'] and has_emotions['angry']) or mixed_score > 0:
            mixed_score += 1

        total_score = sum(scores.values()) + mixed_score

        if total_score == 0:
            return {
                'main_emotion': 'neutral',
                'confidence': 100,
                'scores': {e: 0 for e in self.emotion_emojis.keys()},
                'details': 'No strong emotional indicators detected in the text.',
                'detected_words': {}
            }

        # Calculate percentages
        percentages = {}
        max_score = 0
        main_emotion = 'neutral'

        for emotion in self.emotion_lexicon.keys():
            pct = round((scores[emotion] / total_score) * 100)
            percentages[emotion] = pct
            if scores[emotion] > max_score:
                max_score = scores[emotion]
                main_emotion = emotion

        # Handle mixed emotions
        if mixed_score > 1 or (mixed_score > 0 and max_score < 2):
            main_emotion = 'mixed'
            percentages['mixed'] = min(50, mixed_score * 15)
            reduction_factor = (100 - percentages['mixed']) / 100
            for emotion in list(percentages.keys()):
                if emotion != 'mixed':
                    percentages[emotion] = round(percentages[emotion] * reduction_factor)
        else:
            percentages['mixed'] = min(20, mixed_score * 10)

        # Set neutral
        strong_count = sum(1 for s in scores.values() if s > 0)
        if strong_count == 0:
            percentages['neutral'] = 100
        elif strong_count == 1 and max_score < 1:
            percentages['neutral'] = 50
            percentages[main_emotion] = 50
        else:
            current_sum = sum(percentages.values())
            percentages['neutral'] = max(0, 100 - current_sum)

        # Normalize to 100
        total_pct = sum(percentages.values())
        if total_pct != 100:
            factor = 100 / total_pct
            for emotion in percentages:
                percentages[emotion] = round(percentages[emotion] * factor)

        # Recalculate main emotion
        max_pct = 0
        for emotion, pct in percentages.items():
            if pct > max_pct and emotion != 'neutral':
                max_pct = pct
                main_emotion = emotion

        if percentages['neutral'] > max_pct:
            main_emotion = 'neutral'

        # Generate details
        if main_emotion == 'neutral':
            details = "The text appears emotionally neutral with no strong positive or negative indicators."
        elif main_emotion == 'mixed':
            details = "The text contains conflicting emotional signals, suggesting complex or mixed feelings."
        else:
            details = f"The text shows strong indicators of {self.emotion_names[main_emotion]}. "

            if detected_words[main_emotion]:
                unique_words = list(dict.fromkeys(detected_words[main_emotion]))[:5]
                details += f"Key words detected: {', '.join(unique_words)}."

        if len(sentences) > 1:
            sentence_emotions = []
            for s in sentences:
                r = self.detect_emotion(s)
                sentence_emotions.append(r['main_emotion'])
            unique = list(dict.fromkeys(sentence_emotions))
            if len(unique) > 1:
                details += f" Different sentences show varying emotions ({', '.join(unique)})."

        return {
            'main_emotion': main_emotion,
            'confidence': percentages[main_emotion],
            'scores': dict(percentages),
            'details': details,
            'detected_words': dict(detected_words)
        }

    def display_results(self, result):
        # Update main emotion
        self.emoji_label.config(text=self.emotion_emojis[result['main_emotion']])
        self.emotion_name_label.config(
            text=result['main_emotion'].upper(),
            fg=self.emotion_colors[result['main_emotion']]
        )
        self.confidence_label.config(text=f"Confidence: {result['confidence']}%")

        # Update bars
        for emotion, (bar, pct_label, container) in self.bar_widgets.items():
            percentage = result['scores'].get(emotion, 0)

            # Calculate width based on container width
            container.update_idletasks()
            container_width = container.winfo_width()
            bar_width = int((percentage / 100) * container_width)

            bar.config(width=bar_width)
            pct_label.config(text=f"{percentage}%")

        # Update details
        self.details_text.config(text=result['details'])


def main():
    root = tk.Tk()
    app = EmotionDetectorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()