# PlantEncylopedia

## Summary
*scraper.py* scrapes Wikipedia using BeautifulSoup to collect data on 2000+ plants.  The data is stored in a csv file.

*index.html* Converts the plant database csv file into JSON and uses D3.js and vanilla javascript to dynamically render a taxonomy tree visualization, and the relevant content for each plant.  The search bar has a custom coded autocomplete functionality which searches the list of plants based on query.

## Code Style
Javascript - Linter-js-standard 6.1.1
Python - Linter-pylama 0.10.1

## Next Steps
1. Improve quality of description text being scraped
2. Improve quality and scalability of python scraping code
3. Remove bracket references [4] in description
4. Modularize logic
5. improve [website design](https://starmorph.com)


