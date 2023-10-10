# Coding-Assignment-1-Traynor

Polygon free API link
https://polygon.io/docs/stocks/getting-started
Base API endpoint
https://api.polygon.io/v2/aggs/ticker/

Problem Occured in API web-scraping: Initially used Wikipedia, topic I initially chose was animals and animal groups. In scraping the data, I struggled to get certain data off the site, as it was listed in weird and different formats that were inconsistent. Forced me to find a different API. Polygon is a paid API I found online, but managed to get free data. 

Project Goal and Description: As I mentioned, I started with something simple like animals for my data, but ran into problems and just didn't feel like it was a good topic as a whole. Decided to source for data that I cared for more, something I Was actually interested in. While looking for new API's I decided to switch to looking at Stocks. It was fairly easy to get enough data(200 datapoints) once I came across Polygon. From there I just had to pick what analyses I was going to make. In my processed data, I added the date as prompted, and created transactions for each stock's : Closing Price, Highest Price, Lowest Price, Number of Transactions made, Open Price, Volume, and its Average Price. From this I had a multitude of options from which I could choose to make my graphs. I initialy attempted to look at a day to day change in prices for each, and looking at their individual volumes, but it became too complicated and I could not write that code to plot successfully. I ended up choosing to look at the gain/loss for each stock over a period of time, and also graph the number of transactions for each. I planned to look at these two graphs and compare the stocks that had significant gain or loss, and how many transactions were made for them. 


MIT License

Copyright 2023 Patrick Traynor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
