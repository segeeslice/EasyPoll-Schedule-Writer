# EasyPoll Schedule Writer

This is a **Python** script that writes commands for use with the [**EasyPoll
Discord Bot**](https://easypoll.bot/), providing an easy way to query for
**scheduling and availability**.

It makes this process easier by **filling in dates for you**, only requiring a
beginning and end date.

## General Intended Usage

1. Invite [EasyPoll](https://easypoll.bot/) to your Discord channel
1. Run this script
1. Paste the results into your Discord channel chat box & send

## Quick Example

For instance, say you want to use EasyPoll to check players DnD availability
over the next week. This could be any day from Monday, June 6, 2022 to Sunday,
June 12, 2022.

To use EasyPoll without this script, you would need to go through the tedious
process of addng each and every date as a separate parameter.

With the help of this script, you can instead just run the following:

``` sh
python .\easy_poll_schedule_writer.py -sd 2022-06-06 -ed 2022-06-12 -q "DnD this week?" -t "@everyone answer this ASAP! :)"
```

This will automatically fill the gaps between those dates, spitting out an
EasyPoll command for you to use:

```
/poll maxchoices: Unlimited question: DnD this week? text: @everyone answer this ASAP! :) answer1: Monday, June 6 answer2: Tuesday, June 7 answer3: Wednesday, June 8 answer4: Thursday, June 9 answer5: Friday, June 10 answer6: Saturday, June 11 answer7: Sunday, June 12 answer8: ❌ None of the above
```

## Requirements

- Python3 _(may work on older versions, but they have not been tested)_
