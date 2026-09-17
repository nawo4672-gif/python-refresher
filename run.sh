#no error
python3 print_fires.py -c Albania -f Agrofood_co2_emission.csv

#file not found error
python3 print_fires.py -c Canada -f Aggrofood_co2_emission.csv

#value error
python3 print_fires.py -c Mexico -f Agrofood_co2_emission.csv -fc 0