# Intuition
We can create a `count` array with
- **index**: *the count of the numbers*
- **value**: *the list of numbers with the count*

Example: [1,1,1,2,2,3] --> [ [], [3], [2], [1], [], [], [] ]

Then, iterate the array from the back to the front. Append the value to a `res` array, until `len(res) == k`.

Return the `res` array once `len(res) == k`.

## Algorithm
1. Initialise a hash map (`{ number : count }`) to store the frequency of each number.
2. Convert the hash map to the `count` array.
3. Iterate the `count` array in the reverse direction, and populate the `res` array for each element in the `count` array.
4. Once the `len(res)` equals to `k`, returns the `res` array.