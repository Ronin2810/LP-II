from nltk.chat.util import Chat, reflections

pairs =[
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['(.*) your name ?', ['My name is ChatMan']],
    ['(.*) do you do ?', ['We provide a platform for chatting, a wide range of options !']],
    ['(.*) how are you ?' ,["I'm doing great. How about You ?"]],
    ['sorry (.*)',['Its alright","Its OK, never mind']],
    ['I am fine',['Great to hear that, How can I help you?']],
    ['I (.*) good',['Nice to hear that','How can I help you?:)']],
    ['(.*) age?',['I am a computer program dude Seriously you are asking me this?']],
    ['what (.*) want ?',['Make me an offer I cannot refuse']],
    ['(.*) created ?',['Rohit created me using Python NLTK library ','  top secret ;)']],
    ['(.*) (location|city) ?',['Pune, Maharashtra']],
    ['how is weather in (.*)?',['Weather in %1 is awesome like always','Too hot man here in %1','Too cold man here in %1','Never even heard about %1']],
    ['i work in (.*)?',['%1 is an Amazing company', 'I have heard about it. But they are in huge loss these days.']],
    ['(.*)raining in (.*)',['No rain since last week here in %2','Damn its raining too much here in %2']],
    ['how (.*) health(.*)',['I am a computer program, so I am always healthy ']],
    ['(.*) (sportz|game) ?',['I am a very big fan of Cricket','I like watching football']],
    ['who (.*) sportsperson ?',['Rohit Sharma','Virat Kohli','MS Dhoni', 'Lionel Messi', 'Christiano Ronaldo']],
    ['who (.*) (moviestar|actor)?',['Shah Rukh Khan']],
    ['quit',['Thank you for using our services']]
]

chat = Chat(pairs, reflections)
chat.converse()
