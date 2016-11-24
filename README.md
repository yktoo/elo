This is my implementation of a test assigment for a position of DevEngineer.

## The Assignment: Game Rankings

Implement a ranking program using the [Elo ranking](https://en.wikipedia.org/wiki/Elo_rating_system) algorithm.

Given two files:

1. `names`, where each line has an ID number and a name for said ID
2. `matches`, where each line contains the ID of the two players of a match and the first one is the winner of said match.

Implement a program that can read both files and then:

1. Score each player based on the games played
2. Generate a list of players sorted by score, their ranking (position in the list) and their number of wins and losses.
3. Generate a report for each person, showing with whom they played and how they fared.
4. Generate a list of suggested next matches.

### Implementation notes

1. You can choose how to implement the different functionalities for the program. You may choose to implement it as a command line parameter (e.g. `./elo names matches show_ranking`, `elo names matches show_rank USER_NAME`, etc).
2. Try to keep the output format independent of the main application logic (ie design it so that it is possible to add new output formats if needed).

## My Implementation

* It's built for **Python 2.7**
* Invocation format is as follows:

    ```bash
    elo.py <names_file> <matches_file> [<view_file>] [<view_options>]
    ```

    where
    * `names_file` - text file with names
    * `matches_file` - text file with matches
    * `view_file` - optional, name of the Python module to render the output result, provided options are:
        * `view_players_scores`
        * `view_player_report`
        * `view_next_matches`
    * `view_options` - optional, options for the view. For now it's only sorting options, one of the following:
        * `ID`     - by ID (default)
        * `NAME`   - by name
        * `RATING` - by rating
        * `RANK`   - by rank
        * `WINS`   - by number of wins
        * `LOSSES` - by number of losses
* I may have over-engineered the file loading part, but the idea was to give it more flexibility
* There's basic input data validity checking implemented
* The algorithm uses Elo rating value of **1500** as a starting (average) value
* The algorithm uses constant value of **16** for K-factor (no factor adjustment used)
* Side note: the format of specifying matches does not allow to denote a draw (only win/lose outcome)

### Examples of invocations

```bash
$ ./elo.py names.txt matches.txt
Rnk       ID Rtng Win Los Name
=== ======== ==== === === ============================================================
 31        0 1492   0   1 Wesley
 35        1 1486   2   4 Melodie
 32        2 1492   0   2 Solange
 36        3 1486   1   5 Johanne
 40        4 1476   2   6 Bunny
  6        5 1530   4   1 Tai
 10        6 1523   2   0 Kami
 38        7 1484   0   5 Michale
 28        8 1493   3   5 Dortha
 37        9 1485   2   4 Aleen
 19       10 1508   3   2 Micheline
 26       11 1499   1   1 Marica
 15       12 1515   2   1 Ira
  7       13 1530   5   2 Hunter
 33       14 1492   0   3 Tracey
 23       15 1506   3   3 Antwan
 13       16 1517   2   1 Meda
 24       17 1501   3   3 Margareta
 21       18 1507   2   3 Damion
 22       19 1507   1   2 Windy
 39       20 1479   2   5 Brianna
 34       21 1492   2   3 Janene
 16       22 1510   2   1 Ileana
  8       23 1525   4   1 Denyse
 29       24 1493   2   3 Jeanine
 11       25 1522   3   3 Dave
  1       26 1539   3   0 Brice
 27       27 1494   2   4 Inez
 18       28 1509   3   3 Joella
 25       29 1500   2   3 Johnna
 14       30 1516   5   3 Jaye
  4       31 1531   5   2 Fernanda
 12       32 1518   3   2 Augustine
 17       33 1510   4   3 Wm
 20       34 1508   2   2 Ute
  9       35 1524   4   2 Berna
  2       36 1536   5   1 Jacquelynn
 30       37 1493   1   2 Karina
  5       38 1531   4   2 Cassondra
  3       39 1532   4   1 Odette

./elo.py names.txt matches.txt view_players_scores
[same output]

$ ./elo.py names.txt matches.txt view_players_scores RANK
Rnk       ID Rtng Win Los Name
=== ======== ==== === === ============================================================
  1       26 1539   3   0 Brice
  2       36 1536   5   1 Jacquelynn
  3       39 1532   4   1 Odette
  4       31 1531   5   2 Fernanda
  5       38 1531   4   2 Cassondra
  6        5 1530   4   1 Tai
  7       13 1530   5   2 Hunter
  8       23 1525   4   1 Denyse
  9       35 1524   4   2 Berna
 10        6 1523   2   0 Kami
 11       25 1522   3   3 Dave
 12       32 1518   3   2 Augustine
 13       16 1517   2   1 Meda
 14       30 1516   5   3 Jaye
 15       12 1515   2   1 Ira
 16       22 1510   2   1 Ileana
 17       33 1510   4   3 Wm
 18       28 1509   3   3 Joella
 19       10 1508   3   2 Micheline
 20       34 1508   2   2 Ute
 21       18 1507   2   3 Damion
 22       19 1507   1   2 Windy
 23       15 1506   3   3 Antwan
 24       17 1501   3   3 Margareta
 25       29 1500   2   3 Johnna
 26       11 1499   1   1 Marica
 27       27 1494   2   4 Inez
 28        8 1493   3   5 Dortha
 29       24 1493   2   3 Jeanine
 30       37 1493   1   2 Karina
 31        0 1492   0   1 Wesley
 32        2 1492   0   2 Solange
 33       14 1492   0   3 Tracey
 34       21 1492   2   3 Janene
 35        1 1486   2   4 Melodie
 36        3 1486   1   5 Johanne
 37        9 1485   2   4 Aleen
 38        7 1484   0   5 Michale
 39       20 1479   2   5 Brianna
 40        4 1476   2   6 Bunny

$ ./elo.py names.txt matches.txt view_player_report NAME
[lots of output]

$./elo.py names.txt matches.txt view_next_matches RANK
Brice (26; 1539) vs. Jacquelynn (36; 1536)
Jacquelynn (36; 1536) vs. Brice (26; 1539)
Odette (39; 1532) vs. Cassondra (38; 1531)
Fernanda (31; 1531) vs. Cassondra (38; 1531)
Cassondra (38; 1531) vs. Fernanda (31; 1531)
Tai (5; 1530) vs. Hunter (13; 1530)
Hunter (13; 1530) vs. Tai (5; 1530)
Denyse (23; 1525) vs. Berna (35; 1524)
Berna (35; 1524) vs. Kami (6; 1523)
Kami (6; 1523) vs. Dave (25; 1522)
Dave (25; 1522) vs. Kami (6; 1523)
Augustine (32; 1518) vs. Meda (16; 1517)
Meda (16; 1517) vs. Jaye (30; 1516)
Jaye (30; 1516) vs. Ira (12; 1515)
Ira (12; 1515) vs. Jaye (30; 1516)
Ileana (22; 1510) vs. Wm (33; 1510)
Wm (33; 1510) vs. Ileana (22; 1510)
Joella (28; 1509) vs. Micheline (10; 1508)
Micheline (10; 1508) vs. Ute (34; 1508)
Ute (34; 1508) vs. Micheline (10; 1508)
Damion (18; 1507) vs. Windy (19; 1507)
Windy (19; 1507) vs. Damion (18; 1507)
Antwan (15; 1506) vs. Damion (18; 1507)
Margareta (17; 1501) vs. Johnna (29; 1500)
Johnna (29; 1500) vs. Marica (11; 1499)
Marica (11; 1499) vs. Johnna (29; 1500)
Inez (27; 1494) vs. Dortha (8; 1493)
Dortha (8; 1493) vs. Jeanine (24; 1493)
Jeanine (24; 1493) vs. Dortha (8; 1493)
Karina (37; 1493) vs. Dortha (8; 1493)
Wesley (0; 1492) vs. Solange (2; 1492)
Solange (2; 1492) vs. Wesley (0; 1492)
Tracey (14; 1492) vs. Wesley (0; 1492)
Janene (21; 1492) vs. Wesley (0; 1492)
Melodie (1; 1486) vs. Johanne (3; 1486)
Johanne (3; 1486) vs. Melodie (1; 1486)
Aleen (9; 1485) vs. Melodie (1; 1486)
Michale (7; 1484) vs. Aleen (9; 1485)
Brianna (20; 1479) vs. Bunny (4; 1476)
Bunny (4; 1476) vs. Brianna (20; 1479)
```

## The Outcome

I've got the job :)
