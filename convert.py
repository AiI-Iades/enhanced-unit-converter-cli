import argparse
from typing import Dict

UNIT_CONVERSIONS = {
    'length': {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'in': 39.3701,
        'ft': 3.28084,
        'mi': 1609.34
    },
    'weight': {
        'kg': 1,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274
    },
    'temperature': {
        'celsius': 1,
        'fahrenheit': 9/5,
        'kelvin': 1
    }
}

def convert_value(value: float, from_unit: str, to_unit: str, category: str) -> float:
    if category not in UNIT_CONVERSIONS:
        raise ValueError(f'Unsupported category: {category}')
    
    if from_unit not in UNIT_CONVERSIONS[category] or to_unit not in UNIT_CONVERSIONS[category]:
        raise ValueError(f'Unsupported unit: {from_unit} or {to_unit} for category {category}')
    
    return value * UNIT_CONVERSIONS[category][to_unit] / UNIT_CONVERSIONS[category][from_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Unit Converter')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('--from-unit', required=True, help='Source unit')
    parser.add_argument('--to-unit', required=True, help='Target unit')
    parser.add_argument('--category', required=True, choices=['length', 'weight', 'temperature'],
                        help='Category of units (length, weight, temperature)')
    args = parser.parse_args()
    
    try:
        result = convert_value(args.value, args.from_unit, args.to_unit, args.category)
        print(f'{args.value} {args.from_unit} = {result:.6f} {args.to_unit}')
    except ValueError as e:
        print(f'Error: {e}')