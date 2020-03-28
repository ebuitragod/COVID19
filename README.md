![Devpost](https://devpost-challengepost.netdna-ssl.com/assets/reimagine2/devpost-logo-646bdf6ac6663230947a952f8d354cad.svg)
# COVID-19 Global Hackathon 1.0

Main repo

### Structure

- data
      - raw
      - clean
- notebooks


### Team members

- Laura Jula from Bogotá, Colombia: 
I am a math PhD student in the University of Göttingen, Germany. My current research is focused on change point problems and HMM techniques with application to biological problems, in particular to Ion Channels in the cells. Other interests include Machine learning and biostatistics.
[email](ljulava@uni-goettingen.de)
[twitter](https://twitter.com/LauJula)

- Karthik from Singapore
I am a software engineer/architect, living in Singapore. I have worked on telecom/finance/insurance and health tech engineering teams for design and development of software and platforms.
[email](kalakkal@gmail.com)
[twitter](https://twitter.com/_kkarthik)
[github](https://github.com/kkarthik19)
[linkedin](https://www.linkedin.com/in/karthikeyan-kanapathy-b2928424/)

- Pablo Sierra from Argentina

- Mayank Pandav from Gujarat, India:  I'm working as a fullstack developer including react ,react native, graphql, relay js, AWS , [email](mpandav1998@gmail.com), 
[github](https://github.com/mayankpandav)

- Esperanza Buitrago from Bogotá, Colombia
I am a mathematician from Colombia. 
[email](ebuitragod@gmail.com)
[twitter](https://twitter.com/ebuitragod)

### About the project
[COVID GLOBAL HACKATON](https://covid-global-hackathon.devpost.com/)

## Inspiration
When we read the news, we find how the Health Care System Groans Under Coronavirus. Every single country is falling apart when it does not have enough people, enough technology, enough beds to treat the ones that have already the COVID19, meanwhile the virus spread rapidly in everysingle country... at least with all the data that is registered. 

What we have been told, for the past month, is that there is only one possible way to stop the spreading of the virus: stay at home, keep social distance. But the real question is *how do we really flatten the curve? what are the strategies that the countries took in order to flatten de curve effectively? what were the strategies that did nothing or get the curve to grow even faster? what'd be the best series of strategies to take in order to flatten the curve as fast as it is possible*.

It is different how the statistics and the data work around the world. Meanwhile we saw a chinese hospital to be build up in less than two weeks and after two months of a very strict quarentine in the zero-zone, we may see only three cases in Kenia. We are witnessing Italy or Spain falling apart, but how long many countries such as the Latin American or African ones will be silently falling apart by the virus, with no strategy, with no an effective way to detect the virus, with a health care system already collapse. 

That's why we want to study de measurement contents. What are the best for the time that they have been took. What is the best for a country to take, what is the optimal order, what to expect. 

## What it does 
- [] We evaluate the data, and show it in a different way available. 
- [] We use the data and cross it with the measurement contents by country and date in order to understand the 
- [] To evaluate the optimal way to take decisions in order to control the curve in an optimal way. 

## How we built it
First we did a research of the best API's and DATA available in order to collected in one single place and study the data. At the same time, we took the time to understand how to collect in one place the data of the measurement contents by country, and date and undertand how it was related to the distrubution curve of the virus (including new cases by day, deaths and recoveries). We study how those decisions impact into the distribution curve. 

Later on, we study the mathematical models in order to see the impact of the decisions on the data, give it a score and understood the best way that could have stopped the spread of the virus. 

Finally, we run different models on wheather given a decision a the curve up to that day worked or not. 

## Challenges we ran into
One of the most difficult ones was to get the data as detailed as we could find. Actually, finding APIs was harsh, but we could find several resources that we could get into. 

## Accomplishments that we're proud of

## What we learned
It seems like there is very little mathematical modeling of the COVID19, very little literature and very little use; Although, lots of data, lots of visualization, lots of analysis. We learned to take all that knowledge and put it together into one predictive modeling. 

Also, we learned to work with people in 5 very different timezones. That was a great experience. 

## What's next for Measurement contents: Good or not? 
Well, once we get whethe a measurement is good or not, what is remaining is to understand what is the best path. Undestand it taking other cultural atributes: a measurment makes sense inside the society that is being decided. 

# Sources:
Modelos: https://github.com/epimath/param-estimation-SIR
APIs: https://covid-19-apis.postman.com/
