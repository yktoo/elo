from base_view import BaseView

class View(BaseView):
  """Outputs a report for each player, providing ites name and a list of its matches.

    Supported options specify sorting method:
      ID     - by ID (default)
      NAME   - by name
      RATING - by rating
      RANK   - by rank
      WINS   - by number of wins
      LOSSES - by number of losses
  """

  @classmethod
  def render(cls, participants, matches, options):
    # Define sorting method
    if options=="NAME":
      sorter = lambda x,y: cmp(x.name, y.name)
    elif options=="RATING":
      sorter = lambda x,y: int(x.rating)-int(y.rating)
    elif options=="RANK":
      sorter = lambda x,y: x.rank-y.rank
    elif options=="WINS":
      sorter = lambda x,y: x.num_wins-y.num_wins
    elif options=="LOSSES":
      sorter = lambda x,y: x.num_losses-y.num_losses
    else:
      sorter = lambda x,y: x.id-y.id

    # Output the content
    for p in sorted(participants.values(), sorter):
      print "Player: {} (ID: {})".format(p.name, p.id)
      print "    Rating: {}".format(int(p.rating))
      print "    Rank: {}".format(p.rank)
      print "    Matches:"
      p_matches = [m for m in matches if m.id_winner==p.id or m.id_loser==p.id]
      for m in p_matches:
        if m.id_winner==p.id:
          print "        {} (won)".format(participants[m.id_loser].name)
        else:
          print "        {} (lost)".format(participants[m.id_winner].name)
      print "================================================================================"
