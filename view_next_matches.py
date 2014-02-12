from base_view import BaseView

class View(BaseView):
  """Outputs a list of suggested next matches for each player.

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
      # Identify the list of players p hasn't played with
      opponent_ids = list(
        set(participants.keys()) -
        set([p.id]) -
        set([m.id_winner for m in matches if m.id_loser==p.id]) -
        set([m.id_loser  for m in matches if m.id_winner==p.id])
      )
      # Check there are opponents
      if len(opponent_ids)==0:
        print "{} has no option for an opponent".format(p.name)
      else:
        # Sort the list by rating difference with p
        opponent_ids = sorted(
          opponent_ids,
          lambda x,y: abs(int(p.rating)-int(participants[x].rating)) - abs(int(p.rating)-int(participants[y].rating)))
        # Pick the top one (with the closest rating)
        opponent = participants[opponent_ids[0]]
        print "{} ({}; {}) vs. {} ({}; {})".format(p.name, p.id, int(p.rating), opponent.name, opponent.id, int(opponent.rating))
