# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Eshan Shakrani
# netid: eshakrani
# Student ID: 112802596

import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "b37NODAQBwDTT7QqLcM6gZMsR"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "luCsdclCIafY3qu1LaWM2OoUpuwZ4tKPIU4AI0Q0UIIDWkriQg"

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    print('10 Tweets from Home Timeline:')
    for tweet in simple_twit.get_home_timeline(api, 10):
        print('ID:', tweet.id, '\n', 
        'Author Name:', tweet.author.name, '\n', 
        'Screen Name:', tweet.author.screen_name, '\n', 
        'Creation Date:', str(tweet.created_at).split(' ')[0], '\n', 
        'Full Text:', tweet.full_text, '\n')
 

# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    print('10 Tweets from User IAE101_ckane Timeline:')
    for tweet in simple_twit.get_user_timeline(api, 'IAE101_ckane', 10):
        print('ID:', tweet.id, '\n', 
        'Author Name:', tweet.author.name, '\n', 
        'Screen Name:', tweet.author.screen_name, '\n', 
        'Creation Date:', str(tweet.created_at).split(' ')[0], '\n', 
        'Full Text:', tweet.full_text, '\n')


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    s = 'This is a test tweet.\nSeconds since the epoch: ' + str(time.time())
    simple_twit.send_tweet(api, s)


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    s = 'This is a test media tweet.\nSeconds since the epoch: ' + str(time.time())
    failed = False
    try:
        simple_twit.send_media_tweet(api, s, r'E:\eshak\Documents\College\Year_3\Fall_2021\IAE_101\IAE101\Twitter_Project\twitter_logo.jpg')
    except Exception as e:
        failed = True 
    if failed:
        simple_twit.send_media_tweet(api, s, r'C:\Users\eshak\OneDrive\Documents\IAE101\Twitter_Project\twitter_logo.jpg')
    

# End of Project 04 Exercises

quotes = [
    (r'''"The greatest glory in living lies not in never falling, but in rising every time we fall."''', 'Nelson Mandela'),
    (r'''"The way to get started is to quit talking and begin doing."''', 'Walt Disney'),
    (r'''"If life were predictable it would cease to be life, and be without flavor."''', 'Eleanor Roosevelt'),
    (r'''"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."''', 'Oprah Winfrey'),
    (r'''"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."''', 'James Cameron'),
    (r'''"Spread love everywhere you go. Let no one ever come to you without leaving happier."''', 'Mother Teresa'),
    (r'''"When you reach the end of your rope, tie a knot in it and hang on."''', 'Franklin D. Roosevelt'),
    (r'''"Always remember that you are absolutely unique. Just like everyone else."''', 'Margaret Mead'),
    (r'''"Don't judge each day by the harvest you reap but by the seeds that you plant."''', 'Robert Louis Stevenson'),
    (r'''"The future belongs to those who believe in the beauty of their dreams."''', 'Eleanor Roosevelt'),
    (r'''"Tell me and I forget. Teach me and I remember. Involve me and I learn."''', 'Benjamin Franklin'),
    (r'''"The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart."''', 'Helen Keller'),
    (r'''"It is during our darkest moments that we must focus to see the light."''', 'Aristotle'),
    (r'''"Whoever is happy will make others happy too."''', 'Anne Frank'),
    (r'''"Do not go where the path may lead, go instead where there is no path and leave a trail."''', 'Ralph Waldo Emerson'),
    (r'''"You will face many defeats in life, but never let yourself be defeated."''', 'Maya Angelou'),
    (r'''"In the end, it's not the years in your life that count. It's the life in your years."''', 'Abraham Lincoln'),
    (r'''"Never let the fear of striking out keep you from playing the game."''', 'Babe Ruth'),
    (r'''"Life is either a daring adventure or nothing at all."''', 'Helen Keller'),
    (r'''"Many of life's failures are people who did not realize how close they were to success when they gave up."''', 'Thomas A. Edison'),
    (r'''"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose."''', 'Dr. Seuss'),
    (r'''"Life is never fair, and perhaps it is a good thing for most of us that it is not."''', 'Oscar Wilde'),
    (r'''"The only impossible journey is the one you never begin."''', 'Tony Robbins'),
    (r'''"In this life we cannot do great things. We can only do small things with great love."''', 'Mother Teresa'),
    (r'''"Only a life lived for others is a life worthwhile."''', 'Albert Einstein'),
    (r'''"The purpose of our lives is to be happy."''', 'Dalai Lama'),
    (r'''"Life is what happens when you're busy making other plans."''', 'John Lennon'),
    (r'''"You only live once, but if you do it right, once is enough."''', 'Mae West'),
    (r'''"Live in the sunshine, swim the sea, drink the wild air."''', 'Ralph Waldo Emerson'),
    (r'''"Go confidently in the direction of your dreams! Live the life you've imagined."''', 'Henry David Thoreau'),
    (r'''"Life is really simple, but we insist on making it complicated."''', 'Confucius'),
    (r'''"Life itself is the most wonderful fairy tale."''', 'Hans Christian Andersen'),
    (r'''"Do not let making a living prevent you from making a life."''', 'John Wooden'),   
    (r'''"Life is ours to be spent, not to be saved."''', 'D.H. Lawrence'),
    (r'''"Keep smiling, because life is a beautiful thing and there's so much to smile about."''', 'Marilyn Monroe'),
    (r'''"Life is a long lesson in humility."''', 'James M. Barrie'),
    (r'''"In three words I can sum up everything I've learned about life: it goes on."''', 'Robert Frost'),
    (r'''"Love the life you live. Live the life you love."''', 'Bob Marley'),
    (r'''"Life is made of ever so many partings welded together."''', 'Charles Dickens'),
    (r'''"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking."''', 'Steve Jobs'),
    (r'''"Life is trying things to see if they work."''', 'Ray Bradbury'),
    (r'''"Success is not final; failure is not fatal: It is the courage to continue that counts."''', 'Winston S. Churchill'),
    (r'''"Success usually comes to those who are too busy to be looking for it."''', 'Henry David Thoreau'),
    (r'''"If you really look closely, most overnight successes took a long time."''', 'Steve Jobs'),
    (r'''"The secret to success is to do the common thing uncommonly well."''', 'John D. Rockefeller Jr.'),
    (r'''"I find that the harder I work, the more luck I seem to have."''', 'Thomas Jefferson'),
    (r'''"The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere."''', 'Barack Obama'),
    (r'''"Don't be distracted by criticism. Remember - the only taste of success some people get it to take a bite out of you."''', 'Zig Ziglar'),
    (r'''"I never dreamed about success, I worked for it."''', 'Estee Lauder'),
    (r'''"Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit."''', 'Conrad Hilton'),
    (r'''"There are no secrets to success. It is the result of preparation, hard work, and learning from failure."''', 'Colin Powell'),
    (r'''"The only limit to our realization of tomorrow will be our doubts of today."''', 'Franklin D. Roosevelt'),
    (r'''"It is better to fail in originality than to succeed in imitation."''', 'Herman Melville'),
    (r'''"Successful people do what unsuccessful people are not willing to do. Don't wish it were easier; wish you were better."''', 'Jim Rohn'),
    (r'''"The road to success and the road to failure are almost exactly the same."''', 'Colin R. Davis'),
    (r'''"I failed my way to success."''', 'Thomas Edison'),
    (r'''"A successful man is one who can lay a firm foundation with the bricks others have thrown at him."''', 'David Brinkley'),
    (r'''"Things work out best for those who make the best of how things work out."''', 'John Wooden'),
    (r'''"Try not to become a man of success. Rather become a man of value."''', 'Albert Einstein'),
    (r'''"Don't be afraid to give up the good to go for the great."''', 'John D. Rockefeller'),
    (r'''"Always bear in mind that your own resolution to success is more important than any other one thing."''', 'Abraham Lincoln'),
    (r'''"Success is walking from failure to failure with no loss of enthusiasm."''', 'Winston Churchill'),
    (r'''"You know you are on the road to success if you would do your job and not be paid for it."''', 'Oprah Winfrey'),
    (r'''"If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work."''', 'Thomas J. Watson'),
    (r'''"If you genuinely want something, don't wait for it - teach yourself to be impatient."''', 'Gurbaksh Chahal'),
    (r'''"The only place where success comes before work is in the dictionary."''', 'Vidal Sassoon'),
    (r'''"If you are not willing to risk the usual, you will have to settle for the ordinary."''', 'Jim Rohn'),
    (r'''"Before anything else, preparation is the key to success."''', 'Alexander Graham Bell'),
    (r'''"People who succeed have momentum. The more they succeed, the more they want to succeed and the more they find a way to succeed. Similarly, when someone is failing, the tendency is to get on a downward spiral that can even become a self-fulfilling prophecy."''', 'Tony Robbins'),
    (r'''"Whether you think you can or you think you can't, you're right."''', 'Henry Ford'), 
    (r'''"I have learned over the years that when one's mind is made up, this diminishes fear."''', 'Rosa Parks'),
    (r'''"I alone cannot change the world, but I can cast a stone across the water to create many ripples."''', 'Mother Teresa'),
    (r'''"Nothing is impossible, the word itself says, 'I'm possible!'"''', 'Audrey Hepburn'),
    (r'''"The question isn't who is going to let me, it's who is going to stop me."''', 'Ayn Rand'),
    (r'''"The only person you are destined to become is the person you decide to be."''', 'Ralph Waldo Emerson'),
    (r'''"Believe you can and you're halfway there."''', 'Theodore Roosevelt'),
    (r'''"I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel."''', 'Maya Angelou'),
    (r'''"Winning isn't everything, but wanting to win is."''', 'Vince Lombardi'),
    (r'''"The most difficult thing is the decision to act, the rest is merely tenacity."''', 'Amelia Earhart'), 
    (r'''"How wonderful it is that nobody need wait a single moment before starting to improve the world."''', 'Anne Frank'),
    (r'''"An unexamined life is not worth living."''', 'Socrates'), 
    (r'''"Everything you've ever wanted is on the other side of fear."''', 'George Addair'), 
    (r'''"Dream big and dare to fail."''', 'Norman Vaughan'),
    (r'''"You may be disappointed if you fail, but you are doomed if you don't try."''', 'Beverly Sills'),
    (r'''"Life is 10% what happens to me and 90% of how I react to it."''', 'Charles Swindoll'),
    (r'''"It does not matter how slowly you go as long as you do no stop."''', 'Confucius'),
    (r'''"When everything seems to be going against you, remember that the airplane takes off against the wind, not with it."''', 'Henry Ford'),
    (r'''"Too many of us are not living our dreams because we are living our fears."''', 'Les Brown'),
    (r'''"I didn't fail the test. I just found 100 ways to do it wrong."''', 'Benjamin Franklin'),
    (r'''"If you're offered a seat on a rocket ship, don't ask what seat! Just get on."''', 'Sheryl Sandberg'),
    (r'''"I would rather die of passion than of boredom."''', 'Vincent van Gogh'),
    (r'''"Dreaming, after all, is a form of planning."''', 'Gloria Steinem'),
    (r'''"Whatever the mind of man can conceive and believe, it can achieve."''', 'Napoleon Hill'),
    (r'''"First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end."''', 'Aristotle'),
    (r'''"Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover."''', 'Mark Twain')
    ]
    
used = []

# YOUR BOT CODE GOES IN HERE
def twitterbot(api, quotes, used):
    if len(quotes) != 0:
        index = random.randint(0, len(quotes) - 1)
        tup = quotes.pop(index)
        used.append(tup)
        s = tup[0] + '\n\t--' + tup[1]
        simple_twit.send_tweet(api, s)
    else:
        quotes = [ quote for quote in used ]
        used = []
        twitterbot(api, quotes, used)


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    exercise1(api)
    exercise2(api)
    exercise3(api)
    exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api, quotes, used)
