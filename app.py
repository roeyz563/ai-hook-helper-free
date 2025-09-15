# app.py
# Import libraries
import streamlit as st
from openai import OpenAI

# 1. Set up the page
st.set_page_config(page_title="AI Hook Helper", page_icon="🚀", layout="wide")
st.title("🚀 AI Viral Hook Helper")
st.markdown("Paste your video script below and get 5 viral hook options generated from proven viral templates.")

# 2. Securely input your API Key. 
# We use Streamlit's secrets management for deployment.
# For local run, we'll use a sidebar input.
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    if api_key:
        client = OpenAI(api_key=api_key)
        st.success("API key set successfully!")
    else:
        st.info("Please enter your API key to begin.")
    st.markdown("---")
    st.markdown("**How to use:**\n1. Enter your API key.\n2. Paste your script in the main box.\n3. Click 'Generate Hooks'.")

# 3. Load your hook templates. 
# PASTE YOUR 257 HOOKS INSIDE THE TRIPLE QUOTES!
hook_templates = """
Here’s exactly how to [outcome]. [solution]. 
Here’s exactly how you’re gonna [outcome].
Here’s the exact 3 step process to [outcome].
Here’s exactly how to NEVER [opposite of outcome].
Here’s the only [solution] that will let you [personal outcome].
Here’s the only method/way/strategy/hack that will let you [personal outcome].
Here’s the only guide to [solution] you will ever need.
Here’s how to never [opposite of solution] for the rest of your life.
Alright if I was you and I needed to [outcome] really quickly, I’m gonna tell you exactly what I would do. Free sauce.
You ever see videos on Youtube of [outcome], and you’re like how the hell is that even possible?
Everybody that tells you that you don’t need to [solution] to [outcome] is lying to you.
If there’s one piece of advice about how to [outcome] today, please let it be this.
If you wanna [outcome] in 3 months time, here’s your 5 step checklist for you to do right now, if you just do this I promise you’ll [outcome]. Step 1…
A lot of people who wanna [outcome] fail to do so because they’re not [solution].
Wanna know why most people never [outcome]?
Here’s how to stop [opposite of outcome]. [Solution].
If I was young again and I had to [personal outcome] all over again, this is exactly how I’d do it.
I’m gonna show you exactly how to [outcome] in a very very specific way.
Alright I’m gonna teach you exactly how to [outcome] in one video.
Here’s the story of how I accidentally [personal outcome].
You ever see people who just have [outcome], and you kinda wonder like, what it is that makes them so special?
You ever see people who seem to [outcome] SO easily, and you kinda wonder like, what it is that makes them so special?
In 60 seconds I’m going to logically prove to you how you can literally [outcome].
Here’s why you should [solution].
Here’s how to [outcome]. Stop [solution, if about quitting something].
Here’s how to [outcome]. [Solution].
Here’s the ONE [solution] I used to [outcome]. Like I [personal outcome] literally just spamming this ONE [solution].
Here’s how to [outcome]. The solution that’s always worked for me is [solution].
Here’s how to stop [opposite of outcome]. Stop [solution, if about quitting something].
Today, we’re gonna be talking about how to [outcome].
Alright this is the single easiest way to [outcome].
If you want to instantly [outcome], this is the ONLY video you will ever need to watch.
Here’s exactly how you’re gonna [outcome] in 2024. You’re gonna [solution].
Here’s the only video you will ever need to watch to [outcome].
Here’s the strategy I used to [outcome]. I used a strategy I like to call [solution].
The easiest way to [outcome] is to [solution].
Here’s exactly how you’re gonna [outcome] in 2024. You’re gonna [solution].
The way to instantly [outcome] is to simply [solution].
If there’s one thing you can do to [outcome] that actually takes ZERO work, it’s this.
If you’re tired of [opposite of outcome], here’s the ultimate guide to [outcome]. Take notes and thank me later.
If you’re tired of never [outcome], you NEED to watch this video.
I’m gonna give you guys my BEST [solution] as someone who [personal outcome] that’s literally gonna help you [outcome].
So I heard you wanna [outcome]. This is the SIMPLEST and BEST way to [outcome], coming from a guy whose [personal outcome].
Here’s exactly how you’re gonna [verb] your first [outcome].
I get this question SO often. How did you [personal outcome]? And I Iiterally just [solution].
Here’s some unethical life hacks to [outcome] that you definitely shouldn’t use.
Here’s exactly how you’re gonna [outcome] in the next 60 seconds.
Here’s exactly how I [personal outcome]. I [solution].
I [personal outcome], and I just wanna break down the exact [solution] I used to get such crazy results.
I recently [personal outcome], and I just wanna break down the exact [solution] I used to get such crazy results.
So you failed to [personal outcome]. Tough love, but it’s because you didn’t [solution].
Here’s how to ACTUALLY [outcome]. [Solution].
Here’s how to NOT [opposite of outcome]. Stop [opposite of solution]
It is officially the easiest time to [outcome], and I’m gonna give yall all the sauce on how you’re gonna [outcome] in the next week.
In 60 seconds, I’ll show you how to [outcome].
I’m gonna show you exactly how to become a [outcome] in one video.
I’m gonna show you exactly how to get over your [outcome] in one video.
It took me 4 years to learn what I’m about to teach you in a minute and a half.
This is how to [outcome]. What you’re gonna need is a [solution]. What is a [solution]?
Every day I [personal outcome], and here are my 8 tips to [personal outcome].
After years of [personal outcome], these are the 6 rules of [outcome] I know to be true.
After years of research, I’ve developed the greatest routine to [outcome]. Here are the 7 steps you should take every day.
I just completed [personal outcome]. Here’s why I haven’t stopped.
3 steps for becoming [outcome].
5 principles for becoming [outcome].
3 things I wish I knew in my early 20s. [solution].
4 ways to [outcome].
5 things you need to know if you want to [outcome].
This goes out to all my homies who struggle with [outcome].
Here’s a life hack that’s gonna [outcome] that they never taught you in school.
Here’s how to [outcome] in a way a 5 year-old could understand.
This is exactly how to [outcome] in a way a 5 year-old could understand.
You wanna [outcome] in 2024, I recommend listening to this video all the way through because the trends/methods/strategies/tricks that have worked for [outcome] in the past aren’t anymore, but the new trend/method/strategy/trick you need to use is…
I was just [personal story] and I just got the best advice on [outcome] that I’ve ever heard.
This is the ultimate guide on how to [outcome].
Does [solution] ACTUALLY get you [outcome]?
You guys ever heard of the [solution]? Cus the [solution] is life-changing.
One of the things I really like to do if I wanna [outcome] but I don’t know how is the [solution] method.
Alright if you want one of your average [noun from the outcome] to look like this, the best thing you can do is [solution].
Here’s how to [outcome] literally anywhere.
If I needed to [dream outcome] or someone was gonna blow my brains out, this is what I would do.
Your [thing/situation]s will feel way less [outcome] when you understand these 3 things.
Here are 3 rules you should follow if you actually wanna [dream outcome].
Here are 3 reasons why you’re gonna [dream outcome].
In 60 seconds I’m gonna logically prove to you how you can [dream outcome].
There are 3 reasons you’re [problem] right now. Either one, you [negative habit/action]…
Having [dream outcome] is pretty fucking cool. So if you wanna [dream outcome], here are 3 ways you can actually do that. Number one…[habit/action].
So I just [personal dream outcome] yesterday, and I wanted to tell yall some lessons I’ve learned along the way to teach you what I wish I knew now.
So I just [personal dream outcome] last week/month/year, and here are 3 lessons I’ve learned along the way.
Here are 3 [niche] hacks guaranteed to turn you into a [dream outcome].
If I could teleport back to before I [personal dream outcome], here are the 3 things that I would sell my kidney today to tell past me.
Here are the 3 easiest ways to [dream outcome].
The 3 [thing/action/habit]s you need to [dream outcome].
Here are 3 ways to actually [dream outcome]. If you don’t implement some sort of system to [same dream outcome], you’re gonna have [problem].
These are 3 [thing/situation] tips that you fuckin’ need. Lock in, implement them, and [dream outcome].
3 signs you’re probably the [trait] homie.
I’m not sure if you guys know this or not, but right now people are boycotting [thing].
If you’re a guy and there’s this [dream outcome], or you’re a girl and there’s this [female variation of dream outcome], I’mma give you 3 ways to [dream outcome].
"Here's what (group) don't want you to know about (thing)"
"Here are the top 5 (thing avatar wants) for (avatar)"
"Here's how to get (thing avatar wants) literally anywhere"
"3 (resource type) that will save you from ebola as a (avatar) in 2023"
"The secret to (thing they want) is (intriguing phrasing of simple concept)"
"How to ACTUALLY (achieve thing they want)"
"How to get (thing they want)" - with green screen and you showing a guide
"The goated (way to do thing that is important to them)"
"The most important decision you have to make as a (avatar) is ()"
"Underrated (avatar) hack"
"I'm literally gonna solve all your (section of their life) problems in one video"
17 ways to not be (thing they dont want to be)
Here’s the TRUTH about (thing they will experience)
Here’s how to do XYZ like the rich
(Thing they experience) 101
Here are 3 strange (topic) hacks guaranteed to turn you into a (term for someone really good at that topic)
You wanna know what the (most adjective they want) mf’s in (their age group/demographic) have in common?
I don’t think people understand how fucked up it is that we let people (do X thing)
The biggest problem with the (XX system) that nobody talks about is (bold claim)
Here are the 3 best (things related to your niche) for the year 2030
Let’s get you (thing they want) papi/bro/homie.
Here’s the no-fail system to getting (thing they want) your (roasting their normal source of information) didn’t teach you
If you want to win at (thing they experience) you need (thing that sounds counterintuitive)
The WORST (thing they do/choose) in 2024 is…
Here are 3 signs you picked the wrong (thing in your niche)
If you’re having trouble {thing they need to do}, watch this video, I’m gonna change your life. It might not change your life, but I’m gonna help you {dream outcome}.
If you’re not getting [dream outcome] in [situation/time], it’s probably because you don’t know the [solution name] framework.
There’s only 3 ways you can compete as a [title/identity/dream persona].
If you’re a {title} and you wanna crush it in {thing}, you need to watch this video, lock the f*ck in, because no one’s gonna give you the sauce. I’m gonna give you the complete roadmap to kill it in [thing]. It’s gonna help you [dream outcome examples].
Here are the 3 biggest “no-nos” when it comes to (your niche)
It’s (today’s date) and it’s not too late for you to (achieve thing they want)
This is gonna sound like pedantic advice, it’s gonna sound so obvious like ohhh shut the f*ck up! But if you’re crazy [nightmare problem situation] in [situation/place/time], you’re in one of those days where [example], you can take a breath and remind yourself that [solution/opinion].
This is gonna sound like repetitive advice, it’s gonna sound so obvious like ohhh shut the f*ck up! But if you’re crazy [nightmare problem situation] in [situation/place/time], you’re in one of those days where [example], take a breath and remember the [solution name].
If you’re down f*cking sad in {niche/position/situation/thing/pursuit}, you need to start {solution}.
Here are 4 fascinating facts about {thing they’re interested in}.
If you’re a [position/title], this is the EASIEST way to wake up with a [dream outcome].
When things click they click for (your IVP).
(reassuring the viewer video) If you’re a [title], there is nothing wrong with you if you are struggling in [thing/place/situation/title]. Like it’s okay if you’re [example 1], it’s okay if you’re [example 2].
If you’re in [thing/place/time/position] and your [thing they care about] is all f*cked up and you’re worried about [dream outcome], the NUMBER ONE thing you can do is go [solution].
You need to hear this if you’re obsessed with (thing)
I don’t think I could say this with any more conviction, but [thing a lot of people like] is so f*cking dumb.
So if you’re in [place/time/situation], and you feel like you [nightmare problem situation description with examples], watch this video and it’ll change your life.
One of the best things you can do for your [thing they need to do] in [time/situation/place] is literally just [one-word solution].
There are many times in [thing] where you take a massive f*cking L, and the only thing you can do is [solution].
These are the 3 hallmarks of a goated (thing they need to do)
Here are the 3 signs of a goated (thing they need to do).
Here are 3 {thing in your niche} tips that you f*cking need.
There’s only 2 kinds of people who get (dream outcome)s, one of whom is the most miserable, sad, upset people on earth, and the other one is the [dream outcome/persona], who you should try to be like.
This is what nobody seems to understand about [thing].
Ultimate [thing] hack for men is being able to [action], but [twist to solution]. You have to understand, [opinion].
When you actually [major event/accomplishment], there’s only 2 things you can do to [dream outcome].
When you actually graduate college/highschool, there’s only 2 things you can really do to [dream outcome].
In [place/time/age], there are a couple defining moments. There are gonna be times where [example 1], and there’s gonna be times where [example 2]. These 3 things are where all the [event/thing] comes out.
The number one decision you can make (in a situation your IVP finds themselves in)
(Category of celebrity / pop culture thing) as (things in your niche) part 1
If you’re a (IVP), you need to get (thing that sounds awful)
Whenever I get to a [bad situation], where I think, why do I even bother, I just try to remind myself: [insert quote]. 
Stop [habit/action] if you actually want to become successful.
Here’s 3 reasons why you need to [habit/action] in 2024.
Everybody that tells you you need to [opposite of solution, or negative habit/action] is lying to you.
If you want to ACTUALLY [outcome] in 2024, you need to [solution].
This is how I went from [personal outcome before] to [dream personal outcome] in _ years/months/days.
Use specific numbers and dates
You don’t understand the 4 phases of [outcome].
All [niche] advice absolutely sucks. This is the only good piece of [niche] advice I’ve ever gotten, and it’s the most useful by far.
A lot of people who want to [outcome] fail to do so because…
You know what the problem is with this generation bro? None of you are [trait/solution] enough.
This is kinda fucked up, but I feel like [opinion].
A lot of people think you have to [limiting belief] to be [outcome]. I [personal outcome].
Everybody that tells you you have to [action] to [outcome] is lying to you. I am one of the [adjective version of the action]est people I know, and the reason why I’ve [personal outcome] is because I simply [solution].
Alright so if you’re young and you [problem], let me tell you a lil secret. This is coming from someone who also [problem] like 3 years ago, and now I [personal dream outcome].
I recently [personal dream outcome], and it’s really not that great.
Alright there’s this myth going around that [dream outcome] does not change your life whatsoever, and that [expand upon myth], and that is WRONG. I currently [personal dream outcome], and I will tell you what it’s actually like.
If you’re under 25 and you feel like you [problem], please just watch this video.
The reason you [problem] is because you’re trying to [limiting habit/action]
If you pause and genuinely [solution], you will never struggle with [negative outcome] again.
The way to instantly make your [situation/thing] way more [outcome] and way easier than it is right now is to simply understand that [opinion/idea].
The way to instantly make your [situation/thing] way easier than it is right now is to simply understand that [opinion/idea].
Take a second to pause and ask yourself, how would I live my life if I [solution]?
If there’s one thing you can do to [outcome] in your early 20’s that actually takes 0 work, it’s this.
I think a reason why a lot of men/women are [negative outcome] is because they [limiting action].
The reason why most men are [negative outcome] is because they think that [limiting action] will get them [outcome].
It took me about _ years to realize that [opinion].
Your [problem] will go away once you realize that [opinion].
The biggest sign of [dream outcome] is [solution].
Your [thing/situation]s will never be [problem] and you’ll [dream outcome] once you’re comfortable with [solution].
Your [thing/situation]s will never be [problem] once you start [solution].
Yo if you’re in college/highschool right now and you wanna [dream outcome] and you don’t wanna be [problem], watch this video.
If you just [situation/thing], these next 6 to 12 months will set you up for the rest of your life. So if you fuck this up, you’re probably gonna [negative outcome].
When you start to [outcome] but you don’t [habit/action], you start to lose [dream outcome].
I don’t agree with this trend on this app that’s like…
I’m starting to notice any cool guy I’ve ever met always has a cooler sister.
[thing 1] or [thing 2]? Now having done both, let me tell you the pros and cons, so you know what to expect.
Reasons why you should [action/solution]. I’m going to get straight into the point, so if you’re struggling with making that decision, this will push you over the edge.
Use/take [thing 1] or [thing 2]? Today I’m going to tell you the pros and cons so you know what to expect.
I don’t know who needs to hear this but if you’re a [title] and you’ve been [action], and [nightmare problem], bro. [opinion].
When I tell yall [problem] has gotten so bad, my homie has to [action] now.
I’m not gonna lie to yall, this [thing] hate is gettin crazy. It’s always that one person talkin about… [quote/paraphrase]
If I became the president of the United States today, the first thing that I’m banning is [thing creator hates].
Yall ever got [outcome] and then you realized there wasn’t splish you could do about it? I used to have a friend who was [story].
A lot of yall be talkin about, “oh I’m top 3 [thing],” but don’t even know what [thing] looks like. I’m gonna tell yall about the most [thing] shi I’ve ever done.
Is it possible to {personal goal} in 1 DAY/WEEK/MONTH?
I just spent $X on {thing}, and…{other hook}.
I LOVE {thing}. So in order to learn more about {thing}, today I decided to {personal action}.
THIS is my {thing}. And today, we’re going to {personal action, related to thing}.
I have an irrational fear of {personal fear}
I have been {adjective} for as long as I can remember. And at this point, I’m just gonna {personal action}.
I have wanted {personal goal} for the longest time, but today is the day we finally {personal action}.
I feel really {feeling/adjective}. Because I just {personal action}.
I have a confession to make. I regret {personal action}.
Come with me as I {action}.
Today, we {action;past tense}, and I {feeling}.
Tonight, I’m {action}.
Today is the first time I’m {action}, and I’m {feeling}.
I have X days left of my college/highschool semester, and/but/so…
I have X days left of being {personal title}, and/but/so…
I have been {personal action/title} for the past X hours/days/months/years, and I wanna show you guys…
So I just found out, if you {personal action}, you can
It is {time}AM/PM and I am {feeling}. So today, I’m going to be {personal action}.
You guys are overreacting. I just {personal action}, and {opinion on personal action}.
{Question}? This is a question I ask myself every single day as a {profession/title}.
{Statement}. This is something I tell myself every single day as a {profession/title}. Like everyone else, I’m just trying to {personal goal}.
I regret {personal action} as a {profession}.
I regret {personal action}. Well, kind of.
I spent the last X hours/days/months doing {personal action}, and I realized that {opinion}.
I spent the last X hours/days/months/years chasing {personal goal}, but today is the day I realized that {opinion}.
Hi, I’m {name}. And… {use other hook}.
I just {personal action}, and I’m now realizing that {opinion}.
I used to be obsessed with {thing related to personal action}, but today is the day we finally {personal action related to thing}
Today I learned it is actually possible to {personal action} without {condition}.
I was having a conversation with this girl today, and she said, “{quote of what person said to you},” and one of my very toxic traits is that I like to {}, so I said…
Somebody asked me why I’m {trait} that’s because I’m dedicated to {thing}.
My favorite thing about being the family disappointment is that {opinion/story}.
Here is my full day of eating that I used to increase my muscle mass as a [title/profession].
I’ve completed {thing/goal} at _ years old. And if you don’t know what I’m talking about, let me explain.
Today was my last day of work/school, and one of my coworkers said, it’s only a trend to hate on [thing].
The bad news is, [controversial opinion]. The good news is, [same controversial opinion]. So just [action].
Why is it so hard to [action]?
They said, just [action, preferably popular wisdom]. That’s a lie.
What if I told you I got [number] more in [thing], JUST by [action]? Here’s how I did it.
What if I told you I increased my [thing] JUST by [action]? Here’s how I did it.
You know, I’m sick of seeing people on TikTok/Instagram being like “Oh, [opinion paraphrased in a casual way].” Oh, so [opinion]? Well, [examples disproving opinion]
Having a [thing] is the most underrated shit, I now [action, explaining why thing is good].
You know, I can’t stand the people that come to me and be like, “Yo, [opinion].”
For those of you who are too closed-minded to understand [idea], I’m going to change your mind.
Cus you need to [action]. You need to [synonym of action]. If you’re not [dream result], you need to [action]. Fuck all these people that are telling you [opposite of action].
You don’t [action] as much as you say you do. You like to talk about it, you like to post about it.
If you’re [situation], and then [situation] happens, like “[quote paraphrasing event], or “[secondary quote paraphrasing event], if it’s within reason, then [opinion].
Some of you have got to cut [thing], the thought of [thing synonym] out of your life, and here’s why. Most of the time, when I see [identity] trying to [thing], it’s because they’re [deeper motivation that’s darker].
You have to believe [thing]. Every fiber of your being has to believe it. And I want you to believe it. Because you need to understand that if you don’t believe it, then you just [consequence].
One of my favorite hobbies is [odd thing].
2025 is here. You need [thing]. It’s not hard.
How much can I [action] in a week as a X year-old full-time [identity]?
I just got the strong urge to talk about some of the biggest [niche] myths that people still believe that keep them [negative situation] and [stronger example depiction of negative situation].
With all due respect, if you are an [identity], and you are still [action], grow the f*ck up. You will [highly specific description of negative life outcome].
Growing up is understanding that [controversial opinion].
A year ago, I was [action], and [extended action] every single night because I couldn’t [overcome big problem].
After 3 years of cycling through [thing 1] and [thing 2], I [solution] because I realized ONE THING… [truth].
2 years ago, I became addicted to [bad thing] every single day because I’d never felt more [bad emotion] in my LIFE.

"""
# Paste ALL your 257 hooks inside the triple quotes above.

hook_list = [hook.strip() for hook in hook_templates.split('\n') if hook.strip()]

# 4. Define the system prompt (the AI's instructions)
system_prompt = """
You are an expert viral hook analyst. Your knowledge base is a list of proven hook templates.

USER'S GOAL:
1. The user will give you the FULL SCRIPT or a detailed description of the video/content they are creating.
2. Your task is to analyze the script's core message and pick the TOP 5 BEST matching templates from the provided list.
3. You MUST output your response in the following exact format for EACH of the 5 hooks:

<HOOK_ANALYSIS_START>
**Core Concept from Script:** [Identify the 1-2 core ideas, conflicts, or revelations in the user's script that this hook captures.]
**Why This Hook Works:** [Explain the psychological mechanism this hook uses (e.g., curiosity gap, fear of missing out, agreement with a strong opinion, solution to a frustration) without naming the specific template.]
**Generated Hook:** [ Apply the script's concept to the template. Fill in the variables ([BRACKETS]) with specific, compelling words from the script's context. Output the final, complete hook.]
</HOOK_ANALYSIS_END>

RULES:
- You MUST output FIVE different hook analyses.
- Choose FIVE DISTINCT templates. Show a range of strategies (e.g., one curiosity gap, one controversial, one how-to).
- Do not output any other text before, after, or between the five analysis blocks.
- Do not invent new templates. You must choose from the provided list.
- The generated hook must be a direct and logical application of the chosen template to the user's script.
"""

# 5. Define the function that calls the AI (the same brain from Colab)
def analyze_script_for_hooks(user_script):
    if not api_key:
        st.error("❌ Please enter your OpenAI API key in the sidebar first.")
        return None

    full_instructions = (
        system_prompt +
        "\n\nHere is the list of hook templates you MUST choose from:\n" +
        "\n".join([f"- {hook}" for hook in hook_list]) +
        "\n\nNow, analyze this user's script and generate 5 hooks:"
    )

    try:
        with st.spinner('🧠 AI is analyzing your script and generating 5 hooks... (This may take 10-20 seconds)'):
            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "system", "content": full_instructions},
                    {"role": "user", "content": user_script}
                ],
                temperature=0.7
            )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def format_ai_response(raw_response):
    """
    This function takes the AI's raw response with XML tags and
    returns a clean, beautifully formatted version for the user.
    It adds line breaks after each section for better readability.
    """
    # Check if the response has the expected structure
    if not raw_response or "<HOOK_ANALYSIS_START>" not in raw_response:
        return raw_response  # Return as-is if it doesn't have the expected format

    # Split the response into individual hook analysis blocks
    hooks = raw_response.split('<HOOK_ANALYSIS_START>')[1:]  # Ignore anything before the first tag

    formatted_output = ""

    # Loop through each hook analysis block
    for i, hook in enumerate(hooks):
        # Remove the closing tag and any extra whitespace
        hook_content = hook.replace('</HOOK_ANALYSIS_END>', '').strip()
        
        # Add a nice header for each hook option
        formatted_output += f"### 🪝 Hook Option #{i+1}\n\n"
        
        # Split the hook content into lines and process each line
        lines = hook_content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('**Core Concept from Script:**'):
                formatted_output += f"**Core Concept from Script:**\n{line.replace('**Core Concept from Script:**', '').strip()}\n\n"
            elif line.startswith('**Why This Hook Works:**'):
                formatted_output += f"**Why This Hook Works:**\n{line.replace('**Why This Hook Works:**', '').strip()}\n\n"
            elif line.startswith('**Generated Hook:**'):
                formatted_output += f"**Generated Hook:**\n{line.replace('**Generated Hook:**', '').strip()}\n\n"
            elif line:  # Add any other non-empty lines as they are
                formatted_output += f"{line}\n"
        
        formatted_output += "---\n\n"  # Add a divider between hooks

    return formatted_output

# 6. Create the main user interface: A text area and a button
user_script = st.text_area("Paste your video script here:", height=200, placeholder="e.g., This video is about a new morning routine I've been using that has completely stopped my procrastination...")

if st.button("Generate Hooks", type="primary"):
    if user_script:
        # Call the function and get the result
        result = analyze_script_for_hooks(user_script)
        
        # Display the result in a nice box
        if result:
            st.success("✅ Done! Here are your 5 viral hook options:")
            st.markdown("---")
            
            # Clean and format the AI's response before displaying it
            cleaned_result = format_ai_response(result)
            st.markdown(cleaned_result)  # <-- Now this shows the beautiful version
    else:
        st.warning("Please enter a script to generate hooks.")

st.markdown("---")
st.caption("AI Hook Helper v1.0 | Built with Streamlit & OpenAI")