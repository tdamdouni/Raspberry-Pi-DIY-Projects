# Google’s AI Invents Sounds Humans Have Never Heard Before

_Captured: 2017-05-19 at 11:23 from [www.wired.com](https://www.wired.com/2017/05/google-uses-ai-create-1000s-new-musical-instruments/)_

![](https://assets.wired.com/photos/w_1720/wp-content/uploads/2017/05/AISoundTA.jpg)

> _ Getty Images_

Jesse Engel is playing an instrument that's somewhere between a clavichord and a Hammond organ--18th-century classical crossed with 20th-century rhythm and blues. Then he drags a marker across his laptop screen. Suddenly, the instrument is _somewhere else_ between a clavichord and a Hammond. Before, it was, say, 15 percent clavichord. Now it's closer to 75 percent. Then he drags the marker back and forth as quickly as he can, careening though all the sounds between these two very different instruments.

"This is not like playing the two at the same time," says one of Engel's colleagues, Cinjon Resnick, from across the room. And that's worth saying. The machine and its software aren't layering the sounds of a clavichord atop those of a Hammond. They're producing entirely new sounds using the mathematical characteristics of the notes that emerge from the two. And they can do this with about a thousand different instruments--from violins to balafons--creating countless new sounds from those we already have, thanks to artificial intelligence.

Engel and Resnick are part of Google Magenta--a small team of AI researchers inside the internet giant building computer systems that can make their own art--and this is their latest project. It's called [NSynth](https://magenta.tensorflow.org/nsynth), and the team will publicly demonstrate the technology later this week at [Moogfest](http://www.moogfest.com), the annual art, music, and technology festival, held this year in Durham, North Carolina.

The idea is that NSynth, which Google first discussed in a [blog post](https://magenta.tensorflow.org/nsynth) last month, will provide musicians with an entirely new range of tools for making music. Critic Marc Weidenbaum points out that the approach isn't very far removed from what orchestral conductors have done for ages--"the blending of instruments is nothing new," he says--but he also believes that Google's technology could push this age-old practice into new places. "Artistically, it could yield some cool stuff, and because it's Google, people will follow their lead," he says.

### The Boundaries of Sound

Magenta is part of Google Brain, the company's central AI lab, where a small army of researchers are exploring the limits of neural networks and other forms of machine learning. [Neural networks](https://www.wired.com/2015/04/jeff-dean/) are complex mathematical systems that can learn tasks by analyzing large amounts of data, and in recent years they've proven to be an enormously effective way of recognizing objects and faces in photos, identifying commands spoken into smartphones, and translating from one language to another, among other tasks. Now the Magenta team is turning this idea on its head, using neural networks as a way of teaching machines to make new kinds of music and other art.

NSynth begins with a massive database of sounds. Engel and team collected a wide range of notes from about a thousand different instruments and then fed them into a neural network. By analyzing the notes, the neural net--several layers of calculus run across a network of computer chips--learned the audible characteristics of each instrument. Then it created a mathematical "vector" for each one. Using these vectors, a machine can mimic the sound of each instrument--a Hammond organ or a clavichord, say--but it can also combine the sounds of the two.

In addition to the NSynth "slider" that Engel recently demonstrated at Google headquarters, the team has also built a two-dimensional interface that lets you explore the audible space between four different instruments at once. And the team is intent on taking the idea further still, exploring the boundaries of artistic creation. A second neural network, for instance, could learn new ways of mimicking and combining the sounds from all those instruments. AI could work in tandem with AI.

The team has also created a new playground for AI researchers and other computer scientists. They've released a research paper describing the NSynth algorithms, and anyone can download and use their database of sounds. For Douglas Eck, who oversees the Magenta team, the hope is that researchers can generate a much wider array of tools for any artist, not just musicians. But not too wide. Art without constraints ceases to be art. The trick will lie in finding the balance between here and the infinite.
