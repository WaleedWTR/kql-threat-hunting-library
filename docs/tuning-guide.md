# Tuning Guide

## Start with a question

Good hunting begins with an observable behaviour, not a desire to generate alerts.

## Baseline

Understand:

- normal event volume
- administrative tooling
- service accounts
- automation
- expected countries/networks
- standard software deployment patterns

## Tune carefully

Prefer transparent filters that analysts can explain.

Avoid hiding broad categories of activity solely to reduce alert counts.

## Production readiness

A detection candidate should have:

- documented data source
- tested query
- owner
- severity logic
- investigation guidance
- response criteria
- known false positives
- review date
