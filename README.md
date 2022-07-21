# Rotating Meal Plan
This program takes meals in text files and outputs a meal plan into a text file for however many days you want. Note, meals are *rotated*, not randomized.

**IMPORTANT:** Before running the program, place meals that you want in `breakfast.txt`, `lunch.txt`, or `dinner.txt`.

## Output
The program outputs into `meals.md` as:

```markdown
## 2022-07-21
- breakfast: eggs
- lunch: salad
- dinner: pasta

## 2022-07-22
- breakfast: cereal
- lunch: chicken wrap
- dinner: rice

## 2022-07-23
- breakfast: oatmeal
- lunch: hamburger
- dinner: pasta
```

Don't like the date format? Change it on line 113. View `strftime` documentation [here](https://strftime.org).

### Common date formats
`dd-mm-yyyy`: `'%d-%m-%Y'`

`mm-dd-yyyy`: `%m-%d-%Y`

### JSON
`meals.json` saves your meal plan. It would contain:
```json
{"2022-07-21": {"breakfast": "eggs", "lunch": "salad", "dinner": "pasta"}, "2022-07-22": {"breakfast": "cereal", "lunch": "chicken wrap", "dinner": "rice"}, "2022-07-23": {"breakfast": "oatmeal", "lunch": "hamburger", "dinner": "pasta"}
```

With formatting, that would be:
```json
{
  "2022-07-21": {
  "breakfast": "eggs", 
  "lunch": "salad", 
  "dinner": "pasta"
  }, 
  "2022-07-22": {
    "breakfast": "cereal", 
    "lunch": "chicken wrap", 
    "dinner": "rice"
  }, 
  "2022-07-23": {
    "breakfast": "oatmeal", 
    "lunch": "hamburger", 
    "dinner": "pasta"
  }
}
```

## Known Issues
This script may pick a day ahead or behind depending on your current time zone in relation to UTC. For instance, it may be a day ahead when UTC is a day ahead (i.e. UTC is **2022-01-01 1:00** when local time is **2021-12-31 11:00**).