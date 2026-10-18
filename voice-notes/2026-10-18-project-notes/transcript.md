# Voice note, 2026-10-18: open questions and ideas

An unscripted 18-minute voice note (18 min 19 s) by the speaker, recorded on 2026-10-18 on
a street in Jerusalem, about where the project should go next. Audio: [`voice-note.mp3`](voice-note.mp3).
The points it raises are summarised in the main README under **Open questions and ideas**.

The text below is the raw AssemblyAI transcript (Universal model, transcript id
`82124cb6-21f3-443c-af67-7d228c65604a`), unedited. Known misrecognitions:

| Transcript says | Meant |
|---|---|
| Pyrakeet | Parakeet |
| OnePlus Nord 3.5G | OnePlus Nord 3 5G |
| us (accent list) | US (American) |
| Shukmana, Yehuda | Shuk Machane Yehuda |
| half naya, Hapna yah | hafnaya (a medical referral) |
| GGF | GGUF |
| MDX | MLX |
| my weird prompt | My Weird Prompts (the speaker's AI-generated podcast) |
| Latin tokenizer | [Hebrew-Latin-Token-Classifier](https://github.com/danielrosehill/Hebrew-Latin-Token-Classifier) |
| Nefesh be Nefesh | Nefesh B'Nefesh |

The two pronunciations of "Rosh Hashanah" the speaker contrasts are written identically,
because the transcript cannot show the difference; listen to the audio from 7:20 to 7:40.

---

All right, so I'm just recording a bit of context data for the Parakeet fine tune project. Today is the 18th, correct, 18th of October 2026. So I uploaded today or uploaded a bit more clips to the data set and another checkpoint bringing it to V3. So it's a bit confusing. It's V3 of Pyrakeet V2 0.6 billion parameter, aka 600 million parameter model.

And this is a fine tune for code switching. So the way that this data shape has been, has been shaped is I figured that I'd like to try a fine tune for tech vocab. My day to day need, or what I see Parakeet not doing well in my day to day use of the tool is tech vocab recognition and code switching. So that's why the data set is structured like this. Now I thought it would make sense to do separate fine tunes.

I've already done the code switching. Eventually we'll do the tech one when I have enough clips and maybe a third one that is just the third one, which is why I've created a third data set. So the idea is that you've got one fine tune for tech vocabulary, one fine tune for code switching. I'm not sure there's actually really a need for code switching plus Hebrew because the Hebrew clips, the code switching clips already contain a lot. But basically, I think the powerful part of data set preparation as I'm learning the art and science, is this idea of being able to decide data blending.

Okay, we'll, you know, we'll have this, this many clips or held out ones will have this percentage of fine tuning because the risk might sound, you know, on the one hand it sounds appealing to cover tick hold boxes. On the other, if you don't need a certain domain, you're risking overfitting and of course catastrophic forgetting for no reason. So I prefer the idea of keeping them targeted to fine tunes. The one I'm actually most excited about by far is the code switching one. That's the really, that's the core of this effort.

But the main data set is what I want to use because I've been doing fine tuning for quite a bit of time now for ASR models and I figure I'll always have a need for clips, a clip library and then I can also splice that out. Now what I want to do is at the moment I'm recording all the clips so far for the code switching data set have been recorded on my phone. My OnePlus Nord 3.5G, the trusty OnePlus. And that's a product of the fact that at the moment I'm still not quite set up on my desktop after we moved apartment, but as I am, it'll be more convenient to record there. And I want to get a mixture of microphones.

I think that's very important. There's a few things that I want to get that are kind of on the vision, on the project list for this fine tune. The first is to get different audio, different acoustic conditions. So I'm trying to capture some clips when our dear son Ezra is fussing in the background, because that's a very realistic transcribing environment I'm constantly using exactly at that moment when I can't type and I'm trying to hold a baby and the baby is fussing. So I've deliberately recorded some clips with audible crying in the background and you know, just general noise environments.

Right now I'm sitting on the side of Yaffo street in Jerusalem and there's that kind of ambient city noise, a little bit of jackhammering going on from that bloody construction site by the market, the interminable drilling going on there. You've got, you know, other environments, the shook, I would say the acoustic profile in Israel. What I would say would be very interesting to me from a fine tuning perspective. A few things. Firstly, there is a lot of different languages spoken here and one of the fine tuning targets that has nothing to do with code switching, which I think is interesting in its own right, is non speaker audio.

So if I'm transcribing and there is a conversation going on behind me, I haven't looked too carefully into that question about architecturally, what supports, you know, does that require diarization and speaker identification as an accessory model to say, no, that's not the speaker. Or can it just infer that from the volume differential? Because, you know, frequently you'll be recording a voice note using dictation, parakeet, whatever, at a coffee store and you'll just of course, in the background you're hearing random conversations in English. That's what's interesting about Hebrew Israel is you'll commonly find them in different languages all at the same time. Background music, know shops, layering things.

So at the moment I've been recording the voice clips mostly at home, but I think it's very important to capture them in the messy real world that I encounter when I'm actually doing the transcription. So even if we don't extend the vocab, I think there's value in just going out the annotation part. So I've used Claude code to build a great little recording GUI for my Android, which is fantastic. And there is like, I can change the tags there. I feel like I'm probably not going to be that good about doing it because it's just a bit awkward on a phone.

So I might, as a second pass, do data annotation post facto correcting some and, you know, build a little web GUI for that, editing the tag, saying, wait, this was noisy. Maybe even doing some, you know, AI detection for if I can say this is a clip with a child screaming. If there's, anyone's, you know, one shot learning, can you identify any other clips that aren't tagged with that?

So that's that. That's what I'm thinking. There is. I'll probably be a bit loose. The second one is that I'm sure if I asked around for my friends.

Hey, would you mind reading a few sentences? The challenge here in this data set with what I'm thinking about the. The users I have in mind, which is basically English immigrants to Israel. You've got South Africans, Australians, British people, us, you know, probably mostly us. I'm my accent, the Irish accent makes me a very, very small.

I'm a tiny minority linguistically, phonetically pronouncing code, switching Hebrew with an Irish accent. So I think firstly, gender, some female samples, secondly, different accents. Thirdly, and this is where the material becomes important, even within the same accent group, you have different ways of pronouncing Hebrew words based upon whether people are from a Sephardic, Ashkenazi background. So one sample, which is why sometimes when recording the training data, currently, if, let's say there's a word, there's a sentence with this Rosh Hashanah I'm going to show. So at the moment what I'm doing is recording deliberately with a couple of common permutations you'll hear.

So I'll record a few samples with this Rosh Hashanah, which is how you know, the maybe you call classic Diaspora pronunciation, and then one with this Rosh Hashanah. So pronouncing it like an Israeli name. I rationale and idea here is that if I get samples of both into the training data set, it'll be flexible enough to accommodate those different ways of pronouncing it. So that's really. And then in terms of the materials.

So the more. This is one of those things where the more I think about it, the more complicated it becomes. If you're an English speaker in Israel, you might throw in terms like mamish. So Hebrew is mamesh, Mamish is I guess probably technically Yiddish code code switching. So I don't think it's important to split that here in this data set because there is a decent amount of crossover.

But very technically it might be more correct to maybe record within the data set which is this containing code. Switched words in there are Hebrew, Yiddish. And the reason I say it gets complex when you're splitting hairs is the fact that if you really want to get into it, a lot of the Hebrew words and slang really originate from other languages. So I think for simplicity and to try keep this as a useful dictation tool and not try to resolve these messy linguistic arguments, it probably makes more sense to tend towards being less correct about the actual origin of words and recognizing that the people who would use this app might be using a mixture of words that straddle different languages of origin. So that's the project and what I'd really like to do.

My vision for this, I guess is, you know, the first couple of checkpoints was basically proof of concept. I've already shown that the word error rate or code switch Hebrew is moving in the right direction and that's very encouraging. I'm going to try it on my mobile today with a little proof of concept app that Claude put together. And what I'd love to do is then just gradually accumulate the training data, less frequent updates. Of course, maybe I'll spend 20, 30 minutes a week or every few days gradually decreasing the pace, but if it continues to show promise, my ultimate idea is to be able to use this as my own day to day transcription tool.

Because so much of what I actually dictate daily into Parakeet is going to have all these errors that I'm mitigating as this app comes to fruition. It would be great to have a Android dictation app that wasn't what I created for this purpose. I can load arbitrary GGF weights. There is one I found it's a little bit, a little bit buggy in places. So I felt like if I'm just going to be using this one app, I'm gonna make the apk, but that's up there.

Datasets started and I think now the ball's rolling and working on incremental improvements for the forthcoming versions. The final thing I will say is if I can eventually get around to spreading the word with friends and whatever. And I'm particularly interested in creating a version for Apple, I believe, and I'll have to look into this. It's MDX for inference. Whatever pathways are available.

I think the people who would be most interested in are not people deep into local AI, it's people like me who might be using these tools and noticing that whenever you say a sentence with a Hebrew word, even with whisper, even with the greatest models, whatever, it frequently fails. So I think probably the niche of the AI world that are English speakers. And the final note that I have is I have a couple of friends who are much more religious than I am. And deep in that world, I'm thinking of a guy called Mike in particular. And Mike is Australian, so I might have him contribute some sentences.

But I'd love to sit down with someone like Mike and say, I know you also use dictation tools. What are the words that you know, you find it always botches and get his list. Because I have blind spots, because I don't use that vocabulary, I might take vocab. So I suspect that as. As this goes on, I'll kind of identify more little niches.

What I'm filling at the moment is what you might call second cities in Israel. Like not Tel Aviv, not Jerusalem, but all the long list of little moshavim and kibbutzim that and then cities, streets, street names in Jerusalem and Tel Aviv, celebrity names, politician names. And my podcast, my weird prompt is actually quite a good little. It's tts, but I can kind of see in reverse what it's struggling with phonetically. So it said, today there's a party called Amcha Yisrael.

And it called it Amcha Yisrael because it's not in the lexicon. So that's an example of a word as it's a new political party that I should probably be incorporating into this data set. So I have a function on the app for. I'm using Claude to generate word lists, and I can have one where I provide a word, provide the surrounding context, and it will. It will generate sentence pairs.

The final thing I will say, well, this is not really a final thing. There is. This is the kind of the. The thing that I feel like there's a lot of meat. Once you get past the obvious ones like Shukmana, Yehuda, Yerushalayim, you begin finding all sorts of words that are that.

That you know that there are to correct for. The final thing that I will conclude with is an open question that I don't have the answer to currently, which I'm thinking about is how many examples are necessary to get something Robust. So one one use case I think is extremely important is medical. Medical words not for doctors but for lay people. So to give one example we have the word let's say hafnaya.

Hafnaya means a referral. So it's something you'd say all the time. I need to get a half naya for my doctor for whatever the rheumatologist the doctor now is six sentences with Hapna yah enough should it be 12?

The question I really have is how much repetition is needed if I can say this is a really important word. You know there's ones that are in the long tail.

Claude has generated many examples of this and I said, you know it's a good word. It definitely is something I've seen AI get wrong. But it's a day that happens once a year. The failure mode to use it's one of its favorite words that would have a bigger positive impact in my life if it could always get it right. Was would be where there's an IKEA because you're doing transcription or you're using voice to text to type into waze and it doesn't.

It doesn't get that. So that's another example of where I think this could be helpful small quantized models for on device inference for you know, navigation apps running on on cart. I think there's lots and lots that this could be really useful for and a reminder to self or notes to self or to as this actually as I validate this in my own day to day usage and begin seeing Wait, this works really well. I'll be. I can share it with Nefesh be Nefesh maybe in other other groups.

One final thought. This voice note was clearly not planned very well or it's very much off the cuff. I've already reached out to a couple of organizations in the Israeli AI and NLP community Dicta and I'm very eager just to have a conversation with them. I shared a Latin tokenizer a few days ago which I was very surprised as he didn't exist for classifying Hebrew in Latin characters. And I have to follow up on the correspondence there but very eager to collaborate with people who have been working on the other side of this problem namely getting better support for Hebrew LLMs and TTs and SST.

This is a smaller use case but we're you know, we're all in one country. We're all working with the challenges of Hebrew being a minor language and all the little sort of blips in use cases like Translation and dictation, that kind of spring that are downstream of that fact. I think that's about it. Oh, the couple of other things, I'm not sure where these fit in with the training plan. So other categories that are in the data set are homophones and numerics.

So that's one thing I've noticed after I moved over from whisper to parakeet V2 and I'm using, by the way, at the moment I'm using a great app called Whisperian and I'm using parakeet V2, which is English only. And firstly, moving over from Whisper to that on my phone was an absolute complete change in the best way. It suddenly was fast enough to actually work well. But I did notice that things, things that Whisper did seamlessly, Parakeet didn't do well. One of them was the numeric representations.

So the year is 2026, you know, coming out with the word letter spelled out. So that's part of the training set. And homophones are as well, which I found it struggles with the best. Now, those are general. My attempt to create general targeted improvements on Parakeet.

Now the question, the open question I have for my fine tuning is should those general improvements that part of the data set, that tag, should that be also included in the training for Hebrew and for code switching and for general or for just for general improvement like will it dilute the usefulness of the targeted fine tuning for domain knowledge and for code switching? If I also include those. But it would, if not, it would seem preferable that in the data mixture for those two fine tunes that we've got the general tune up stuff as well. All right, that's it. That's the reason I'm doing this, sharing this building in public and invite anyone to contribute so I could create a little login, mechanism them for contributing audio samples at a later point in time once the project gets a little bit of momentum and I share with a few people to increase the diversity of speaker voices again, I think it'd be very useful.

That's it.
