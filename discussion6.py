import unittest
import os
import csv

class HorseRaces:
    def __init__(self, filename):
        self.race_dict = self.load_results(self.process_csv(filename))

    def process_csv(self, f):
        '''
        Parameters: 
            f, name or path or CSV file: string

        Returns:
            list of lists
        '''
        table = []

        # Do not modify this code
        # This opens the CSV and saves it as a list of lists
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, f)
        # Open the file to be read by Python
        with open(full_path) as file:
            # Get each of the rows in this file
            rows = file.readlines()
            for row in rows:
                # Because this is a CSV, we SPLIT the row by commas
                # We go through each line and build a list of cells
                table_row = []
                for cell in row.strip().split(','):
                    table_row.append(cell)
                # Append the list of cells to the table
                table.append(table_row)
        # print(table)
        return table

###############################################################################
##### TASK 1
###############################################################################
    def load_results(self, table):
        def load_results(self, table):
        # header row: ["Horse", "Tenno Sho Fall", "Tenno Sho Spring", "Teio Sho"]
            header = table[0]
            races = header[1:]

            race_dict = {}

        # remaining rows: ["Special Week", "16.5", "16.3", "17.0"]
            for row in table[1:]:
                if not row or len(row) < 2:   # safety for any blank/malformed row
                    continue

                horse = row[0]
                inner = {}

                for i, race in enumerate(races):
                    # convert time to float
                    inner[race] = float(row[i + 1])

                race_dict[horse] = inner

            return race_dict

###############################################################################
##### TASK 2
###############################################################################

    def horse_fastest_race(self, horse):
        if horse not in self.race_dict:
            return (None, 999.9)

        inner = self.race_dict[horse]  # dict of race -> time
        fastest_race, fastest_time = min(inner.items(), key=lambda kv: kv[1])
        return (fastest_race, fastest_time)

###############################################################################
##### TASK 3
###############################################################################
        
    def horse_personal_best(self):
        best = {}
        for horse in self.race_dict:
            best[horse] = self.horse_fastest_race(horse)
        return best

###############################################################################
##### TASK 4
###############################################################################

    def get_average_time(self):
        '''
        Calculate the average race time for each horse.

        Returns:
            A dictionary with each horse and their average time.
            EXAMPLE: {'Gold Ship': 16.5, 'Daiwa Scarlet': 17.2}
        '''
        pass

###############################################################################
##### DO NOT MODIFY THE UNIT TESTS BELOW!
###############################################################################
class dis7_test(unittest.TestCase):
    '''
    Unit tests to check that our functions were implemented correctly.
    '''
    def setUp(self):
        self.horse_races = HorseRaces('race_results.csv')

    def test_load_results(self):
        # Check that outer values are dictionaries
        self.assertIsInstance(self.horse_races.race_dict['Special Week'], dict)
        # Check one horse's time
        self.assertAlmostEqual(self.horse_races.race_dict['Special Week']['Tenno Sho Spring'], 16.3)

    def test_horse_fastest_race(self):
        nonexistent_horse = self.horse_races.horse_fastest_race('Bob')
        self.assertEqual(nonexistent_horse[0], None)
        fastest_horse = self.horse_races.horse_fastest_race('Symboli Rudolf')
        self.assertEqual(fastest_horse[0], 'Teio Sho')
        self.assertAlmostEqual(fastest_horse[1], 14.8)

    def test_horse_personal_best(self):
        self.assertEqual(self.horse_races.horse_personal_best()['Oguri Cap'][0], 'Tenno Sho Fall')
        self.assertAlmostEqual(self.horse_races.horse_personal_best()['Oguri Cap'][1], 16.6)

    def test_get_average_time(self):
        self.assertAlmostEqual(self.horse_races.get_average_time()['Gold Ship'], 16.5)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
