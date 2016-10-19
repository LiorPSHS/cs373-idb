# Title

## Team Name: Team Research Papers

## Team Members:
- Charles Tian
- Eric Erickson
- Ryan Shea
- Addison Juarez
- Lior Vansteenkiste

# Introduction

# Design

## Selecting our subjects
When choosing pillars we ended up making several changes along the way. These changes were driven by three main criteria. First, that our pillar be reachable by a direct database query. Second, that our pillar's characteristics be reachable from a direct database query without requiring a prohibitive amount of work. Third, that our pillars contain characteristics capable of connecting them.

When going in (and posting our topics on piazza) we were planning on using "Authors" as a pillar. However, we quickly discovered that individual authors were not directly reachable as a query. Instead, each piece of information describing a paper contained a string that could have one or more authors, deliniated by inconsistent delimiters! What this would mean, is that to build a database of Authors from the source we had chosen, we would have had to get the information for every single paper, and parsed the author string (in an only arguably valid way) millions of times. So many calls is simply prohibitive, and we instead migrated the pillar to "Countries."

However, countries also did a poor job of meeting our new-found criteria. Many, if not most, papers contained multiple authoring countries, in no guarenteed order. Attempting to match an authoring (or most-authoring) country to a paper, as it would appear in our table, is simply unreliable at best. Furthermore, we considered organizing years by highest contributing country as providing inadequate information. Most years saw the same top contributor. (U.S.A! U.S.A!) With countries bringing less than satisfactory information, we finally settled on "Journals". 

Journals contain conveniently accessed and extremely relevant information when grouped with the other two pillars. Journals vary their rate of publication over time and the "publications by year" list, as pulled from the database, comes sorted by popularity. This means that our connection: Journal->Year is both cheap and relevant. Journals also tend to prefer certain subjects over others and, once again, this list of subjects is sorted by popularity. As such our Journal->Subject connection is also both cheap and relevant.

## Selecting our characteristics
When choosing what characteristics to attach to each pillar, we once again had specific criteria. First, our characteristics must be conveniently reachable from our database. This one is not as bad as it seems, as we are building the database, and can structure it according to the characteristics we choose. Second, for each pillar, for other pillar, at least one characteristic of the former must connect to each of the latter. Third, the information cannot be worthless. (irrelevant in any context)

Paper's Characteristics:
 - Title > Relevant, useful, exactly one per paper.
 - Authors > Relevant, useful. Only one string per paper
 - Journal > Relevant, connects to another pillar, only one string per paper.
 - Year > Relevant, connects to another pillar. One field.
 - Abstract > Extremely relevant, single string.

Journal's Characteristics:
 - Name > Relevant, identifier, only one
 - Number of Publications > Relevant, gives an indication of size
 - Most Popular Subject > Relevant, gives an indication of what the Journal is all about
 - Most Popular Year > Connects to another pillar, changes w/ time. gives an indication of when a journal is/was active
 - Most Contributing Country > Relevant, can be retrieved from a sorted list in original database
 - Papers > Connects to Papers? #######################--NEED HELP WITH THIS ONE--########################

Year's Characteristics:
 - Year(name) > Identifier.
 - Number of Publications > Relevant, shows overall activity over time
 - Most Popular Subject > Shows trends over time.
 - Most Popular Keyword > Shows less distinct but more specific trends over time
 - Top Journal > Connects to other pillar
 - Papers > Connects to Papers? ##################-- HELP AGAIN PLEASE --##################



# Tools

# Hosting


