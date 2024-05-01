
# Dynamic Subset Sum Solver

## Description

This repository houses a versatile implementation of the subset sum algorithm utilizing dynamic programming with a depth-first search (DFS) approach. The algorithm efficiently computes all possible combinations with unique keys provided in the output. It is capable of handling both positive and negative float and integer numbers, offering robust functionality across a wide range of numerical scenarios.

## Authors

- [@princekumardobariya](https://github.com/PrinceDobariya0710)
- [@princekumar-dobariya-LinkedIn](https://www.linkedin.com/in/princekumar-dobariya-198637154/)

### Key Features:

- **Dynamic Programming with DFS**: Utilizes a dynamic programming paradigm with depth-first search for efficient subset sum computation.
  
- **Supports Positive and Negative Numbers**: Handles both positive and negative float and integer numbers, ensuring versatility in solving various problem instances.
  
- **Customizable Constraints**: Users can specify constraints such as time limits, accuracy thresholds, and maximum combinations to tailor the algorithm's behavior to specific requirements.
  
#### Time Complexity: 
The time complexity of the algorithm is `O(2^n)`, where `n` is the size of the input set.

#### Space Complexity:
The space complexity of the algorithm is `O(n)`, where `n` is the size of the input set.

This dynamic subset sum solver empowers users with a flexible and powerful tool for tackling subset sum problems across diverse use cases.

## Installation

Install subsetsumdfs with pip

```bash
  pip install subsetsumdfs
```
    
## Please follow provided input data structure to avoid errors

## Example usage

For a case user has to make a code like this:

```python
from subsetsumdfs import subsetsum

data =[
        {
            "value": 40806839.37,
            "unique_key": "1"
        },
        {
            "value": -23995624.33,
            "unique_key": "2"
        },
        {
            "value": -58386586.35,
            "unique_key": "3"
        },
        {
            "value": 93705577.71,
            "unique_key": "4"
        },
        {
            "value": 56065510.55,
            "unique_key": "5"
        },
        {
            "value": -16366515,
            "unique_key": "6"
        },
        {
            "value": -19421385,
            "unique_key": "7"
        },
        {
            "value": -254331.86,
            "unique_key": "8"
        },
        {
            "value": -57561556.47,
            "unique_key": "9"
        },
        {
            "value": 2609628022,
            "unique_key": "10"
        },
        {
            "value": 1104.92,
            "unique_key": "11"
        },
        {
            "value": -980.88,
            "unique_key": "12"
        },
        {
            "value": 745847.81,
            "unique_key": "13"
        },
        {
            "value": 231520.34,
            "unique_key": "14"
        },
        {
            "value": 6438.48,
            "unique_key": "15"
        },
        {
            "value": 2860.77,
            "unique_key": "16"
        },
        {
            "value": 81026.7,
            "unique_key": "17"
        },
        {
            "value": 497896.57,
            "unique_key": "18"
        },
        {
            "value": 3223.43,
            "unique_key": "19"
        },
        {
            "value": -575095.08,
            "unique_key": "20"
        },
        {
            "value": 342730.6,
            "unique_key": "21"
        },
        {
            "value": 26119.62,
            "unique_key": "22"
        },
        {
            "value": 17127.86,
            "unique_key": "23"
        },
        {
            "value": 309.19,
            "unique_key": "24"
        },
        {
            "value": 4086683.03,
            "unique_key": "25"
        }
        # Add more data entries as needed
    ]
]

result = subset_sum(items=data, target=4086683.03, max_time=300, accuracy=1, max_combinations=2)
```

### Example Output :
```[
    [{'value': -254331.86, 'unique_key': '8'}, {'value': -980.88, 'unique_key': '12'}, {'value': 745847.81, 'unique_key': '13'}, {'value': 81026.7, 'unique_key': '17'}, {'value': 3223.43, 'unique_key': '19'}, {'value': -575095.08, 'unique_key': '20'}, {'value': 309.19, 'unique_key': '24'}, {'value': 4086683.03, 'unique_key': '25'}],
    [{'value': 4086683.03, 'unique_key': '25'}]
]
```
### Here's what the arguments represent in the above code:

- **items**: a list of dictionaries according to the provided data structure, each containing "value" and "unique_key" for identifying combinations.
- **target**: a float number for which the user wants to find all possible combinations that sum to that target.
- **max_time**: the maximum time for the subset sum algorithm to run (in seconds). Useful when dealing with large list.
- **accuracy**: an accuracy parameter indicating the precision for which the target can be achieved.
- **max_combinations**: the maximum number of combinations the user wants to find.

### Support
Use it! Write about it! Star it! If you love this.



