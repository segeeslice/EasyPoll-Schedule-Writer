#!/usr/bin/env python3

import argparse
import sys
import calendar

from datetime import datetime, timedelta

DEFAULT_DATE_DAYS = 7

# === Argument Parsing ===

def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d")

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--question', type=str, required=True,
                        help='Poll question')
    parser.add_argument('-t', '--text', type=str,
                        help='Poll text (displayed as a normal message in Discord)')
    parser.add_argument('-sd', '--start-date', type=parse_date, required=True,
                        help='The date the argument values should start at. Format YYYY-MM-DD')
    parser.add_argument('-ed', '--end-date', type=parse_date,
                        help='The date the argument should end at (if not provided - will use one week). Format YYYY-MM-DD')

    return parser.parse_args(sys.argv[1:])

# === Date Utilities ===

def get_dates_between(start_date, end_date = None):
    date_days = (end_date - start_date).days if end_date is not None else DEFAULT_DATE_DAYS

    if date_days < 1:
        raise Exception("End date must be after start date to get date difference")

    return [start_date + timedelta(days=i) for i in range(0, date_days + 1)]

def get_weekday_name(date):
    return calendar.day_name[date.weekday()]

def get_month_name(date):
    return calendar.month_name[date.month]

def get_pretty_date(date):
    return "%s, %s %s" % (get_weekday_name(date), get_month_name(date), date.day)

# === Easy Poll ===

def build_easy_poll_command(question, text, choices):
    command = "/poll maxchoices: Unlimited"

    if question:
        command += " question: " + question

    if text:
        command += " text: " + text

    if choices:
        for i, choice in enumerate(choices):
            command += " answer%d: %s" % (i + 1, choice)

    choice_count = len(choices) if choices else 0
    command += " answer%d: ❌ None of the above" % (choice_count + 1)

    return command

# === Main ===

def main():
    args = parse_args()

    days = get_dates_between(args.start_date, args.end_date)
    pretty_days = [get_pretty_date(day) for day in days]
    command = build_easy_poll_command(args.question, args.text, pretty_days)

    print(command)

if __name__ == "__main__":
    main()
