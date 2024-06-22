Calendar Program:

Description:
Calendar program allows users to book events without double bookings. Events are represented as interval [start, end] where the start time is inclusive and the end time is exclusive.

Debugging Steps:
Problem: Initial implementation of the calendar class and its Node structure did not correctly handle event insertion, leading to potential double bookings.

Solution:
Overlap Condition:
Added a proper check for overlapping events. Two events overlap if 'node.start < self.end' and 'node.end > self.start'.
Insertion Logic:
Inserting events into the left or right subtree based on their start and end times relative to the current node.

steps:

Check for Overlap: 
Ensure the newevent does not overlap with the current node before inserting it.

Insert into left or right subtree:
If the new event ends before the current event starts, insert it into the left subtree.
If the new event starts after the current event ends, insertit into right subtree.

Update the Calendar class:
When the calendar is initially empty, create the root node with te first event.
Use the insert method to add subsequent events.
