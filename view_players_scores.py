from base_view import BaseView

class View(BaseView):
  """Default view. Outputs all player results in a table, providing id, rating, numbers of wins and losses and the name.

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

    # Output the header
    print "Rnk       ID Rtng Win Los Name"
    print "=== ======== ==== === === ============================================================"

    # Output the content
    for p in sorted(participants.values(), sorter):
      print "{:3} {:8} {:4} {:3} {:3} {}".format(p.rank, p.id, int(p.rating), p.num_wins, p.num_losses, p.name)
