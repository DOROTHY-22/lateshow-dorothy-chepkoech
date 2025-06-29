# seed.py
from app import app
from extensions import db
from models import db, Episode, Guest, Appearance

def parse_guest_list(guest_str):
    """Parse guest string that may contain multiple names"""
    if ',' in guest_str:
        return [name.strip() for name in guest_str.split(',')]
    return [guest_str]

with app.app_context():
    print("Starting seed...")
    db.drop_all()
    db.create_all()

    # Sample seed data - use your actual data here
    seed_data = """
YEAR GoogleKnowlege_Occupation Show Group Raw_Guest_List
1999 actor 1/11/99 Acting Michael J. Fox
1999 Comedian 1/12/99 Comedy Sandra Bernhard
1999 television actress 1/13/99 Acting Tracey Ullman
1999 film actress 1/14/99 Acting Gillian Anderson
1999 actor 1/18/99 Acting David Alan Grier
1999 actor 1/19/99 Acting William Baldwin
1999 Singer-lyricist 1/20/99 Musician Michael Stipe
1999 model 1/21/99 Media Carmen Electra
1999 actor 1/25/99 Acting Matthew Lillard
1999 stand-up comedian 1/26/99 Comedy David Cross
1999 actress 1/27/99 Acting Yasmine Bleeth
1999 actor 1/28/99 Acting D. L. Hughley
1999 television actress 10/18/99 Acting Rebecca Gayheart
1999 Comedian 10/19/99 Comedy Steven Wright
1999 actress 10/20/99 Acting Amy Brenneman
1999 actress 10/21/99 Acting Melissa Gilbert
1999 actress 10/25/99 Acting Cathy Moriarty
1999 comedian 10/26/99 Comedy Louie Anderson
1999 actress 10/27/99 Acting Sarah Michelle Gellar
1999 Singer-songwriter 10/28/99 Musician Melanie C
1999 actor 10/4/99 Acting Greg Proops
1999 television personality 10/5/99 Media Maury Povich
1999 actress 10/6/99 Acting Brooke Shields
1999 Comic 10/7/99 Comedy Molly Shannon
1999 actor 11/1/99 Acting Chris O'Donnell
1999 actress 11/15/99 Acting Christina Ricci
1999 Singer-songwriter 11/16/99 Musician Tori Amos
1999 actress 11/17/99 Acting Yasmine Bleeth
1999 comedian 11/18/99 Comedy Bill Maher
1999 actress 11/2/99 Acting Jennifer Love Hewitt
1999 rock band 11/29/99 Musician Goo Goo Dolls
1999 musician 11/3/99 Musician Dave Grohl
1999 Film actor 11/30/99 Acting Stephen Rea
1999 Model 11/4/99 Media Roshumba Williams
1999 television actress 11/8/99 Acting Kellie Martin
1999 actress 11/9/99 Acting Kathy Griffin
1999 actress 12/1/99 Acting Laura San Giacomo
1999 journalist 12/13/99 Media Joan Lunden
1999 actress 12/14/99 Acting Shannen Doherty
1999 NA 12/15/99 NA Greatest Millennium Special
1999 comedian 12/16/99 Comedy George Carlin
1999 actor 12/2/99 Acting Michael Boatman
1999 actor 12/20/99 Acting David Boreanaz
1999 singer-songwriter 12/21/99 Musician Jewel
1999 actor 12/6/99 Acting Paul Rudd
1999 us senator 12/7/99 Politician Senator Bob Dole
1999 us senator 12/8/99 Politician Senator Bob Dole
1999 actor 12/9/99 Acting Rob Schneider
1999 comedian 2/1/99 Comedy George Carlin
1999 actress 2/10/99 Acting Pamela Anderson, Natalie Raitano, Molly Culver
1999 film actor 2/11/99 Acting Daniel Stern
1999 actress 2/16/99 Acting Melina Kanakaredes
1999 comedian 2/17/99 Comedy Ed McMahon
1999 actor 2/18/99 Acting Mike Judge
1999 actor 2/2/99 Acting Dave Foley
1999 television actress 2/3/99 Acting Kellie Martin
1999 actor 2/4/99 Acting Jerry O'Connell
1999 actress 2/8/99 Acting Melissa Gilbert
1999 actor 2/9/99 Acting Brendan Fraser
1999 pianist 3/1/99 Musician John Tesh
1999 Vocalist 3/10/99 Musician Sammy Hagar
1999 rock band 3/11/99 Musician Hootie & the Blowfish, Billy Crystal
1999 actor 3/11/99 Acting Hootie & the Blowfish, Billy Crystal
1999 Film actor 3/15/99 Acting Peter Krause
1999 musician 3/16/99 Musician Chris Isaak
1999 writer 3/17/99 Media Frank DeCaro's Oscar Special, John Larroquette
1999 actor 3/17/99 Acting Frank DeCaro's Oscar Special, John Larroquette
1999 actor 3/18/99 Acting Joseph Gordon-Levitt
1999 actor 3/2/99 Acting Eric McCormack
1999 actress 3/22/99 Acting Jennifer Grey
1999 Stand-up comedian 3/23/99 Comedy Norm Macdonald
1999 actress 3/24/99 Acting Sandra Bullock
1999 actress 3/25/99 Acting Janine Turner
1999 Film director 3/29/99 Media Ron Howard
1999 actress 3/3/99 Acting Jeri Ryan
1999 actor 3/30/99 Acting Omar Epps
1999 actress 3/31/99 Acting Diane Lane
1999 actor 3/4/99 Acting Ryan Phillippe
1999 actor 3/8/99 Acting Ian McKellen
1999 actor 3/9/99 Acting Jon Voight
1999 actor 4/1/99 Acting Stephen Baldwin
1999 actor 4/12/99 Acting Ernie Hudson
1999 film actor 4/13/99 Acting Josh Charles
1999 actor 4/14/99 Acting Jackie Chan
1999 actress 4/15/99 Acting Marlee Matlin
1999 actress 4/19/99 Acting Sharon Lawrence
1999 actor 4/20/99 Acting Rob Estes
1999 actress 4/21/99 Acting Angelina Jolie
1999 stand-up comedian 4/22/99 Comedy David Spade
1999 actor 4/26/99 Acting Seth Green
1999 actress 4/27/99 Acting Sheryl Lee Ralph
1999 singer 4/28/99 Musician Chris Robinson
1999 comedian 4/29/99 Comedy Joy Behar
1999 actor 5/10/99 Acting Thomas Gibson
1999 actress 5/11/99 Acting Paula Cale
1999 actor 5/12/99 Acting Ted Danson
1999 actor 5/13/99 Acting Esai Morales
1999 actress 5/17/99 Acting Jane Seymour
1999 Comedian 5/18/99 Comedy Robert Schimmel
1999 actress 5/19/99 Acting Camryn Manheim
1999 actor 5/20/99 Acting Ray Romano
1999 television actress 5/24/99 Acting Patricia Richardson
1999 actress 5/25/99 Acting Suzanne Somers
1999 actress 5/26/99 Acting Natalie Portman
1999 actor 5/27/99 Acting Jamie Foxx
1999 actor 6/10/99 Acting Timothy Hutton
1999 actor 6/14/99 Acting Mike Myers
1999 actor 6/15/99 Acting Rob Lowe
1999 actor 6/16/99 Acting Mike Myers
1999 actress 6/17/99 Acting Heather Graham
1999 film actress 6/21/99 Acting Felicity Huffman
1999 television host 6/22/99 Media Jimmy Kimmel
1999 actor 6/23/99 Acting Adam Sandler
1999 Stand-up comedian 6/24/99 Comedy Richard Belzer
1999 Comedian 6/28/99 Comedy Margaret Cho
1999 actor 6/29/99 Acting Scott Wolf
1999 actress 6/30/99 Acting Roseanne Barr
1999 singer 6/7/99 Musician Harry Connick Jr.
1999 comedian 6/8/99 Comedy Caroline Rhea
1999 actor 6/9/99 Acting Damon Wayans
1999 actor 7/1/99 Acting Rob Schneider
1999 televison actor 7/12/99 Acting Adam Arkin
1999 muppet 7/13/99 Media Miss Piggy
1999 actor 7/14/99 Acting John Leguizamo
1999 Stand-up comedian 7/15/99 Comedy Robert Klein
1999 actress 7/19/99 Acting Christa Miller
1999 stand-up comedian 7/20/99 Comedy David Brenner
1999 NA 7/21/99 NA Third Anniversary Special
1999 actress 7/22/99 Acting Joely Fisher
1999 singer 7/26/99 Musician Donny Osmond
1999 actress 7/27/99 Acting Wendie Malick
1999 Vocalist 7/28/99 Musician Vince Neil
1999 film actress 7/29/99 Acting Janeane Garofalo
1999 comedian 8/10/99 Comedy Dom Irrera
1999 actor 8/11/99 Acting Pierce Brosnan
1999 director 8/12/99 Media Eduardo Sanchez, Daniel Myrick
1999 american television personality 8/16/99 Media Carson Daly
1999 actress 8/17/99 Acting Molly Ringwald
1999 actress 8/18/99 Acting Sarah Jessica Parker
1999 actor 8/19/99 Acting French Stewart
1999 actress 8/2/99 Acting Bebe Neuwirth
1999 actress 8/23/99 Acting Cheryl Ladd
1999 rapper 8/24/99 Musician LL Cool J
1999 singer-songwriter 8/25/99 Musician Dwight Yoakam
1999 actress 8/26/99 Acting Nia Long
1999 actor 8/3/99 Acting Garry Marshall
1999 actor 8/4/99 Acting Denis Leary
1999 actor 8/5/99 Acting Jeffrey Tambor
1999 actor 8/9/99 Acting Dave Foley
1999 comedian 9/13/99 Comedy Elayne Boosler
1999 actor 9/14/99 Acting Tom Green
1999 actor 9/15/99 Acting Jason Priestley
1999 stand-up comedian 9/16/99 Comedy David Cross
1999 actor 9/20/99 Acting Andy Richter
1999 singer 9/21/99 Musician Donny Osmond, Marie Osmond
1999 comedian 9/22/99 Comedy Dave Chappelle
1999 actor 9/23/99 Acting Steve Zahn
1999 Stand-up comedian 9/27/99 Comedy Norm Macdonald
1999 actress 9/28/99 Acting Melissa Joan Hart
1999 Comedian 9/29/99 Comedy Richard Lewis
1999 actor 9/30/99 Acting Bruce McCulloch, Mark McKinney
    """.strip().split('\n')[1:]  # Skip header

    episode_counter = 1
    episode_map = {}  # date -> episode instance
    guest_map = {}    # name -> guest instance

    for line in seed_data:
        parts = line.strip().split(maxsplit=4)
        if len(parts) < 5:
            continue
            
        year, occupation, date, group, guest_str = parts
        guests = parse_guest_list(guest_str)
        
        # Create/get episode
        if date not in episode_map:
            new_episode = Episode(
                date=date,
                number=episode_counter
            )
            episode_counter += 1
            db.session.add(new_episode)
            episode_map[date] = new_episode
        
        # Create guests and appearances
        for guest_name in guests:
            if guest_name not in guest_map:
                new_guest = Guest(
                    name=guest_name,
                    occupation=occupation
                )
                db.session.add(new_guest)
                guest_map[guest_name] = new_guest
            
            # Create appearance
            appearance = Appearance(
                rating=3,  # Default rating
                episode=episode_map[date],
                guest=guest_map[guest_name]
            )
            db.session.add(appearance)

    db.session.commit()
    print("Seed completed successfully!")
