from sports_parser import get_sports
from events_parser import get_events
from db_methods import add_records, clear_live

if __name__ == '__main__':
    sports_dict = get_sports()
    clear_live()
    for sport in sports_dict.keys():
        all_events = get_events(sport, sports_dict[sport], live=False)
        live_events = get_events(sport, sports_dict[sport], live=True)
        add_records('all_events', all_events)
        add_records('live_events', live_events)
