# ** Calendar Program**
## Description
The Calendar Program allows users to book events without the risk of double bookings. Events are represented as intervals [start, end], where the start time is inclusive and the end time is exclusive.

## Debugging Steps
### Problem
The initial implementation of the Calendar class and its Node structure did not correctly handle event insertion, leading to potential double bookings.

## Solution
### Overlap Condition
Added a proper check for overlapping events. Two events overlap if:
node.start < self.end and
node.end > self.start

## Insertion Logic
### Inserted events into the left or right subtree based on their start and end times relative to the current node:
If the new event ends before the current event starts, insert it into the left subtree.
If the new event starts after the current event ends, insert it into the right subtree.

## Implementation Steps

### 1. Check for Overlap
Ensure the new event does not overlap with the current node before inserting it.
### 2. Insert into Left or Right Subtree
If the new event ends before the current event starts, insert it into the left subtree.
If the new event starts after the current event ends, insert it into the right subtree.
### 3. Update the Calendar Class
When the calendar is initially empty, create the root node with the first event.
Use the insert method to add subsequent events.
